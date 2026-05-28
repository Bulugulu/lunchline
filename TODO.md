# TODO

Working backlog for the Lunchline Partners case study. Newest at top within each section. Resolved items move to CHANGELOG.

For analytical workstreams (per-candidate work after selection), see `docs/methodology.md` § Sequenced Analytical Workstream. This file tracks **build**, **research**, and **decision** items for the project as a whole.

---

## Decisions blocking other work

- [ ] **Company selection** — narrow remaining clean candidates → pick 1 via pitch tournament (see below). Pre-framework leaders (DOMO 4.35, LPSN 4.25, DH 4.00, MCHX 3.70) are stale — LPSN/KPLT are mid-deal, DOMO/BBGI/SKLZ are founder-controlled. Two calibration anchors (EXFY 2.65, SCOR 2.85) both landed below the 3.0 viability threshold under v2 scoring.
- [ ] **FMP API key** — `fetch_fmp.py` works but `/v4/price-target` and competitor-comps endpoints likely require the paid Starter tier ($14/mo). Without it, consensus price target and competitor metrics endpoints will fail. Decide: pay for one month, or skip the sell-side-consensus signal.
- [ ] **Friendly-transaction framework treatment** — DOMO/BBGI are founder-controlled (DEAL_BREAKER per current logic) BUT have active strategic reviews. That's a founder-led-sale setup, conceptually different from hostile-PE-attack. Decide: re-frame PE Realism scoring for this case, or treat as out-of-scope for the Lunchline operator-investor brief.

---

## Pitch Tournament (next major step)

Run the v2 pipeline on a slate of candidates, then have each candidate "pitched" by a dedicated subagent (one concise pitch + supporting data per ticker). I attack each pitch; we iterate until convergence on a single selection.

### Setup

For each candidate to pitch, run pipeline end-to-end:
1. `build_dossier.py TICKER`
2. `check_voting_structure.py TICKER`
3. `check_deal_status.py TICKER`
4. `build_peer_set.py TICKER --add <peer-tickers-from-WebSearch>`
5. Dispatch 6 specialists in parallel via `agent_prompts.build_prompts`
6. Synthesize specialist outputs → adversarial reviewer
7. Aggregator (Claude) judges adversarial critiques + produces final weighted score

### Pitch agent (new — per candidate)

Once pipeline outputs exist, dispatch a **pitch agent** for each ticker. Its job:
- Read all dossier artifacts (scoring outputs, adversarial review, model output, voting/deal status, peer benchmarks)
- Produce a **concise one-page pitch** for Aviv:
  - 1-sentence thesis (variant perception: "Market sees X. We see Y because Z.")
  - 3 thesis pillars with evidence anchors
  - 1 catalyst with a date
  - 3-year IRR with probability-weighted price target
  - 2 kill criteria (specific, monitorable thresholds)
  - The single strongest counter and its rebuttal
- Tone: institutional, dense, no padding — Pershing/Trian voice (per design system Direction 1)

### Tournament round

For each pitch I receive, I attack:
- Where is the thesis weakest?
- Which kill criterion is most likely to trigger?
- Does the adversarial critique kill the pitch, or did the pitch absorb it?
- How does this pitch compare to the others?

Iterate (refine pitch / attack / surface new issues) until one candidate survives with a defensible thesis.

### Candidates to put in the bracket

Confirmed clean structural filters (current state):
- [ ] **CDLX** — Cardlytics, $191M EV, US adtech, recent Bridg divestiture, single-class voting, no deal in progress
- [ ] **NRDY** — Nerdy, $91M EV, US edtech, multi-class but 1:1 voting, no deal in progress
- [ ] **SCOR** — comScore, $219M EV, audience measurement, single-class voting + active strategic review (Goldman retained Aug 2025) ← already scored, would re-pitch under v2

Friendly-transaction candidates (founder-controlled but in active sale process — pending decision above):
- [ ] **DOMO** — BI/analytics, $268M EV, 95.9% founder voting + Feb 2026 formal strategic alternatives
- [ ] **BBGI** — Beasley Broadcast, $289M EV, 92% Class B + strategic alternatives committee + debt refi

Untested 6/7s worth adding to bracket:
- [ ] **BZFD** (BuzzFeed) — media, $140M EV, US
- [ ] **TTGT** (TechTarget) — IT services, $421M EV, US — recent Informa merger 2024 (need to verify status)
- [ ] **AENT** (Alliance Entertainment) — entertainment distribution, $410M EV
- [ ] **ANGI** (Angi Inc) — Internet services, $474M EV
- [ ] **THRY** (Thryv Holdings) — SaaS, $413M EV

### Out of scope for pitch tournament
- Per-candidate full mispricing diagnosis / consensus dossier / operating model — those happen AFTER selection per methodology.md workstream sequence.
- The pitch is a 1-pager, not a deck. Deck build is downstream of selection.

---

## Research items (do before related build)

