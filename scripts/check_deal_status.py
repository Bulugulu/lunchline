"""
Detect whether a candidate is mid-deal (definitive merger, tender offer, strategic
review, etc.). Surfaces deal-in-progress BEFORE deep scoring — these candidates
are not usable for a search-fund-style pitch case because the operator angle is
moot once a transaction is announced.

Mirrors scripts/check_voting_structure.py architecture. Reads from a candidate's
dossier (data/dossiers/{ticker}/) and writes deal_status.json.

Classification:
  NONE                — no deal signals
  EXPLORING           — strategic review / advisors engaged / no agreement
  TENDER_OFFER        — company-initiated buyback tender OR third-party takeover offer
  DEFINITIVE          — signed merger agreement / plan of merger
  CLOSED              — transaction completed

Risk levels for our screener:
  LOW          — NONE
  MEDIUM       — TENDER_OFFER (company buyback OK; takeover bid problematic)
  HIGH         — EXPLORING (could pivot to definitive any time)
  DEAL_BREAKER — DEFINITIVE or CLOSED

Usage:
    python scripts/check_deal_status.py SCOR
    python scripts/check_deal_status.py LPSN  # should DEAL_BREAKER (SoundHound deal)
"""

import argparse
import json
import re
from pathlib import Path

from bs4 import BeautifulSoup

DATA_DIR = Path(__file__).parent.parent / "data"
DOSSIER_DIR = DATA_DIR / "dossiers"

# Signal patterns — TARGET-OF-DEAL ONLY (company being acquired, not acquiring)
# Tightened to avoid false positives from asset sales / divestitures / recaps.
DEFINITIVE_PATTERNS = [
    r"agreement\s+and\s+plan\s+of\s+merger",
    r"to\s+be\s+acquired\s+by",
    r"agreed\s+to\s+be\s+acquired",
    r"merger\s+of\s+(the\s+)?company\s+with\s+and\s+into",
    r"going[- ]private\s+(transaction|proposal|merger)",
    r"take[- ]private\s+(transaction|deal|offer|proposal)",
    r"stockholders\s+(will|shall)\s+receive\s+\$",  # target-side consideration
    r"(merger|deal)\s+consideration\s+of\s+\$",
    r"all[- ](stock|cash)\s+(transaction|deal|acquisition|merger)\s+(to\s+acquire|with|valued)",
    r"non[- ]binding\s+(proposal|indication\s+of\s+interest)\s+to\s+acquire",
    r"definitive\s+merger\s+agreement",
]

# Patterns that often co-occur with asset-sale / divestiture language — used to
# DOWNGRADE definitive hits to non-deal events.
ASSET_SALE_NEGATORS = [
    r"sold\s+its\s+",
    r"divest(ed|iture)\s+of",
    r"sale\s+of\s+(the\s+)?(?:movies|broadcasting|publishing|wholesale)\s+",  # division names
    r"purchase\s+of\s+certain\s+assets",
    r"asset\s+purchase\s+agreement",  # often used for non-company purchases
    r"equity\s+purchase\s+agreement.{0,300}(division|business|segment|product\s+line)",
]

CLOSED_PATTERNS = [
    r"consummation\s+of\s+(the\s+)?merger",
    r"closing\s+of\s+(the\s+)?(merger|going[- ]private)",
    r"merger\s+(was|has\s+been)\s+(closed|consummated|completed)",
    r"company\s+(was|has\s+been)\s+acquired\s+by",
]

EXPLORING_PATTERNS = [
    r"strategic\s+alternatives",
    r"review\s+of\s+strategic\s+(options|alternatives)",
    r"evaluating\s+strategic\s+(options|alternatives)",
    r"exploring\s+(strategic\s+)?alternatives",
    r"engaged\s+(an?\s+)?(financial\s+)?advisor",
    r"retained\s+.{0,30}(financial\s+)?advisor",
    r"hired\s+.{0,30}(to\s+)?(advise|explore)",
    r"strategic\s+review",
    r"formal\s+process\s+to\s+explore",
]

TENDER_OFFER_PATTERNS = [
    r"tender\s+offer",
    r"dutch\s+auction\s+tender",
    r"modified\s+dutch\s+auction",
    r"self[- ]tender",
]

# Indicators that a tender offer is for DEBT (notes/bonds) not equity (shares)
# When present in the same 8-K, downgrade tender_offer signal — debt tender is
# refinancing, not a takeover bid.
DEBT_TENDER_NEGATORS = [
    r"PIK\s+Notes?",
    r"Senior\s+(Secured\s+|Unsecured\s+)?Notes?",
    r"Subordinated\s+Notes?",
    r"Convertible\s+Notes?",
    r"Term\s+Loan",
    r"\d{4}\s+Notes?\b",  # "2027 Notes", "2030 Senior Notes", etc.
    r"Debentures?",
    r"Indenture",
    r"consent\s+solicitation",  # almost always paired with debt tenders
]

