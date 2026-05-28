"""
Build a peer set for a candidate company from EXTERNAL sources (not the
filtered investable universe).

Sources used:
  1. 10-K Item 1 "Competition" section (company's self-described competitors)
  2. Web search via DuckDuckGo HTML ("{company} competitors", "{company} vs")
  3. stockanalysis.com competitors page (when available)
  4. yfinance enrichment for any public tickers identified

Output: data/dossiers/{ticker}/peers/
  - competition_section.txt  (raw text from 10-K Item 1)
  - peer_candidates.json     (all peer names found, with sources)
  - peer_table.json          (resolved tickers + light metrics)

Note: for high-stakes calibration, augment with manual WebSearch since
DDG is flaky and 10-K language can be generic.

Usage:
    python scripts/build_peer_set.py EXFY
"""

import argparse
import csv
import json
import re
import time
from datetime import date
from pathlib import Path

import requests
from bs4 import BeautifulSoup
import yfinance as yf

DATA_DIR = Path(__file__).parent.parent / "data"
DOSSIER_DIR = DATA_DIR / "dossiers"
RESEARCH_DIR = DATA_DIR / "research"

# Match scripts/valuation.py PEER_CSV_COLUMNS
PEER_CSV_COLUMNS = [
    "peer_ticker", "peer_name", "inclusion",
    "ev_ebitda", "ev_revenue", "ev_gross_profit", "ev_fcf",
    "revenue_growth_pct", "gross_margin", "ebitda_margin", "fcf_margin",
    "as_of_date", "source", "notes",
]

UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36"
HEADERS = {"User-Agent": UA}


# ---------- 10-K parse ----------

COMP_HEADERS = [
    r"Competition\b",
    r"Our\s+Competition\b",
    r"Competitive\s+Landscape\b",
    r"Competitors?\b",
]


def parse_competition_section(html_path: Path, max_chars: int = 6000) -> str:
    """Find the Competition subsection in 10-K Item 1, return as plain text."""
    if not html_path or not html_path.exists():
        return ""
    try:
        soup = BeautifulSoup(html_path.read_bytes(), "html.parser")
    except Exception:
        return ""
    for tag in soup(["script", "style"]):
        tag.decompose()
    text = soup.get_text(separator="\n", strip=True)

    for header in COMP_HEADERS:
        m = re.search(header, text, re.IGNORECASE)
        if m:
            start = m.start()
            # Take a chunk until the next major header (e.g., "Human Capital", "Properties")
            end_markers = [
                r"\nHuman\s+Capital\b",
                r"\nIntellectual\s+Property\b",
                r"\nGovernment\s+Regulation\b",
                r"\nEmployees\b",
                r"\nItem\s+1A\b",
                r"\nRisk\s+Factors\b",
            ]
            end = start + max_chars
            for em in end_markers:
                em_match = re.search(em, text[start:start + max_chars * 2])
                if em_match:
                    end = start + em_match.start()
                    break
            return text[start:end]
    return ""


# ---------- Web search ----------

def ddg_search(query: str, max_pages: int = 2):
    """DuckDuckGo HTML search. Returns list of {title, url, snippet}."""
    results = []
    url = "https://html.duckduckgo.com/html/"
    for page in range(max_pages):
        params = {"q": query, "s": page * 30}
        try:
            r = requests.post(url, data=params, headers=HEADERS, timeout=20)
            r.raise_for_status()
        except Exception:
            break
        soup = BeautifulSoup(r.text, "html.parser")
        for div in soup.find_all("div", class_="result"):
            link = div.find("a", class_="result__a")
            snippet = div.find("a", class_="result__snippet") or div.find("div", class_="result__snippet")
            if not link:
                continue
            results.append({
                "title": link.get_text(strip=True),
                "url": link.get("href", ""),
                "snippet": snippet.get_text(strip=True) if snippet else "",
            })
        time.sleep(1.0)
    return results


