# Company Screening Research

## Status: Framework Complete — Ready for Systematic Screening

## Approach
Use the quantitative filters from [public-company-pitch.md](public-company-pitch.md) Section 4 to systematically screen, then score candidates against the weighted framework in Section 2.

## Screening Tools & Data Sources

| Tool | URL | What It Gives Us | Access Method |
|------|-----|-----------------|---------------|
| **yfinance** (Python) | via `scripts/screen_companies.py` | Real-time EV, market cap, margins, FCF, analyst count, ratios | Free API, automated |
| **SEC EDGAR** | data.sec.gov | 10-K, 10-Q, 8-K filings + XBRL structured financials | Free API via `scripts/fetch_edgar.py` |
| **Finviz Screener** | finviz.com/screener | Market cap filter, sector/industry, technical signals | Free (no direct EV filter on free tier) |
| **StockAnalysis** | stockanalysis.com | Filterable micro/nano-cap lists, financial data | Free |
| **The Acquirer's Multiple** | acquirersmultiple.com | EV-based deep-value screening | Free (limited) / Paid |
| **EDGAR Full-Text Search** | efts.sec.gov/LATEST/search-index | Search 8-K filings for keywords (strategic alternatives, management change, etc.) | Free API |
| **SEC EDGAR Company Search** | www.sec.gov/cgi-bin/browse-edgar | Find specific companies, CIK lookup | Free |

## Screening Process (To Execute)

### Step 1: Generate Universe
- Pull all NYSE/Nasdaq stocks with market cap $10M-$500M from Finviz or StockAnalysis
- Filter to relevant sectors (Application Software, SaaS, AI/ML, Gaming, Consumer Internet, Data Analytics, Digital Media, Marketing Tech, Vertical SaaS)
- Export as CSV into `data/universe/`

### Step 2: Enrich with EV and Key Metrics
- Run `scripts/screen_companies.py` against universe to get real-time EV
- Filter to EV $10M-$500M (prefer $30M-$250M)
- Apply secondary messiness filters: EV/Revenue < 1.5x, >40% decline from 52wk high, 0-3 analysts

### Step 3: Apply Messiness Signals
- Search EDGAR 8-K filings for keywords: "strategic alternatives," "exploring options," "management transition," "restatement"
- Check for insider buying (Form 4 data)
- Check for recent CEO/CFO departures

### Step 4: Score Against Framework
- Take top 10-15 candidates that pass all primary filters
- Score each on the 6-criterion weighted framework
- Rank and select top 3 for deeper diligence

### Step 5: Deep Dive (Top 3)
- Pull full financial statements (5 years)
- Read earnings call transcripts
- Check Seeking Alpha article count (obviousness test)
- Assess data availability for full financial model

## Candidates (Post-Framework Screening)
*To be populated after systematic screening is executed.*
