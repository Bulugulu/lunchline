# AI Prompt Log & Workflow Appendix

*Lunchline Partners Case Study · Aviv Sheriff · how AI was used across the project — the tools, the prompts that worked, and where AI helped or hurt.*

Reconstructed from the full Claude Code session transcripts for this project — roughly **524 user prompts across 2026-05-26 → 2026-06-01**, pulled via the Motif CLI. The work ran in seven phases, summarized below. Rather than a verbatim dump, each phase gives the representative prompts, what actually ran, and the honest helped/hurt.

---

## At a glance — the workflow in seven phases

| # | Phase | Dates | What it produced | Verdict |
|---|---|---|---|---|
| 1 | Infrastructure & screening | 5/26–5/28 | Reproducible data pipeline; all-sector framework screen | 57 cheap, profitable, under-followed names |
| 2 | Valuation tooling | 5/28 | Ported a DCF / multi-method valuation engine; per-company peer benchmarks | Bespoke comps, no hardcoded multiples |
| 3 | Multi-agent scoring | 5/28 | 5 specialists + adversarial reviewer + light model | Worked, but manufactured false precision → **retired** |
| 4 | Memo system & numbers audit | 5/29 | Buffett-voice guide; 11 one-page memos; verification pass | A wrong load-bearing number in **every** memo → caught & fixed |
| 5 | The Deep Flow & tournament | 5/29–5/30 | Full SOTP + DCF + Porter + sensitivity + VCP per name | USNA, HCKT, AENT, MIND, SWAG, HOUR deep-flowed |
| 6 | ARTW selection & build | 5/30 | Chose ARTW as an operator carve-out; deck + Excel model | Asset-protected, asymmetric search-acquisition thesis |
| 7 | Deck, value model & delivery | 5/30–6/1 | Voice rewrites, bottom-up value model, PPTX/PDF/Excel package | The shipped deliverables |

---

## Phase 1 · Infrastructure & screening *(5/26–5/28)*

**Goal:** stop relying on stale web data; build a reproducible screen over the full NYSE/Nasdaq universe for $10M–$500M EV, "messy, mispriced, under-followed" names.

**Representative prompts:** "set up the project and identify qualifying companies"; "replace web-sourced data with a reproducible pipeline from yfinance and EDGAR"; "build a defensible framework for 'messy, mispriced, under-followed — avoid obvious names'"; "apply the filters to the whole tech + comms universe."

**What ran:** `scripts/fetch_edgar.py` (SEC filings + XBRL, compliant User-Agent) and `scripts/framework_screen.py` (Finviz universe → yfinance enrichment → filters). A 10-archetype messiness / 8-pattern mispricing framework with quantitative under-followed thresholds. Funnel: 622 → 292 → 227 → 171 qualifying, 83 in the sweet spot (EV/Rev < 1.5× and 0–3 analysts), 45 ultra. Sanity-checked by hand (EXFY 7/7, GDEV 6/7).

**Helped:** scaffolded multi-step, reproducible screening in a single pass. **Fell short:** the first web-sourced candidate list was stale and had to be thrown out; some Chinese ADRs showed corrupt EV/Rev ratios needing manual review.

## Phase 2 · Valuation tooling *(5/28)*

**Goal:** a per-company valuation engine, not sector-generic rules of thumb.

**Representative prompts:** read the FinRobot repo and decide "install it or borrow specific methods"; "port the 10-K analyzer prompts"; "we shouldn't hardcode benchmarks without peer analysis — each company gets bespoke comps, and agents update the CSV so we don't redo the research."

**What ran:** read the actual FinRobot source (rejected the AutoGen orchestration as overkill; borrowed three artifacts — 10-K analyzer prompts, FMP endpoints, a pure-Python DCF). Ported into `analyze_10k.py`, `fetch_fmp.py` (fixed an off-by-one revenue-growth bug in the original), and `valuation.py` (DCF + EV/FCF + EV/GP + Rule-of-40 + path-to-profitability, auto-routed by EBITDA sign). Designed `data/research/<ticker>/peer_benchmarks.csv` so multiples resolve peer → CLI → skip, never a silent default — code-level enforcement of "comp-proven, not theoretical." Regression-tested against AAPL so the positive-EBITDA path didn't break.

**Helped:** distinguished FinRobot's marketing from its working code by reading the tree; caught and fixed the growth-rate bug while porting. **Fell short:** path-DCF defaults are sector-generic and need per-company tuning before a pitch defense.

## Phase 3 · Multi-agent scoring — built, then retired *(5/28)*

**Goal:** rank the 57 survivors objectively, setting aside my own sector bias.

**Representative prompts:** "how would we run the weighted-criterion scoring?"; "split into subagents for task-focus and objectivity"; "ignore my own expertise at this phase… add an adversarial 7th pass using solid investment logic."

**What ran:** five dimension specialists (messiness, value-creation, data, contrarianism, PE-realism) + an adversarial reviewer + a light returns model, plus voting-structure and deal-status detectors. Calibrated on EXFY (rescaled to 3.35/5; detector caught an 84.7% voting trust) and SCOR (adversarial pass caught the fake $103.9M net income + a covenant waiver).

**Helped:** the adversarial reviewer and the voting/deal-status detectors caught structural deal-breakers (super-voting trusts, mid-deal targets like LPSN/KPLT) the specialists missed. **Fell short:** the numeric 1–5 scores were *false precision* — confident and not robust to scrutiny. This directly motivated retiring scoring in favor of the Deep Flow (Phase 5).

