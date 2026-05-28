"""
Fetch financial data from Financial Modeling Prep (FMP).

Ports the FMP utility functions from FinRobot's `finrobot/data_source/fmp_utils.py`
(MIT-licensed). Adds two signals that yfinance + EDGAR alone don't give us:

  1. Analyst price targets — sell-side consensus (min / max / median) to triangulate
     against our own valuation.
  2. Competitor financial metrics — peer EV/EBITDA, P/E, margins, FCF conversion,
     Revenue Growth, ROIC across multiple years in one structured table for comps.

Plus historical market cap, BVPS, and a single-company financial-metrics table.

Requires:  FMP_API_KEY environment variable (free tier at financialmodelingprep.com,
           note: the /v4/price-target endpoint usually requires the paid Starter plan)

Usage:
    python scripts/fetch_fmp.py EXFY                                   # metrics + price target
    python scripts/fetch_fmp.py EXFY --competitors BILL,COUP,SAP       # peer comps
    python scripts/fetch_fmp.py EXFY --years 5                         # 5 years of data
    python scripts/fetch_fmp.py EXFY --only metrics                    # specific endpoints
"""

import argparse
import json
import os
import sys
from datetime import datetime, timedelta
from pathlib import Path

import numpy as np
import pandas as pd
import requests

DATA_DIR = Path(__file__).parent.parent / "data"
FMP_DIR = DATA_DIR / "fmp"
FMP_DIR.mkdir(parents=True, exist_ok=True)

BASE_V3 = "https://financialmodelingprep.com/api/v3"
BASE_V4 = "https://financialmodelingprep.com/api/v4"


def get_api_key() -> str:
    key = os.environ.get("FMP_API_KEY")
    if not key:
        print("ERROR: FMP_API_KEY environment variable not set.")
        print("  PowerShell:  $env:FMP_API_KEY = 'your-key-here'")
        print("  Get a key:   https://site.financialmodelingprep.com/developer/docs")
        sys.exit(1)
    return key


def _get(url: str) -> dict | list | None:
    """GET an FMP endpoint, handle common error shapes."""
    try:
        r = requests.get(url, timeout=15)
    except requests.RequestException as e:
        print(f"  network error: {e}")
        return None
    if r.status_code != 200:
        print(f"  HTTP {r.status_code} for {url.split('?')[0]}")
        return None
    try:
        body = r.json()
    except ValueError:
        print(f"  non-JSON response from {url.split('?')[0]}")
        return None
    # FMP returns {"Error Message": "..."} on plan limits or bad symbols
    if isinstance(body, dict) and ("Error Message" in body or "error" in body):
        msg = body.get("Error Message") or body.get("error")
        print(f"  FMP error: {msg}")
        return None
    return body


def get_next_weekday(date_str: str) -> datetime:
    """If date falls on weekend, push forward to next Monday (FMP has no weekend data)."""
    d = datetime.strptime(date_str, "%Y-%m-%d")
    while d.weekday() >= 5:
        d += timedelta(days=1)
    return d


# ---------- Endpoints ----------

def get_target_price(ticker: str, on_date: str, api_key: str) -> dict:
    """Analyst consensus price target near `on_date` (within 999 days).
    Returns {'min', 'max', 'median', 'n_estimates', 'estimates': [...]}.
    Note: /v4/price-target usually requires FMP Starter plan or above."""
    url = f"{BASE_V4}/price-target?symbol={ticker}&apikey={api_key}"
    data = _get(url)
    if not data:
        return {"error": "no data (endpoint may require paid plan)"}
    if not isinstance(data, list):
        return {"error": f"unexpected response shape: {type(data).__name__}"}

    anchor = datetime.strptime(on_date, "%Y-%m-%d")
    estimates = []
    for tp in data:
        try:
            pd_str = tp.get("publishedDate", "").split("T")[0]
            pdt = datetime.strptime(pd_str, "%Y-%m-%d")
        except (ValueError, AttributeError):
            continue
        if abs((pdt - anchor).days) <= 999:
            estimates.append({
                "published": pd_str,
                "target": tp.get("priceTarget"),
                "analyst": tp.get("analystName"),
                "firm": tp.get("analystCompany"),
            })

    if not estimates:
        return {"error": "no estimates within 999 days of anchor"}

    targets = [e["target"] for e in estimates if e["target"] is not None]
    return {
        "anchor_date": on_date,
        "n_estimates": len(targets),
        "min": float(np.min(targets)),
        "max": float(np.max(targets)),
        "median": float(np.median(targets)),
        "mean": float(np.mean(targets)),
        "estimates": estimates,
    }