def extract_company_names(text: str) -> set:
    """Heuristic: find candidate company names in text.
    Looks for patterns like 'Foo Inc.', 'BarCorp', 'Baz Holdings', 'Acme Group'.
    """
    candidates = set()
    # Match phrases like "Acme Inc.", "ABC Holdings", "Foo Corp", "Bar Group"
    suffixes = r"(?:Inc\.?|Corp\.?|Corporation|LLC|Ltd\.?|Limited|Holdings?|Group|plc|N\.V\.|Co\.?)"
    pattern = re.compile(
        rf"\b([A-Z][a-zA-Z0-9.&'-]+(?:\s+[A-Z][a-zA-Z0-9.&'-]+){{0,3}}\s+{suffixes})\b"
    )
    for m in pattern.finditer(text):
        name = m.group(1).strip()
        if len(name) > 3 and len(name) < 60:
            candidates.add(name)
    # Common single-word brand names (uppercased) — be less greedy here.
    brand_pattern = re.compile(r"\b([A-Z][a-z]+(?:[A-Z][a-z]+)+)\b")
    for m in brand_pattern.finditer(text):
        name = m.group(1)
        if name not in candidates and len(name) > 4:
            candidates.add(name)
    return candidates


# ---------- Ticker resolution ----------

def resolve_to_ticker(company_name: str) -> str | None:
    """Try to map a company name to a public ticker via yfinance search."""
    try:
        # yfinance has a search method exposed via Search class
        from yfinance import Search
        s = Search(company_name, max_results=3)
        for q in s.quotes or []:
            sym = q.get("symbol")
            if sym and "-" not in sym and len(sym) <= 6:
                return sym
    except Exception:
        pass
    return None


# ---------- Light dossier ----------

def light_dossier(ticker: str) -> dict:
    """Pull a small set of yfinance metrics for a peer."""
    try:
        t = yf.Ticker(ticker)
        info = t.info
        return {
            "ticker": ticker,
            "name": info.get("shortName") or info.get("longName"),
            "country": info.get("country"),
            "industry": info.get("industry"),
            "market_cap": info.get("marketCap"),
            "enterprise_value": info.get("enterpriseValue"),
            "revenue_ttm": info.get("totalRevenue"),
            "revenue_growth": info.get("revenueGrowth"),
            "gross_margin": info.get("grossMargins"),
            "operating_margin": info.get("operatingMargins"),
            "fcf": info.get("freeCashflow"),
            "ev_to_revenue": info.get("enterpriseToRevenue"),
            "ev_to_ebitda": info.get("enterpriseToEbitda"),
            "analysts": info.get("numberOfAnalystOpinions"),
            "inst_ownership": info.get("heldPercentInstitutions"),
            "current_price": info.get("currentPrice"),
            "52wk_high": info.get("fiftyTwoWeekHigh"),
            "52wk_low": info.get("fiftyTwoWeekLow"),
        }
    except Exception as e:
        return {"ticker": ticker, "error": str(e)}


# ---------- Orchestration ----------

