"""
Detect dual/triple-class share structures, voting trusts, and controlled-company
status from SEC filings. Surfaces governance deal-breakers BEFORE deep scoring
(e.g., EXFY's 83.6% Voting Trust would have flagged at this stage).

Reads from a candidate's dossier (data/dossiers/{ticker}/edgar/filings/):
  - Latest DEF 14A (proxy) — beneficial ownership table, voting power %
  - Latest 10-K — capital stock note, controlled company disclosure

Outputs:
  - data/dossiers/{ticker}/voting_structure.json
  - Risk classification: LOW / MEDIUM / HIGH / DEAL_BREAKER

Usage:
    python scripts/check_voting_structure.py EXFY
"""

import argparse
import json
import re
from pathlib import Path

from bs4 import BeautifulSoup

DATA_DIR = Path(__file__).parent.parent / "data"
DOSSIER_DIR = DATA_DIR / "dossiers"

# Heuristic signal patterns
CLASS_PATTERNS = [
    r"\bClass\s+[ABCDE]\b",
    r"\bSeries\s+[ABCDE]\b",
    r"\b(LT10|LT50|HV)\b",  # special voting share names
]
TRUST_PATTERNS = [
    r"voting\s+trust",
    r"Voting\s+Trust",
]
CONTROLLED_COMPANY_PATTERNS = [
    r"controlled\s+company",
    r"controlled[- ]company\s+exemption",
]
VOTING_POWER_PATTERN = re.compile(
    r"(?:approximately\s+)?(\d{1,3}(?:\.\d+)?)\s*%\s+of\s+(?:the\s+)?(?:total\s+)?voting\s+power",
    re.IGNORECASE,
)
ECONOMIC_INTEREST_PATTERN = re.compile(
    r"(\d{1,3}(?:\.\d+)?)\s*%\s+of\s+(?:the\s+)?economic\s+interest",
    re.IGNORECASE,
)
SUPER_VOTING_RATIO_DIGIT = re.compile(
    r"(\d{1,3})\s+vote[s]?\s+per\s+share",
    re.IGNORECASE,
)
# Word-number variants common in proxy filings ("ten votes per share")
WORD_TO_NUM = {
    "one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7,
    "eight": 8, "nine": 9, "ten": 10, "fifteen": 15, "twenty": 20, "twenty-five": 25,
    "thirty": 30, "forty": 40, "fifty": 50, "seventy-five": 75, "one hundred": 100,
}
SUPER_VOTING_RATIO_WORD = re.compile(
    r"\b(one|two|three|four|five|six|seven|eight|nine|ten|fifteen|twenty|thirty|forty|fifty|seventy-five|one\s+hundred)\s+vote[s]?\s+per\s+share",
    re.IGNORECASE,
)


def extract_text(html_path: Path) -> str:
    """Extract clean text from an SEC filing HTML."""
    try:
        soup = BeautifulSoup(html_path.read_bytes(), "html.parser")
    except Exception:
        return ""
    for tag in soup(["script", "style"]):
        tag.decompose()
    return soup.get_text(separator=" ", strip=True)


def find_latest(filings_dir: Path, form_pattern: str) -> Path | None:
    """Find the most recent filing of a given form type by filename date prefix."""
    candidates = sorted(filings_dir.glob(f"*_{form_pattern}_*.htm*"), reverse=True)
    return candidates[0] if candidates else None


