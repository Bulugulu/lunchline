"""
Screen NYSE/Nasdaq companies by enterprise value using yfinance.
Pulls real-time market data and key financials for candidate companies.

Usage:
    python scripts/screen_companies.py                  # Run full screen of candidates
    python scripts/screen_companies.py --ticker MCHX    # Pull detailed data for one ticker
"""

import argparse
import json
import sys
from datetime import datetime
from pathlib import Path

import pandas as pd
import yfinance as yf

DATA_DIR = Path(__file__).parent.parent / "data"
DATA_DIR.mkdir(exist_ok=True)

CANDIDATE_TICKERS = [
    # Populated after framework-driven screening — see docs/selection-framework.md
]

SUMMARY_FIELDS = [
    "shortName",
    "exchange",
    "sector",
    "industry",
    "marketCap",
    "enterpriseValue",
    "totalRevenue",
    "revenueGrowth",
    "grossMargins",
    "operatingMargins",
    "profitMargins",
    "ebitda",
    "totalCash",
    "totalDebt",
    "debtToEquity",
    "freeCashflow",
    "operatingCashflow",
    "trailingPE",
    "forwardPE",
    "priceToBook",
    "enterpriseToRevenue",
    "enterpriseToEbitda",
    "trailingEps",
    "forwardEps",
    "sharesOutstanding",
    "floatShares",
    "heldPercentInsiders",
    "heldPercentInstitutions",
    "shortRatio",
    "bookValue",
    "currentPrice",
    "targetMeanPrice",
    "numberOfAnalystOpinions",
    "recommendationKey",
    "fiftyTwoWeekLow",
    "fiftyTwoWeekHigh",
    "fiftyDayAverage",
    "twoHundredDayAverage",
    "dividendYield",
    "payoutRatio",
    "fullTimeEmployees",
    "website",
    "longBusinessSummary",
]


def fetch_company_data(ticker: str) -> dict:
    t = yf.Ticker(ticker)
    info = t.info
    result = {"ticker": ticker, "fetchedAt": datetime.now().isoformat()}
    for field in SUMMARY_FIELDS:
        result[field] = info.get(field)
    return result


def fetch_financials(ticker: str) -> dict:
    t = yf.Ticker(ticker)
    data = {}

    for name, df in [
        ("income_stmt", t.income_stmt),
        ("balance_sheet", t.balance_sheet),
        ("cashflow", t.cashflow),
    ]:
        if df is not None and not df.empty:
            df_clean = df.copy()
            df_clean.columns = [str(c.date()) if hasattr(c, "date") else str(c) for c in df_clean.columns]
            data[name] = df_clean.to_dict()
        else:
            data[name] = {}

    return data


def screen_all():
    print(f"Screening {len(CANDIDATE_TICKERS)} candidates...\n")
    rows = []
    for ticker in CANDIDATE_TICKERS:
        try:
            print(f"  Fetching {ticker}...", end=" ", flush=True)
            data = fetch_company_data(ticker)
            rows.append(data)
            ev = data.get("enterpriseValue")
            mc = data.get("marketCap")
            rev = data.get("totalRevenue")
            print(f"EV={fmt(ev)}  MCap={fmt(mc)}  Rev={fmt(rev)}")
        except Exception as e:
            print(f"ERROR: {e}")
            rows.append({"ticker": ticker, "error": str(e)})

    df = pd.DataFrame(rows)
    out_path = DATA_DIR / "candidate_screen.csv"
    df.to_csv(out_path, index=False)
    print(f"\nSaved: {out_path}")

    json_path = DATA_DIR / "candidate_screen.json"
    with open(json_path, "w") as f:
        json.dump(rows, f, indent=2, default=str)
    print(f"Saved: {json_path}")

    print("\n--- Summary ---")
    display_cols = ["ticker", "shortName", "enterpriseValue", "marketCap", "totalRevenue",
                    "enterpriseToRevenue", "operatingMargins", "freeCashflow",
                    "numberOfAnalystOpinions"]
    available = [c for c in display_cols if c in df.columns]
    summary = df[available].copy()
    for col in ["enterpriseValue", "marketCap", "totalRevenue", "freeCashflow"]:
        if col in summary.columns:
            summary[col] = summary[col].apply(fmt)
    print(summary.to_string(index=False))


def deep_dive(ticker: str):
    print(f"Deep dive: {ticker}\n")

    print("Fetching summary data...")
    data = fetch_company_data(ticker)
    summary_path = DATA_DIR / f"{ticker.lower()}_summary.json"
    with open(summary_path, "w") as f:
        json.dump(data, f, indent=2, default=str)
    print(f"Saved: {summary_path}\n")

    for key, val in data.items():
        if key in ("longBusinessSummary", "fetchedAt"):
            continue
        if val is not None:
            print(f"  {key}: {fmt(val) if isinstance(val, (int, float)) and abs(val) > 10000 else val}")

    print(f"\n  Business Summary:\n  {data.get('longBusinessSummary', 'N/A')[:500]}...")

    print("\nFetching financial statements...")
    financials = fetch_financials(ticker)
    fin_path = DATA_DIR / f"{ticker.lower()}_financials.json"
    with open(fin_path, "w") as f:
        json.dump(financials, f, indent=2, default=str)
    print(f"Saved: {fin_path}")

    for stmt_name, stmt_data in financials.items():
        if stmt_data:
            df = pd.DataFrame(stmt_data)
            print(f"\n  {stmt_name} ({len(df)} line items, {len(df.columns)} periods)")
            csv_path = DATA_DIR / f"{ticker.lower()}_{stmt_name}.csv"
            df.to_csv(csv_path)
            print(f"  Saved: {csv_path}")


def fmt(val):
    if val is None:
        return "N/A"
    if not isinstance(val, (int, float)):
        return str(val)
    if abs(val) >= 1e9:
        return f"${val/1e9:.2f}B"
    if abs(val) >= 1e6:
        return f"${val/1e6:.1f}M"
    if abs(val) >= 1e3:
        return f"${val/1e3:.1f}K"
    return f"${val:.2f}"


def main():
    parser = argparse.ArgumentParser(description="Screen companies by enterprise value")
    parser.add_argument("--ticker", "-t", help="Deep dive on a single ticker")
    args = parser.parse_args()

    if args.ticker:
        deep_dive(args.ticker.upper())
    else:
        screen_all()


if __name__ == "__main__":
    main()
