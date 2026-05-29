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

## Session 4: FinRobot Repo Review + Analyzer/Valuation Port (2026-05-28)

### Prompt 6: FinRobot Repo Synthesis
**Tool:** Subagent (general-purpose research)
**Purpose:** Decide whether to install FinRobot (https://github.com/AI4Finance-Foundation/FinRobot) or borrow specific methods. Initial framing rejected wholesale install (AutoGen overhead, OpenAI cost, originality risk for the case study).
**Key Outputs:**
- Identified `finrobot_equity/` (Mar 2026) as the load-bearing module — 8 specialized agents mapping ~1:1 onto a buyside pitch.
- Confirmed README's "Adanos" reference is hype — no source code uses it. Real sentiment stack is Finnhub + Reddit + FinNLP.
- Surfaced three borrowable artifacts: (a) six tightly-scoped 10-K analyzer prompts pairing table + section + instruction, (b) FMP endpoints for analyst targets + competitor comps, (c) pure-Python DCF + football-field generator in `valuation_engine.py`.
- Flagged red flags: AutoGen group-chat orchestration unnecessary for one-shot analysis, 11-agent quant factor team is mostly stub system messages, notebook-driven dev in places.
**Where AI helped:** Distinguished marketing claims from working code by reading the actual source tree; identified the small subset (~3 modules) worth porting vs. the bulk of the framework to skip.
**Where AI may have gaps:** Did not verify FMP free-tier limits empirically; price-target endpoint is /v4 which typically requires the Starter plan.

### Prompt 7: Port 10-K Analyzer Prompts
**Tool:** Claude Code (Claude Opus 4.7)
**Purpose:** Port FinRobot's seven `analyzer.py` prompts (income / balance / cash flow / segment / business highlights / company description / risk) into `scripts/analyze_10k.py`. Each prompt pairs a financial table (yfinance) with the matching 10-K section (local EDGAR HTML) and an instruction.
**Approach:** Wrote BS4 + regex section extractor with a TOC-discrimination heuristic — score each "Item N" candidate by how many other Item markers appear in the next 2000 chars (TOC entries cluster; real section starts are isolated).
**Key Outputs:**
- `scripts/analyze_10k.py` — generates seven ready-to-paste prompt files per ticker.
- Verified against EXFY's 2026 10-K: Item 1 (54k chars), Item 1A (120k cap), Item 7 (48k). All three start at the actual section heading, not the TOC.
**Where AI helped:** Wrote a pragmatic section extractor that handles the common iXBRL 10-K layout in one pass.
**Where AI may have gaps:** Heuristic is tuned to recent 10-K HTML structure; older filings (pre-2020) may need different handling.

### Prompt 8: Port FMP Fetcher
**Tool:** Claude Code (Claude Opus 4.7)
**Purpose:** Port FinRobot's `fmp_utils.py` endpoints into `scripts/fetch_fmp.py` — analyst price targets (consensus min/max/median), historical market cap, BVPS, single-company financial metrics, and competitor comps.
**Approach:** Fixed a bug in the original `Revenue Growth` calc (uses `year_offset-1` when `year_offset==0`, which wraps to the oldest year — wrong). Added graceful error handling for missing API key, plan-tier limits, and bad symbols. Output paths under `data/fmp/<ticker>/`.
**Where AI helped:** Identified and fixed the off-by-one growth-rate bug while porting.
**Where AI may have gaps:** Did not exercise live API calls (requires FMP_API_KEY). The /v4 price-target endpoint likely requires the paid Starter plan; tested only the no-key error path locally.

### Prompt 10: Pre-EBITDA Valuation Methods Research
**Tool:** Subagent (general-purpose research)
**Purpose:** Determine standard institutional practice for valuing companies with negative TTM EBITDA. Triggered by `valuation.py` aborting on EXFY (the framework's flagship 7/7 candidate) — needed to know what professional analysts actually do instead of EV/EBITDA + DCF.
**Key Outputs:**
- Triangulation stack: EV/FCF (bypasses SBC debate) + Rule of 40-anchored EV/Revenue (Bessemer/Meritech) + Path-to-Profitability DCF with survival haircut (Damodaran). Cross-check with normalized year-3 EBITDA at search-fund 4-6x for downside anchor.
- The SBC fault line: value/PE camp treats SBC as cash cost; growth-equity adds it back. Lunchline's PE lens sides with value camp — should be stated explicitly in the deck.
- Meritech standard is EV/NTM Gross Profit, not EV/Revenue — rationale that GP captures business-model quality (vertical SaaS ~11x GP vs horizontal ~5x).
- Sourced from Damodaran (NYU Stern), Morningstar methodology, Bessemer Cloud Index, Meritech benchmarking, FTI Consulting / Oldfield (SBC critique).
**Where AI helped:** Surfaced the SBC fault line as a methodological signal worth stating explicitly in the pitch, and the convergent "three-layer triangulation" framing used across Bessemer / Meritech / Damodaran.
**Where AI may have gaps:** Multiple ranges cited are 2024-Q4 2025 data; sector defaults should be re-verified against current cloud-index data closer to pitch date.

### Prompt 12: Per-Company Peer Benchmarks Refactor
**Tool:** Claude Code (Claude Opus 4.7)
**Purpose:** Replace hardcoded sector-generic multiples in `valuation.py` with per-company bespoke peer benchmarks persisted to CSV. Triggered by user feedback: "we shouldn't hard-code benchmarks without peer analysis" + "we should specify so that each company gets bespoke benchmarks" + "we can instruct the agents to update the csv whenever they do research so we don't have to re-do it every time."
**Approach:** Designed `data/research/<ticker>/peer_benchmarks.csv` schema (14 columns: peer ticker/name/inclusion tag + 4 multiples + 4 margins/growth + date/source/notes). Each ticker gets its own file. Subject anchor row pre-populated from yfinance. When file missing, script writes the empty template with instructions and exits — code-level enforcement of methodology #3 ("comp-proven, not theoretical"). Added agent instruction to CLAUDE.md so future sessions know to persist peer findings.
**Key Outputs:**
- Removed hardcoded R40 band table (1/2/3.5/5.5/7.5/10x). Replaced with `value_ev_revenue` (peer-derived multiple, R40 reported as diagnostic context).
- Three multiple-resolution sources: peer CSV (target=median, low=min, high=max across primaries) > CLI override > skip. Each method labels its source in output.
- Validation: EXFY with 3 primary peers → blended $5.74 (+397% vs $1.16). AAPL regression: unchanged when CLI overrides match prior defaults.
- New `TODO.md` capturing pending build/research items per the new methodology direction.
**Where AI helped:** Designed a clean three-tier multiple resolution (peer → CLI → skip) that prevents silent defaults while keeping CLI bypass available for one-off runs. Schema includes the subject row as anchor so agents have local reference.
**Where AI may have gaps:** Schema may need additional columns over time (e.g., size adjustment factor, growth-adjusted multiple, NTM vs LTM toggle). Defer until real peer-research workflows surface what's missing.

### Prompt 11: Extend valuation.py with Pre-EBITDA Methods
**Tool:** Claude Code (Claude Opus 4.7)
**Purpose:** Implement the four pre-EBITDA methods from Prompt 10's research into `scripts/valuation.py`.
**Key Outputs:**
- Added `value_ev_fcf`, `value_ev_gp`, `value_rule40`, `value_path_dcf`.
- Method routing via `--methods auto` (positive-EBITDA → ev_ebitda+dcf, pre-EBITDA → ev_fcf+ev_gp+rule40+path_dcf) or explicit `--methods` list.
- Sensitivity matrix now auto-picks EBITDA or FCF mode.
- EXFY validation: 4 methods bracket $2.50-$4.92 → blended $3.86 vs $1.15 current (+236%). Consistent with net-cash position making effective EV/FCF ~2.4x trailing.
- AAPL regression: unchanged outputs from prior version ($173 EV/EBITDA, $110 DCF, $145 blended).
**Where AI helped:** Carefully refactored without breaking the positive-EBITDA path (verified by AAPL regression). Auto-routing kept the CLI ergonomic despite adding 12 new flags.
**Where AI may have gaps:** Path-DCF defaults (15/12/10/8/6% growth, -5/0/5/10/15% margin) are sector-generic; per-company tuning required before pitch defense.

### Prompt 9: Port DCF + Football Field
**Tool:** Claude Code (Claude Opus 4.7)
**Purpose:** Port `valuation_engine.py` (10-yr DCF, EV/EBITDA, peer comp) and `sensitivity_analyzer.py` (2D revenue × margin matrix) into `scripts/valuation.py`. Pure numpy/pandas/matplotlib — no LLM dependency.
**Approach:** Exposed all DCF assumptions as CLI flags (`--growth-near`, `--growth-far`, `--terminal-growth`, `--wacc`, `--fcf-conversion`) rather than hardcoding FinRobot's defaults, so assumptions are visible and iterable. Bear/bull range = ±200bps WACC, ±50bps terminal growth. Confidence-weighted blended target reported.
**Key Outputs:**
- Sanity-tested on AAPL: EV/EBITDA @ 18x → $173 (low $134, high $213), DCF @ 5/3% growth + 8.5% WACC → $110 (low $78, high $186). Blended $145 vs. current $311.46 — i.e. the model says AAPL is expensive on these assumptions, which is the expected directional result.
- Outputs: `dcf_projection.csv`, `sensitivity.csv`, `football_field.png`, `summary.json`.
- Pre-EBITDA companies (e.g. EXFY current TTM) trigger an early-exit warning recommending EV/Sales or SOTP — DCF is uninformative when base FCF is negative.
**Where AI helped:** Surfaced that the framework's many sweet-spot candidates are pre-EBITDA, which forces a methodological choice (multi-method valuation per-candidate vs. one method for all).
**Where AI may have gaps:** Football-field chart is matplotlib-default styling — fine for working artifacts, may want a designer pass before the final deck.

## Session 6: Memo system, candidate expansion, and a numbers audit (2026-05-29)
**Tool:** Claude Code (Claude Opus 4.8, 1M context)

### Prompt: build an investment-memo voice guide from exemplars
**Purpose:** The project had a design system but no *writing* guidance; Aviv cited Buffett's letters as the reference. Dispatched a research subagent over Berkshire letters, Howard Marks memos, and an Einhorn writeup.
**Output:** `docs/memo-voice.md` (8 voice principles with verbatim exemplar sentences, plain-English vocabulary table, inline-sourcing patterns, narrative-arc templates, annotated 1-page skeleton) + `docs/memo-principles.md` (checklist + forbidden moves).
**Where AI helped:** Extracted concrete, imitable patterns rather than generic "write clearly" advice.
**Where AI may have gaps:** Two source PDFs were binary-locked and substituted; noted in the doc.

### Prompt: triage the 21 unevaluated Layer-2 candidates, then build pitch memos
**Approach:** A batch script ran dossier + voting + deal-status on all 21 (16 survived); 8 parallel subagents produced findings on the 16; 10 parallel subagents drafted one-page HTML memos against the template. 11 memos total in `mockups/pitches/`.
**Where AI helped:** Parallel fan-out turned a multi-day sweep into a single session.
**Where AI HURT — important disclosure:** the memo-drafting agents inherited unverified numbers from the findings stage and, in places, fabricated plausible figures. A follow-up audit (below) found at least one wrong load-bearing number in **every** memo.

### Prompt: verify every memo's numbers against filings (the audit)
**Purpose:** After catching a 7x adjusted-EBITDA error in IZEA by hand, ran one verification subagent per memo — GAAP vs XBRL, non-GAAP vs the 10-K reconciliation table, derived figures recomputed.
**Key outputs:** Four repeatable failure modes documented (data-vendor aggregate fields, non-GAAP inherited not sourced, conflation of similar-magnitude figures, period/share-count slips). Thesis-altering corrections on CDLX, MIND, SCOR, IZEA, UONE; RSSS/UPLD/SWAG/AENT survived clean. Lesson encoded in `docs/memo-principles.md`.
**Where AI helped:** The verification pass is the most valuable single step in the session — it caught errors that read as plausible and would have survived a human read-through.
**Where AI may have gaps / lesson:** LLM agents will state a confident specific number that is wrong; treat any agent-produced figure as unverified until checked against the primary filing. yfinance `enterpriseValue`/`marketCap`/`freeCashFlow` are especially unreliable for dual-class/earnout/preferred structures — compute from the balance sheet instead.
