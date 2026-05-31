# Changelog

All notable changes to the Lunchline Partners case study project.

## 2026-05-30 (later) — Searched beyond the five finalists; selected ARTW as the case-study build; built the deck + Excel model

After USNA/HCKT, ran a broader hunt and pivoted the thesis from public-mispricing to **take-private-and-operate**, landing on **Art's-Way Manufacturing (ARTW)** as the deck/model build target.

**Screening infrastructure.** Re-ran the all-sector screen and built a richer comparison than cheapness alone for the ~69 untouched operating candidates: enriched with **operating margin vs. industry, institutional-ownership trend, and float**; then layered **search-fund acquirability signals** (owner-dependence, under-professionalization, no-M&A-history, underinvested-growth, succession) and an **industry macro tailwind/headwind + fragmentation** read; rendered as a sortable HTML board (`scripts/build_catalog_html.py`; catalog CSVs/HTML gitignored, regenerable). Emergent finding: cheap + under-followed + high-quality + clean + actionable is a near-empty set — the best take-private setups (PNRG, GENC, FONR) are usually already resolved by insiders.

**Two more deep-flows (both passes):** **HOUR** (Hour Loop) — un-actionable Amazon reseller; corrected bottoms-up DCF ~$0.34–0.50 vs the $1.91 quote on a no-price-discovery 5% float. **INTG** (InterGroup) — briefed and passed; its value is a hotel cap-rate call, i.e., real-estate/asset valuation outside the operating-analysis edge (`feedback_prefer_operating_not_asset_plays`).

**ARTW carve-out deep-flow (v2.1, lead-reviewed)** — `data/research/artw/model.md`. Thesis: acquire ARTW, wind down the loss-making farm-equipment segment, own Art's-Way Scientific (modular biocontainment/research + animal-biosecurity buildings, ~17% op margin, backlog +103% YoY). Depth reversed the "free gem" hope: net debt + a large ag-inventory balance imply the modular business at ~6–9× standalone EBITDA inside the ~$20M EV (fair, not free); FY25 "profit" is an ERC mirage (real op income $0.3M, OCF −$0.9M). Recentered base FV ~$2.46 (−4% vs $2.58); the return lives in the operator value-creation plan + the bull; a take-private at a FONR-style 31.5% premium is underwater on the base (0.73× MOIC). Real asset floor (passes both Graham tests). Catalyst entirely family-gated (McConnell 51.5%). Most original output: the **two-leg policy hedge** (NIH-funded research labs vs USDA-funded animal biosecurity). Lead-review fixes: tightened an optimistic ag-disposal mark (v1 $8.9M → $7.72M; base FV $2.69 → $2.46) and reconciled the bull EV up to the workbook's $22.6M ($4.88 FV / $2.64 weighted / 1.44× bull MOIC).

**Case-study deliverables built on ARTW (the working pick):**
- **Excel model** — `scripts/build_artw_xlsx.py` builds the 10-tab `ARTW_model.xlsx` (Summary, SegmentP&L+ERC, SOTP, two-leg ModularDCF, TwoLeg, Scenarios+MOIC, ValueLenses, Graham, Peers, Assumptions/WACC), live formulas, following the HCKT workbook conventions (.xlsx gitignored; regenerable).
- **Pitch deck** — `mockups/pitches/artw-deck.html`, 12 slides + AI appendix, Direction-1 design. Iterated heavily on voice/clarity: rewrote from an activist-pitch register into the **Buffett objective-underwriting voice** (no selling words, no em-dashes); **de-glossed standard finance terms** for the sophisticated Lunchline audience (context only for business/industry specifics); **restructured to the case's required slide order** (Business Overview with customers/geography/history; End Market with a sourced TAM range + fragmentation; the four value-creation buckets); reframed the thesis as the **operator play** (sell the farm line, fund + scale modular; price is fair for the status quo, not for the modular growth an owner could unlock); added **active-hyperlink citations**; verified each pass with a no-context cold-reader audit. Status: improving but **not yet final**.

**New standing rules to memory:** `feedback_memo_voice` (Buffett voice, savvy audience / no finance-101 glosses, no em-dashes, tight > long, active hyperlinks), `feedback_search_fund_acquirability_signals`, `feedback_prefer_operating_not_asset_plays`, `feedback_candidate_screening_columns`. Committed + pushed as `9c16871`.

