"""
Apply geography + liquidity filters to the scored universe, then re-rank.

Filters added on top of the existing 7-check framework:
  - Drop China/HK-domiciled companies (governance/delisting risk; not investable
    for a US-focused PE/search fund)
  - Drop avg daily $ volume < $50K (framework liquidity rule)
  - Drop float-as-pct-of-shares < 30% (framework liquidity rule)

Reads from data/scored_candidates.csv but re-fetches country and liquidity
fields from yfinance for the 6/7 and 7/7 candidates only.
"""

import time
from pathlib import Path

import pandas as pd
import yfinance as yf

DATA_DIR = Path(__file__).parent.parent / "data"

# China/HK-domiciled exclusion list — these countries map to ADR governance risks
EXCLUDE_COUNTRIES = {"China", "Hong Kong"}

# Liquidity thresholds (from docs/public-company-pitch.md:190-197)
MIN_DAILY_DOLLAR_VOL = 50_000
MIN_FLOAT_PCT = 0.30


def fetch_extra_fields(tickers):
    """Pull country, avg volume, current price, float, shares for each ticker."""
    fields = [
        "country", "averageDailyVolume10Day", "averageVolume",
        "currentPrice", "floatShares", "sharesOutstanding",
    ]
    out = []
    n = len(tickers)
    for i, tkr in enumerate(tickers):
        try:
            info = yf.Ticker(tkr).info
            row = {"ticker": tkr}
            for f in fields:
                row[f] = info.get(f)
            out.append(row)
        except Exception as e:
            out.append({"ticker": tkr, "fetch_error": str(e)})
        if (i + 1) % 10 == 0:
            print(f"  {i+1}/{n}...")
        time.sleep(0.2)
    return pd.DataFrame(out)


def main():
    scored = pd.read_csv(DATA_DIR / "scored_candidates.csv")
    # Focus on candidates that scored 6 or 7 (highest signal density)
    high = scored[scored["framework_score"] >= 6].copy()
    print(f"Loaded {len(scored)} scored. {len(high)} score >=6/7.")
    print(f"\nFetching country + liquidity fields for {len(high)} tickers...")

    extra = fetch_extra_fields(high["ticker"].tolist())
    merged = high.merge(extra, on="ticker", how="left")

    # Compute liquidity metrics
    merged["daily_dollar_vol"] = merged["averageDailyVolume10Day"].fillna(0) * merged["currentPrice_y"].fillna(merged["currentPrice_x"])
    merged["float_pct"] = merged["floatShares"] / merged["sharesOutstanding"]

    # Apply filters
    merged["fail_china_hk"] = merged["country"].isin(EXCLUDE_COUNTRIES)
    merged["fail_liquidity"] = merged["daily_dollar_vol"] < MIN_DAILY_DOLLAR_VOL
    merged["fail_float"] = merged["float_pct"] < MIN_FLOAT_PCT

    print("\n" + "=" * 70)
    print("FILTER ATTRITION (candidates scoring 6/7 or 7/7)")
    print("=" * 70)
    print(f"Starting:                 {len(merged)}")
    print(f"China/HK domiciled:       {merged['fail_china_hk'].sum()}")
    print(f"Daily $ vol < $50K:       {merged['fail_liquidity'].sum()}")
    print(f"Float < 30%:              {merged['fail_float'].sum()}")

    passes = merged[
        ~merged["fail_china_hk"] & ~merged["fail_liquidity"] & ~merged["fail_float"]
    ].copy()
    print(f"\nPasses all filters:       {len(passes)}")

    for target in [7, 6]:
        bucket = passes[passes["framework_score"] == target].sort_values("enterpriseValue")
        print("\n" + "=" * 70)
        print(f"{target}/7 — INVESTABLE FOR US PE/SEARCH FUND  (n={len(bucket)})")
        print("=" * 70)
        if len(bucket) == 0:
            continue
        out = bucket.copy()
        out["EV_M"] = out["enterpriseValue"].apply(lambda x: f"${x/1e6:.0f}M")
        out["Rev_M"] = out["totalRevenue"].apply(lambda x: f"${x/1e6:.0f}M")
        out["EV/Rev"] = out["enterpriseToRevenue"].apply(lambda x: f"{x:.2f}x" if pd.notna(x) else "N/A")
        out["Analysts"] = out["numberOfAnalystOpinions"].apply(lambda x: int(x) if pd.notna(x) else 0)
        out["52wk%"] = out.apply(
            lambda r: f"{((r['currentPrice_x']/r['fiftyTwoWeekHigh']-1)*100):.0f}%"
            if pd.notna(r["currentPrice_x"]) and pd.notna(r["fiftyTwoWeekHigh"]) else "N/A",
            axis=1,
        )
        out["InstOwn"] = out["heldPercentInstitutions"].apply(
            lambda x: f"{x*100:.0f}%" if pd.notna(x) else "N/A"
        )
        out["DailyVol$K"] = out["daily_dollar_vol"].apply(lambda x: f"${x/1e3:.0f}K" if pd.notna(x) else "N/A")
        out["Float%"] = out["float_pct"].apply(lambda x: f"{x*100:.0f}%" if pd.notna(x) else "N/A")
        cols = ["ticker", "shortName", "country", "industry", "EV_M", "Rev_M",
                "EV/Rev", "Analysts", "52wk%", "InstOwn", "DailyVol$K", "Float%"]
        avail = [c for c in cols if c in out.columns]
        with pd.option_context("display.max_rows", None, "display.max_colwidth", 38,
                               "display.width", 220):
            print(out[avail].to_string(index=False))

    out_path = DATA_DIR / "investable_candidates.csv"
    passes.to_csv(out_path, index=False)
    print(f"\nSaved investable shortlist: {out_path}")


if __name__ == "__main__":
    main()
