"""
Fetch earnings call transcripts from roic.ai.

Roic.ai publishes earnings call transcripts publicly (free) for most US-listed
companies. URL pattern:
    https://www.roic.ai/quote/{TICKER}/transcripts
    https://www.roic.ai/quote/{TICKER}/transcripts/{year}-year/{quarter}-quarter

Usage:
    python scripts/fetch_transcripts.py EXFY              # Last 8 transcripts
    python scripts/fetch_transcripts.py EXFY --limit 4    # Last 4
    python scripts/fetch_transcripts.py EXFY --all        # All available
"""

import argparse
import json
import re
import time
from pathlib import Path
from urllib.parse import urljoin

import requests
from bs4 import BeautifulSoup

DATA_DIR = Path(__file__).parent.parent / "data"
DOSSIER_DIR = DATA_DIR / "dossiers"

UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36"
HEADERS = {"User-Agent": UA}

BASE = "https://www.roic.ai"


def list_transcripts(ticker: str):
    """Return list of dicts: {year, quarter, date_label, url}."""
    url = f"{BASE}/quote/{ticker.upper()}/transcripts"
    r = requests.get(url, headers=HEADERS, timeout=30)
    r.raise_for_status()
    soup = BeautifulSoup(r.text, "html.parser")

    pattern = re.compile(r"/quote/[A-Z]+/transcripts/(\d{4})-year/(\d)-quarter")
    items = []
    seen = set()
    for a in soup.find_all("a", href=True):
        m = pattern.search(a["href"])
        if not m:
            continue
        href = a["href"]
        if href in seen:
            continue
        seen.add(href)
        year, qtr = m.group(1), m.group(2)
        items.append({
            "year": int(year),
            "quarter": int(qtr),
            "date_label": a.get_text(strip=True),
            "url": urljoin(BASE, href),
        })
    # Sort newest first
    items.sort(key=lambda x: (x["year"], x["quarter"]), reverse=True)
    return items


def fetch_transcript(url: str) -> str:
    """Fetch a single transcript and return cleaned plain text."""
    r = requests.get(url, headers=HEADERS, timeout=30)
    r.raise_for_status()
    soup = BeautifulSoup(r.text, "html.parser")

    # Strip nav, script, style
    for tag in soup(["script", "style", "nav", "header", "footer"]):
        tag.decompose()

    text = soup.get_text(separator="\n", strip=True)

    # The transcript content starts after the listing nav.
    # Heuristic: cut everything before the first occurrence of a phrase that
    # commonly opens earnings calls.
    start_markers = [
        "Good afternoon", "Good morning", "Good evening",
        "Welcome to", "thank you for joining", "Thank you for joining",
        "Ladies and gentlemen",
    ]
    cut = 0
    for marker in start_markers:
        idx = text.find(marker)
        if idx > 0:
            # Back up to start of line
            line_start = text.rfind("\n", 0, idx) + 1
            cut = line_start
            break

    if cut > 0:
        text = text[cut:]

    return text


def fetch_all_for_ticker(ticker: str, limit: int = 8):
    out_dir = DOSSIER_DIR / ticker.lower() / "transcripts"
    out_dir.mkdir(parents=True, exist_ok=True)

    print(f"Listing transcripts for {ticker}...")
    try:
        items = list_transcripts(ticker)
    except Exception as e:
        print(f"  Failed to list transcripts: {e}")
        return []

    print(f"  Found {len(items)} transcripts available")
    if not items:
        return []

    to_fetch = items[:limit] if limit else items
    saved = []
    for t in to_fetch:
        fname = f"{t['year']}-Q{t['quarter']}.txt"
        out_path = out_dir / fname
        if out_path.exists() and out_path.stat().st_size > 1000:
            print(f"  [skip] {fname} already exists ({out_path.stat().st_size} bytes)")
            saved.append({"path": str(out_path), **t})
            continue
        print(f"  Fetching {fname}...", end=" ", flush=True)
        try:
            text = fetch_transcript(t["url"])
            if len(text) < 500:
                print(f"too short ({len(text)} chars), skipping")
                continue
            out_path.write_text(text, encoding="utf-8")
            print(f"OK ({len(text)} chars)")
            saved.append({"path": str(out_path), "chars": len(text), **t})
        except Exception as e:
            print(f"err: {e}")
        time.sleep(0.5)

    index_path = out_dir / "index.json"
    with open(index_path, "w") as f:
        json.dump(saved, f, indent=2)
    print(f"  Index: {index_path}")
    print(f"  Saved {len(saved)} transcripts to {out_dir}")
    return saved


def main():
    p = argparse.ArgumentParser()
    p.add_argument("ticker")
    p.add_argument("--limit", type=int, default=8)
    p.add_argument("--all", action="store_true", help="Fetch all available")
    args = p.parse_args()
    limit = 0 if args.all else args.limit
    fetch_all_for_ticker(args.ticker, limit=limit)


if __name__ == "__main__":
    main()
