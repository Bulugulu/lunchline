# Prompt Log — AI Usage Appendix

Running log of AI interactions for the Lunchline Partners case study.

## Session 1: Project Setup & Initial Screening (2026-05-26)

### Prompt 1: Project Initialization & Company Screening
**Tool:** Claude Code (Claude Opus 4.7)
**Purpose:** Set up project structure, identify qualifying companies ($10M-$500M EV on NYSE/Nasdaq), cross-reference with Aviv's sector expertise
**Approach:** Parallel subagent architecture — one agent scanned Life_Admin project for background context, another researched micro/nano-cap universe
**Key Outputs:**
- Identified ~1,500-2,500 companies in the $10M-$500M EV range across all sectors
- Narrowed to ~200-400 in technology/software/services
- Shortlisted 13 specific candidates across tiers (Tier 1: MNDO, DH, MCHX, DOMO, EGAN, SMSI, IDN, LPSN, VERI, GVP)
- Established router-based project documentation architecture
**Where AI helped:** Rapidly synthesizing company screening across multiple sources, cross-referencing sector fit with professional background
**Where AI may have gaps:** EV figures are approximate and may be stale; need real-time verification via SEC filings or financial data providers

## Session 2: Data Pipeline & Framework (2026-05-27)

### Prompt 2: Build Data Pipeline
**Tool:** Claude Code (Claude Opus 4.7)
**Purpose:** Replace web-sourced data with reproducible Python pipeline pulling from yfinance and SEC EDGAR
**Key Outputs:**
- `scripts/screen_companies.py` for yfinance-based screening (EV, ratios, FCF, analyst coverage)
- `scripts/fetch_edgar.py` for SEC filings + XBRL structured financials
- Pulled real-time data for the original 11 candidates; revealed EDGAR data current as of Q1 2026
**Where AI helped:** Fast scaffolding of reproducible data scripts with proper SEC User-Agent compliance
**Where AI may have gaps:** Initial candidate list was based on stale web data — confirmed the need for framework-first approach

### Prompt 3: Selection Framework Development
**Tool:** Subagent (general-purpose research)
**Purpose:** Build rigorous framework for interpreting Lunchline's criteria ("messy, mispriced, under-followed; avoid obvious names")
**Key Outputs:**
- 10 messiness archetypes ranked by analytical richness
- 8 mispricing signal patterns specific to micro/nano-cap
- Quantitative under-followed thresholds
- 6-criterion weighted scoring framework (Value Creation 25%, Complexity 20%, Sector Fit 15%, Data 15%, Contrarian 15%, PE Realism 10%)
- Quantitative screening filters (primary + secondary)
- Research on what PE/search fund evaluators reward
**Where AI helped:** Synthesized PE/search fund evaluation criteria into a defensible, scoreable framework
**Where AI may have gaps:** Pre-scored old candidates using web data; those scores are now obsolete given fresh framework-driven screening

## Session 3: Systematic Screening & Validation (2026-05-27 to 2026-05-28)

### Prompt 4: Systematic Framework Screen
**Tool:** Claude Code (Claude Opus 4.7)
**Purpose:** Apply framework filters to full NYSE/Nasdaq Tech + Comm Services universe
**Approach:** Built `scripts/framework_screen.py` with three steps: Finviz universe pull, yfinance enrichment, framework filter application
**Key Outputs:**
- 622 → 292 → 227 → 171 qualifying companies through funnel
- 83 in sweet spot (EV/Rev < 1.5x AND 0-3 analysts)
- 45 in ultra sweet spot ($30-250M EV + sweet spot)
- Industry distribution: 58 Software-Application, 34 Software-Infrastructure, 19 Internet Content, 13 IT Services, 10 Advertising, 9 Gaming
**Where AI helped:** Built reproducible, multi-step screening script in one pass; handled Finviz pagination, yfinance batching, and filter application
**Where AI may have gaps:** Some Chinese ADRs (CCG, LZMH, LGCL) show extreme EV/Rev ratios — may be data quality issues; need manual review

### Prompt 5: Sanity Check Sweet-Spot Candidates
**Tool:** Claude Code (Claude Opus 4.7)
**Purpose:** Validate framework by manually checking 2 candidates against all framework dimensions
**Key Outputs:**
- GDEV (gaming): 6/7 checks passed. Profitable, cash-rich, under-followed.
- EXFY (SaaS): 7/7 checks passed. Cash-rich, FCF positive, classic broken-SaaS story.
**Where AI helped:** Framework checks ran cleanly against real data; framework is producing legitimate candidates
