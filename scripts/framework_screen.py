"""
Framework-driven company screener.

Step 1: Pull universe from Finviz (market cap $10M-$500M, relevant sectors, NYSE/NASDAQ)
Step 2: Enrich with yfinance for EV and key metrics
Step 3: Apply framework filters from docs/public-company-pitch.md
Step 4: Report counts, types, and characteristics

Usage:
    python scripts/framework_screen.py              # Full screen
    python scripts/framework_screen.py --step1-only  # Just pull universe (fast)
    python scripts/framework_screen.py --sanity TICKER  # Sanity check a specific company
"""

import argparse
import json
import time
import sys
from datetime import datetime
from pathlib import Path

import pandas as pd
import yfinance as yf

DATA_DIR = Path(__file__).parent.parent / "data"
DATA_DIR.mkdir(exist_ok=True)

# --- Sector mappings aligned with our framework ---
# Finviz sector/industry filters
INCLUDE_SECTORS_FINVIZ = [
    "Technology",
    "Communication Services",
]

# More granular: industries within those sectors that match our framework
INCLUDE_INDUSTRIES = [
    "Software - Application",
    "Software - Infrastructure",
    "Information Technology Services",
    "Internet Content & Information",
    "Electronic Gaming & Multimedia",
    "Advertising Agencies",
    "Publishing",
    "Entertainment",
    "Education & Training Services",
    "Consulting Services",
    # Data / analytics adjacent
    "Scientific & Technical Instruments",
]

EXCLUDE_INDUSTRIES = [
    "Semiconductors",
    "Semiconductor Equipment & Materials",
    "Consumer Electronics",
    "Computer Hardware",
    "Electronic Components",
    "Solar",
    "Communication Equipment",
]

# Framework thresholds
EV_MIN = 10_000_000
EV_MAX = 500_000_000
EV_SWEET_MIN = 30_000_000
EV_SWEET_MAX = 250_000_000
MIN_REVENUE = 10_000_000
MAX_ANALYSTS = 3
EV_REV_THRESHOLD = 1.5


def step1_pull_universe():
    """Pull universe from Finviz screener via finvizfinance."""
    from finvizfinance.screener.overview import Overview

    all_results = []

    for cap_label, cap_filter in [
        ("Nano", "Nano (under $50mln)"),
        ("Micro", "Micro ($50mln to $300mln)"),
        ("Small", "Small ($300mln to $2bln)"),
    ]:
        for sector in INCLUDE_SECTORS_FINVIZ:
            print(f"  Fetching {cap_label} cap / {sector}...", end=" ", flush=True)
            try:
                foverview = Overview()
                filters_dict = {
                    "Market Cap.": cap_filter,
                    "Sector": sector,
                }
                foverview.set_filter(filters_dict=filters_dict)
                df = foverview.screener_view()
                if df is not None and not df.empty:
                    df["cap_category"] = cap_label
                    df["sector_filter"] = sector
                    all_results.append(df)
                    print(f"{len(df)} companies")
                else:
                    print("0 companies")
                time.sleep(1)
            except Exception as e:
                print(f"ERROR: {e}")
                time.sleep(2)

    if not all_results:
        print("No results found!")
        return pd.DataFrame()

    universe = pd.concat(all_results, ignore_index=True)
    universe = universe.drop_duplicates(subset=["Ticker"])

    out_path = DATA_DIR / "universe_raw.csv"
    universe.to_csv(out_path, index=False)
    print(f"\nTotal unique companies: {len(universe)}")
    print(f"Saved: {out_path}")

    print(f"\nBy cap category:")
    print(universe["cap_category"].value_counts().to_string())
    print(f"\nBy sector:")
    print(universe["sector_filter"].value_counts().to_string())

    if "Industry" in universe.columns:
        print(f"\nTop 15 industries:")
        print(universe["Industry"].value_counts().head(15).to_string())

    return universe


