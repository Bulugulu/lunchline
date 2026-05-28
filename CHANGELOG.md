# Changelog

All notable changes to the Lunchline Partners case study project.

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
