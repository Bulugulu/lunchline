"""
Fetch SEC EDGAR filings for candidate companies.
Downloads filing metadata, XBRL financials, and primary document content.

Filing types supported: 10-K, 10-Q, 8-K, DEF 14A, Form 4.

Usage:
    python scripts/fetch_edgar.py EXFY                          # Default filing types + content download
    python scripts/fetch_edgar.py EXFY --xbrl                   # Also pull XBRL structured financials
    python scripts/fetch_edgar.py EXFY --types 10-K,10-Q        # Custom filing types
    python scripts/fetch_edgar.py EXFY --no-content             # Metadata only, no document download
    python scripts/fetch_edgar.py EXFY --limit 5                # Cap downloads per filing type
"""

import argparse
import json
import sys
import time
from pathlib import Path

import requests
import pandas as pd

DATA_DIR = Path(__file__).parent.parent / "data"
EDGAR_DIR = DATA_DIR / "edgar"
EDGAR_DIR.mkdir(parents=True, exist_ok=True)

HEADERS = {
    "User-Agent": "LunchlineResearch avivsheriff@gmail.com",
    "Accept-Encoding": "gzip, deflate",
}

CANDIDATE_TICKERS = [
    # Populated after framework-driven screening — see docs/selection-framework.md
]

TICKER_TO_CIK = {}


def get_cik(ticker: str) -> str:
    if ticker in TICKER_TO_CIK:
        return TICKER_TO_CIK[ticker]

    cache_path = EDGAR_DIR / "ticker_cik_map.json"
    if cache_path.exists():
        with open(cache_path) as f:
            mapping = json.load(f)
        if ticker.upper() in mapping:
            TICKER_TO_CIK[ticker] = mapping[ticker.upper()]
            return mapping[ticker.upper()]

    url = "https://www.sec.gov/files/company_tickers.json"
    resp = requests.get(url, headers=HEADERS)
    resp.raise_for_status()
    raw = resp.json()

    mapping = {}
    for entry in raw.values():
        t = entry["ticker"].upper()
        cik = str(entry["cik_str"]).zfill(10)
        mapping[t] = cik

    with open(cache_path, "w") as f:
        json.dump(mapping, f, indent=2)

    cik = mapping.get(ticker.upper())
    if cik:
        TICKER_TO_CIK[ticker] = cik
    return cik


DEFAULT_FILING_TYPES = ("10-K", "10-Q", "8-K", "DEF 14A", "4")

# Per-type download caps so 100s of 8-Ks/Form 4s don't blow up disk.
DEFAULT_LIMITS = {
    "10-K": 5,
    "10-Q": 8,
    "8-K": 20,
    "DEF 14A": 3,
    "4": 30,
}


def fetch_filings(ticker: str, filing_types=DEFAULT_FILING_TYPES, download_content=True, limits=None):
    cik = get_cik(ticker)
    if not cik:
        print(f"  Could not find CIK for {ticker}")
        return None

    if limits is None:
        limits = DEFAULT_LIMITS

    print(f"  CIK: {cik}")
    url = f"https://data.sec.gov/submissions/CIK{cik}.json"
    resp = requests.get(url, headers=HEADERS)
    resp.raise_for_status()
    data = resp.json()

    ticker_dir = EDGAR_DIR / ticker.lower()
    ticker_dir.mkdir(exist_ok=True)
    filings_dir = ticker_dir / "filings"
    filings_dir.mkdir(exist_ok=True)

    company_path = ticker_dir / "submissions.json"
    with open(company_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"  Saved submission data: {company_path}")

    recent = data.get("filings", {}).get("recent", {})
    if not recent:
        print("  No recent filings found")
        return data

    forms = recent.get("form", [])
    dates = recent.get("filingDate", [])
    accessions = recent.get("accessionNumber", [])
    primary_docs = recent.get("primaryDocument", [])
    descriptions = recent.get("primaryDocDescription", [])

    # Group by form type so per-type limits work
    by_form = {ft: [] for ft in filing_types}
    for i, form in enumerate(forms):
        if form in filing_types and i < len(primary_docs):
            by_form[form].append({
                "form": form,
                "filingDate": dates[i] if i < len(dates) else None,
                "accessionNumber": accessions[i] if i < len(accessions) else None,
                "primaryDocument": primary_docs[i],
                "description": descriptions[i] if i < len(descriptions) else None,
                "url": f"https://www.sec.gov/Archives/edgar/data/{cik.lstrip('0')}/{accessions[i].replace('-', '')}/{primary_docs[i]}",
            })

    all_filings = []
    for ft, items in by_form.items():
        cap = limits.get(ft, 10)
        all_filings.extend(items[:cap])

    filings_path = ticker_dir / "filings_index.json"
    with open(filings_path, "w") as f:
        json.dump(all_filings, f, indent=2)
    print(f"  Indexed {len(all_filings)} filings across {', '.join(filing_types)}")
    by_form_counts = {ft: len(items[:limits.get(ft, 10)]) for ft, items in by_form.items()}
    for ft, n in by_form_counts.items():
        print(f"    {ft}: {n}")

    if download_content and all_filings:
        print(f"\n  Downloading primary documents to {filings_dir}...")
        for f_meta in all_filings:
            safe_form = f_meta["form"].replace(" ", "_").replace("/", "_")
            ext = Path(f_meta["primaryDocument"]).suffix or ".htm"
            out_name = f"{f_meta['filingDate']}_{safe_form}_{f_meta['accessionNumber']}{ext}"
            out_path = filings_dir / out_name
            if out_path.exists():
                continue
            try:
                r = requests.get(f_meta["url"], headers=HEADERS, timeout=30)
                if r.status_code == 200:
                    out_path.write_bytes(r.content)
                else:
                    print(f"    {f_meta['form']} {f_meta['filingDate']}: HTTP {r.status_code}")
            except Exception as e:
                print(f"    {f_meta['form']} {f_meta['filingDate']}: {e}")
            time.sleep(0.15)  # SEC rate limit 10 req/sec
        downloaded = list(filings_dir.glob("*.htm*")) + list(filings_dir.glob("*.txt"))
        print(f"  Downloaded {len(downloaded)} primary documents")

    return data


