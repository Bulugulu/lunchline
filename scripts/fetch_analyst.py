"""
Fetch sell-side analyst data from yfinance.

Captures:
  - recommendationKey, recommendationMean (current consensus)
  - analyst_price_targets (current PT distribution: low/mean/median/high)
  - upgrades_downgrades (full history of analyst actions)
  - recommendations (rolling consensus by month)
  - earnings_estimate, revenue_estimate, eps_trend if available

Usage:
    python scripts/fetch_analyst.py EXFY
"""

import argparse
import json
from pathlib import Path

import pandas as pd
import yfinance as yf

DATA_DIR = Path(__file__).parent.parent / "data"
DOSSIER_DIR = DATA_DIR / "dossiers"


def fetch(ticker: str):
    out_dir = DOSSIER_DIR / ticker.lower()
    out_dir.mkdir(parents=True, exist_ok=True)

    print(f"Fetching analyst data for {ticker}...")
    t = yf.Ticker(ticker)

    info = t.info
    summary = {
        "recommendationKey": info.get("recommendationKey"),
        "recommendationMean": info.get("recommendationMean"),
        "numberOfAnalystOpinions": info.get("numberOfAnalystOpinions"),
        "targetMeanPrice": info.get("targetMeanPrice"),
        "targetMedianPrice": info.get("targetMedianPrice"),
        "targetLowPrice": info.get("targetLowPrice"),
        "targetHighPrice": info.get("targetHighPrice"),
        "currentPrice": info.get("currentPrice"),
    }
    try:
        summary["analyst_price_targets"] = t.analyst_price_targets
    except Exception:
        pass

    # Recommendations (rolling consensus by month)
    try:
        recs = t.recommendations
        if isinstance(recs, pd.DataFrame) and not recs.empty:
            summary["recommendations_rolling"] = recs.to_dict(orient="records")
    except Exception as e:
        print(f"  recommendations error: {e}")

    # Upgrades/downgrades — full history of analyst actions
    try:
        ud = t.upgrades_downgrades
        if isinstance(ud, pd.DataFrame) and not ud.empty:
            ud_reset = ud.reset_index()
            ud_reset["GradeDate"] = ud_reset["GradeDate"].astype(str)
            summary["upgrades_downgrades"] = ud_reset.to_dict(orient="records")
    except Exception as e:
        print(f"  upgrades_downgrades error: {e}")

    # Earnings/revenue estimates
    for attr in ("earnings_estimate", "revenue_estimate", "eps_trend", "growth_estimates"):
        try:
            v = getattr(t, attr)
            if isinstance(v, pd.DataFrame) and not v.empty:
                summary[attr] = v.reset_index().to_dict(orient="records")
        except Exception:
            pass

    out_path = out_dir / "analyst.json"
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(summary, f, indent=2, default=str)
    print(f"  Saved analyst data to {out_path}")

    # Console summary
    print(f"\n  Current consensus: {summary.get('recommendationKey')} "
          f"(mean rating {summary.get('recommendationMean')}, "
          f"{summary.get('numberOfAnalystOpinions')} analysts)")
    pt = summary.get("analyst_price_targets") or {}
    if pt:
        print(f"  Price targets: low={pt.get('low')}, mean={pt.get('mean')}, "
              f"high={pt.get('high')} vs current {pt.get('current')}")
    if "upgrades_downgrades" in summary:
        print(f"  Upgrade/downgrade actions on record: {len(summary['upgrades_downgrades'])}")

    return summary


def main():
    p = argparse.ArgumentParser()
    p.add_argument("ticker")
    args = p.parse_args()
    fetch(args.ticker)


if __name__ == "__main__":
    main()
