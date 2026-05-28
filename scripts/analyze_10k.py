"""
Generate ready-to-paste 10-K analysis prompts for a ticker.

Ports the seven analyzer prompts from FinRobot's `finrobot/functional/analyzer.py`
(MIT-licensed, https://github.com/AI4Finance-Foundation/FinRobot). Each prompt pairs
a financial table (from yfinance) with the matching 10-K section (from local EDGAR
HTML) and an instruction tuned for a buyside equity pitch.

Output: data/analysis/<ticker>/prompt_<analysis>.txt — one file per analysis, ready
to paste into Claude or any LLM.

Usage:
    python scripts/analyze_10k.py EXFY                         # use most recent 10-K
    python scripts/analyze_10k.py EXFY --fyear 2025            # pick a fiscal year
    python scripts/analyze_10k.py EXFY --analyses risk,company # subset of analyses
    python scripts/analyze_10k.py EXFY --no-sections           # skip section extraction
"""

import argparse
import re
import sys
from pathlib import Path
from textwrap import dedent

import yfinance as yf
from bs4 import BeautifulSoup

DATA_DIR = Path(__file__).parent.parent / "data"
EDGAR_DIR = DATA_DIR / "edgar"
ANALYSIS_DIR = DATA_DIR / "analysis"


# ---------- 10-K section extraction ----------

SECTION_NEXT = {
    "1": ["1A", "1B", "2"],
    "1A": ["1B", "1C", "2"],
    "7": ["7A", "8"],
    "7A": ["8"],
}


def find_latest_10k(ticker: str, fyear: str | None = None) -> Path | None:
    """Find the most recent 10-K HTML file in data/edgar/<ticker>/filings/.
    If fyear given, prefer filings whose name year matches (filings are dated by
    filing date, which is the year *after* the fiscal year for most issuers)."""
    fdir = EDGAR_DIR / ticker.lower() / "filings"
    if not fdir.exists():
        return None
    candidates = sorted(fdir.glob("*_10-K_*"), reverse=True)
    if not candidates:
        return None
    if fyear:
        target_year = int(fyear) + 1  # filed the year after fiscal year-end
        for c in candidates:
            if c.name.startswith(str(target_year)):
                return c
    return candidates[0]


def extract_section(html_path: Path, item: str) -> str | None:
    """Best-effort extraction of a 10-K Item section.

    Strategy: get all text, find every occurrence of 'Item <item>' in non-TOC form,
    pick the longest stretch between that occurrence and the next 'Item ...' marker
    we know about. Returns None if extraction looks unreliable.
    """
    try:
        html = html_path.read_text(encoding="utf-8", errors="ignore")
    except Exception:
        return None

    soup = BeautifulSoup(html, "html.parser")
    text = soup.get_text(separator="\n")
    text = re.sub(r"[ \t]+", " ", text)
    text = re.sub(r"\n{3,}", "\n\n", text)

    # Find all lines that look like "Item <item>." or "Item <item> "
    item_re = re.compile(
        rf"(?:^|\n)\s*item\s+{re.escape(item)}\b[\.\s]", re.I
    )
    starts = [m.start() for m in item_re.finditer(text)]
    if not starts:
        return None

    # Score each candidate by how few other "Item N" markers appear in the next 2000
    # chars. TOC entries have many neighbors; real section starts have ~0-1.
    any_item_re = re.compile(r"(?:^|\n)\s*item\s+\d+[A-Z]?\b[\.\s]", re.I)
    scored = []
    for s in starts:
        window = text[s + 50 : s + 2000]
        neighbor_count = len(any_item_re.findall(window))
        scored.append((neighbor_count, s))
    # Sort by (fewest neighbors, latest position) — TOC matches cluster at the top
    scored.sort(key=lambda x: (x[0], -x[1]))
    chosen_start = scored[0][1]

    # Find next item marker
    next_items = SECTION_NEXT.get(item, [])
    next_pos = len(text)
    for ni in next_items:
        ni_re = re.compile(rf"(?:^|\n)\s*item\s+{re.escape(ni)}\b[\.\s]", re.I)
        for m in ni_re.finditer(text):
            if m.start() > chosen_start + 200:
                next_pos = min(next_pos, m.start())
                break

    section = text[chosen_start:next_pos].strip()
    # Sanity: section should be at least 500 chars to be useful
    if len(section) < 500:
        return None
    # Cap at ~120k chars (~30k tokens) — Claude has 1M context but we want room
    # for the other sections and the financial tables.
    return section[:120_000]


# ---------- Financial tables (yfinance) ----------

def get_financials(ticker: str) -> dict:
    """Pull income / balance / cash-flow tables from yfinance."""
    t = yf.Ticker(ticker)
    return {
        "income_stmt": t.income_stmt,
        "balance_sheet": t.balance_sheet,
        "cash_flow": t.cashflow,
        "info": t.info,
    }


# ---------- Prompt builders (ported from analyzer.py) ----------