def step2_enrich_with_ev(universe_df, batch_size=20):
    """Enrich universe with EV and key metrics from yfinance."""
    tickers = universe_df["Ticker"].tolist()
    print(f"\nEnriching {len(tickers)} companies with yfinance data...")

    all_data = []
    fields = [
        "shortName", "sector", "industry", "marketCap", "enterpriseValue",
        "totalRevenue", "revenueGrowth", "grossMargins", "operatingMargins",
        "ebitda", "freeCashflow", "totalCash", "totalDebt",
        "enterpriseToRevenue", "enterpriseToEbitda",
        "numberOfAnalystOpinions", "recommendationKey",
        "fiftyTwoWeekLow", "fiftyTwoWeekHigh", "currentPrice",
        "heldPercentInstitutions", "shortRatio", "sharesOutstanding",
        "floatShares", "fullTimeEmployees",
    ]

    for i in range(0, len(tickers), batch_size):
        batch = tickers[i:i + batch_size]
        print(f"  Batch {i // batch_size + 1}/{(len(tickers) + batch_size - 1) // batch_size}: {batch[0]}-{batch[-1]}...", end=" ", flush=True)

        try:
            batch_str = " ".join(batch)
            ytickers = yf.Tickers(batch_str)

            for ticker in batch:
                try:
                    info = ytickers.tickers[ticker].info
                    row = {"ticker": ticker}
                    for f in fields:
                        row[f] = info.get(f)
                    all_data.append(row)
                except Exception:
                    all_data.append({"ticker": ticker, "error": True})

            print(f"OK")
        except Exception as e:
            print(f"batch error: {e}")
            for ticker in batch:
                all_data.append({"ticker": ticker, "error": True})

        time.sleep(0.5)

    enriched = pd.DataFrame(all_data)
    out_path = DATA_DIR / "universe_enriched.csv"
    enriched.to_csv(out_path, index=False)
    print(f"\nEnriched {len(enriched)} companies. Saved: {out_path}")
    return enriched