## Phase 4 · Memo system & the numbers audit *(5/29)*

**Goal:** a repeatable one-page memo in a real investor voice, and a check that the numbers are true.

**Representative prompts:** "build an investment-memo voice guide from Buffett's letters / Marks / Einhorn"; "triage the unevaluated candidates, then draft one-page memos"; "verify every memo's numbers against the filings."

**What ran:** a research subagent produced `docs/memo-voice.md` (8 voice principles with verbatim exemplars) and `memo-principles.md` (checklist + forbidden moves). A batch ran dossier + voting + deal-status on 21 candidates (16 survived); parallel subagents drafted 11 one-page HTML memos. Then one verification subagent per memo recomputed every figure against GAAP/XBRL and non-GAAP reconciliations.

**Helped:** the verification pass is the single most valuable step in the project — it caught errors that read as plausible and would survive a human read-through (thesis-altering fixes on CDLX, MIND, SCOR, IZEA, UONE). **Fell short — the key disclosure:** the drafting agents *fabricated* plausible numbers; the audit found ≥1 wrong load-bearing figure in **every** memo. Four repeatable failure modes are documented in `memo-principles.md`.

## Phase 5 · The Deep Flow & candidate tournament *(5/29–5/30)*

**Goal:** replace shallow scoring with a single deep, verdict-producing process per name.

**Representative prompts:** "how are we picking from the 42?"; the skeptical-analyst USNA deep-flow prompt + "I'm the reviewing lead; we iterate until we've extracted everything the filings allow"; "why did the stock collapse 54% — did we read the earnings calls?"; "enrich the catalog with owner-dependence / key-man / acquirability signals — don't override the methodology, enrich it."

**What ran:** the **Deep Flow** — SOTP + driver model + DCF on *cash* taxes + Porter's + sensitivity tornado + value-creation plan + kill criteria, run as agent-builds → lead-reviews → iterate — on USNA, HCKT, AENT, MIND, SWAG, HOUR. Scoring was formally retired (it had called USNA a value trap; the Deep Flow reversed, then disciplined, that call). Catalog enriched with search-fund acquirability signals.

**Helped:** the build→review loop extracted far more from the filings than any single pass; the USNA reversal proved the depth was worth it. **Fell short:** needed the lead to repeatedly re-anchor it ("enrich, don't override") — without a method in mind the analysis drifts.

## Phase 6 · ARTW selection & first build *(5/30)*

**Goal:** pick the name and assemble the Part-1 package.

**Representative prompts:** "tell me about ARTW"; "do our deep-dive on this"; "explain the demand/conversion math — do we have actual metrics that demand outran capacity?"; "let's build the slide deck and the Excel model."

**What ran:** ARTW chosen as a take-private-and-operate carve-out — a cyclical farm-equipment shell around a 17%-margin lab builder. Combed the filings for the demand-constraint signal (backlog +103%, a thin part-time commercial org). Built `ARTW_model.xlsx` and the first Part-1 HTML deck.

**Helped:** surfaced ARTW out of the untouched part of the screen and assembled the carve-out package quickly. **Fell short:** first-pass deck leaned salesy and needed the voice discipline that followed.

## Phase 7 · Deck, value model & delivery *(5/30–6/1)*

**Goal:** get the deck into a real investor voice, harden the value-creation model, and ship the package.

**Representative prompts:** "did you use the Buffett style? it feels too salesy — more concise, cut the marketing language"; "assume savvy readers, don't gloss 'operating margin'"; "you reintroduced em-dashes — remove them"; "model the operational path bottom-up… these compound with the multiple, don't cap it top-down"; "critique the approach and help me decide whether to use it at all"; "remove '~' everywhere; drop the redundant downside box; make each subtitle one line"; "Excel for the model, decks as PPTs, prompt log as a presentable PDF — make the repo public or add collaborators?"

**What ran:** multiple voice rewrites verified by no-context "cold-reader" subagents; em-dash and salesy-phrasing purges. Rebased the value-creation waterfall to a control basis ($14.0M → $22.9M); an independent agent reversed a dismissive monitoring take into an installed-base annuity thesis; built a benchmarked bottom-up driver model, then — after a self-critique flagged it as an assumption-stacked hero-bridge — **disciplined it back** (base-anchored, re-rate de-emphasized). Final line-edits to the deck, then rendered **both decks to pixel-perfect PPTX + PDF** via a reusable headless-Chromium script (`scripts/build_deck_artifacts.py`), regenerated this appendix to PDF (`scripts/build_promptlog_pdf.py`), confirmed the Excel, and — after a clean secrets scan (no keys tracked; scripts read from `os.environ`) — made the repo public.

**Helped:** cold-reader subagents gave honest outside-eye feedback on clarity; a self-critique caught the bottom-up model overreaching before it shipped; scripting the renderers kept the HTML deck the single source of truth. **Fell short:** repeatedly reintroduced banned patterns until shown explicit examples, and the previously-built PPTX went stale silently the instant the HTML changed — caught only by an explicit "rebuild before you ship" step.

---

*Full detail for any phase — the per-prompt narrative, the model iterations, and the source citations — lives in the repo: `docs/` (methodology, voice, principles), `data/research/artw/` (model + comps), and the commit history.*
