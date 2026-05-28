"""
Build a comprehensive research dossier for a single ticker.

Runs all fetchers and consolidates outputs in data/dossiers/{ticker}/:
  - edgar/        — SEC filings (10-K, 10-Q, 8-K, DEF 14A, Form 4) + XBRL
  - transcripts/  — Earnings call transcripts (last 8 quarters by default)
  - news.json     — Recent news headlines (yfinance)
  - analyst.json  — Sell-side analyst data (yfinance)
  - seeking_alpha.json — SA coverage estimate (DuckDuckGo)
  - yfinance_info.json — Full company info snapshot
  - summary.md    — Human-readable index of what was collected

Usage:
    python scripts/build_dossier.py EXFY
    python scripts/build_dossier.py EXFY --transcripts 4
"""

import argparse
import json
import shutil
import sys
import time
from pathlib import Path

import yfinance as yf

# Ensure local imports work regardless of CWD.
SCRIPTS_DIR = Path(__file__).parent
sys.path.insert(0, str(SCRIPTS_DIR))

import fetch_edgar
import fetch_transcripts
import fetch_news
import fetch_analyst
import fetch_seeking_alpha

DATA_DIR = SCRIPTS_DIR.parent / "data"
DOSSIER_DIR = DATA_DIR / "dossiers"


def fetch_yfinance_snapshot(ticker: str, out_dir: Path):
    """Save the full yfinance info dict as a snapshot."""
    print(f"\n[yfinance] Fetching company snapshot for {ticker}...")
    t = yf.Ticker(ticker)
    info = t.info
    out_path = out_dir / "yfinance_info.json"
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(info, f, indent=2, default=str)
    print(f"  Saved: {out_path} ({len(info)} fields)")
    return info


def fetch_edgar_into_dossier(ticker: str, dossier_dir: Path):
    """Run fetch_edgar, then move its output into the dossier directory."""
    print(f"\n[EDGAR] Fetching SEC filings for {ticker}...")
    fetch_edgar.fetch_filings(ticker)
    fetch_edgar.fetch_xbrl_financials(ticker)

    # Move from data/edgar/{ticker}/ into data/dossiers/{ticker}/edgar/
    src = DATA_DIR / "edgar" / ticker.lower()
    dst = dossier_dir / "edgar"
    if src.exists():
        if dst.exists():
            shutil.rmtree(dst)
        shutil.copytree(src, dst)
        print(f"  Copied EDGAR data to {dst}")