def fetch_xbrl_financials(ticker: str):
    cik = get_cik(ticker)
    if not cik:
        print(f"  Could not find CIK for {ticker}")
        return

    url = f"https://data.sec.gov/api/xbrl/companyfacts/CIK{cik}.json"
    resp = requests.get(url, headers=HEADERS)
    if resp.status_code == 404:
        print(f"  No XBRL data available for {ticker}")
        return
    resp.raise_for_status()
    data = resp.json()

    ticker_dir = EDGAR_DIR / ticker.lower()
    ticker_dir.mkdir(exist_ok=True)
    xbrl_path = ticker_dir / "xbrl.json"
    with open(xbrl_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"  Saved XBRL company facts: {xbrl_path}")

    us_gaap = data.get("facts", {}).get("us-gaap", {})
    key_metrics = [
        "Revenues", "RevenueFromContractWithCustomerExcludingAssessedTax",
        "NetIncomeLoss", "OperatingIncomeLoss", "GrossProfit",
        "Assets", "Liabilities", "StockholdersEquity",
        "CashAndCashEquivalentsAtCarryingValue",
        "LongTermDebt", "EarningsPerShareBasic",
        "OperatingCashFlow", "FreeCashFlow",
    ]

    found = []
    for metric in key_metrics:
        if metric in us_gaap:
            units = us_gaap[metric].get("units", {})
            for unit_type, entries in units.items():
                if entries:
                    latest = [e for e in entries if e.get("form") in ("10-K", "10-Q")]
                    latest.sort(key=lambda x: x.get("end", ""), reverse=True)
                    if latest:
                        found.append({
                            "metric": metric,
                            "value": latest[0].get("val"),
                            "period_end": latest[0].get("end"),
                            "form": latest[0].get("form"),
                            "unit": unit_type,
                        })

    if found:
        df = pd.DataFrame(found)
        print(f"\n  Key XBRL metrics:")
        print(df.to_string(index=False))
        csv_path = ticker_dir / "xbrl_summary.csv"
        df.to_csv(csv_path, index=False)
        print(f"  Saved: {csv_path}")


def main():
    parser = argparse.ArgumentParser(description="Fetch SEC EDGAR filings")
    parser.add_argument("ticker", nargs="?", help="Ticker symbol")
    parser.add_argument("--all", action="store_true", help="Fetch all candidates")
    parser.add_argument("--xbrl", action="store_true", help="Also fetch XBRL financial data")
    parser.add_argument("--types", type=str, default=None,
                        help="Comma-separated filing types (default: 10-K,10-Q,8-K,DEF 14A,4)")
    parser.add_argument("--no-content", action="store_true",
                        help="Skip downloading primary document HTML")
    parser.add_argument("--limit", type=int, default=None,
                        help="Cap downloads per filing type (overrides per-type defaults)")
    args = parser.parse_args()

    if args.all:
        tickers = CANDIDATE_TICKERS
    elif args.ticker:
        tickers = [args.ticker.upper()]
    else:
        print("Provide a ticker or use --all")
        sys.exit(1)

    if args.types:
        filing_types = tuple(t.strip() for t in args.types.split(","))
    else:
        filing_types = DEFAULT_FILING_TYPES

    limits = None
    if args.limit is not None:
        limits = {ft: args.limit for ft in filing_types}

    for ticker in tickers:
        print(f"\n{'='*50}")
        print(f"Fetching EDGAR data for {ticker}")
        print(f"{'='*50}")
        fetch_filings(ticker, filing_types=filing_types,
                      download_content=not args.no_content, limits=limits)
        if args.xbrl:
            print()
            fetch_xbrl_financials(ticker)
        time.sleep(0.2)


if __name__ == "__main__":
    main()
