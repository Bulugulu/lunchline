# Screening Data Sources

Reference table for the screening data sources used by `scripts/framework_screen.py` and `scripts/fetch_edgar.py`.

Screening results and the full screening narrative live in [../CHANGELOG.md](../CHANGELOG.md) (2026-05-28 entries). Filter specifications live in [public-company-pitch.md § 4](public-company-pitch.md).

## Tools & Data Sources

| Tool | URL | What It Gives Us | Access Method |
|------|-----|-----------------|---------------|
| **yfinance** (Python) | via `scripts/framework_screen.py` | Real-time EV, market cap, margins, FCF, analyst count, ratios | Free API, automated |
| **SEC EDGAR** | data.sec.gov | 10-K, 10-Q, 8-K filings + XBRL structured financials | Free API via `scripts/fetch_edgar.py` |
| **Finviz Screener** | finviz.com/screener | Market cap filter, sector/industry, technical signals | Free (no direct EV filter on free tier) |
| **StockAnalysis** | stockanalysis.com | Filterable micro/nano-cap lists, financial data | Free |
| **The Acquirer's Multiple** | acquirersmultiple.com | EV-based deep-value screening | Free (limited) / Paid |
| **EDGAR Full-Text Search** | efts.sec.gov/LATEST/search-index | Search 8-K filings for keywords (strategic alternatives, management change, etc.) | Free API |
| **SEC EDGAR Company Search** | www.sec.gov/cgi-bin/browse-edgar | Find specific companies, CIK lookup | Free |
| **Financial Modeling Prep** | financialmodelingprep.com | Analyst price targets, historical market cap, single-company metrics, comp data | Free tier + paid Starter for `/v4/price-target` |
| **roic.ai** | roic.ai | Earnings call transcripts (scraped) | Free (flaky) |