- [ ] **Operator-investor value creation lever framework.** Before building `value_creation_levers.py`, research the structure of institutional VCP analysis across five lever categories — M&A, capital structure, operations, marketing, **digital operations** (data, experimentation, AI adoption; Aviv's specific edge). Each category needs: standard prompt/checklist, "comp-proven lever" requirement (per methodology #3), and a way to quantify EBITDA/revenue/multiple delta. Output: `docs/value-creation-framework.md` with the framework + 2-3 worked exemplars from Trian / Pershing / Starboard / search-fund canon. Then build the script.

- [ ] **Mispricing diagnosis framework.** The 9-row checklist in `methodology.md` is the structure. Research: what evidence sources prove/disprove each row? (Zero coverage → FactSet count; SPAC overhang → S-1 lock-up dates; sector misclassification → GICS vs. business segments; etc.) Output: a per-row evidence-source map. Then build `scripts/mispricing_diagnosis.py`.

- [ ] **Consensus baseline dossier framework.** Decide which sell-side data source is realistic without paid feeds (Visible Alpha, FactSet are paid; can scrape sell-side reports from SeekingAlpha or use FMP analyst-estimates endpoint if available on free tier). Output: a dossier template covering Street numbers + peer multiples + retail narrative + earnings Q&A themes.

---

## Build items (ready to start)

### Tooling — generic across companies

- [ ] **C: `scripts/triangulate.py`** — IR-vs-SEC triangulation prompt generator. Methodology calls this the highest-leverage AI use case. Takes a ticker, pulls last 4 earnings call transcripts + most recent 10-K, generates a prompt asking Claude to find specific claim-vs-filing gaps ("management says 'diversified customer base'; 10-K says top 3 customers = 65% of revenue"). Open question: where do we get transcripts? (Options: Seeking Alpha scraping, FMP transcripts endpoint, manual paste.)

- [ ] **B: `scripts/value_creation_levers.py`** — generic operator-investor VCP scaffold across the 5 lever categories. **Blocked by research item** above (need framework first).

- [ ] **A: `scripts/mispricing_diagnosis.py`** — runs the 9-row checklist from methodology.md, pulls evidence per row from existing data sources. **Blocked by research item** above.

- [ ] **D: `scripts/consensus_dossier.py`** — aggregates Street estimates + peer multiples + retail narrative + earnings Q&A themes. **Blocked by research item** above.

### Tooling — improvements to existing scripts

- [x] **E (DONE in this session): Per-company peer benchmark CSV for `valuation.py`.** Removes hardcoded multiple bands. Each ticker has its own `data/research/<ticker>/peer_benchmarks.csv`. Script reads from CSV, computes median/min/max per metric. When CSV is missing or empty, prints research instructions + writes an empty schema template. Agents update the CSV during peer research so we never re-do it.

- [ ] **`analyze_10k.py` enhancement** — make the section extractor handle older (pre-2020) 10-K layouts. Current heuristic is tuned for recent iXBRL filings.

- [ ] **`fetch_fmp.py` graceful free-tier handling** — currently errors when an endpoint requires Starter plan. Add a "tier probe" that reports which endpoints work on the current key.

### Tooling — new

- [ ] **`scripts/comp_transitions_library.py`** — supports methodology #3 (comp-proven levers). Given a proposed lever, search for 3-5 peers who executed it with date / outcome / source. Probably LLM-driven with web search.

- [ ] **`scripts/thesis_monitor.py`** — supports methodology #5 (kill criteria). Generates a thesis-monitor sheet template (metric / threshold / source / next data point) from a 1-paragraph thesis input.

- [ ] **`scripts/compression_test.py`** — supports methodology compression discipline. Takes a draft thesis paragraph, checks it against the five required elements (own / variant perception / catalyst / IRR-MOIC / kill criterion), flags missing ones.

### Deck pipeline

- [ ] **HTML → python-pptx export** — wire mockups/ Direction 1 HTML to a python-pptx renderer that consumes the operating model as source of truth.

---

## Methodology-adjacent open questions

- [ ] **Operating model** — where does it live? `models/<ticker>.xlsx`? Markdown alternative for version control? Need a decision before workstream #3 starts.
- [ ] **Primary research workflow** — methodology #4 says 5-10 calls. Need a system to track outreach + notes per call (Notion? simple `data/primary/<ticker>/calls.md`?).
- [ ] **Peer benchmark refresh policy** — peer_benchmarks.csv files will go stale. Decide: refresh on every run? Manual re-research on a cadence? Mark stale after N days?

---

## How agents should use this file

When you start a session:
1. Read `MEMORY.md` and project memory (auto-loaded).
2. Read this `TODO.md` to see open items.
3. If you complete a build or research item during the session, move it to `CHANGELOG.md` and remove from here.
4. If you discover a new item (research gap, missing tool, decision needed), add it to the appropriate section.
5. **Per-candidate work** (mispricing diagnosis, consensus dossier, operating model for a specific ticker) does not go in this file — see methodology.md workstream sequence and the candidate's own `data/research/<ticker>/` directory.