**Next:** iterate the ARTW deck to final shape → review `ARTW_model.xlsx` → build the one-page written memo (`option-a-scroll` companion) → populate `docs/prompt-log.md` to back the AI-disclosure appendix.

## 2026-05-30 — HCKT deep-dive (value lenses + decline autopsy + financial-condition test) → passed over as the case-study pick

Pressure-tested HCKT (the stronger finalist on the *quality* of the variant) and decided **not** to use it as the case study. Built a live, formula-driven Excel model — `data/research/hckt/HCKT_model.xlsx` (builder `scripts/build_hckt_xlsx.py`) — and added Graham/Buffett value lenses plus a call-by-call decline autopsy:
- **Decline autopsy:** the −54% 12-month drop ($26→$11.61) was a staircase of guide-downs; the decisive leg was the Q4-FY25 print (Feb 2026, Barrington PT $27→$17). Management **already broke one AI-inflection promise** (guided FY25 "+3-5% / consequential AI uplift," delivered −2.6%), so the Q3-FY26 catalyst the thesis rests on gets a credibility haircut → re-weighted bear/base/bull 40/45/15 → **45/42/13**.
- **Value lenses:** EPV (no-growth) **$9.40–$12.45 brackets the $11.61 price**; reverse DCF implies just **+1.6%** perpetual growth; owner-earnings yield 11.1%. **Graham strong-financial-condition test FAILS both prongs** — current ratio **1.88×** (<2.0) and long-term debt **$78.8M > working capital $38.2M** (2.1×) → no asset floor.
- **Bottom line:** base-case worth ~$14.3 (+23%), but **probability-weighted expected value ~$12.76 (~+7%/yr total incl. dividend)** once the 45% bear is weighted. Thin edge + no balance-sheet floor + a single binary catalyst → not a meaningful enough margin of safety to anchor the case study. **USNA remains the risk-adjusted-preferred finalist** (similar IRR, real asset floor).

Adopted three **model-workbook build conventions** (now embodied in the HCKT workbook as the reference template; documented in `methodology.md`): (1) net financial debt tested against assets via the Graham financial-condition test; (2) a **Peers** tab carrying the comp multiples behind every valuation input (read live from `peer_benchmarks.csv`); (3) an **Assumptions** tab decomposing every judgment input — WACC built bottom-up from CAPM (~9.8% mechanical + 0.75pt illiquidity/binary-catalyst overlay = 10.5%), no orphan hard-coded inputs.

## 2026-05-29 — Deep Flow run on the remaining 4 live candidates (HCKT, AENT, MIND, SWAG)

Ran the full Deep Flow on the four un-modeled names in the live set, as parallel agent-builds → lead-review → iterate (v2) loops, so all five candidates (incl. USNA) are now on equal footing. Each produced `data/research/<ticker>/model.md` + peer files. **The deep flow behaved symmetrically — it rescued nothing falsely and disciplined three of four down.**

