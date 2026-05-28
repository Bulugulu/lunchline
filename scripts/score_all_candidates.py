"""
Score every qualifying candidate against the full 7-check sanity framework
(not just the 4 hard filters). Produces a ranked list of 7/7, 6/7, 5/7 candidates.

The 7 checks:
  1. EV in $10M-$500M
  2. Revenue > $10M
  3. EV/Revenue < 1.5x
  4. Under-followed (0-3 analysts)
  5. Down >40% from 52wk high (fallen angel)
  6. Institutional ownership < 50%
  7. Market cap / EV disconnect (EV/MCap > 2x or < 0.5x)

Usage:
    python scripts/score_all_candidates.py
    python scripts/score_all_candidates.py --from-cache    # use cached enrichment
"""

import argparse
import time
from pathlib import Path

import pandas as pd
import yfinance as yf

DATA_DIR = Path(__file__).parent.parent / "data"
DATA_DIR.mkdir(exist_ok=True)

EV_MIN = 10_000_000
EV_MAX = 500_000_000
EV_SWEET_MIN = 30_000_000
EV_SWEET_MAX = 250_000_000
MIN_REVENUE = 10_000_000
MAX_ANALYSTS = 3
EV_REV_THRESHOLD = 1.5

INCLUDE_SECTORS_FINVIZ = ["Technology", "Communication Services"]
EXCLUDE_INDUSTRIES = [
    "Semiconductors", "Semiconductor Equipment & Materials",
    "Consumer Electronics", "Computer Hardware",
    "Electronic Components", "Solar", "Communication Equipment",
]


def pull_universe():
    from finvizfinance.screener.overview import Overview
    all_results = []
    for cap_label, cap_filter in [
        ("Nano", "Nano (under $50mln)"),
        ("Micro", "Micro ($50mln to $300mln)"),
        ("Small", "Small ($300mln to $2bln)"),
    ]:
        for sector in INCLUDE_SECTORS_FINVIZ:
            print(f"  {cap_label} / {sector}...", end=" ", flush=True)
            try:
                fo = Overview()
                fo.set_filter(filters_dict={"Market Cap.": cap_filter, "Sector": sector})
                df = fo.screener_view()
                if df is not None and not df.empty:
                    df["cap_category"] = cap_label
                    all_results.append(df)
                    print(f"{len(df)}")
                else:
                    print("0")
                time.sleep(1)
            except Exception as e:
                print(f"ERR: {e}")
                time.sleep(2)
    universe = pd.concat(all_results, ignore_index=True).drop_duplicates(subset=["Ticker"])
    universe.to_csv(DATA_DIR / "universe_raw.csv", index=False)
    print(f"Total: {len(universe)}")
    return universe


def enrich(universe_df, batch_size=20):
    tickers = universe_df["Ticker"].tolist()
    fields = [
        "shortName", "sector", "industry", "marketCap", "enterpriseValue",
        "totalRevenue", "operatingMargins", "freeCashflow", "totalCash", "totalDebt",
        "enterpriseToRevenue", "numberOfAnalystOpinions",
        "fiftyTwoWeekHigh", "currentPrice", "heldPercentInstitutions",
        "fullTimeEmployees",
    ]
    all_data = []
    n_batches = (len(tickers) + batch_size - 1) // batch_size
    for i in range(0, len(tickers), batch_size):
        batch = tickers[i:i + batch_size]
        print(f"  Batch {i // batch_size + 1}/{n_batches}...", end=" ", flush=True)
        try:
            ytickers = yf.Tickers(" ".join(batch))
            for tkr in batch:
                try:
                    info = ytickers.tickers[tkr].info
                    row = {"ticker": tkr}
                    for f in fields:
                        row[f] = info.get(f)
                    all_data.append(row)
                except Exception:
                    all_data.append({"ticker": tkr, "error": True})
            print("OK")
        except Exception as e:
            print(f"err: {e}")
            for tkr in batch:
                all_data.append({"ticker": tkr, "error": True})
        time.sleep(0.4)
    enriched = pd.DataFrame(all_data)
    enriched.to_csv(DATA_DIR / "universe_enriched.csv", index=False)
    return enriched


