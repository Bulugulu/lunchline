# Changelog

All notable changes to the Lunchline Partners case study project.

## 2026-05-28 (late late) — Pipeline restructure + framework diagnostic + 3 new candidates

### Calibration runs on CDLX + NRDY
Ran full v2 pipeline (6 specialists + adversarial + model) on both. Both landed in the same 2.85-2.95 post-adversarial band as EXFY (2.65) and SCOR (2.85). Notable specialist findings:
- **CDLX (2.85):** Messiness 5.0 (BofA exit, Bridg divestiture, CEO/CFO turnover, $49M goodwill impairment on core platform). Adversarial caught Value Creation specialist's ACPU math error (cited $0.50→$0.65; actual Q1 2026 is $0.10 — 5x off due to deprecated MAU denominator). IR-vs-SEC found BofA non-renewal known April 22, 2025 but undisclosed on calls until Q4. Lender LOOSENED minimum cash covenant $25M → $20M in Q1 2026 (covenant relief signal). Model: blended $1.36 vs $0.74, +22.6% IRR (right at hurdle).
- **NRDY (2.95):** CEO Cohn purchased ~1.81M shares Dec 3-16, 2025 at $1.20-$1.35 (11 sequential Form 4s). +1,500bps margin expansion, -22% headcount, V3 AI platform shipped March 2026. Adversarial caught the CHGG bear inversion: specialist cited CHGG as positive precedent, but CHGG ran the SAME AI cost reset while revenue collapsed -48% — that's the bear case, not the bull. True runway ~15 months under Hercules covenants, not 2-3 years. Cohn's $2.3M open-market purchase is 3% of his ~$77M paper stake (optics, not conviction). Model: $1.56 vs $0.84, ~+20% IRR.

### Framework discrimination diagnostic (FAST as control)
Pattern observation: every candidate in our screened pool scored 2.65-2.95 post-adversarial. Possible interpretations: (a) framework is broken, (b) pool is genuinely homogeneous, (c) something else. Ran FAST (Fastenal) through the full pipeline as a control — clean profitable compounder, categorical opposite of Lunchline's mandate.

Result: **the framework discriminates strongly across archetypes; our pool is just self-similar.** FAST per-criterion fingerprint was nearly INVERSE to the messy pool: Messiness 3.0 vs 4.5-5.0; Value Creation 1.5 vs 3.5; Data 5.0 vs 4.5; Contrarianism 1.0 vs 3.5; IR-SEC 4.0 vs 2.5-2.8; PE Realism 1.0 vs 2.0. FAST weighted pre-adversarial: 2.58. The framework correctly placed FAST below every messy candidate without ever seeing CDLX/NRDY/SCOR.

Per-criterion range across the FAST + messy comparison: 1.5-2.5 points. Strong discrimination capability. The 0.30-point within-pool spread was correct — pool homogeneity, not framework failure.

### Findings-mode pipeline (lighter, sharper)
Built `build_findings_prompts(ticker)` in `scripts/agent_prompts.py` — 3 specialists (Lever Ideation, Mispricing Diagnosis, IR-vs-SEC) + findings-mode adversarial. Each specialist outputs 5 bull + 5 bear findings with filing anchors, NO 1-5 score. Adversarial outputs 3 most material attacks + kill criteria, NO weighted score. Compute is ~50% of calibration mode.

Why drop the criteria we dropped:
- **Messiness scoring:** every screened candidate scores 4.5-5.0. Constant.
- **Data Availability scoring:** every public candidate with full SEC filings scores 4.5-5.0. Constant.
- **PE Realism scoring:** every small-cap messy name scores ~2.0 (LBO math fails). Constant.
- **Weighted aggregation:** compresses to 2.7 ± 0.15 regardless of inputs.

Why keep what we kept:
- **Lever Ideation, Mispricing Diagnosis, IR-vs-SEC** generate the specific, anchored, named findings that actually feed pitch construction.
- **Adversarial** is the most cost-effective layer (per dollar of compute, produces the most pitch-shaping insight — BZFD board capture, THRY ABL collision, CDLX ACPU error, all came from adversarials).

