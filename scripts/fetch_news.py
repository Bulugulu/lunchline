"""
Fetch recent news headlines for a ticker via yfinance Ticker.news.

yfinance returns news items with: id, content (which has title, summary,
pubDate, provider, clickThroughUrl, etc.). Free, public.

Usage:
    python scripts/fetch_news.py EXFY
"""

import argparse
import json
from pathlib import Path

import yfinance as yf

DATA_DIR = Path(__file__).parent.parent / "data"
DOSSIER_DIR = DATA_DIR / "dossiers"


def fetch(ticker: str):
    out_dir = DOSSIER_DIR / ticker.lower()
    out_dir.mkdir(parents=True, exist_ok=True)

    print(f"Fetching news for {ticker}...")
    raw = yf.Ticker(ticker).news or []
    print(f"  yfinance returned {len(raw)} items")

    # Normalize. yfinance has changed schemas; handle both shapes.
    normalized = []
    for item in raw:
        content = item.get("content", item)
        normalized.append({
            "id": item.get("id"),
            "title": content.get("title"),
            "summary": content.get("summary"),
            "pub_date": content.get("pubDate") or content.get("displayTime"),
            "provider": (content.get("provider") or {}).get("displayName")
                        if isinstance(content.get("provider"), dict)
                        else content.get("provider"),
            "url": (content.get("clickThroughUrl") or {}).get("url")
                   if isinstance(content.get("clickThroughUrl"), dict)
                   else content.get("link"),
            "type": content.get("contentType"),
        })

    out_path = out_dir / "news.json"
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(normalized, f, indent=2, default=str)
    print(f"  Saved {len(normalized)} items to {out_path}")

    if normalized:
        print(f"\n  Recent headlines:")
        for item in normalized[:5]:
            title = (item.get("title") or "")[:80]
            provider = item.get("provider") or ""
            date = item.get("pub_date") or ""
            print(f"    [{date[:10]}] {provider}: {title}")

    return normalized


def main():
    p = argparse.ArgumentParser()
    p.add_argument("ticker")
    args = p.parse_args()
    fetch(args.ticker)


if __name__ == "__main__":
    main()