- **HCKT (The Hackett Group)** — **MISPRICED-BUT-SHOW-ME; the strongest new finalist.** The load-bearing bear ("AI disintermediates its benchmarking/advisory IP; Gen-AI pivot is a veneer on a no-growth body shop") **fails on the filings**: AI is *raising* delivery margins (+500bps US S&BT project margin from XT/XPLR), HCKT is cutting headcount on its own AI productivity, and the "16%→7.7% margin collapse" is ~95% a one-time non-cash stock-comp event ($16.8M FY25 stock-price-award) — OCF held $40.3M, FCF $32.4M. The bear *survives only on near-term revenue* (FY25 −2.6%, Q1 FY26 −11.6%, "elongated decision cycles on AI ROI uncertainty"). Discount driver = misperception (GICS "IT Services" → 6× body-shop multiple) + neglect + a genuine cyclical air-pocket. **v2: base SOTP $14.43 / base DCF ~$14.50 (converge), prob-weighted 3-yr FV $14.28, ~+11% total IRR. NO asset floor (net debt, goodwill) → −30% bear; binary on the Q3-FY26 inflection.** Lead-review corrected a SOTP corporate double-count (+$2/sh), cut the base terminal +2%→+1%, and re-weighted the bear 35%→40%.
- **AENT (Alliance Entertainment)** — **fairly-priced AS a distributor; thin, deferred mispricing.** Confirms the prior `project_aent_thesis_weakness` ("already priced as a distributor"): on EV/EBITDA it trades ~8.1× = pure-distributor ScanSource; the 0.37× EV/sales is a gross-margin artifact, not a free lunch. Durable higher-margin mix shift (vinyl 32%, CD +90% inflection, collectibles) is real but the P&L benefit is deferred to FY27-28; debt is a self-liquidating WC ABL. **Major data fix: true market cap ≈ $323M, not yfinance's $703.6M** (yfinance counted the 60M untriggered Class E earnout shares). **v2: base multiple 8.75× (derived from AENT's near-zero-capex FCF-conversion premium to ScanSource), base FV ~$7.80, prob-weighted IRR ~+10%. NO asset floor (negative liquidation equity); founder take-private optionality is double-edged (77% control, squeeze-out risk).**
- **MIND (MIND Technology)** — **PASS / AVOID at $6.91.** The disciplining mirror of USNA: the reverse-SOTP shows the operating business *already* at fair-to-full ~8.5× adj EBITDA / ~1.1× rev; base FV ~$5.25 sits *below* the price → ~−7%/yr IRR. Clean catch: the bear's "preferred siphons cash" pillar is **factually dead** (the 9.00% Series A was converted to common and retired 2024-09-04, no arrears). ~60% recurring aftermarket is a real floor, but systems orders are lumpy, FY27 is guided down, and defense revenue is **$0 to date** — the re-rate is entirely unbooked. Re-entry only sub-$5 or on a booked order. Optionality not credited as upside (management dilutes via ATM, won't commit to buybacks above SOTP base, no aligned control holder).
- **SWAG (Stran & Company)** — **investable small position; PASS as the headline pitch.** Bear's *mechanism* (illusory float EV) falsified (cash is genuine AFS securities, AR>>AP — Stran extends credit, doesn't hold float), but the cash is working-capital not excess and was melting until Q1'26. Q1'26 inflected positive but full-year public-company overhead *grew* +58% vs revenue +40% — not yet structurally diluting. **v2: single reconciled base $1.85, prob-weighted IRR ~+1.4%.** Benched for the case on thin asymmetry + soft floor + six disclosed material weaknesses + reaudit + a related-party buyback of the CEO's shares.

**Selection picture:** five names now deep-flowed. **USNA (~+9%, asset-protected) and HCKT (~+11%, no floor, bear genuinely fails) are the two finalists**; AENT (~+10%, no floor) is a credible #3; MIND and SWAG are passes for the headline slot. HCKT is the only one of the four where the discount rests on a *misclassification/quality misperception that the fundamentals contradict*, rather than a thin asset/cash story.

## 2026-05-29 (process change) — Shallow analytical verdict retired; the Deep Flow is now the standard

