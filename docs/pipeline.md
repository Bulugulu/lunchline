# Per-Candidate Pipeline

End-to-end workflow to evaluate a candidate ticker. Each script writes to `data/dossiers/<ticker>/` or `data/research/<ticker>/`.

> **⚠️ SUPERSEDED (2026-05-29) — the shallow scoring/findings verdict is retired.** The dossier + structural-gate scripts (steps 1–3 below) are still used, but candidate *evaluation* no longer uses the 6-criterion or findings-mode scoring — those produced wrong conclusions (USNA was scored a "value trap"; the deep flow reversed it). **Use the Deep Flow instead:** `docs/methodology.md` § The Deep Flow (SOTP + operating/driver model + DCF on cash taxes + Porter's + sensitivity tornado + consensus + VCP + kill criteria + known-unknowns, run as agent-builds → lead-reviews → iterate). The "scoring modes" below are retained for historical context only.

**Two scoring modes (historical — superseded by the Deep Flow):**
- **Calibration mode** (`build_prompts`) — original 6-criterion + adversarial + model. Use ONCE per archetype to calibrate what good/bad looks like. Heavy: 7-8 agents per candidate.
- **Findings mode** (`build_findings_prompts`) — lighter 3-specialist + adversarial. Use for any candidate AFTER the archetype is calibrated. Drops the 1-5 scoring layer that compressed every candidate in our screened pool to 2.65-2.95 (see CHANGELOG 2026-05-28 late for the diagnostic). Outputs structured findings (5 bull + 5 bear per specialist, file-anchored) instead of scores.

## Sequence

1. **`python scripts/build_dossier.py TICKER`**
   EDGAR filings (10-K / 10-Q / 8-K / DEF 14A / Form 4) + earnings call transcripts + news + analyst data + Seeking Alpha coverage + yfinance snapshot + `summary.md`.
   Output: `data/dossiers/<ticker>/`

2. **`python scripts/check_voting_structure.py TICKER`**
   Detects multi-class / voting trust / controlled-company risk. Classifies as LOW / MEDIUM / HIGH / DEAL_BREAKER.
   Output: `data/dossiers/<ticker>/voting_structure.json`

3. **`python scripts/check_deal_status.py TICKER`**
   Detects merger / acquisition / strategic-review status. Run BEFORE expensive scoring to filter out closed deals or active take-private processes.
   Output: `data/dossiers/<ticker>/deal_status.json`

4. **`python scripts/build_peer_set.py TICKER --add PEER1,PEER2,...`**
   Builds peer table from 10-K Item 1 + web search + yfinance enrichment + manual `--add` augmentation (canonical workflow).
   Dual-writes:
   - `data/dossiers/<ticker>/peers/peer_table.json` (light schema)
   - `data/research/<ticker>/peer_benchmarks.csv` (the format `valuation.py` reads)

5a. **Calibration mode — `build_prompts('TICKER')`**
   Returns 8 ready-to-dispatch prompts:
   - 6 specialists (Messiness, Value Creation, Data Availability, Contrarianism, PE Realism, IR-vs-SEC Triangulation)
   - 1 adversarial reviewer (sees all 6, attacks with 9 named investment frames)
   - 1 model agent (invokes `scripts/valuation.py` 7-method engine)
   The 6 weighted criteria: Value Creation 25%, Situation Complexity 20%, Sector Fit 15%, Data 15%, Contrarianism 15%, PE Realism 10%. Viability threshold 3.0/5.

5b. **Findings mode — `build_findings_prompts('TICKER')`** (preferred for candidates after calibration is done)
   Returns 4 ready-to-dispatch prompts:
   - **Lever Ideation** — 5 named comp-proven levers + 5 lever blockers, each with filing anchor
   - **Mispricing Diagnosis** — 9-row checklist rule-ins + 2-sentence variant perception
   - **IR-vs-SEC Triangulation** — gap report (claim-vs-filing pairs) — reused unchanged from calibration mode
   - **Findings Adversarial** — 3 most material attacks, prioritized, with kill criteria
   Drops: Messiness, Data Availability, PE Realism scoring (all near-constants for our pool). Drops weighted-score aggregation. Drops in-loop model agent (run `valuation.py` separately when a candidate advances to underwriting).

6. **Calibration mode:** dispatch 6 specialists in parallel → synthesize → adversarial reviewer → aggregator produces final weighted score.
   **Findings mode:** dispatch 3 specialists in parallel → synthesize specialist outputs into the adversarial → adversarial produces 3 attacks + kill criteria. No score; the findings themselves drive the pitch/pass decision.

## Optional supporting tools

- **`python scripts/valuation.py TICKER`** — 7-method valuation (EV/EBITDA, EV/FCF, EV/GP, EV/Revenue, peer comp, 10-yr DCF, Path-to-Profitability DCF) with football-field chart + 2D sensitivity matrix. Reads peer benchmarks CSV.
- **`python scripts/analyze_10k.py TICKER`** — generates 7 ready-to-paste 10-K analysis prompts (income, balance sheet, cash flow, segment, business highlights, company description, risk).
- **`python scripts/fetch_fmp.py TICKER`** — Financial Modeling Prep wrapper for analyst price targets, BVPS, competitor comps. Requires `FMP_API_KEY`.

## Reference

- Methodology behind the 6 criteria + adversarial frames: [methodology.md](methodology.md)
- Industry-specific KPIs injected into prompts: `scripts/industry_kpis.json`
- Per-candidate research artifacts: `data/research/<ticker>/` (peer_benchmarks.csv, peer_notes.md, model.md, etc.)
- Pitch tournament queue and candidate slate: [../TODO.md](../TODO.md)

## Why two modes exist (the framework discrimination diagnostic)

We ran the original 6-criterion pipeline on EXFY, SCOR, CDLX, NRDY and every candidate landed 2.65-2.95 post-adversarial. Initially looked like the framework was broken. A control-company test (FAST — clean compounder, premium valuation, well-followed) ran through the same pipeline and scored 2.58 pre-adversarial with a near-INVERSE per-criterion fingerprint (Messiness 3, Value Creation 1.5, Data 5, Contrarianism 1, IR-SEC 4, PE Realism 1 vs the messy pool's 5, 3.5, 4.5, 3.5, 2.5, 2). Per-criterion range across archetypes: 1.5-2.5 points. The framework DID discriminate; our pool was just self-similar by design (pre-screened for the same archetype the framework was built to identify).

What this told us:
1. The scoring layer is decoration after calibration — for any new candidate in the pre-screened pool, predict score 2.7 ± 0.2 without running the agents.
2. The findings layer (specific, anchored, named evidence) is what the agents are actually producing of value.
3. The adversarial reviewer is the most cost-effective single layer — it generates the most pitch-shaping findings per token (BZFD Allen 51% board capture, THRY ABL maturity collision, CDLX ACPU math error).

Findings mode is the response to (1) and (2). It keeps what's working and drops what isn't.