ACQUIRER_PATTERNS = [  # disambiguation: ticker is BUYING someone else, not being bought
    r"to\s+acquire\s+[A-Z][a-zA-Z\s,]+(Inc|Corp|Ltd|LLC|Holdings|Group)",
    r"completed\s+the\s+acquisition\s+of\s+[A-Z]",
    r"agreement\s+to\s+acquire\s+[A-Z]",
]

# Recency: only flag 8-Ks from the last 24 months
import datetime
RECENCY_CUTOFF = (datetime.date.today() - datetime.timedelta(days=24 * 30)).isoformat()


def extract_text(html_path: Path) -> str:
    try:
        soup = BeautifulSoup(html_path.read_bytes(), "html.parser")
    except Exception:
        return ""
    for tag in soup(["script", "style"]):
        tag.decompose()
    return soup.get_text(separator=" ", strip=True)


def analyze(ticker: str):
    dossier_dir = DOSSIER_DIR / ticker.lower()
    filings_dir = dossier_dir / "edgar" / "filings"
    news_path = dossier_dir / "news.json"

    if not filings_dir.exists():
        return {"error": f"No filings directory at {filings_dir}. Run build_dossier first."}

    eight_ks = sorted(
        [p for p in filings_dir.glob("*_8-K_*.htm*")
         if p.name.split("_")[0] >= RECENCY_CUTOFF],
        reverse=True,
    )

    findings = {
        "ticker": ticker.upper(),
        "recency_cutoff": RECENCY_CUTOFF,
        "n_8ks_scanned": len(eight_ks),
        "signals": {
            "definitive_hits": [],
            "closed_hits": [],
            "exploring_hits": [],
            "tender_offer_hits": [],
            "acquirer_signals": [],
        },
        "news_signals": [],
    }

    for path in eight_ks:
        text = extract_text(path)
        if not text:
            continue
        text_lower = text.lower()

        # First check: is this 8-K dominated by asset-sale / divestiture language?
        # If so, downgrade any definitive hits to a "asset_sale" classification.
        is_asset_sale = any(
            re.search(neg, text_lower, re.IGNORECASE) for neg in ASSET_SALE_NEGATORS
        )
        # Second check: is this a debt tender / debt refinancing 8-K, not equity?
        is_debt_tender = any(
            re.search(neg, text, re.IGNORECASE) for neg in DEBT_TENDER_NEGATORS
        )

        def collect(patterns: list, bucket: str, suppress_if_asset_sale: bool = False,
                    suppress_if_debt: bool = False):
            if suppress_if_asset_sale and is_asset_sale:
                return
            if suppress_if_debt and is_debt_tender:
                return
            for pat in patterns:
                for m in re.finditer(pat, text_lower, re.IGNORECASE):
                    start = max(0, m.start() - 80)
                    end = min(len(text), m.end() + 80)
                    snippet = text[start:end].replace("\n", " ")[:300]
                    findings["signals"][bucket].append({
                        "file": path.name,
                        "pattern": pat,
                        "snippet": snippet,
                        "asset_sale_co_occurs": is_asset_sale,
                        "debt_tender_co_occurs": is_debt_tender,
                    })
                    return

        # Suppress definitive / closed when the same 8-K is clearly an asset sale.
        collect(DEFINITIVE_PATTERNS, "definitive_hits", suppress_if_asset_sale=True)
        collect(CLOSED_PATTERNS, "closed_hits", suppress_if_asset_sale=True)
        collect(EXPLORING_PATTERNS, "exploring_hits")
        # Suppress tender offers when accompanied by debt-instrument language.
        collect(TENDER_OFFER_PATTERNS, "tender_offer_hits", suppress_if_debt=True)
        collect(ACQUIRER_PATTERNS, "acquirer_signals")

    # ALSO scan recent earnings call transcripts for EXPLORING / DEFINITIVE language.
    # Management often signals strategic alternatives on calls BEFORE filing 8-Ks.
    transcripts_dir = dossier_dir / "transcripts"
    if transcripts_dir.exists():
        transcript_files = sorted(transcripts_dir.glob("*.txt"), reverse=True)[:6]
        for path in transcript_files:
            try:
                text = path.read_text(encoding="utf-8")
            except Exception:
                continue
            text_lower = text.lower()
            # Don't re-trigger definitive/closed from transcripts — those are 8-K-grade events.
            # Only scan for exploring language (mgmt commentary signals direction).
            for pat in EXPLORING_PATTERNS:
                m = re.search(pat, text_lower, re.IGNORECASE)
                if m:
                    start = max(0, m.start() - 80)
                    end = min(len(text), m.end() + 80)
                    snippet = text[start:end].replace("\n", " ")[:300]
                    findings["signals"]["exploring_hits"].append({
                        "file": f"transcripts/{path.name}",
                        "pattern": pat,
                        "snippet": snippet,
                        "source_type": "transcript",
                    })
                    break  # one hit per transcript

    # News file
    if news_path.exists():
        try:
            news = json.loads(news_path.read_text(encoding="utf-8"))
            for item in news[:30]:
                title = (item.get("title") or "").lower()
                summary = (item.get("summary") or "").lower()
                text = f"{title} {summary}"
                for pat in DEFINITIVE_PATTERNS + EXPLORING_PATTERNS:
                    if re.search(pat, text, re.IGNORECASE):
                        findings["news_signals"].append({
                            "date": (item.get("pub_date") or "")[:10],
                            "provider": item.get("provider"),
                            "title": item.get("title"),
                            "pattern": pat,
                        })
                        break
        except Exception:
            pass

    # Classify
    has_definitive = len(findings["signals"]["definitive_hits"]) > 0
    has_closed = len(findings["signals"]["closed_hits"]) > 0
    has_exploring = len(findings["signals"]["exploring_hits"]) > 0
    has_tender = len(findings["signals"]["tender_offer_hits"]) > 0
    has_acquirer_signal = len(findings["signals"]["acquirer_signals"]) > 0

    # Acquirer signals can confuse definitive — if there are MANY acquirer signals
    # and few/no other definitive signals, it might just be that THIS company
    # is acquiring others (not being acquired). Heuristic: if acquirer signals
    # are >=3x other definitive hits, treat as acquirer-mode and downgrade.
    if has_acquirer_signal and not has_definitive:
        status = "NONE_ACQUIRER_MODE"
        risk = "LOW"
        reasoning = ["Company is acquiring others, not being acquired. No target-of-deal signals."]
    elif has_closed:
        status = "CLOSED"
        risk = "DEAL_BREAKER"
        reasoning = [f"Transaction CLOSED ({len(findings['signals']['closed_hits'])} signals)."]
    elif has_definitive:
        status = "DEFINITIVE"
        risk = "DEAL_BREAKER"
        reasoning = [
            f"DEFINITIVE deal signals found ({len(findings['signals']['definitive_hits'])}); "
            "merger/acquisition agreement in place. Not usable for search-fund pitch."
        ]
    elif has_tender and not has_definitive:
        status = "TENDER_OFFER"
        risk = "MEDIUM"
        reasoning = [
            f"Tender offer detected ({len(findings['signals']['tender_offer_hits'])} signals). "
            "If company-initiated buyback, OK; if third-party takeover, problematic. Verify manually."
        ]
    elif has_exploring:
        status = "EXPLORING"
        risk = "HIGH"
        reasoning = [
            f"Strategic alternatives review detected ({len(findings['signals']['exploring_hits'])} signals). "
            "Could pivot to definitive at any time. Treat with caution."
        ]
    else:
        status = "NONE"
        risk = "LOW"
        reasoning = ["No deal signals in 8-Ks or news within trailing 24 months."]

    findings["status"] = status
    findings["risk_level"] = risk
    findings["reasoning"] = reasoning

    out_path = dossier_dir / "deal_status.json"
    dossier_dir.mkdir(parents=True, exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(findings, f, indent=2)

    # Console
    print(f"\n{'='*60}")
    print(f"DEAL STATUS — {ticker.upper()}")
    print(f"{'='*60}")
    print(f"Status: {status}")
    print(f"Risk:   {risk}")
    for r in reasoning:
        print(f"  - {r}")
    print()
    print(f"8-Ks scanned: {len(eight_ks)}")
    print(f"Definitive signals:   {len(findings['signals']['definitive_hits'])}")
    print(f"Closed signals:       {len(findings['signals']['closed_hits'])}")
    print(f"Exploring signals:    {len(findings['signals']['exploring_hits'])}")
    print(f"Tender offer signals: {len(findings['signals']['tender_offer_hits'])}")
    print(f"Acquirer-mode hits:   {len(findings['signals']['acquirer_signals'])}")
    print(f"News deal-language:   {len(findings['news_signals'])}")
    def _safe(s: str) -> str:
        return (s or "").encode("ascii", errors="replace").decode()

    for label, key in [("definitive", "definitive_hits"),
                       ("exploring", "exploring_hits"),
                       ("tender_offer", "tender_offer_hits"),
                       ("acquirer-mode", "acquirer_signals")]:
        hits = findings["signals"][key]
        if hits:
            print(f"\nTop {label} snippets:")
            for h in hits[:2]:
                print(f"  [{h['file']}] {_safe(h['snippet'])[:200]}...")
    print(f"\nSaved: {out_path}")
    return findings


def main():
    p = argparse.ArgumentParser()
    p.add_argument("ticker")
    args = p.parse_args()
    analyze(args.ticker)


if __name__ == "__main__":
    main()
