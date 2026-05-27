"""
Fetch SEC EDGAR filings for candidate companies.
Downloads 10-K and 10-Q filing metadata and XBRL financials.

Usage:
    python scripts/fetch_edgar.py MCHX          # Fetch filings for one ticker
    python scripts/fetch_edgar.py --all          # Fetch for all candidates
    python scripts/fetch_edgar.py MCHX --xbrl   # Also pull XBRL financial data
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


def fetch_filings(ticker: str, filing_types=("10-K", "10-Q")):
    cik = get_cik(ticker)
    if not cik:
        print(f"  Could not find CIK for {ticker}")
        return None

    print(f"  CIK: {cik}")
    url = f"https://data.sec.gov/submissions/CIK{cik}.json"
    resp = requests.get(url, headers=HEADERS)
    resp.raise_for_status()
    data = resp.json()

    company_path = EDGAR_DIR / f"{ticker.lower()}_submissions.json"
    with open(company_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"  Saved full submission data: {company_path}")

    recent = data.get("filings", {}).get("recent", {})
    if not recent:
        print("  No recent filings found")
        return data

    forms = recent.get("form", [])
    dates = recent.get("filingDate", [])
    accessions = recent.get("accessionNumber", [])
    primary_docs = recent.get("primaryDocument", [])
    descriptions = recent.get("primaryDocDescription", [])

    filings = []
    for i, form in enumerate(forms):
        if form in filing_types:
            filings.append({
                "form": form,
                "filingDate": dates[i] if i < len(dates) else None,
                "accessionNumber": accessions[i] if i < len(accessions) else None,
                "primaryDocument": primary_docs[i] if i < len(primary_docs) else None,
                "description": descriptions[i] if i < len(descriptions) else None,
                "url": f"https://www.sec.gov/Archives/edgar/data/{cik.lstrip('0')}/{accessions[i].replace('-', '')}/{primary_docs[i]}" if i < len(primary_docs) else None,
            })

    filings_path = EDGAR_DIR / f"{ticker.lower()}_filings.json"
    with open(filings_path, "w") as f:
        json.dump(filings, f, indent=2)
    print(f"  Found {len(filings)} filings ({', '.join(filing_types)})")
    print(f"  Saved: {filings_path}")

    if filings:
        df = pd.DataFrame(filings)
        print(f"\n  Recent filings:")
        print(df[["form", "filingDate", "description"]].head(10).to_string(index=False))

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

    xbrl_path = EDGAR_DIR / f"{ticker.lower()}_xbrl.json"
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
        csv_path = EDGAR_DIR / f"{ticker.lower()}_xbrl_summary.csv"
        df.to_csv(csv_path, index=False)
        print(f"  Saved: {csv_path}")


def main():
    parser = argparse.ArgumentParser(description="Fetch SEC EDGAR filings")
    parser.add_argument("ticker", nargs="?", help="Ticker symbol")
    parser.add_argument("--all", action="store_true", help="Fetch all candidates")
    parser.add_argument("--xbrl", action="store_true", help="Also fetch XBRL financial data")
    args = parser.parse_args()

    if args.all:
        tickers = CANDIDATE_TICKERS
    elif args.ticker:
        tickers = [args.ticker.upper()]
    else:
        print("Provide a ticker or use --all")
        sys.exit(1)

    for ticker in tickers:
        print(f"\n{'='*50}")
        print(f"Fetching EDGAR data for {ticker}")
        print(f"{'='*50}")
        fetch_filings(ticker)
        if args.xbrl:
            print()
            fetch_xbrl_financials(ticker)
        time.sleep(0.2)  # SEC rate limit: 10 req/sec


if __name__ == "__main__":
    main()