def combine(instruction: str, resource: str, table: str = "") -> str:
    parts = []
    if table:
        parts.append(table)
    parts.append(f"Resource:\n{resource}")
    parts.append(f"Instruction:\n{instruction}")
    return "\n\n".join(parts)


PROMPT_BUILDERS = {}


def register(name):
    def deco(fn):
        PROMPT_BUILDERS[name] = fn
        return fn
    return deco


@register("income")
def income_prompt(fin, sections):
    instruction = dedent("""
        Conduct a comprehensive analysis of the company's income statement for the current fiscal year.
        Start with an overall revenue record, including Year-over-Year or Quarter-over-Quarter comparisons,
        and break down revenue sources to identify primary contributors and trends. Examine the Cost of
        Goods Sold for potential cost control issues. Review profit margins such as gross, operating, and
        net profit margins to evaluate cost efficiency, operational effectiveness, and overall profitability.
        Analyze Earnings Per Share to understand investor perspectives. Compare these metrics with historical
        data and industry or competitor benchmarks to identify growth patterns, profitability trends, and
        operational challenges. The output should be a strategic overview of the company's financial health
        in a single paragraph, less than 130 words, summarizing the previous analysis into 4-5 key points
        under respective subheadings with specific discussion and strong data support.
    """).strip()
    table = "Income statement:\n" + str(fin["income_stmt"])
    return combine(instruction, sections.get("7", "(MD&A section unavailable)"), table)


@register("balance_sheet")
def balance_sheet_prompt(fin, sections):
    instruction = dedent("""
        Delve into a detailed scrutiny of the company's balance sheet for the most recent fiscal year,
        pinpointing the structure of assets, liabilities, and shareholders' equity to decode the firm's
        financial stability and operational efficiency. Focus on evaluating the liquidity through current
        assets versus current liabilities, the solvency via long-term debt ratios, and the equity position
        to gauge long-term investment potential. Contrast these metrics with previous years' data to
        highlight financial trends, improvements, or deteriorations. Finalize with a strategic assessment
        of the company's financial leverage, asset management, and capital structure, providing insights
        into its fiscal health and future prospects in a single paragraph. Less than 130 words.
    """).strip()
    table = "Balance sheet:\n" + str(fin["balance_sheet"])
    return combine(instruction, sections.get("7", "(MD&A section unavailable)"), table)


@register("cash_flow")
def cash_flow_prompt(fin, sections):
    instruction = dedent("""
        Dive into a comprehensive evaluation of the company's cash flow for the latest fiscal year, focusing
        on cash inflows and outflows across operating, investing, and financing activities. Examine the
        operational cash flow to assess the core business profitability, scrutinize investing activities for
        insights into capital expenditures and investments, and review financing activities to understand
        debt, equity movements, and dividend policies. Compare these cash movements to prior periods to
        discern trends, sustainability, and liquidity risks. Conclude with an informed analysis of the
        company's cash management effectiveness, liquidity position, and potential for future growth or
        financial challenges in a single paragraph. Less than 130 words.
    """).strip()
    table = "Cash flow statement:\n" + str(fin["cash_flow"])
    return combine(instruction, sections.get("7", "(MD&A section unavailable)"), table)


@register("segment")
def segment_prompt(fin, sections):
    instruction = dedent("""
        Identify the company's business segments and create a segment analysis using the Management's
        Discussion and Analysis and the income statement, subdivided by segment with clear headings.
        Address revenue and net profit with specific data, and calculate the changes. Detail strategic
        partnerships and their impacts, including details like the companies or organizations. Describe
        product innovations and their effects on income growth. Quantify market share and its changes, or
        state market position and its changes. Analyze market dynamics and profit challenges, noting any
        effects from national policy changes. Include the cost side, detailing operational costs,
        innovation investments, and expenses from channel expansion, etc. Support each statement with
        evidence, keeping each segment analysis concise and under 60 words, accurately sourcing
        information. For each segment, consolidate the most significant findings into one clear, concise
        paragraph, excluding less critical or vaguely described aspects to ensure clarity and reliance on
        evidence-backed information. For each segment, the output should be one single paragraph within
        150 words.
    """).strip()
    table = "Income statement (Segment Analysis):\n" + str(fin["income_stmt"])
    return combine(instruction, sections.get("7", "(MD&A section unavailable)"), table)


@register("business_highlights")
def business_highlights_prompt(fin, sections):
    instruction = dedent("""
        According to the given information, describe the performance highlights for each company's
        business line. Each business description should contain one sentence of a summarization and one
        sentence of explanation.
    """).strip()
    resource = (
        "Business summary (Item 1):\n"
        + sections.get("1", "(unavailable)")
        + "\n\n"
        + "Management's Discussion and Analysis (Item 7):\n"
        + sections.get("7", "(unavailable)")
    )
    return combine(instruction, resource)