### Three new candidates scored under findings-mode: THRY, BZFD, AENT
- **THRY (unpitchable):** SEC Division of Enforcement investigation into "Company's previously publicly announced strategic conversion of clients from Digital marketing services solutions platform to its SaaS solutions platform" disclosed in 10-K Item 1A — NEVER mentioned on any of the last 4 earnings calls. Same mechanic mgmt sells on every call. Plus: Seasoned NRR 96%→98%→94%→93% (sub-100% is not a compounder), $253.8M SaaS goodwill being interim-impairment-tested, ABL maturity May 2028 collides with print publication end (Lever #1 + Lever #5 collapse simultaneously). Marketing Center platform "being replaced very soon" — the 30% growth asset bull thesis hangs on is being torn out.
- **BZFD (unpitchable):** Allen Family Digital closed $120M PIPE May 26, 2026 (TWO DAYS before case due) taking 51% voting + 6 of 9 board seats for $20M real cash ($100M is 5-year PIK note secured only by BZFD shares Allen just bought — circular collateral). Operator-investor thesis structurally evaporated. "BF Island AI-native platform" anchored 4 straight quarters of calls — appears ZERO times in 10-K. Going-concern language, Nasdaq sub-$1 noncompliance, four 8-K amendments to extend a single $5M payment. Q4 2025 and Q1 2026 earnings calls took no Q&A.
- **AENT (pitchable but bounded):** Paramount (Jan 2025) + MGM (Jan 2026) exclusive licensing real (movie rev +37%, ASP +18.8%, GM +170bps); Handmade by Robots collectibles roll-up working. BUT: adj EBITDA +47% vs OCF -55% (inventory absorbed $24M to support studio model); sector-reclassification variant fails op-margin test (AENT 1.4% op margin → CORE/AVT/ARW commoditized band 0.11-0.38x, not FAST/GWW/MSM value-add band 0.5-1.2x). Walker/Ogilvie founder control 75% eliminates activist catalyst. Bounded 30-50% upside on Class E dilution self-cancellation + clean-audit anniversary, NOT 2-3x.

### Final viable candidate slate
Four real survivors for pitch tournament: **CDLX, NRDY, SCOR, AENT**. Each has a distinct adversarial fingerprint — pick on story, not on score.

### Bug fix: deal_status acquirer/target weighting
Fixed false positive that nearly dropped THRY for the wrong reason. THRY's Oct 2024 acquisition of Keap triggered a "definitive merger agreement" hit; the script now suppresses target-side flags when every definitive_hit comes from a file that also contains an acquirer_signal. Regression-safe (LPSN still correctly flagged CLOSED).

### Selection framework restructure (removed Layer 3)
Updated `docs/public-company-pitch.md` § 2 to replace the 6-criterion weighted scoring framework with an explicit 2-layer filter + fundamental analysis on every survivor. No Layer 3 ranking by sector / EV size / signal density — each of those was either (a) institutional bias the brief explicitly rejects (size floor for "credibility" contradicts the $10-500M EV mandate), (b) anti-correlated with the under-followed goal (high signal density = visible catalyst = other analysts saw it), or (c) better applied at the END as a tiebreaker (sector fit / Aviv's edge zones). The framework now mirrors the actual selection logic we converged on.

Also reframed § 4 "Sector Filters" as **universe-scope** decision (which sectors Finviz pulls from), explicitly NOT a candidate-level filter. Aviv's edge fit moved to post-findings tiebreaker.

### Files modified
- `scripts/agent_prompts.py`: added `build_findings_prompts`, `lever_findings_prompt`, `mispricing_findings_prompt`, `findings_adversarial_prompt`
- `scripts/check_deal_status.py`: acquirer/target weighting fix
- `docs/pipeline.md`: documented two modes + diagnostic narrative
- `docs/public-company-pitch.md`: Layer 3 removed; Sector Filters reframed as universe scope; Selection Criteria Summary rewritten as ordered process
- `TODO.md`: synced candidate landscape + funnel state (42 → 11 mechanical out → 10 evaluated → 21 to evaluate)

---

## 2026-05-28 (late night) — Multi-Agent Scoring Pipeline v2

### Per-Company Dossier System
Built end-to-end dossier builder (`scripts/build_dossier.py`) that produces a full research package in ~25 seconds per ticker. Pulls and consolidates:

- **EDGAR filings** (extended `fetch_edgar.py`) — 10-K, 10-Q, 8-K, DEF 14A, Form 4 with content download (not just metadata). Per-form download caps so 30 Form 4s don't blow up disk.
- **Earnings call transcripts** (`fetch_transcripts.py`) — scrapes roic.ai for last 4-8 quarters. Heuristic to skip nav/listing text and keep transcript body only.
- **News headlines** (`fetch_news.py`) — yfinance `.news` attribute, 10 recent items normalized to a consistent schema.
- **Analyst data** (`fetch_analyst.py`) — recommendations rolling, upgrade/downgrade history (48-event depth on EXFY), price target distribution, earnings/revenue estimates.
- **Seeking Alpha coverage** (`fetch_seeking_alpha.py`) — DuckDuckGo `site:seekingalpha.com TICKER` search to count articles for the "obviousness" check. Flaky but useful as a soft signal.
- **yfinance snapshot** (166 fields) + human-readable `summary.md` for quick scan.

Output structure: `data/dossiers/<ticker>/` with `summary.md`, `edgar/`, `transcripts/`, `news.json`, `analyst.json`, `seeking_alpha.json`, `yfinance_info.json`.

### Voting Structure Check (`scripts/check_voting_structure.py`)
Surfaces dual/triple-class share structures, voting trusts, and controlled-company status from DEF 14A + 10-K cap stock notes BEFORE deep scoring. Risk classifications: LOW / MEDIUM / HIGH / DEAL_BREAKER.

Discovered an extremely common pattern in our 7/7 candidate pool — **founder-controlled super-voting structures**:
- EXFY: 84.7% Voting Trust with 50/10-vote LT shares
- DOMO: 95.9% via 40-vote Class A
- SKLZ: 87.0% via 20-vote Class B
- BBGI: 92.0% via 10-vote Class B (spelled "ten" in proxy)

NRDY correctly downgraded to LOW after detecting multi-class but 1:1 voting (capital structure complexity only; no take-private blocker).

Pipeline cleanliness pass caught: NBSP-duplicate class names, missing word-number vote ratios ("ten votes per share"), misleading reasoning strings.

### Deal-In-Progress Filter (`scripts/check_deal_status.py`)
Detects merger/acquisition/strategic-review status. Classifies as NONE / EXPLORING / TENDER_OFFER / DEFINITIVE / CLOSED. Critical to filter BEFORE expensive scoring — caught:
- **LPSN** = CLOSED (SoundHound all-stock deal Apr 2026)
- **KPLT** = CLOSED (Aaron's + CCF merger agreement Dec 2025)
- **SCOR, DOMO, BBGI, SKLZ** = EXPLORING (active strategic alternatives processes)
- **EXFY** = TENDER_OFFER (Dutch auction — company self-buyback, OK)
- **CDLX, NRDY** = NONE

Pipeline cleanliness pass added: debt-tender exclusion (BBGI 2027 PIK Notes was false TENDER_OFFER), asset-sale negator (SCOR Movies divestiture was false DEFINITIVE), transcript scanning for "evaluating strategic alternatives" (SKLZ's Q1 call wasn't in 8-Ks).

### Peer Set Builder (`scripts/build_peer_set.py`)
Identifies real-world peers via (a) 10-K Item 1 Competition parse, (b) DDG web search, (c) yfinance enrichment, (d) manual `--add TICKERS` augmentation for WebSearch-sourced peers (the canonical workflow).

Dual-writes both `data/dossiers/<ticker>/peers/peer_table.json` (light schema) AND `data/research/<ticker>/peer_benchmarks.csv` (the format `valuation.py` reads, with subject anchor row + primary/secondary/excluded inclusion tags).

Cleanliness pass: industry sanity check (POWL = Powell Industries was accidentally added to NRDY's edtech peers — now auto-skipped with reason), delisted-ticker handling (SUMO was taken private 2023, returns no yfinance data — now gracefully skipped), `--force` flag to override when intentional.

### Industry-Aware Agent Prompts (`scripts/agent_prompts.py` + `industry_kpis.json`)
Configurable per-criterion prompts that auto-inject the candidate's industry KPIs (SaaS: NRR / Rule of 40 / CAC payback; adtech: take rate / RPM; gaming: DAU/MAU / ARPDAU; etc.), the peer table, voting structure findings, and private-peers notes.

`build_prompts(ticker)` returns 8 ready-to-dispatch prompts:
- **6 specialists in parallel**: Messiness, Value Creation, Data Availability, Contrarianism (with mispricing-diagnosis 9-row checklist), PE Realism, IR-vs-SEC Triangulation (the highest-leverage AI task per methodology)
- **Adversarial reviewer** (sees all 6, attacks with real investment logic using 9 named frames)
- **Model agent** (invokes `scripts/valuation.py` 7-method engine — no more reinventing back-of-envelope models)

Methodology v2 disciplines baked into prompts:
- Value Creation now REQUIRES 2-3 comp-proven transitions per lever (lesson #3)
- Contrarianism requires the 9-row mispricing diagnosis (lesson #6 — score capped at 2 if zero rule-ins)
- IR-vs-SEC triangulation as 6th specialist (Structural Discipline)
- Model agent outputs explicit kill criteria with dated thresholds (lesson #5)

### Calibration Runs

**EXFY** (calibration anchor 1):
- v1 specialists: 3.35/5 rescaled
- After adversarial: **2.65/5** — adversarial caught the 83.6% Voting Trust standstill ban, capitalized software inflating "FCF," $14M F1 movie sponsorship signal, migration thesis stalling

**SCOR** (calibration anchor 2):
- v1 specialists: 3.65/5 rescaled — initially looked stronger than EXFY
- After adversarial: **2.85/5** — adversarial caught $22.4M capitalized internal-use software (kills the "20% cash yield" math), Stockholders Agreement explicitly bans Cerberus from publicly soliciting take-private, Q1 2026 Blue Torch covenant waiver, cross-platform Q4 growth decelerated to ~10%, Q4 2025 net income $103.9M was non-cash extinguishment gain

Both anchors landed below the framework's 3.0 minimum viability threshold. Lightweight model on SCOR: expected IRR 25-30% at face but only ~17% when probability-reweighted to the post-adversarial score — qualitative and quantitative views are in tension.

### Structural Filter Sweep on 5 Untested Candidates
Built dossier + ran voting + deal status on DOMO, SKLZ, CDLX, BBGI, NRDY:
- **CDLX** — LOW voting (single class), LOW deal status — clean
- **NRDY** — LOW (multi-class but 1:1 voting), LOW — clean
- **DOMO, SKLZ, BBGI** — all DEAL_BREAKER on voting (founder-controlled super-voting Class A/B)

Surfaced conceptual gap: founder-controlled-with-active-strategic-review (DOMO, BBGI) is a *friendly transaction* setup, not a hostile-PE-attack setup. Current framework conservatively flags as deal-breaker; this is a known scoring limitation worth revisiting.

### Files Added / Modified
New: `scripts/build_dossier.py`, `fetch_transcripts.py`, `fetch_news.py`, `fetch_analyst.py`, `fetch_seeking_alpha.py`, `check_voting_structure.py`, `check_deal_status.py`, `build_peer_set.py`, `agent_prompts.py`, `industry_kpis.json`, `score_all_candidates.py`, `filter_and_rescore.py`, `model_scor.py`.

Modified: `fetch_edgar.py` (multi-filing-type support + content download).

### Next Steps
- Run pitch tournament on remaining clean candidates (see TODO.md "Pitch Tournament" section)
- Decide framework treatment of friendly-transaction setups (founder-led strategic review)

---

## 2026-05-28 (evening) — Deck Structure, Design System, Methodology

### Deck Format Decision
- **Authoring pipeline:** HTML + CSS for drafting (fast iteration, version-controlled), python-pptx for final `.pptx` export (Lunchline brief requires PowerPoint), PDF as backup deliverable.
- **Rationale:** HTML lets us iterate visually with real text reflow; python-pptx makes the Excel returns model the source of truth for slide numbers ("render model to deck," not "type numbers into PowerPoint").

### Deck Structure Research (two parallel subagents)
- **Content/structure agent:** Researched best-in-class equity investment pitch decks across activist, MBA stock-pitch competition, and search-fund canon. Per-section world-class patterns, anti-patterns, and exemplars for all 7 slide sections.
- **Design system agent:** Researched typography, color, layout conventions across institutional pitches. Returned 3 candidate directions with concrete specs.
- Top exemplar references: Trian "Restore the Magic" Disney white paper, Pershing Square Challenge 2019 Hertz winner, Pershing Square 2025 Annual Presentation, Starboard Value deck library, Stanford GSB Search Fund Primer, IESE "First 100 Days."
- Captured in `docs/deck-structure.md` with cross-cutting principles (takeaway headlines not topic labels, variant perception structure, operator framing, institutional density).

### Design System — LOCKED to Direction 1 (Institutional Classic)
- Built HTML mockups in `mockups/` (index.html + d1/d2/d3.html) served via `python -m http.server 8765`.
- Five sample slides for Direction 1: Cover, Business Overview (KPI dashboard), Investment Thesis, Investment Risks (multi-column table), Value Creation Plan (value bridge + lever cards).
- Aviv picked **Direction 1** after preview. Spec: Inter typography (one family, 3 weights), navy `#0A2540` + ink + slate, red `#C8102E` accent for thesis emphasis only, dense 12-col grid matching Pershing/Trian institutional canon.

### Analytical Methodology (new doc: `docs/methodology.md`)
Distilled six lessons from the exemplar decks that change how we work:
1. **Operating model first, deck second** — every slide number reconciles to the Excel model
2. **Consensus baseline before variant perception** — quantify what consensus says before disagreeing
3. **Comp-proven levers** — every VCP lever cites a peer that already executed
4. **Primary research is the actual differentiator** — 5-10 expert/customer/ex-employee calls, the one thing AI can't fake
5. **Kill criteria as part of the thesis** — specific, dated, monitorable thresholds
6. **Diagnose WHY mispricing persists** — structural reason is part of the variant perception

Plus two disciplines: IR-vs-SEC triangulation (highest-leverage AI use case) and 1-paragraph compression test before deck draft.

### Sequenced Analytical Workstream
Replaced ad-hoc "next steps" with structured sequence in `public-company-pitch.md` deliverables:
1. Mispricing diagnosis (1-2 days)
2. Consensus baseline dossier (1 day)
3. Operating model v0 (3-5 days) — critical path
4. Comparable transitions library (2-3 days)
5. Primary research outreach (1-2 wks, parallel from week 1)
6. IR-vs-SEC triangulation (0.5 day)
7. Thesis synthesis + 1-para compression test (1 day)
8. Deck draft, HTML → pptx (2-3 days)

Total elapsed with parallelism: ~2.5–3 weeks from company selection to draft.

### Doc Updates
- `CLAUDE.md` router updated with new entries for methodology.md and deck-structure.md.
- `public-company-pitch.md` deliverables checklist restructured: Analytical Workstreams (pre-deck) + Final Deck Artifacts (post-deck).

### Next Steps
- **Still blocking everything:** company selection. Narrow 45 ultra-sweet-spot → top 5-8 via full 6-criterion scoring + obviousness check + 8-K event search.
- After selection: kick off mispricing diagnosis + consensus dossier in parallel.

---

## 2026-05-28 (later)

### FinRobot Method Borrow — Analyzer, FMP, Valuation
Reviewed the FinRobot repo (https://github.com/AI4Finance-Foundation/FinRobot) and decided against installing the framework — AutoGen orchestration, OpenAI API cost, and originality risk make it net-negative for a buyside case study. Instead ported three high-leverage methods into our pipeline:

- **`scripts/analyze_10k.py`** — generates seven ready-to-paste 10-K analysis prompts (income, balance sheet, cash flow, segment, business highlights, company description, risk). Each pairs a financial table (yfinance) with the matching 10-K section (local EDGAR HTML) and a tightly-scoped instruction ported from FinRobot's `analyzer.py`. Includes a BS4 + regex section extractor with TOC-discrimination heuristic. Verified on EXFY's 2026 10-K — all three Items (1, 1A, 7) start at the real section heading.
- **`scripts/fetch_fmp.py`** — Financial Modeling Prep wrapper for analyst price targets (consensus min/max/median), historical market cap, BVPS, single-company financial metrics, and competitor comps. Fixed a Revenue Growth bug in the original FinRobot code (off-by-one when `year_offset==0` wraps to oldest year). Requires `FMP_API_KEY` env var.
- **`scripts/valuation.py`** — three-method valuation (EV/EBITDA, peer comp, 10-yr DCF with two-phase growth + perpetuity terminal) with football-field chart and 2D sensitivity matrix (revenue × margin). Pure numpy/pandas/matplotlib — no LLM. All DCF assumptions exposed as CLI flags. Sanity-checked on AAPL.

Updated `requirements.txt`: added `beautifulsoup4`, `numpy`, `matplotlib`. Updated `docs/prompt-log.md` with sessions 6-9 (FinRobot synthesis + the three ports).

### Pre-EBITDA Valuation Methods
Researched institutional standard practice for valuing companies with negative TTM EBITDA (common in our sweet-spot pool — broken-SaaS, fallen-angel growth tech). Key finding: the cleanest triangulation is EV/FCF + Rule of 40-anchored EV/Revenue + Path-to-Profitability DCF, with Damodaran-style survival-probability haircut. Meritech's standard is EV/Gross Profit, not EV/Revenue. SBC fault line: value/PE camp (Lunchline's lens) treats SBC as a cash cost; growth-equity camp adds it back. Sources: Damodaran (NYU Stern), Morningstar methodology PDF, Bessemer Cloud Index, Meritech benchmarking.

Extended `scripts/valuation.py` with four additional methods (now seven total):
- **EV/FCF** — primary for pre-EBITDA-but-FCF-positive names; bypasses SBC debate. Confidence 0.60.
- **EV/Gross Profit** — Meritech's preferred SaaS metric. Vertical SaaS ~11x GP, horizontal ~5x.
- **Rule of 40 → EV/Rev band** — computes growth + FCF margin, applies band-based EV/Rev multiple (Bessemer/Meritech calibration). Defaults: bands at 0/20/40/60/80% → 1.0/2.0/3.5/5.5/7.5/10.0x EV/Rev.
- **Path-to-Profitability DCF** — 5-year explicit forecast with revenue growth path + EBITDA margin path (negative→positive crossover), terminal at year 5 via EV/EBITDA multiple, equity value haircut by P(survive). Confidence 0.40.

Method routing: `--methods auto` picks `ev_ebitda+dcf` for positive-EBITDA names (unchanged) and `ev_fcf+ev_gp+rule40+path_dcf` for pre-EBITDA. All assumptions exposed as CLI flags. Sensitivity matrix now picks EBITDA or FCF mode based on EBITDA sign.

EXFY test: blended target $3.86 vs current $1.15 (+236%). All four methods bracket $2.50-$4.92, consistent with EXFY's net-cash position making effective EV/FCF ~2.4x trailing — the deep-value broken-SaaS story.

### Open items
- FMP /v4 price-target endpoint likely requires the paid Starter plan; need to either get an API key or skip the consensus signal.
- Path-to-Profitability DCF defaults (15/12/10/8/6% revenue growth, -5/0/5/10/15% margin path) are sector-generic — should be tuned per-company before defending in the pitch.
- Per-sector EV/GP and EV/FCF multiple defaults are calibrated for SaaS; broadcasters, ad tech, and gaming may need different bands.

### Per-Company Peer Benchmarks (replaces hardcoded multiples)
Removed all hardcoded multiple defaults from `valuation.py`. Multiples now come from one of three sources, with explicit labeling in the output:
1. **Peer benchmarks CSV** at `data/research/<ticker>/peer_benchmarks.csv` — read by `load_peer_benchmarks`, target/low/high computed as median/min/max across `primary` peers (with `secondary` fallback if <3 primaries).
2. **CLI override** (`--target-multiple X`, `--fcf-target-multiple Y`, etc.) — for one-off use without the CSV.
3. **None** → method skips with a clear message.

When `valuation.py` runs on a ticker with no peer file AND no CLI override, it writes an empty schema template (with the subject's own multiples pre-populated as the anchor row) and prints detailed research instructions to the agent. This is the "comp-proven not theoretical" discipline from `docs/methodology.md` #3 enforced in code.

Replaced `value_rule40` band-lookup method with `value_ev_revenue` (peer-derived multiple) + `compute_rule40` (diagnostic-only). The Rule of 40 score is reported alongside the EV/Rev valuation as context, not used to pick a multiple from a hardcoded table.

`path_dcf` terminal y5 multiple also auto-resolves from peer EV/EBITDA when the CSV has data; falls back to CLI flag.

Added agent instruction to `CLAUDE.md`: when researching peers during a session, persist findings to the per-company CSV so future sessions don't re-do the work.

Created `TODO.md` capturing build/research/decision items including: operator-investor value creation lever framework (needs research first), IR-vs-SEC triangulation tool, consensus dossier tool, mispricing diagnosis tool, and the per-company peer CSV refactor (done in this session).

EXFY validation: with 3 hypothetical primary peers (BILL, DOCN, AMPL) → blended target $5.74 vs $1.16 current (+397%). AAPL regression: identical outputs to pre-refactor when CLI overrides match prior defaults ($173 EV/EBITDA, $110 DCF, $145 blended).

---

## 2026-05-28

### Framework Validation — Sanity Checks
- Sanity-checked two ultra-sweet-spot candidates against the framework:
  - **GDEV Inc.** (Electronic Gaming): 6/7 framework checks passed. EV $162M, EV/Rev 0.40x, 15% operating margin, $113M cash, 1 analyst, 2.2% institutional ownership, -64% from 52wk high. Strong gaming sector fit.
  - **Expensify (EXFY)**: 7/7 framework checks passed. EV $50M, EV/Rev 0.36x, FCF positive ($18M), 2 analysts, 36% institutional ownership, -56% from 52wk high.
- Framework is producing legitimate candidates with real messiness/mispricing signals.

### Next Steps
- Narrow from 45 ultra-sweet-spot candidates to top 5-8 for scoring against full 6-criterion framework.
- Add a "fix obviousness check" — Google/Seeking Alpha article counts to validate under-followed status.
- Add 8-K event search via EDGAR full-text search for messiness signals (strategic alternatives, management transitions, restatements).
- Begin Part 2 (Market Mapping) end-market selection in parallel.

---

## 2026-05-26 to 2026-05-27

### Project Setup
- Initialized git repo and pushed to GitHub: https://github.com/Bulugulu/lunchline (private).
- Built router-architecture `CLAUDE.md` pointing to domain-specific docs.
- Created `docs/` directory with: case-overview, public-company-pitch, market-mapping, screening-research, background-context, prompt-log.
- Saved project memory entry for cross-conversation continuity.

### Background Research
- Pulled Aviv's professional background from Life_Admin repo. Established sector edge zones (gaming, AI/ML, SaaS, consumer software, data analytics, enterprise sales) and weak zones (finance, healthcare, industrial).

### Selection Framework
- Built comprehensive framework for interpreting Lunchline's criteria ("messy, mispriced, under-followed; avoid obvious names"):
  - 10 messiness archetypes ranked by analytical richness
  - 8 mispricing signal patterns specific to $10M-$500M EV range
  - Quantitative under-followed thresholds (0-3 analysts, <40% institutional ownership, <$500K daily volume)
  - "Obviousness" test for micro/nano-cap
- 6-criterion weighted scoring system (Value Creation 25%, Situation Complexity 20%, Sector Fit 15%, Data 15%, Contrarianism 15%, PE Realism 10%).
- Quantitative screening filters (hard + soft requirements).

### Data Pipeline
- `scripts/screen_companies.py` — pulls real-time EV, market cap, margins, FCF via yfinance.
- `scripts/fetch_edgar.py` — fetches SEC filing metadata and XBRL structured financials.
- `scripts/framework_screen.py` — systematic three-step screener:
  1. Universe pull from Finviz (Tech + Comm Services, nano-to-small cap, NYSE/Nasdaq)
  2. Enrichment with yfinance for EV and key metrics
  3. Framework filter application + messiness/mispricing signal counts
  - Includes `--sanity TICKER` mode for individual company validation against framework checks
- `.gitignore` configured to exclude raw data files (reproducible via scripts).
- `requirements.txt` for yfinance, pandas, requests.

### Screening Results (Run on 2026-05-27)
- **Raw universe:** 622 companies (Tech + Comm Services, nano-to-small cap)
- **After EV $10M-$500M filter:** 292 companies
- **After min revenue $10M filter:** 227 companies
- **After excluding hardware/semis/solar:** 171 qualifying companies
- **Messiness signal counts:**
  - 111 with EV/Revenue < 1.5x
  - 78 under-followed (0-3 analysts)
  - 115 down >40% from 52-week high
- **Sweet spot (EV/Rev < 1.5x AND under-followed):** 83 companies
- **Ultra sweet spot ($30-250M EV + sweet spot):** 45 companies

### Cleanup
- Removed pre-framework candidate list (DH, MCHX, MNDO, DOMO, EGAN, etc.) — those were derived from web research before the framework existed.
- Reset screening_research.md to describe the systematic process.

---

## Process Notes

- All AI prompts and outputs are logged in `docs/prompt-log.md` for the required AI disclosure appendix.
- Subagents are used for research, framework development, and objectivity-requiring tasks.
- Data files in `data/` are excluded from git (reproducible via scripts).