def build(ticker: str):
    dossier_dir = DOSSIER_DIR / ticker.lower()
    peers_dir = dossier_dir / "peers"
    peers_dir.mkdir(parents=True, exist_ok=True)

    print(f"Building peer set for {ticker}...")

    # Get company name
    try:
        info = yf.Ticker(ticker).info
        company_name = info.get("shortName") or info.get("longName") or ticker
    except Exception:
        company_name = ticker

    print(f"  Company: {company_name}")

    # Step 1: Parse Competition section from latest 10-K
    filings_dir = dossier_dir / "edgar" / "filings"
    tenk_files = sorted(filings_dir.glob("*_10-K_*.htm*"), reverse=True) if filings_dir.exists() else []
    competition_text = ""
    if tenk_files:
        print(f"  Parsing Competition section from {tenk_files[0].name}...")
        competition_text = parse_competition_section(tenk_files[0])
        (peers_dir / "competition_section.txt").write_text(competition_text, encoding="utf-8")
        print(f"    Extracted {len(competition_text)} chars")
    else:
        print(f"  No 10-K in dossier")

    names_from_10k = extract_company_names(competition_text)

    # Step 2: Web search
    print(f"  Searching web for competitors...")
    queries = [
        f"{company_name} top competitors",
        f"{company_name} vs",
        f"alternatives to {company_name}",
    ]
    web_results = []
    for q in queries:
        results = ddg_search(q, max_pages=2)
        web_results.extend(results)
        print(f"    '{q}': {len(results)} results")

    # Extract names from web result titles + snippets
    web_text = " ".join(
        f"{r['title']} {r['snippet']}" for r in web_results
    )
    names_from_web = extract_company_names(web_text)

    all_names = names_from_10k | names_from_web
    # Remove the company itself
    all_names = {n for n in all_names if ticker.upper() not in n.upper()
                 and company_name.split()[0].lower() not in n.lower()}

    # Save candidate names
    candidates = {
        "ticker": ticker.upper(),
        "company_name": company_name,
        "names_from_10k": sorted(names_from_10k),
        "names_from_web": sorted(names_from_web),
        "combined_unique": sorted(all_names),
        "n_web_results": len(web_results),
    }
    (peers_dir / "peer_candidates.json").write_text(json.dumps(candidates, indent=2))
    print(f"  Total unique peer candidates: {len(all_names)}")

    # Step 3: Resolve to tickers (limit to top ~15 candidates for time)
    print(f"  Resolving names to tickers (may take a moment)...")
    resolved = {}
    for name in list(all_names)[:25]:
        sym = resolve_to_ticker(name)
        if sym and sym != ticker.upper():
            resolved[sym] = name
        time.sleep(0.3)
    print(f"    Resolved {len(resolved)} unique tickers")

    # Step 4: Light dossier for each
    print(f"  Building light dossier for each resolved peer...")
    peer_table = []
    for sym, name in resolved.items():
        d = light_dossier(sym)
        d["resolved_from_name"] = name
        peer_table.append(d)
        time.sleep(0.3)

    # Sort by revenue desc
    peer_table.sort(key=lambda x: x.get("revenue_ttm") or 0, reverse=True)

    out_path = peers_dir / "peer_table.json"
    out_path.write_text(json.dumps(peer_table, indent=2, default=str))
    print(f"\n  Saved peer table: {out_path}")

    # Dual-write CSV format for valuation.py consumption
    write_peer_benchmarks_csv(ticker, peer_table)

    # Console summary
    print(f"\n{'='*70}")
    print(f"PEER SET — {ticker.upper()}")
    print(f"{'='*70}")
    print(f"{'Ticker':<8}{'Name':<32}{'Country':<14}{'Rev_TTM':<12}{'EV/Rev':<8}")
    for p in peer_table[:15]:
        if "error" in p:
            continue
        name = (p.get("name") or "")[:30]
        rev = p.get("revenue_ttm") or 0
        ev_rev = p.get("ev_to_revenue")
        rev_s = f"${rev/1e6:.0f}M" if rev else "N/A"
        ev_rev_s = f"{ev_rev:.2f}x" if ev_rev else "N/A"
        print(f"{p['ticker']:<8}{name:<32}{(p.get('country') or '')[:13]:<14}{rev_s:<12}{ev_rev_s:<8}")

    print(f"\nNOTE: Many real-world peers may be private (e.g., Brex, Ramp, Coupa).")
    print(f"Augment manually via WebSearch at calibration time if peer set looks thin.")

    return peer_table


def _row_from_peer(p: dict, inclusion: str = "primary") -> dict:
    """Convert a peer light-dossier dict into a peer_benchmarks.csv row."""
    ev = p.get("enterprise_value")
    rev = p.get("revenue_ttm")
    gm = p.get("gross_margin")
    om = p.get("operating_margin")
    fcf = p.get("fcf")
    ev_rev = p.get("ev_to_revenue")
    ev_ebitda = p.get("ev_to_ebitda")

    # Derived metrics
    ev_gross_profit = None
    if ev and rev and gm:
        gross_profit = rev * gm
        if gross_profit > 0:
            ev_gross_profit = round(ev / gross_profit, 2)

    ev_fcf = None
    if ev and fcf and fcf > 0:
        ev_fcf = round(ev / fcf, 2)

    fcf_margin = None
    if fcf is not None and rev:
        fcf_margin = round((fcf / rev) * 100, 1)

    revenue_growth_pct = None
    rg = p.get("revenue_growth")
    if rg is not None:
        revenue_growth_pct = round(rg * 100, 1)

    return {
        "peer_ticker": p.get("ticker", ""),
        "peer_name": p.get("name") or "",
        "inclusion": inclusion,
        "ev_ebitda": round(ev_ebitda, 2) if ev_ebitda else "",
        "ev_revenue": round(ev_rev, 2) if ev_rev else "",
        "ev_gross_profit": ev_gross_profit if ev_gross_profit else "",
        "ev_fcf": ev_fcf if ev_fcf else "",
        "revenue_growth_pct": revenue_growth_pct if revenue_growth_pct is not None else "",
        "gross_margin": round(gm * 100, 1) if gm else "",
        "ebitda_margin": "",  # not directly in our light dossier
        "fcf_margin": fcf_margin if fcf_margin is not None else "",
        "as_of_date": date.today().isoformat(),
        "source": p.get("source", "yfinance"),
        "notes": "",
    }


