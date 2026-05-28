"""
Estimate Seeking Alpha coverage for a ticker via DuckDuckGo HTML search.

Seeking Alpha blocks direct scraping (403), so we measure "how much SA writes
about this ticker" by counting indexed results from a search engine.
Used for the framework's "fix obviousness check" — heavy SA coverage =
the name is already obvious to retail/microcap circles.

Outputs:
  - data/dossiers/{ticker}/seeking_alpha.json with:
    * total estimated SA results
    * sample of article titles + URLs (for narrative-flavor check)

Usage:
    python scripts/fetch_seeking_alpha.py EXFY
"""

import argparse
import json
import re
import time
from pathlib import Path
from urllib.parse import quote_plus

import requests
from bs4 import BeautifulSoup

DATA_DIR = Path(__file__).parent.parent / "data"
DOSSIER_DIR = DATA_DIR / "dossiers"

UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36"
HEADERS = {"User-Agent": UA}


def search_ddg(query: str, max_pages: int = 3):
    """DuckDuckGo HTML search. Returns list of {title, url, snippet}."""
    results = []
    url = "https://html.duckduckgo.com/html/"
    for page in range(max_pages):
        params = {"q": query, "s": page * 30}
        try:
            r = requests.post(url, data=params, headers=HEADERS, timeout=20)
            r.raise_for_status()
        except Exception as e:
            print(f"  DDG search err: {e}")
            break
        soup = BeautifulSoup(r.text, "html.parser")
        page_results = soup.find_all("div", class_="result")
        if not page_results:
            break
        for div in page_results:
            link = div.find("a", class_="result__a")
            snippet = div.find("a", class_="result__snippet") or div.find("div", class_="result__snippet")
            if not link:
                continue
            href = link.get("href", "")
            results.append({
                "title": link.get_text(strip=True),
                "url": href,
                "snippet": snippet.get_text(strip=True) if snippet else "",
            })
        time.sleep(1.0)  # DDG rate limit politeness
    return results


def fetch(ticker: str):
    out_dir = DOSSIER_DIR / ticker.lower()
    out_dir.mkdir(parents=True, exist_ok=True)

    queries = [
        f"site:seekingalpha.com {ticker}",
        f"site:seekingalpha.com {ticker} stock",
    ]
    all_results = []
    seen_urls = set()
    for q in queries:
        print(f"  Searching: {q}")
        for hit in search_ddg(q, max_pages=3):
            if "seekingalpha.com" not in hit["url"]:
                continue
            if hit["url"] in seen_urls:
                continue
            seen_urls.add(hit["url"])
            all_results.append(hit)

    # Classify by SA URL pattern: /article, /news, /author
    by_type = {"article": [], "news": [], "other": []}
    for hit in all_results:
        u = hit["url"].lower()
        if "/article/" in u:
            by_type["article"].append(hit)
        elif "/news/" in u:
            by_type["news"].append(hit)
        else:
            by_type["other"].append(hit)

    summary = {
        "ticker": ticker.upper(),
        "method": "DuckDuckGo HTML search of site:seekingalpha.com",
        "total_unique_results": len(all_results),
        "articles_count": len(by_type["article"]),
        "news_count": len(by_type["news"]),
        "other_count": len(by_type["other"]),
        "obviousness_signal": "HIGH" if len(by_type["article"]) >= 10
                              else "MODERATE" if len(by_type["article"]) >= 5
                              else "LOW",
        "results": all_results,
    }
    out_path = out_dir / "seeking_alpha.json"
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(summary, f, indent=2)
    print(f"\n  Total unique SA results found: {len(all_results)}")
    print(f"  Articles (analyst write-ups): {summary['articles_count']}")
    print(f"  News items:                    {summary['news_count']}")
    print(f"  Obviousness signal:            {summary['obviousness_signal']}")
    print(f"  Saved: {out_path}")
    return summary


def main():
    p = argparse.ArgumentParser()
    p.add_argument("ticker")
    args = p.parse_args()
    fetch(args.ticker)


if __name__ == "__main__":
    main()