def get_historical_market_cap(ticker: str, on_date: str, api_key: str) -> float | None:
    date = get_next_weekday(on_date).strftime("%Y-%m-%d")
    url = (f"{BASE_V3}/historical-market-capitalization/{ticker}"
           f"?limit=100&from={date}&to={date}&apikey={api_key}")
    data = _get(url)
    if not data or not isinstance(data, list) or len(data) == 0:
        return None
    return data[0].get("marketCap")


def get_historical_bvps(ticker: str, target_date: str, api_key: str) -> float | None:
    url = f"{BASE_V3}/key-metrics/{ticker}?limit=40&apikey={api_key}"
    data = _get(url)
    if not data or not isinstance(data, list):
        return None
    anchor = datetime.strptime(target_date, "%Y-%m-%d")
    closest, min_diff = None, float("inf")
    for entry in data:
        try:
            d = datetime.strptime(entry["date"], "%Y-%m-%d")
        except (ValueError, KeyError):
            continue
        diff = abs((anchor - d).days)
        if diff < min_diff:
            min_diff, closest = diff, entry
    if closest is None:
        return None
    return closest.get("bookValuePerShare")


def _safe_div(a, b):
    try:
        if b in (None, 0):
            return None
        return a / b
    except TypeError:
        return None


def _pct(x):
    return f"{x*100:.1f}%" if isinstance(x, (int, float)) else None


def get_financial_metrics(ticker: str, api_key: str, years: int = 4) -> pd.DataFrame:
    """Multi-year financial metrics for one company. Each column is a fiscal year."""
    income = _get(f"{BASE_V3}/income-statement/{ticker}?limit={years}&apikey={api_key}")
    ratios = _get(f"{BASE_V3}/ratios/{ticker}?limit={years}&apikey={api_key}")
    keymet = _get(f"{BASE_V3}/key-metrics/{ticker}?limit={years}&apikey={api_key}")

    if not (income and ratios and keymet):
        return pd.DataFrame()

    df = pd.DataFrame()
    for i in range(min(years, len(income), len(ratios), len(keymet))):
        rev = income[i].get("revenue")
        # Bugfix vs FinRobot: only compute growth when prior year exists
        prior_rev = income[i + 1].get("revenue") if i + 1 < len(income) else None
        growth = _pct(_safe_div(rev - prior_rev, prior_rev)) if prior_rev else None

        ev = keymet[i].get("enterpriseValue")
        ev_to_ocf = keymet[i].get("evToOperatingCashFlow")
        fcf = _safe_div(ev, ev_to_ocf) if ev and ev_to_ocf else None
        net_income = income[i].get("netIncome")

        metrics = {
            "Revenue ($M)": round(rev / 1e6) if rev else None,
            "Revenue Growth": growth,
            "Gross Profit ($M)": round(income[i].get("grossProfit") / 1e6) if income[i].get("grossProfit") else None,
            "Gross Margin": round(_safe_div(income[i].get("grossProfit"), rev), 3) if rev else None,
            "EBITDA ($M)": round(income[i].get("ebitda") / 1e6) if income[i].get("ebitda") else None,
            "EBITDA Margin": round(income[i].get("ebitdaratio"), 3) if income[i].get("ebitdaratio") is not None else None,
            "FCF ($M)": round(fcf / 1e6) if fcf else None,
            "FCF Conversion": round(_safe_div(fcf, net_income), 2) if fcf and net_income else None,
            "ROIC": _pct(keymet[i].get("roic")),
            "EV/EBITDA": round(keymet[i].get("enterpriseValueOverEBITDA"), 2) if keymet[i].get("enterpriseValueOverEBITDA") else None,
            "P/E": round(ratios[i].get("priceEarningsRatio"), 2) if ratios[i].get("priceEarningsRatio") else None,
            "P/B": round(keymet[i].get("pbRatio"), 2) if keymet[i].get("pbRatio") else None,
        }
        year = income[i]["date"][:4]
        df[year] = pd.Series(metrics)

    return df.sort_index(axis=1)