def score_row(row):
    """Apply 7-check framework to a single row. Returns (score, checks_dict)."""
    ev = row.get("enterpriseValue")
    rev = row.get("totalRevenue")
    ev_rev = row.get("enterpriseToRevenue")
    analysts = row.get("numberOfAnalystOpinions")
    high52 = row.get("fiftyTwoWeekHigh")
    price = row.get("currentPrice")
    inst = row.get("heldPercentInstitutions")
    mcap = row.get("marketCap")

    checks = {}

    checks["ev_in_range"] = bool(pd.notna(ev) and EV_MIN <= ev <= EV_MAX)
    checks["rev_min"] = bool(pd.notna(rev) and rev >= MIN_REVENUE)
    checks["ev_rev_low"] = bool(pd.notna(ev_rev) and ev_rev < EV_REV_THRESHOLD)
    # Under-followed: pass if NaN/0 OR <= 3
    if pd.isna(analysts):
        checks["under_followed"] = True
    else:
        checks["under_followed"] = analysts <= MAX_ANALYSTS

    if pd.notna(price) and pd.notna(high52) and high52 > 0:
        pct = (price / high52 - 1) * 100
        checks["fallen_angel"] = pct < -40
    else:
        checks["fallen_angel"] = False

    if pd.notna(inst):
        checks["low_inst_own"] = inst < 0.5
    else:
        checks["low_inst_own"] = False

    if pd.notna(ev) and pd.notna(mcap) and mcap > 0:
        ratio = ev / mcap
        checks["ev_mcap_disconnect"] = ratio > 2 or ratio < 0.5
    else:
        checks["ev_mcap_disconnect"] = False

    score = sum(1 for v in checks.values() if v)
    return score, checks


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--from-cache", action="store_true")
    args = parser.parse_args()

    enr_path = DATA_DIR / "universe_enriched.csv"
    raw_path = DATA_DIR / "universe_raw.csv"

    if args.from_cache and enr_path.exists():
        print(f"Loading cached enrichment: {enr_path}")
        enriched = pd.read_csv(enr_path)
    else:
        if args.from_cache and raw_path.exists():
            print(f"Loading cached universe: {raw_path}")
            universe = pd.read_csv(raw_path)
        else:
            print("Pulling universe from Finviz...")
            universe = pull_universe()
        print(f"\nEnriching {len(universe)} tickers...")
        enriched = enrich(universe)

    print(f"\nEnriched rows: {len(enriched)}")
    if "error" in enriched.columns:
        df = enriched[enriched["error"] != True].copy()
    else:
        df = enriched.copy()

    # Apply hard filters (these are entry tickets, not the 7 checks)
    df = df[df["enterpriseValue"].notna()]
    df = df[(df["enterpriseValue"] >= EV_MIN) & (df["enterpriseValue"] <= EV_MAX)]
    df = df[df["totalRevenue"].notna() & (df["totalRevenue"] >= MIN_REVENUE)]
    if "industry" in df.columns:
        df = df[~df["industry"].isin(EXCLUDE_INDUSTRIES)]
    print(f"Qualifying universe (EV+rev+industry filters): {len(df)}")

    # Score every row on the 7 checks
    scores = df.apply(score_row, axis=1)
    df["framework_score"] = [s[0] for s in scores]
    for k in ["ev_in_range", "rev_min", "ev_rev_low", "under_followed",
             "fallen_angel", "low_inst_own", "ev_mcap_disconnect"]:
        df[k] = [s[1][k] for s in scores]

    print("\n" + "=" * 70)
    print("FRAMEWORK SCORE DISTRIBUTION (out of 7 checks)")
    print("=" * 70)
    print(df["framework_score"].value_counts().sort_index(ascending=False).to_string())

    print("\nIn the ULTRA SWEET SPOT band ($30-250M EV, EV/Rev<1.5x, <=3 analysts):")
    ultra = df[
        (df["enterpriseValue"] >= EV_SWEET_MIN) & (df["enterpriseValue"] <= EV_SWEET_MAX) &
        df["ev_rev_low"] & df["under_followed"]
    ]
    print(f"  Total: {len(ultra)}")
    print(ultra["framework_score"].value_counts().sort_index(ascending=False).to_string())

    for target in [7, 6, 5]:
        bucket = df[df["framework_score"] == target].sort_values("enterpriseValue")
        print("\n" + "=" * 70)
        print(f"COMPANIES SCORING {target}/7  (n={len(bucket)})")
        print("=" * 70)
        if len(bucket) == 0:
            continue
        out = bucket.copy()
        out["EV_M"] = out["enterpriseValue"].apply(lambda x: f"${x/1e6:.0f}M")
        out["Rev_M"] = out["totalRevenue"].apply(lambda x: f"${x/1e6:.0f}M")
        out["EV/Rev"] = out["enterpriseToRevenue"].apply(lambda x: f"{x:.2f}x" if pd.notna(x) else "N/A")
        out["Analysts"] = out["numberOfAnalystOpinions"].apply(lambda x: int(x) if pd.notna(x) else 0)
        out["52wk%"] = out.apply(
            lambda r: f"{((r['currentPrice']/r['fiftyTwoWeekHigh']-1)*100):.0f}%"
            if pd.notna(r["currentPrice"]) and pd.notna(r["fiftyTwoWeekHigh"]) else "N/A",
            axis=1,
        )
        out["InstOwn"] = out["heldPercentInstitutions"].apply(
            lambda x: f"{x*100:.0f}%" if pd.notna(x) else "N/A"
        )
        cols = ["ticker", "shortName", "industry", "EV_M", "Rev_M", "EV/Rev",
                "Analysts", "52wk%", "InstOwn"]
        avail = [c for c in cols if c in out.columns]
        with pd.option_context("display.max_rows", None, "display.max_colwidth", 40,
                               "display.width", 200):
            print(out[avail].to_string(index=False))

    # Save scored output
    out_path = DATA_DIR / "scored_candidates.csv"
    df.sort_values("framework_score", ascending=False).to_csv(out_path, index=False)
    print(f"\nFull scored output: {out_path}")


if __name__ == "__main__":
    main()
