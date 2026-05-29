# TODO

Working backlog for the Lunchline Partners case study. Newest at top within each section. Resolved items move to CHANGELOG.

**Process (current):** all-sector screen → neutral prioritization → **the Deep Flow** is the only verdict-producing step. See `CLAUDE.md` Working Conventions and `docs/methodology.md` § The Deep Flow. The legacy 2-sector funnel, the findings-mode / 6-criterion scoring pipeline, and the "pitch tournament / pitch agent" flow are **retired** (history in CHANGELOG, 2026-05-29).

---

## Decisions blocking other work

- [ ] **Company selection — IN PROGRESS (all-sector, non-SaaS, deep-flow only).** Direction: **AVOID SaaS** (small SaaS needs a proprietary-data or regulated-niche moat — `feedback_saas_moat_filter`); sector is an end-stage tiebreaker, not a universe filter (`feedback_sector_not_universe_filter`).
  - **Live candidate set:** USNA, SWAG, AENT, MIND, HCKT.
  - **Deep-flow status:** only **USNA** has a completed (v2, reviewer-iterated) model → `data/research/usna/model.md`. Verdict: modest, catalyst-gated deep-value asset play (SOTP base +34%, ~+9% prob-weighted IRR, floor ~−28%); data floor reached (Hiya unit economics undisclosed). On the list, not an obvious finalist.
  - **Next:** run the Deep Flow on SWAG, AENT, MIND, HCKT for comparable DCF/IRR → pick the finalist on equal footing. Separately re-examine any prior shallow-kill carrying the 3 escalation flags (recent acquisition / net-cash-heavy / control-holder) — the shallow verdict is retired and unreliable.
  - **Demoted (SaaS / software-adjacent), pending deep-flow or drop:** RSSS, CDLX, SCOR. **Shallow-eliminated (revisit only if flagged):** IZEA, ACCS, NRDY, UPLD, MTRX.

- [ ] **FMP API key** — `fetch_fmp.py` works but `/v4/price-target` + competitor-comps endpoints likely need the paid Starter tier ($14/mo). Decide: pay one month, or skip the sell-side-consensus signal. (Consensus baseline is part of the Deep Flow.)

- [ ] **Friendly-transaction framework (deferred)** — founder-controlled names with active strategic reviews (a founder-led-sale setup) read as DEAL_BREAKER under the standard hostile-attack voting logic. Revisit only if the candidate field thins.

---

## Selection process & state (current)

Process: `python scripts/framework_screen.py --all-sectors` generates suspects → neutral prioritization (cheap / under-followed / the 3 escalation flags) → **the Deep Flow** (`methodology.md § The Deep Flow`) is the only verdict step. Selection criteria in `docs/public-company-pitch.md` § Selection Process.

- **Universe:** all sectors, US-listed, EV $10–500M. `data/universe_raw_allsector_full.csv` (2,912) → 1,539 operating (ex financials/funds/SPACs/pre-rev-biotech) → 512 EV-fit → **445 non-SaaS**, of which **57** are cheap+profitable+under-followed (`data/framework_filtered.csv`).
- **Unexamined:** ~51 of the 57 non-SaaS names not yet deep-flowed. Prioritize any carrying the 3 escalation flags.
- **2-sector legacy data** preserved at `data/*_2sector.csv` — do NOT use for new work (it encoded the sector-filter bug).

---

## Research / build backlog (open items)

- [ ] **`scripts/consensus_dossier.py`** — Street estimates + peer multiples + retail narrative + earnings Q&A themes. Part of the Deep Flow's consensus baseline; currently done ad hoc by the deep agent.
- [ ] **`scripts/thesis_monitor.py`** — kill-criteria sheet generator (metric / threshold / source / next data point) from a thesis paragraph.
- [ ] **`scripts/compression_test.py`** — checks a draft thesis paragraph for the five required elements (own view / variant perception / catalyst / IRR-MOIC / kill criterion).
- [ ] **`analyze_10k.py`** — handle older (pre-2020) 10-K layouts.
- [ ] **`fetch_fmp.py` tier probe** — report which endpoints work on the free key instead of erroring.
- [ ] **Deck pipeline: HTML → python-pptx** — render the (markdown) operating model + Direction-1 HTML to PowerPoint. Downstream of selection.

---

## Methodology-adjacent

- [x] **Operating-model location — RESOLVED:** markdown at `data/research/<ticker>/model.md` (version-controllable; precedent USNA, SCOR), built inside the Deep Flow. The case's Excel deliverable is rendered downstream from it.
- [ ] **Primary research workflow** — methodology #4 (5–10 calls). Need a tracker (e.g., `data/primary/<ticker>/calls.md`). This is the step *beyond* the filings data floor — USNA showed exactly where it's needed (Hiya ARPU/CAC/churn).
- [ ] **Peer benchmark refresh policy** — `peer_benchmarks.csv` files go stale; decide refresh cadence / staleness marking.

---

## How agents should use this file

1. Read `MEMORY.md` + project memory and `CLAUDE.md` (auto-loaded) — note the standing rule: **candidate evaluation = the Deep Flow only; no shallow verdicts.**
2. Read this `TODO.md` for open items.
3. Completed work → move to `CHANGELOG.md`, remove here.
4. New gaps (research, tooling, decisions) → add to the right section.
5. **Per-candidate work** lives in `data/research/<ticker>/` (model.md, peer_benchmarks.csv, peer_notes.md), not here.