@register("company_description")
def company_description_prompt(fin, sections):
    name = fin["info"].get("shortName", "the company")
    step1 = dedent(f"""
        According to the given information,
        1. Briefly describe the company overview and company's industry, using the structure:
           "Founded in xxxx, '{name}' is a xxxx that provides ....."
        2. Highlight core strengths and competitive advantages key products or services,
        3. Include topics about end market (geography), major customers (blue chip or not), market share
           for market position section,
        4. Identify current industry trends, opportunities, and challenges that influence the company's
           strategy,
        5. Outline recent strategic initiatives such as product launches, acquisitions, or new
           partnerships, and describe the company's response to market conditions.
        Less than 300 words.
    """).strip()
    resource = (
        f"Company Name: {name}\n\n"
        "Business summary (Item 1):\n"
        + sections.get("1", "(unavailable)")
        + "\n\n"
        + "Management's Discussion and Analysis (Item 7):\n"
        + sections.get("7", "(unavailable)")
    )
    step1_block = combine(step1, resource)
    step2 = "Summarize the analysis, less than 130 words."
    return combine(step2, step1_block)


@register("risk")
def risk_prompt(fin, sections):
    name = fin["info"].get("shortName", "the company")
    instruction = dedent("""
        According to the given information in the 10-k report, summarize the top 3 key risks of the
        company. Then, for each key risk, break down the risk assessment into the following aspects:
        1. Industry Vertical Risk: How does this industry vertical compare with others in terms of risk?
           Consider factors such as regulation, market volatility, and competitive landscape.
        2. Cyclicality: How cyclical is this industry? Discuss the impact of economic cycles on the
           company's performance.
        3. Risk Quantification: Enumerate the key risk factors with supporting data if the company or
           segment is deemed risky.
        4. Downside Protections: If the company or segment is less risky, discuss the downside protections
           in place. Consider factors such as diversification, long-term contracts, and government
           regulation.

        Finally, provide a detailed and nuanced assessment that reflects the true risk landscape of the
        company. And avoid any bullet points in your response.
    """).strip()
    resource = (
        f"Company Name: {name}\n\n"
        "Risk factors (Item 1A):\n"
        + sections.get("1A", "(unavailable)")
    )
    return combine(instruction, resource)


# ---------- Driver ----------

ALL_ANALYSES = list(PROMPT_BUILDERS.keys())


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("ticker")
    parser.add_argument("--fyear", type=str, default=None,
                        help="Fiscal year of 10-K (e.g. 2025). Defaults to most recent filing on disk.")
    parser.add_argument("--analyses", type=str, default=",".join(ALL_ANALYSES),
                        help=f"Comma-separated subset. Default: all. Options: {','.join(ALL_ANALYSES)}")
    parser.add_argument("--no-sections", action="store_true",
                        help="Skip 10-K section extraction (write prompts with placeholder text + file path).")
    args = parser.parse_args()

    ticker = args.ticker.upper()
    analyses = [a.strip() for a in args.analyses.split(",") if a.strip()]
    for a in analyses:
        if a not in PROMPT_BUILDERS:
            print(f"Unknown analysis: {a}. Options: {','.join(ALL_ANALYSES)}")
            sys.exit(1)

    print(f"Pulling financials for {ticker} via yfinance...")
    fin = get_financials(ticker)

    sections = {}
    tenk_path = find_latest_10k(ticker, args.fyear)
    if tenk_path and not args.no_sections:
        print(f"Extracting sections from {tenk_path.name}...")
        for item in ["1", "1A", "7"]:
            sec = extract_section(tenk_path, item)
            if sec:
                sections[item] = sec
                print(f"  Item {item}: {len(sec):,} chars")
            else:
                print(f"  Item {item}: extraction failed (will use placeholder)")
                sections[item] = f"(Item {item} not extracted; full 10-K at {tenk_path})"
    elif tenk_path:
        print(f"Skipping section extraction; 10-K at {tenk_path}")
        for item in ["1", "1A", "7"]:
            sections[item] = f"(see full 10-K at {tenk_path})"
    else:
        print(f"WARNING: no 10-K found in {EDGAR_DIR / ticker.lower() / 'filings'}")
        print("Run: python scripts/fetch_edgar.py", ticker)
        for item in ["1", "1A", "7"]:
            sections[item] = "(10-K not available locally — run scripts/fetch_edgar.py)"

    out_dir = ANALYSIS_DIR / ticker.lower()
    out_dir.mkdir(parents=True, exist_ok=True)

    print(f"\nWriting {len(analyses)} prompts to {out_dir}/")
    for name in analyses:
        prompt = PROMPT_BUILDERS[name](fin, sections)
        out_path = out_dir / f"prompt_{name}.txt"
        out_path.write_text(prompt, encoding="utf-8")
        print(f"  {out_path.name}: {len(prompt):,} chars")

    print(f"\nDone. Paste each prompt into Claude (or any LLM) to get the analysis.")


if __name__ == "__main__":
    main()