def step3_apply_filters(enriched_df):
    """Apply framework filters and report results."""
    df = enriched_df.copy()
    df = df[df.get("error") != True].copy()

    total_start = len(df)
    print(f"\n{'='*60}")
    print(f"APPLYING FRAMEWORK FILTERS")
    print(f"{'='*60}")
    print(f"Starting universe: {total_start} companies")

    # Filter: EV in range
    df_ev = df[df["enterpriseValue"].notna()].copy()
    df_ev = df_ev[(df_ev["enterpriseValue"] >= EV_MIN) & (df_ev["enterpriseValue"] <= EV_MAX)]
    print(f"\nAfter EV filter ($10M-$500M): {len(df_ev)} companies")

    # Filter: Minimum revenue
    df_rev = df_ev[df_ev["totalRevenue"].notna()].copy()
    df_rev = df_rev[df_rev["totalRevenue"] >= MIN_REVENUE]
    print(f"After min revenue filter (>$10M): {len(df_rev)} companies")

    # Exclude certain industries
    if "industry" in df_rev.columns:
        before = len(df_rev)
        df_rev = df_rev[~df_rev["industry"].isin(EXCLUDE_INDUSTRIES)]
        print(f"After excluding hardware/semis/solar: {len(df_rev)} companies (removed {before - len(df_rev)})")

    # Report what we have
    print(f"\n{'='*60}")
    print(f"QUALIFYING UNIVERSE: {len(df_rev)} companies")
    print(f"{'='*60}")

    if "industry" in df_rev.columns:
        print(f"\nBy industry:")
        print(df_rev["industry"].value_counts().head(20).to_string())

    # EV distribution
    print(f"\nEV distribution:")
    ev_bins = [10e6, 30e6, 50e6, 100e6, 150e6, 250e6, 500e6]
    ev_labels = ["$10-30M", "$30-50M", "$50-100M", "$100-150M", "$150-250M", "$250-500M"]
    df_rev["ev_bucket"] = pd.cut(df_rev["enterpriseValue"], bins=ev_bins, labels=ev_labels)
    print(df_rev["ev_bucket"].value_counts().sort_index().to_string())

    # Now apply MESSINESS signals
    print(f"\n{'='*60}")
    print(f"MESSINESS / MISPRICING SIGNALS")
    print(f"{'='*60}")

    # EV/Revenue < 1.5x
    df_rev["ev_to_rev"] = df_rev["enterpriseToRevenue"]
    low_ev_rev = df_rev[df_rev["ev_to_rev"].notna() & (df_rev["ev_to_rev"] < EV_REV_THRESHOLD)]
    print(f"\nEV/Revenue < 1.5x: {len(low_ev_rev)} companies")
    if len(low_ev_rev) > 0:
        print(low_ev_rev[["ticker", "shortName", "enterpriseValue", "totalRevenue", "ev_to_rev", "industry"]].sort_values("ev_to_rev").head(15).to_string(index=False))

    # Under-followed (0-3 analysts)
    under_followed = df_rev[df_rev["numberOfAnalystOpinions"].notna() & (df_rev["numberOfAnalystOpinions"] <= MAX_ANALYSTS)]
    no_coverage = df_rev[df_rev["numberOfAnalystOpinions"].isna() | (df_rev["numberOfAnalystOpinions"] == 0)]
    print(f"\nUnder-followed (0-3 analysts): {len(under_followed)} companies")
    print(f"Zero analyst coverage: {len(no_coverage)} companies")

    # 52-week decline > 40%
    df_rev["pct_from_52wk_high"] = (df_rev["currentPrice"] / df_rev["fiftyTwoWeekHigh"] - 1) * 100
    fallen = df_rev[df_rev["pct_from_52wk_high"].notna() & (df_rev["pct_from_52wk_high"] < -40)]
    print(f"\nDown >40% from 52-week high: {len(fallen)} companies")
    if len(fallen) > 0:
        print(fallen[["ticker", "shortName", "enterpriseValue", "pct_from_52wk_high", "industry"]].sort_values("pct_from_52wk_high").head(10).to_string(index=False))

    # Sweet spot: low EV/Rev AND under-followed
    sweet = df_rev[
        (df_rev["ev_to_rev"].notna()) & (df_rev["ev_to_rev"] < EV_REV_THRESHOLD) &
        ((df_rev["numberOfAnalystOpinions"].isna()) | (df_rev["numberOfAnalystOpinions"] <= MAX_ANALYSTS))
    ]
    print(f"\n{'='*60}")
    print(f"SWEET SPOT: EV/Rev < 1.5x AND 0-3 analysts: {len(sweet)} companies")
    print(f"{'='*60}")
    if len(sweet) > 0:
        display_cols = ["ticker", "shortName", "enterpriseValue", "totalRevenue", "ev_to_rev",
                       "operatingMargins", "freeCashflow", "numberOfAnalystOpinions", "industry"]
        available = [c for c in display_cols if c in sweet.columns]
        sweet_sorted = sweet.sort_values("ev_to_rev")
        for col in ["enterpriseValue", "totalRevenue", "freeCashflow"]:
            if col in sweet_sorted.columns:
                sweet_sorted[col] = sweet_sorted[col].apply(lambda x: f"${x/1e6:.1f}M" if pd.notna(x) else "N/A")
        print(sweet_sorted[available].to_string(index=False))

    # EV sweet spot ($30M-$250M) + low EV/Rev + under-followed
    ultra_sweet = df_rev[
        (df_rev["enterpriseValue"] >= EV_SWEET_MIN) & (df_rev["enterpriseValue"] <= EV_SWEET_MAX) &
        (df_rev["ev_to_rev"].notna()) & (df_rev["ev_to_rev"] < EV_REV_THRESHOLD) &
        ((df_rev["numberOfAnalystOpinions"].isna()) | (df_rev["numberOfAnalystOpinions"] <= MAX_ANALYSTS))
    ]
    print(f"\nULTRA SWEET SPOT ($30-250M EV + EV/Rev < 1.5x + 0-3 analysts): {len(ultra_sweet)} companies")
    if len(ultra_sweet) > 0:
        display_cols = ["ticker", "shortName", "enterpriseValue", "totalRevenue", "ev_to_rev",
                       "operatingMargins", "freeCashflow", "numberOfAnalystOpinions", "industry"]
        available = [c for c in display_cols if c in ultra_sweet.columns]
        us_sorted = ultra_sweet.sort_values("ev_to_rev")
        for col in ["enterpriseValue", "totalRevenue", "freeCashflow"]:
            if col in us_sorted.columns:
                us_sorted[col] = us_sorted[col].apply(lambda x: f"${x/1e6:.1f}M" if pd.notna(x) else "N/A")
        print(us_sorted[available].to_string(index=False))

    # Save filtered results
    out_path = DATA_DIR / "framework_filtered.csv"
    df_rev.to_csv(out_path, index=False)
    print(f"\nSaved full filtered universe: {out_path}")

    sweet_path = DATA_DIR / "sweet_spot_candidates.csv"
    if len(sweet) > 0:
        sweet.to_csv(sweet_path, index=False)
        print(f"Saved sweet spot candidates: {sweet_path}")

    return df_rev, sweet