def get_competitor_financial_metrics(ticker: str, competitors: list[str],
                                     api_key: str, years: int = 4) -> dict[str, pd.DataFrame]:
    """Same metrics across the target ticker + competitor list."""
    out = {}
    for sym in [ticker] + competitors:
        print(f"  fetching {sym}...")
        df = get_financial_metrics(sym, api_key, years=years)
        if df.empty:
            print(f"    no data")
        out[sym] = df
    return out


# ---------- Driver ----------

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("ticker")
    parser.add_argument("--competitors", type=str, default="",
                        help="Comma-separated peer tickers for comps table")
    parser.add_argument("--years", type=int, default=4)
    parser.add_argument("--as-of", type=str, default=None,
                        help="Anchor date for price target / market cap / BVPS (default: today)")
    parser.add_argument("--only", type=str, default="metrics,target,mcap,bvps",
                        help="Comma list of endpoints: metrics,target,mcap,bvps,comps")
    args = parser.parse_args()

    ticker = args.ticker.upper()
    competitors = [c.strip().upper() for c in args.competitors.split(",") if c.strip()]
    as_of = args.as_of or datetime.now().strftime("%Y-%m-%d")
    endpoints = {e.strip() for e in args.only.split(",") if e.strip()}
    if competitors:
        endpoints.add("comps")

    api_key = get_api_key()
    out_dir = FMP_DIR / ticker.lower()
    out_dir.mkdir(parents=True, exist_ok=True)

    if "metrics" in endpoints:
        print(f"\n[metrics] fetching {args.years}-year financial metrics for {ticker}...")
        df = get_financial_metrics(ticker, api_key, years=args.years)
        if not df.empty:
            path = out_dir / "metrics.csv"
            df.to_csv(path)
            print(df.to_string())
            print(f"  saved: {path}")
        else:
            print("  no data returned")

    if "target" in endpoints:
        print(f"\n[target] fetching analyst price targets for {ticker} (as of {as_of})...")
        tp = get_target_price(ticker, as_of, api_key)
        path = out_dir / "target_price.json"
        path.write_text(json.dumps(tp, indent=2))
        if "error" in tp:
            print(f"  {tp['error']}")
        else:
            print(f"  {tp['n_estimates']} estimates: "
                  f"${tp['min']:.2f} - ${tp['max']:.2f} (median ${tp['median']:.2f})")
        print(f"  saved: {path}")

    if "mcap" in endpoints:
        print(f"\n[mcap] historical market cap for {ticker} on {as_of}...")
        mc = get_historical_market_cap(ticker, as_of, api_key)
        if mc:
            print(f"  ${mc/1e6:.1f}M")
            (out_dir / "market_cap.json").write_text(
                json.dumps({"date": as_of, "market_cap": mc}, indent=2))
        else:
            print("  no data")

    if "bvps" in endpoints:
        print(f"\n[bvps] historical BVPS for {ticker} near {as_of}...")
        bvps = get_historical_bvps(ticker, as_of, api_key)
        if bvps:
            print(f"  ${bvps:.2f}")
            (out_dir / "bvps.json").write_text(
                json.dumps({"target_date": as_of, "bvps": bvps}, indent=2))
        else:
            print("  no data")

    if "comps" in endpoints and competitors:
        print(f"\n[comps] competitor metrics: {ticker} vs {','.join(competitors)}")
        all_data = get_competitor_financial_metrics(ticker, competitors, api_key, years=args.years)
        # Wide table: one row per (symbol, metric), columns = years
        rows = []
        for sym, df in all_data.items():
            if df.empty:
                continue
            for metric in df.index:
                row = {"symbol": sym, "metric": metric}
                for yr in df.columns:
                    row[yr] = df.loc[metric, yr]
                rows.append(row)
        if rows:
            comps_df = pd.DataFrame(rows)
            path = out_dir / "comps.csv"
            comps_df.to_csv(path, index=False)
            print(f"\n  saved: {path}")
            print(f"  ({len(all_data)} companies × {comps_df['metric'].nunique()} metrics × {args.years} years)")
        else:
            print("  no comp data returned")


if __name__ == "__main__":
    main()