def analyze(ticker: str):
    dossier_dir = DOSSIER_DIR / ticker.lower()
    filings_dir = dossier_dir / "edgar" / "filings"
    if not filings_dir.exists():
        return {"error": f"No filings directory at {filings_dir}. Run build_dossier first."}

    proxy_path = find_latest(filings_dir, "DEF_14A")
    tenk_path = find_latest(filings_dir, "10-K")

    findings = {
        "ticker": ticker.upper(),
        "sources": {
            "proxy": str(proxy_path) if proxy_path else None,
            "10k": str(tenk_path) if tenk_path else None,
        },
        "signals": {
            "share_classes_detected": [],
            "voting_trust_mentioned": False,
            "controlled_company_status": False,
            "super_voting_ratios": [],
            "voting_power_concentrations": [],  # list of (%, surrounding context)
            "economic_interest_concentrations": [],
        },
    }

    combined_text = ""
    if proxy_path:
        combined_text += extract_text(proxy_path) + "\n\n"
    if tenk_path:
        combined_text += extract_text(tenk_path)

    if not combined_text:
        findings["error"] = "Could not extract text from any filing"
        findings["risk_level"] = "UNKNOWN"
        return findings

    # Detect share classes (limit to first 10 unique matches)
    # Normalize non-breaking spaces (\xa0) and collapse internal whitespace to
    # avoid duplicate detections like "Class A" vs "Class\xa0A".
    classes = set()
    for pat in CLASS_PATTERNS:
        for m in re.findall(pat, combined_text):
            normalized = re.sub(r"\s+", " ", m.replace("\xa0", " ")).strip()
            classes.add(normalized)
            if len(classes) >= 10:
                break
    findings["signals"]["share_classes_detected"] = sorted(classes)

    # Voting trust
    for pat in TRUST_PATTERNS:
        if re.search(pat, combined_text):
            findings["signals"]["voting_trust_mentioned"] = True
            break

    # Controlled company
    for pat in CONTROLLED_COMPANY_PATTERNS:
        if re.search(pat, combined_text, re.IGNORECASE):
            findings["signals"]["controlled_company_status"] = True
            break

    # Super-voting ratios — digit form (e.g., "10 votes per share", "50 votes per share")
    for m in SUPER_VOTING_RATIO_DIGIT.finditer(combined_text):
        try:
            ratio = int(m.group(1))
            if 2 <= ratio <= 100 and ratio not in findings["signals"]["super_voting_ratios"]:
                findings["signals"]["super_voting_ratios"].append(ratio)
        except ValueError:
            pass

    # Super-voting ratios — word form (e.g., "ten votes per share")
    # Also captures "one vote per share" (used to distinguish 1:1 multi-class from
    # super-voting multi-class).
    all_vote_ratios_word = set()
    for m in SUPER_VOTING_RATIO_WORD.finditer(combined_text):
        word = m.group(1).lower().replace("\xa0", " ").strip()
        ratio = WORD_TO_NUM.get(word)
        if ratio is None:
            continue
        all_vote_ratios_word.add(ratio)
        if ratio >= 2 and ratio not in findings["signals"]["super_voting_ratios"]:
            findings["signals"]["super_voting_ratios"].append(ratio)

    # Capture "all 1-vote" multi-class signal (NRDY case: dual-class but 1:1 voting)
    findings["signals"]["all_vote_ratios_observed"] = sorted(
        set(findings["signals"]["super_voting_ratios"]) | all_vote_ratios_word | {1}
        if findings["signals"]["share_classes_detected"] else set()
    )
    findings["signals"]["one_vote_per_share_observed"] = 1 in all_vote_ratios_word

    # Voting power concentration mentions
    for m in VOTING_POWER_PATTERN.finditer(combined_text):
        try:
            pct = float(m.group(1))
            if pct > 5:  # ignore tiny mentions
                start = max(0, m.start() - 120)
                end = min(len(combined_text), m.end() + 120)
                context = combined_text[start:end].replace("\n", " ")
                findings["signals"]["voting_power_concentrations"].append({
                    "pct": pct,
                    "context": context[:300],
                })
        except ValueError:
            pass

    # Economic interest mentions (key for detecting wedge between econ + voting)
    for m in ECONOMIC_INTEREST_PATTERN.finditer(combined_text):
        try:
            pct = float(m.group(1))
            if pct > 1:
                start = max(0, m.start() - 120)
                end = min(len(combined_text), m.end() + 120)
                context = combined_text[start:end].replace("\n", " ")
                findings["signals"]["economic_interest_concentrations"].append({
                    "pct": pct,
                    "context": context[:300],
                })
        except ValueError:
            pass

    # ===== Risk classification =====
    multi_class = sum(1 for c in findings["signals"]["share_classes_detected"]
                     if re.match(r"^Class\s+[ABCDE]$", c)) >= 2
    has_super_voting = any(r >= 2 for r in findings["signals"]["super_voting_ratios"])
    # Distinguish: multi-class WITH 1:1 voting (NRDY) is NOT a take-private blocker.
    # We mark this when (a) multi-class detected AND (b) the only ratio found is 1
    # OR no ratios >=2 were detected AND "one vote per share" was observed.
    one_vote_only = (
        multi_class
        and not has_super_voting
        and findings["signals"]["one_vote_per_share_observed"]
    )
    voting_trust = findings["signals"]["voting_trust_mentioned"]
    controlled = findings["signals"]["controlled_company_status"]

    # Largest single voting concentration mentioned
    max_voting_concentration = max(
        (v["pct"] for v in findings["signals"]["voting_power_concentrations"]),
        default=0,
    )

    risk = "LOW"
    reasoning = []

    if voting_trust and max_voting_concentration >= 50:
        risk = "DEAL_BREAKER"
        reasoning.append(
            f"Voting trust controls {max_voting_concentration}% of voting power "
            "— hostile/unsolicited take-private structurally impossible."
        )
    elif max_voting_concentration >= 50 and has_super_voting:
        ratios_str = "/".join(str(r) for r in findings["signals"]["super_voting_ratios"])
        risk = "DEAL_BREAKER"
        reasoning.append(
            f"Founder/insider voting concentration of {max_voting_concentration}% "
            f"via super-voting class ({ratios_str} votes per share) "
            "— blocks hostile take-private."
        )
    elif max_voting_concentration >= 50 and multi_class and one_vote_only:
        # Multi-class but all 1-vote: concentration matters but no structural blocker.
        risk = "HIGH"
        reasoning.append(
            f"Multi-class structure with 1:1 voting (no super-voting); "
            f"insider voting at {max_voting_concentration}% — significant blocking stake "
            "but not a structural take-private blocker."
        )
    elif max_voting_concentration >= 50 and multi_class:
        # Multi-class detected, concentration high, ratios unknown — conservative DEAL_BREAKER
        risk = "DEAL_BREAKER"
        reasoning.append(
            f"Multi-class share structure with insider voting at {max_voting_concentration}%; "
            "vote ratios per class were not extractable from the proxy — manual verification needed. "
            "Conservatively flagged as deal-breaker."
        )
    elif controlled and max_voting_concentration >= 30:
        risk = "HIGH"
        reasoning.append(
            "Controlled-company status under Nasdaq exemption; "
            f"insider voting at {max_voting_concentration}%."
        )
    elif multi_class and has_super_voting:
        risk = "HIGH"
        reasoning.append(
            "Multi-class structure with super-voting shares present "
            f"({'/'.join(str(r) for r in findings['signals']['super_voting_ratios'])} "
            "votes per share). Verify concentration manually."
        )
    elif multi_class and one_vote_only:
        risk = "LOW"
        reasoning.append(
            "Multi-class share structure detected, BUT all classes have 1 vote per share "
            "(no super-voting). Capital structure complexity only; no take-private blocker."
        )
    elif multi_class:
        risk = "MEDIUM"
        reasoning.append("Multi-class share structure detected; vote ratios not extractable — verify manually.")
    elif controlled:
        risk = "MEDIUM"
        reasoning.append("Controlled-company status — verify voting structure.")

    if not reasoning:
        reasoning.append("No dual-class, voting trust, or controlled-company signals detected.")

    findings["risk_level"] = risk
    findings["reasoning"] = reasoning

    # Persist
    out_path = dossier_dir / "voting_structure.json"
    dossier_dir.mkdir(parents=True, exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(findings, f, indent=2)
    print(f"Saved: {out_path}")

    # Console summary
    print(f"\n{'='*60}")
    print(f"VOTING STRUCTURE — {ticker.upper()}")
    print(f"{'='*60}")
    print(f"Risk level: {risk}")
    for r in reasoning:
        print(f"  - {r}")
    print()
    s = findings["signals"]
    print(f"Share classes detected:        {', '.join(s['share_classes_detected']) or 'None'}")
    print(f"Voting trust mentioned:        {s['voting_trust_mentioned']}")
    print(f"Controlled-company status:     {s['controlled_company_status']}")
    print(f"Super-voting ratios found:     {s['super_voting_ratios']}")
    print(f"Max voting concentration cited: {max_voting_concentration}%")
    if s["economic_interest_concentrations"]:
        wedges = [v["pct"] for v in s["economic_interest_concentrations"]]
        print(f"Economic interest concentrations: {wedges} (wedge between econ + voting suggests dual-class)")

    return findings


def main():
    p = argparse.ArgumentParser()
    p.add_argument("ticker")
    args = p.parse_args()
    analyze(args.ticker)


if __name__ == "__main__":
    main()