def write_peer_benchmarks_csv(ticker: str, peer_table: list[dict]):
    """Write data/research/{ticker}/peer_benchmarks.csv from peer_table.json.

    The subject ticker is added as inclusion='subject'; all others default to 'primary'.
    This is the format consumed by scripts/valuation.py.
    """
    ticker_lower = ticker.lower()
    out_dir = RESEARCH_DIR / ticker_lower
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / "peer_benchmarks.csv"

    # Build subject anchor row from the candidate's own dossier
    subject_info_path = DOSSIER_DIR / ticker_lower / "yfinance_info.json"
    rows = []
    if subject_info_path.exists():
        try:
            info = json.loads(subject_info_path.read_text(encoding="utf-8"))
            subject_p = {
                "ticker": ticker.upper(),
                "name": info.get("shortName") or info.get("longName") or ticker.upper(),
                "enterprise_value": info.get("enterpriseValue"),
                "revenue_ttm": info.get("totalRevenue"),
                "revenue_growth": info.get("revenueGrowth"),
                "gross_margin": info.get("grossMargins"),
                "operating_margin": info.get("operatingMargins"),
                "fcf": info.get("freeCashflow"),
                "ev_to_revenue": info.get("enterpriseToRevenue"),
                "ev_to_ebitda": info.get("enterpriseToEbitda"),
                "source": "yfinance",
            }
            rows.append(_row_from_peer(subject_p, inclusion="subject"))
        except Exception as e:
            print(f"  (could not load subject info: {e})")

    for p in peer_table:
        if "error" in p:
            continue
        if (p.get("ticker") or "").upper() == ticker.upper():
            continue  # Already added as subject
        rows.append(_row_from_peer(p, inclusion="primary"))

    with open(out_path, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=PEER_CSV_COLUMNS)
        w.writeheader()
        for row in rows:
            w.writerow(row)
    print(f"  Wrote {len(rows)} rows (incl subject) to {out_path}")
    return out_path


def _subject_industry(ticker: str) -> tuple[str | None, str | None]:
    """Get the subject's (industry, sector) from its dossier yfinance_info.json."""
    info_path = DOSSIER_DIR / ticker.lower() / "yfinance_info.json"
    if not info_path.exists():
        return None, None
    try:
        info = json.loads(info_path.read_text(encoding="utf-8"))
    except Exception:
        return None, None
    return info.get("industry"), info.get("sector")


# Industries that are clearly NOT plausible peers regardless of subject.
# Used to flag obvious mistakes (e.g., POWL = Powell Industries — electrical
# industrials — accidentally added to NRDY's edtech peer set).
INDUSTRY_RED_FLAGS = {
    "Electrical Equipment & Parts", "Industrial Distribution", "Farm & Heavy Construction Machinery",
    "Oil & Gas", "Banks", "Insurance", "Mining", "Steel", "Aluminum",
    "Pharmaceutical Manufacturers", "Biotechnology", "Medical Devices",
    "REIT", "Utilities", "Tobacco",
}


def _peer_is_plausible(peer_industry: str | None, peer_sector: str | None,
                       subject_industry: str | None, subject_sector: str | None) -> tuple[bool, str]:
    """Returns (is_plausible, reason). Permissive — only flags clear mismatches."""
    if not peer_industry:
        return True, "no industry info — accepted but flag for manual review"
    if peer_industry in INDUSTRY_RED_FLAGS:
        return False, f"industry '{peer_industry}' is in red-flag list"
    # If sectors differ entirely (e.g. Technology vs Energy), flag.
    if subject_sector and peer_sector and subject_sector != peer_sector:
        # Allow some cross-sector pairings (Communication Services ↔ Technology
        # for media+software companies, etc.) — only flag distant pairs.
        allowed_cross_sector = {
            frozenset({"Technology", "Communication Services"}),
            frozenset({"Technology", "Consumer Cyclical"}),  # media/internet
            frozenset({"Communication Services", "Consumer Cyclical"}),
        }
        if frozenset({subject_sector, peer_sector}) not in allowed_cross_sector:
            return False, f"sector mismatch: subject={subject_sector}, peer={peer_sector}"
    return True, "ok"