Decision: stop producing shallow buy/avoid verdicts (the screen-plus-single-bear "trap/keep" call), because they reached wrong conclusions (USNA labeled a value trap; deep modeling reversed it). Encoded the change: the mechanical screen now only *generates suspects* and produces no verdict; **every candidate we evaluate goes through the full Deep Flow** (SOTP + operating/driver model + DCF on cash taxes + sensitivity tornado + Porter's Five Forces + consensus baseline + value-creation plan + kill criteria + known-unknowns), run as an agent-builds → lead-reviews → iterate loop. Documented in `CLAUDE.md` (Working Conventions + router), `docs/methodology.md` (§ The Deep Flow — the step-by-step as run on USNA), and a SUPERSEDED banner on `docs/pipeline.md`. Which suspects get the deep flow is neutral prioritization (cheapness / under-followed / the three escalation flags), never a shallow judgment.

## 2026-05-29 (latest) — Deep-flow test: depth flipped a shallow "value-trap" kill (USNA)

Tested whether our shallow screen/one-bear pass produces false negatives by running ONE ruled-out name (USNA) through the full post-vetting methodology — SOTP + DCF, scenario returns, consensus baseline, value-creation plan, kill criteria (`data/research/usna/model.md`; peers persisted). It **reversed the verdict.** The shallow pass had two hard errors (called Hiya loss-making — it earned +$3.4M FY25 segment EBIT; treated the 72% tax rate as structural — it's a valuation-allowance artifact) and skipped the SOTP: net cash (~$149M) + 78.8% Hiya stake (~$164M at USANA's own transaction price) ≈ $313M vs a $342M market cap, implying the profitable Core (~$54M EBITDA) at ~0.4× EBITDA. SOTP $26.42 / DCF $26.93 base (+43–45%). Deep flow also corrected the *bull* (Hiya is now contracting, subs 224k→186k). Verdict: partial-flip leaning flip; USNA reinstated as "mispriced, own sized for the bear."

Process refinement (in `methodology.md`): the screen is systematically wrong on three setups — recently-consolidated acquisition, net-cash-heavy, control-holder — so **escalate to the deep flow before ruling out any candidate carrying one of those flags.** Live non-SaaS set now: USNA, SWAG, AENT, MIND, HCKT.

## 2026-05-29 (later still) — Dropped the sector constraint; re-screened ALL sectors for non-SaaS

Caught a major scoping error: the Finviz universe pull was scoped to Technology + Communication Services only, which turned Aviv's edge-fit (meant to be an *end-stage tiebreaker*) into a hard universe filter — producing a SaaS-heavy, structurally-problematic pool. Aviv clarified he wants to **AVOID SaaS**, not supplement it.

Fix: added `--all-sectors` to `framework_screen.py` (Country=USA). Re-pulled the universe: **2,912** US small-caps across all 11 sectors (vs 622 in two sectors). Excluded non-operating instrument types (financials/closed-end funds, SPACs/shells, pre-rev biotech) → **1,539** operating cos enriched → **512** clear EV $10–500M + revenue → **445 non-SaaS**, of which **57** are cheap+profitable+under-followed (EV/Rev<1.5x, ≤3 analysts, +op margin, +FCF) and **17** also net-cash-heavy or down >40%. AENT and MIND both surfaced in the screen, validating it.

Corrected `docs/public-company-pitch.md` (sector scope = all operating sectors; edge-fit demoted to end-stage tiebreaker) and saved the lesson to memory (`feedback_sector_not_universe_filter`). Backups: `data/*_2sector.csv`, `data/universe_raw_allsector_full.csv`.

Triage: all six survived the structural gate (USNA's "CLOSED" flag was a false acquirer-side trigger — it *bought* Hiya). Then ran a new **inverted bear-falsification** pass on the top three (state the single load-bearing bear → adversarially try to VALIDATE it → keep only if it fails; baked into `docs/methodology.md`). Result: **USNA and MTRX cut** (bears validated — USNA's MLM customer base declining double-digits; MTRX's "net cash > EV" is customer float atop 7 straight years of operating losses), **HCKT advanced** (bear failed — AI is lifting its delivery margins +500bps, not disintermediating it; an AI *beneficiary* mispriced for AI-fear, though a turnaround on a binary Q3-FY26 catalyst now carrying ~$73M net debt). Verification caught major screen-data errors (USNA net cash stale, MTRX "cash" is customer advances, HCKT is net debt not net cash, HCKT "16% margin" is really ~7.7% GAAP). Live non-SaaS set: SWAG, AENT, MIND + HCKT. Bench: STRT, NATR.

## 2026-05-29 (later) — Pitch tournament cleanup (11 → 7)

Worked the bracket down in a live review session. **Eliminated 4:** IZEA (capital-return-only, ~0% IRR), ACCS (no-moat SaaS — divested its regulated/high-switching compliance business, revenue −2% and now operating-loss-making), NRDY (AI-displacement / Chegg inversion with no offsetting moat), UPLD (melting-SaaS roll-up; declined the preferred/takeout financial-engineering bet). **7 active:** RSSS, SWAG, AENT, SCOR, CDLX, MIND, UONE.

Articulated the governing filter for small SaaS: uninteresting unless (1) proprietary data or (2) regulated-niche high-switching workflow — because AI makes generic SaaS tooling table-stakes. **RSSS kept on a rewritten thesis** (AI-infrastructure / rights-managed entitlement-delivery for the long tail of publishers via API/MCP; B2B-driven organic growth; consumer Scite tier repurposed as a B2C→B2B funnel). Diligence this session: pulled SWAG segment margins (core promo ~33% GM > loyalty/SLS ~21%; consolidated loss is a ~$5.2M public-company-cost artifact → take-private is the unmodeled lever), ACCS revenue mix (~54% recurring, transition <18 months, declining), and RSSS transcripts/analyst actions (Maxim/Lake Street held Buy but cut PT $5→$4 on the Q3 FY26 print).

## 2026-05-29 — Memo system + 16-candidate expansion + 11 verified pitch memos

### Memo voice/principles system (the reusable template)
Built the writing layer the project was missing. Three artifacts:
- `docs/memo-voice.md` — exemplar research (Buffett 1977/89/91/2001, Howard Marks *Sea Change* + *On Bubble Watch*, Einhorn TWTR, Trian) → 8 voice principles, plain-English vocabulary table, inline-sourcing patterns, 3 narrative-arc templates, annotated excerpts, full annotated 1-page skeleton.
- `docs/memo-principles.md` — project checklist: required content blocks (non-obvious / thesis / risks / value-creation across commercial-ops-capital-M&A / forward "what would confirm it"), voice rules, **forbidden moves** (the "wrong industry tag" trick that Aviv killed on AENT), 12-item drafting checklist, and a **number-verification section** (added after the audit below).
- `mockups/pitches/option-a-scroll.html` — canonical AENT memo demonstrating the voice. Layout chosen from a 3-option bake-off (A=scroll, B=tabs, C=index); A won. Plain English, inline hyperlinks (no footnotes), IR-vs-SEC contrast as a narrative element.

Voice/style preference also persisted to auto-memory (`feedback_memo_voice.md`).

### Layer-2 expansion: 21 candidates → 16 structural survivors
Ran `build_dossier` + `check_voting_structure` + `check_deal_status` on all 21 unevaluated Layer-2 names (new helper: `scripts/batch_triage.py`). Triage table at `data/research/layer2_triage_2026-05-28.md`. **16 survived, 5 killed:** ZDGE/SNAL/HIT (super-voting founder lockdown), GIFT (TakeOut7 merger signed), BKKT (NewCo merger closed). Findings-mode dispatched on all 16 (new helper: `scripts/dump_findings_prompts.py` writes per-ticker `findings_prompts.json`); 3 specialist findings files written per ticker under `data/dossiers/<t>/findings/`.

### 11 pitch memos built (the tournament bracket)
Selected 11 viable candidates and built one-page memos for each in `mockups/pitches/`: **CDLX, NRDY, SCOR, AENT** (original 4) + **UPLD, IZEA, RSSS, UONE, MIND, ACCS, SWAG** (new). Bracket index at `mockups/pitches/index.html` (cross-comparison table by archetype + side-by-side multiples matrix). Distressed/blocked names (DRCT, CISO, SURG, CETX, XBP, CTM, FLNT, CNVS, GAME) documented as findings-mode passes.

### Numbers-verification audit (11 parallel agents) — every memo had ≥1 wrong load-bearing number
After catching three fabricated/conflated figures in IZEA by hand (net income $1.2M→$42K; adjusted EBITDA $5.3M→$0.7M, a 7x error that inverted the valuation; Hoozu "write-down" $5.3M→~$2.5M, conflated with an unrelated $4.0M impairment), ran a dedicated verification agent per memo: GAAP vs XBRL, non-GAAP vs the 10-K/10-Q reconciliation table, derived figures recomputed. Findings:
- **Four repeatable failure modes:** (1) data-vendor aggregate fields (yfinance `enterpriseValue`/`marketCap`/`freeCashFlow`/`totalCash`) broke on dual-class/earnout/preferred structures — AENT phantom $704M cap, NRDY EV $91M→$137M, UPLD FCF $36M→$26M; (2) non-GAAP inherited from findings, not the filing; (3) conflation of two similar-magnitude figures; (4) period / share-count inconsistency.
- **Thesis-altering corrections:** CDLX — the "BofA non-renewal wasn't disclosed" pillar is false (named in the April 28 2025 8-K). MIND — the "60% aftermarket is hidden" lever evaporated (it's in the 10-K); the $24.8M NOL is actually a $27.2M valuation allowance; "revenue fell 35%" was 13%. SCOR — per-share targets overstated until rebuilt on fully-diluted ~27.7M shares (Series C at $18.85). IZEA — $0.7M EBITDA makes it a capital-return/sale story, not a re-rate. UONE — IRR rests on a 2031-note price not in the dossier.
- **Survived clean with thesis intact:** RSSS (cleanest), UPLD, SWAG, AENT (marginally stronger — the chairman loan was already repaid).
- Lesson encoded as the number-verification section of `docs/memo-principles.md`.

### Next step
User to review each memo, attack the theses, and pick a company (tournament round). See TODO § Selection Process.

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
