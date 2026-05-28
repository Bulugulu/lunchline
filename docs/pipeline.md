# Per-Candidate Pipeline (v2)

End-to-end workflow to evaluate a candidate ticker. Each script writes to `data/dossiers/<ticker>/` or `data/research/<ticker>/`.

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

5. **`python -c "from scripts.agent_prompts import build_prompts; print(build_prompts('TICKER'))"`**
   Returns 8 ready-to-dispatch prompts:
   - 6 specialists (Messiness, Value Creation, Data Availability, Contrarianism, PE Realism, IR-vs-SEC Triangulation)
   - 1 adversarial reviewer (sees all 6, attacks with 9 named investment frames)
   - 1 model agent (invokes `scripts/valuation.py` 7-method engine)

6. **Dispatch 6 specialists in parallel** → synthesize their outputs → run **adversarial reviewer** → aggregator (Claude in main thread) produces final weighted score.
   The 6 weighted criteria: Value Creation 25%, Situation Complexity 20%, Sector Fit 15%, Data 15%, Contrarianism 15%, PE Realism 10%. Viability threshold 3.0/5.

## Optional supporting tools

- **`python scripts/valuation.py TICKER`** — 7-method valuation (EV/EBITDA, EV/FCF, EV/GP, EV/Revenue, peer comp, 10-yr DCF, Path-to-Profitability DCF) with football-field chart + 2D sensitivity matrix. Reads peer benchmarks CSV.
- **`python scripts/analyze_10k.py TICKER`** — generates 7 ready-to-paste 10-K analysis prompts (income, balance sheet, cash flow, segment, business highlights, company description, risk).
- **`python scripts/fetch_fmp.py TICKER`** — Financial Modeling Prep wrapper for analyst price targets, BVPS, competitor comps. Requires `FMP_API_KEY`.

## Reference

- Methodology behind the 6 criteria + adversarial frames: [methodology.md](methodology.md)
- Industry-specific KPIs injected into prompts: `scripts/industry_kpis.json`
- Per-candidate research artifacts: `data/research/<ticker>/` (peer_benchmarks.csv, peer_notes.md, model.md, etc.)
- Pitch tournament queue and candidate slate: [../TODO.md](../TODO.md)