def add_manual_peers(ticker: str, peer_tickers: list[str], force: bool = False):
    """Append manually-curated peer tickers (e.g., from WebSearch research) to the peer table.

    Performs sanity checks:
      - Skip peers whose yfinance returns no data (likely delisted / private)
      - Skip peers in industries that don't match the subject's sector (unless --force)
    """
    dossier_dir = DOSSIER_DIR / ticker.lower()
    peers_dir = dossier_dir / "peers"
    peers_dir.mkdir(parents=True, exist_ok=True)

    subject_industry, subject_sector = _subject_industry(ticker)
    print(f"  Subject {ticker.upper()}: sector={subject_sector}, industry={subject_industry}")

    out_path = peers_dir / "peer_table.json"
    existing = []
    if out_path.exists():
        try:
            existing = json.loads(out_path.read_text())
        except Exception:
            existing = []

    existing_tickers = {p.get("ticker", "").upper() for p in existing}
    added = []
    skipped = []
    for sym in peer_tickers:
        sym = sym.upper().strip()
        if not sym or sym == ticker.upper() or sym in existing_tickers:
            continue
        print(f"  Pulling light dossier for {sym}...")
        d = light_dossier(sym)
        # Skip if yfinance returned no usable data (delisted / private / fat-fingered)
        has_data = bool(d.get("market_cap") or d.get("revenue_ttm") or d.get("name"))
        if not has_data:
            print(f"    [skip] {sym}: no yfinance data (likely delisted/private/typo)")
            skipped.append((sym, "no_data"))
            time.sleep(0.3)
            continue
        # Industry sanity check
        is_plausible, reason = _peer_is_plausible(
            d.get("industry"), d.get("sector"), subject_industry, subject_sector
        )
        if not is_plausible and not force:
            print(f"    [skip] {sym} ({d.get('name')}): {reason}")
            skipped.append((sym, reason))
            time.sleep(0.3)
            continue
        d["source"] = "manual"
        existing.append(d)
        added.append(sym)
        time.sleep(0.3)

    existing.sort(key=lambda x: x.get("revenue_ttm") or 0, reverse=True)
    out_path.write_text(json.dumps(existing, indent=2, default=str))
    print(f"\nAdded {len(added)} peer(s): {', '.join(added)}")
    if skipped:
        print(f"Skipped {len(skipped)} peer(s):")
        for sym, reason in skipped:
            print(f"  - {sym}: {reason}")
        print("(Use --force to override industry/sector mismatch skipping.)")
    print(f"Total peers in table: {len(existing)}")
    print(f"Saved: {out_path}")

    # Dual-write CSV format for valuation.py consumption
    write_peer_benchmarks_csv(ticker, existing)

    # Print summary table
    print(f"\n{'Ticker':<8}{'Name':<32}{'Country':<14}{'Rev_TTM':<12}{'EV/Rev':<10}{'Source':<8}")
    for p in existing:
        if "error" in p:
            continue
        name = (p.get("name") or "")[:30]
        rev = p.get("revenue_ttm") or 0
        ev_rev = p.get("ev_to_revenue")
        rev_s = f"${rev/1e6:.0f}M" if rev else "N/A"
        ev_rev_s = f"{ev_rev:.2f}x" if ev_rev else "N/A"
        src = p.get("source", "auto")
        print(f"{p['ticker']:<8}{name:<32}{(p.get('country') or '')[:13]:<14}{rev_s:<12}{ev_rev_s:<10}{src:<8}")


def main():
    p = argparse.ArgumentParser()
    p.add_argument("ticker")
    p.add_argument("--add", type=str, default=None,
                   help="Comma-separated peer tickers to add manually (from WebSearch research)")
    p.add_argument("--force", action="store_true",
                   help="Override industry/sector mismatch skipping when adding peers")
    args = p.parse_args()
    if args.add:
        peer_tickers = [t.strip() for t in args.add.split(",") if t.strip()]
        add_manual_peers(args.ticker, peer_tickers, force=args.force)
    else:
        build(args.ticker)


if __name__ == "__main__":
    main()