def write_summary(ticker: str, dossier_dir: Path, info: dict):
    """Write a human-readable index of everything we collected."""
    summary_lines = []
    summary_lines.append(f"# {ticker.upper()} Research Dossier\n")
    summary_lines.append(f"**Company:** {info.get('shortName', 'Unknown')}")
    summary_lines.append(f"**Sector / Industry:** {info.get('sector', 'N/A')} / {info.get('industry', 'N/A')}")
    summary_lines.append(f"**Country:** {info.get('country', 'N/A')}")
    summary_lines.append(f"**Website:** {info.get('website', 'N/A')}")
    summary_lines.append("")

    summary_lines.append("## Snapshot")
    summary_lines.append(f"- Enterprise Value: ${info.get('enterpriseValue', 0)/1e6:.1f}M" if info.get('enterpriseValue') else "- Enterprise Value: N/A")
    summary_lines.append(f"- Market Cap: ${info.get('marketCap', 0)/1e6:.1f}M" if info.get('marketCap') else "- Market Cap: N/A")
    summary_lines.append(f"- Revenue (TTM): ${info.get('totalRevenue', 0)/1e6:.1f}M" if info.get('totalRevenue') else "- Revenue (TTM): N/A")
    ev_rev = info.get('enterpriseToRevenue')
    summary_lines.append(f"- EV/Revenue: {ev_rev:.2f}x" if ev_rev else "- EV/Revenue: N/A")
    summary_lines.append(f"- Operating Margin: {info.get('operatingMargins', 0)*100:.1f}%" if info.get('operatingMargins') is not None else "- Operating Margin: N/A")
    summary_lines.append(f"- Free Cash Flow: ${info.get('freeCashflow', 0)/1e6:.1f}M" if info.get('freeCashflow') else "- Free Cash Flow: N/A")
    summary_lines.append(f"- Cash: ${info.get('totalCash', 0)/1e6:.1f}M" if info.get('totalCash') else "- Cash: N/A")
    summary_lines.append(f"- Debt: ${info.get('totalDebt', 0)/1e6:.1f}M" if info.get('totalDebt') else "- Debt: N/A")
    summary_lines.append(f"- Analyst Coverage: {info.get('numberOfAnalystOpinions', 0)} analysts")
    summary_lines.append(f"- Institutional Ownership: {info.get('heldPercentInstitutions', 0)*100:.1f}%" if info.get('heldPercentInstitutions') is not None else "- Institutional Ownership: N/A")
    summary_lines.append("")

    summary_lines.append("## Files in this dossier")
    summary_lines.append("```")
    for entry in sorted(dossier_dir.rglob("*")):
        if entry.is_file():
            rel = entry.relative_to(dossier_dir)
            size = entry.stat().st_size
            unit = "B" if size < 1024 else "KB" if size < 1024**2 else "MB"
            div = 1 if size < 1024 else 1024 if size < 1024**2 else 1024**2
            summary_lines.append(f"  {str(rel):<60} {size/div:>7.1f} {unit}")
    summary_lines.append("```")
    summary_lines.append("")

    summary_lines.append("## Business Summary")
    summary_lines.append(info.get("longBusinessSummary", "N/A"))
    summary_lines.append("")

    summary_path = dossier_dir / "summary.md"
    summary_path.write_text("\n".join(summary_lines), encoding="utf-8")
    print(f"\n[summary] Wrote {summary_path}")


def build(ticker: str, transcripts_limit: int = 8):
    ticker = ticker.upper()
    dossier_dir = DOSSIER_DIR / ticker.lower()
    dossier_dir.mkdir(parents=True, exist_ok=True)

    print(f"\n{'='*70}")
    print(f"BUILDING DOSSIER FOR {ticker}")
    print(f"Output: {dossier_dir}")
    print(f"{'='*70}")

    start = time.time()
    errors = []

    def try_step(name, fn):
        try:
            fn()
        except Exception as e:
            print(f"  [!] {name} failed: {e}")
            errors.append((name, str(e)))

    info = None

    def _yf():
        nonlocal info
        info = fetch_yfinance_snapshot(ticker, dossier_dir)

    try_step("yfinance snapshot", _yf)
    try_step("EDGAR filings", lambda: fetch_edgar_into_dossier(ticker, dossier_dir))
    try_step("Earnings transcripts", lambda: fetch_transcripts.fetch_all_for_ticker(ticker, limit=transcripts_limit))
    try_step("News headlines", lambda: fetch_news.fetch(ticker))
    try_step("Analyst data", lambda: fetch_analyst.fetch(ticker))
    try_step("Seeking Alpha coverage", lambda: fetch_seeking_alpha.fetch(ticker))

    if info:
        try_step("Summary writeup", lambda: write_summary(ticker, dossier_dir, info))

    elapsed = time.time() - start
    print(f"\n{'='*70}")
    print(f"DOSSIER COMPLETE — {elapsed:.1f}s")
    print(f"{'='*70}")
    if errors:
        print(f"\n{len(errors)} error(s):")
        for name, err in errors:
            print(f"  - {name}: {err}")
    else:
        print("All steps succeeded.")
    print(f"\nDossier: {dossier_dir}")


def main():
    p = argparse.ArgumentParser()
    p.add_argument("ticker")
    p.add_argument("--transcripts", type=int, default=8, help="Number of recent transcripts (default 8)")
    args = p.parse_args()
    build(args.ticker, transcripts_limit=args.transcripts)


if __name__ == "__main__":
    main()