def sanity_check(ticker):
    """Quick sanity check on a specific company against the framework."""
    print(f"\n{'='*60}")
    print(f"SANITY CHECK: {ticker}")
    print(f"{'='*60}")

    t = yf.Ticker(ticker)
    info = t.info

    name = info.get("shortName", "Unknown")
    ev = info.get("enterpriseValue")
    mcap = info.get("marketCap")
    rev = info.get("totalRevenue")
    ev_rev = info.get("enterpriseToRevenue")
    analysts = info.get("numberOfAnalystOpinions")
    inst_own = info.get("heldPercentInstitutions")
    op_margin = info.get("operatingMargins")
    fcf = info.get("freeCashflow")
    high52 = info.get("fiftyTwoWeekHigh")
    price = info.get("currentPrice")
    industry = info.get("industry")
    sector = info.get("sector")
    cash = info.get("totalCash")
    debt = info.get("totalDebt")
    employees = info.get("fullTimeEmployees")
    summary = info.get("longBusinessSummary", "N/A")

    pct_from_high = ((price / high52) - 1) * 100 if price and high52 else None

    print(f"\n  Company: {name}")
    print(f"  Sector: {sector} / {industry}")
    print(f"  Employees: {employees}")
    print(f"  Website: {info.get('website')}")
    print(f"\n  Summary: {summary[:300]}...")

    print(f"\n  --- Financials ---")
    print(f"  Enterprise Value: {fmt(ev)}")
    print(f"  Market Cap:       {fmt(mcap)}")
    print(f"  Total Revenue:    {fmt(rev)}")
    print(f"  EV/Revenue:       {ev_rev:.2f}x" if ev_rev else "  EV/Revenue:       N/A")
    print(f"  Operating Margin: {op_margin:.1%}" if op_margin else "  Operating Margin: N/A")
    print(f"  Free Cash Flow:   {fmt(fcf)}")
    print(f"  Cash:             {fmt(cash)}")
    print(f"  Debt:             {fmt(debt)}")

    print(f"\n  --- Framework Checks ---")

    checks = []

    # EV in range
    if ev and EV_MIN <= ev <= EV_MAX:
        sweet = "SWEET SPOT" if EV_SWEET_MIN <= ev <= EV_SWEET_MAX else "in range"
        checks.append(("EV in $10M-$500M", "PASS", sweet))
    else:
        checks.append(("EV in $10M-$500M", "FAIL", fmt(ev)))

    # Revenue > $10M
    if rev and rev >= MIN_REVENUE:
        checks.append(("Revenue > $10M", "PASS", fmt(rev)))
    else:
        checks.append(("Revenue > $10M", "FAIL", fmt(rev)))

    # EV/Revenue < 1.5x
    if ev_rev is not None and ev_rev < EV_REV_THRESHOLD:
        checks.append(("EV/Revenue < 1.5x (mispriced signal)", "PASS", f"{ev_rev:.2f}x"))
    elif ev_rev is not None:
        checks.append(("EV/Revenue < 1.5x (mispriced signal)", "FAIL", f"{ev_rev:.2f}x"))
    else:
        checks.append(("EV/Revenue < 1.5x (mispriced signal)", "N/A", ""))

    # Under-followed
    if analysts is not None and analysts <= MAX_ANALYSTS:
        checks.append(("Under-followed (0-3 analysts)", "PASS", f"{analysts} analysts"))
    elif analysts is not None:
        checks.append(("Under-followed (0-3 analysts)", "FAIL", f"{analysts} analysts"))
    else:
        checks.append(("Under-followed (0-3 analysts)", "PASS", "0 / unknown analysts"))

    # 52-week decline
    if pct_from_high is not None and pct_from_high < -40:
        checks.append(("Down >40% from 52wk high (fallen angel)", "PASS", f"{pct_from_high:.1f}%"))
    elif pct_from_high is not None:
        checks.append(("Down >40% from 52wk high (fallen angel)", "NO", f"{pct_from_high:.1f}%"))
    else:
        checks.append(("Down >40% from 52wk high (fallen angel)", "N/A", ""))

    # Institutional ownership < 50%
    if inst_own is not None and inst_own < 0.5:
        checks.append(("Institutional ownership < 50%", "PASS", f"{inst_own:.1%}"))
    elif inst_own is not None:
        checks.append(("Institutional ownership < 50%", "NO", f"{inst_own:.1%}"))
    else:
        checks.append(("Institutional ownership < 50%", "N/A", ""))

    # Market cap vs EV disconnect
    if ev and mcap:
        ratio = ev / mcap if mcap > 0 else None
        if ratio and (ratio > 2 or ratio < 0.5):
            checks.append(("Market cap / EV disconnect", "PASS", f"EV/MCap = {ratio:.2f}x"))
        elif ratio:
            checks.append(("Market cap / EV disconnect", "NO", f"EV/MCap = {ratio:.2f}x"))

    print()
    for check_name, result, detail in checks:
        icon = "+" if result == "PASS" else ("-" if result == "FAIL" else "~")
        print(f"  [{icon}] {check_name}: {result} ({detail})")

    pass_count = sum(1 for _, r, _ in checks if r == "PASS")
    total_checks = len(checks)
    print(f"\n  Framework score: {pass_count}/{total_checks} checks passed")

    # Overall assessment
    print(f"\n  --- Assessment ---")
    if pass_count >= 5:
        print(f"  STRONG CANDIDATE — passes most framework criteria")
    elif pass_count >= 3:
        print(f"  MODERATE CANDIDATE — worth investigating further")
    else:
        print(f"  WEAK CANDIDATE — likely doesn't fit framework")


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
    parser = argparse.ArgumentParser(description="Framework-driven company screener")
    parser.add_argument("--step1-only", action="store_true", help="Only pull universe from Finviz")
    parser.add_argument("--sanity", type=str, help="Sanity check a specific ticker")
    parser.add_argument("--from-cache", action="store_true", help="Use cached universe_raw.csv instead of re-fetching")
    args = parser.parse_args()

    if args.sanity:
        sanity_check(args.sanity.upper())
        return

    # Step 1: Pull universe
    cache_path = DATA_DIR / "universe_raw.csv"
    if args.from_cache and cache_path.exists():
        print(f"Loading cached universe from {cache_path}")
        universe = pd.read_csv(cache_path)
        print(f"Loaded {len(universe)} companies")
    else:
        universe = step1_pull_universe()

    if universe.empty:
        print("No universe data. Exiting.")
        return

    if args.step1_only:
        return

    # Step 2: Enrich with yfinance
    enriched_path = DATA_DIR / "universe_enriched.csv"
    enriched = step2_enrich_with_ev(universe)

    # Step 3: Apply filters
    filtered, sweet_spot = step3_apply_filters(enriched)


if __name__ == "__main__":
    main()
