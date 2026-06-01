# TODO

Working backlog for the Lunchline Partners case study. Newest at top within each section. Resolved items move to CHANGELOG.

**Process (current):** all-sector screen → neutral prioritization → **the Deep Flow** is the only verdict-producing step. See `CLAUDE.md` Working Conventions and `docs/methodology.md` § The Deep Flow. The legacy 2-sector funnel, the findings-mode / 6-criterion scoring pipeline, and the "pitch tournament / pitch agent" flow are **retired** (history in CHANGELOG, 2026-05-29).

---

## Part 2 — AI-enabled market mapping (ACTIVE, building since 2026-05-31)

End market worked **directly = executive search, sourced broadly**; 12-month acquisition-search framing. **Scope change to reconcile:** the Phase-1 vertical down-select in `docs/market-mapping.md` (Approach A) was **set aside** for this build — either restore it or formally record the change to "executive search, sourced broadly." Working HTML docs in `mockups/pitches/`; research in `data/research/part2-vendors/`.

Deliverables (3): project plan ✓ · vendor stack ✓ · human-vs-AI map ✓ (folded into the vendor-stack doc, 2026-05-31).

- [x] **Project plan** — `part2-project-plan.html` (12-mo funnel; 4-workstream Gantt; milestone gates). **Reworked 2026-05-31:** title states the goal (acquire an exec-search firm, no "funnel" framing); §01 "Targets" + accountability subtitle; conversion column = percentages only. **Funnel reconciled to the real universe** (`data/research/part2-vendors/exec-search-universe-size.md`): there is no ~3,000-firm cold universe (retained acquirable boutiques ~500–1,000 nationally), so top-of-funnel = **~750 firms at a ~20% blended reply target** (engage most of the addressable universe, warm/multi-channel/referral-supported) → 150 replies → 75 calls → 15 IOI → 5 LOI → 2 → 1. Added a sized addressable-universe callout. Milestones trimmed to 4 (KPI %, deals sourced, first LOI, close). **This makes the broker/referral workstream load-bearing.**
- [x] **Vendor stack** — `part2-vendor-stack.html` (Market Research / Sourcing / CRM+capture / Outbound; recommendation + comparison each; **~$430–800/mo all-in** after the Outbound trim). **Trimmed 2026-05-31** per Aviv: removed the architecture/MCP-spine, recommended-lean-stack, 2026-signals, one-caution, and pricing-note sections. Now 4 sections: principles · exec summary · category profiles · human-vs-AI. Sourced research + README in `data/research/part2-vendors/`.
- [x] **Outbound — pressure-test (researched 2026-05-31, HTML REWRITE PENDING):** Verdict = Smartlead is the wrong paradigm at ~190/mo. Switch to real-domain sending: **Apollo connected-mailbox sequences** (likely already owned, $0 marginal) or **Superhuman** (~$33, AI 1:1 inbox, not a sequencer); rework LinkedIn to **manual + Sales Nav + Clay** (zero ban risk) or **Expandi** (cloud+dedicated IP); add **phone** (OpenPhone/Quo Business $23 + own-voice ringless VM); keep **Handwrytten**, add **Lob** (free dev tier) for typed letters. Three truths to bake in: open-rate tracking is broken (Apple MPP → judge on replies/clicks); AI stays upstream (no AI cold-calling); rent-deliverability-at-scale is net-negative at 10/day. Research in `data/research/part2-vendors/outbound-pressuretest.md`. **HTML applied + prioritized to TWO tools 2026-05-31** — Outbound = **Superhuman ($33) + Handwrytten ($99)**; LinkedIn manual, phone on existing OpenPhone line, Apollo sequences a $0 optional, Smartlead not used. Outbound ~$132/mo; all-in ~$430–800. Section + exec-summary row + considered-not-used + MCP spine + lean-stack table all reconciled in `part2-vendor-stack.html`.
- [ ] **Broker / advisor / referral sourcing workstream → add to PROJECT PLAN (`part2-project-plan.html`), NOT the vendor stack** (Aviv 2026-05-31). Use brokers + advisors to source more deals, supply valuation benchmarks, and feed referrals into proprietary flow. Concretely: Searchfunder ($432 lifetime) + Axial (success-fee tier) + free BizBuySell/Synergy alerts; a one-page **buy-side mandate** to ~5–15 IBBA / M&A Source / exec-search advisors; referral sources run as an Attio pipeline. Frame as the 37%-of-closes insurance leg on the 64% proprietary engine; set 12-mo pace expectation (first LOI ~month 7 or ~40% never close). Research in `data/research/part2-vendors/sourcing-channels-and-brokers.md`.
- [x] **Human-vs-AI map** (deliverable 3) — **DONE 2026-05-31, folded into `part2-vendor-stack.html` as section 04.** Three principles (AI can't replace the relationship; AI accelerates the team; AI is only as good as its controls → start hybrid, automate as the "good examples" library grows) + a funnel-split table (Human-led/only on outreach + calls; AI-led on sourcing/research/pipeline) + a "trajectory" block.
- [ ] **Reconcile with `docs/market-mapping.md`** — restore the Phase-1 vertical down-select or document the scope change.
- [ ] Required appendix: AI prompt log / tools used / where AI helped or hurt (shared with Part 1; `docs/prompt-log.md`).

---

## Decisions blocking other work

- [ ] **Company selection — NARROWING TO A FINALIST (all-sector, non-SaaS, deep-flow only).** Direction: **AVOID SaaS** (small SaaS needs a proprietary-data or regulated-niche moat — `feedback_saas_moat_filter`); sector is an end-stage tiebreaker, not a universe filter (`feedback_sector_not_universe_filter`).
  - **Live candidate set:** USNA, HCKT, AENT, MIND, SWAG — **all five now deep-flowed (v2, lead-reviewed).**
  - **Deep-flow results (all `data/research/<ticker>/model.md`):**
    - **USNA** — mispriced deep-value *asset* play; SOTP base +34%, **~+9% IRR**, **asset floor ~−28%** (net cash + Hiya stake ≈ market cap). Catalyst-gated; data floor reached (Hiya unit economics undisclosed).
    - **HCKT** — **ANALYZED & PASSED OVER as the case-study pick (2026-05-30).** The bear genuinely fails on fundamentals (AI raises its delivery margins) and the variant is sharp, BUT the deep-dive (live model `HCKT_model.xlsx` + value lenses + decline autopsy) showed the *edge is too thin*: base FV ~$14.3 (+23%) but **probability-weighted expected value ~$12.76 (~+7%/yr total)** once the 45% bear is weighted; **no asset floor** (fails Graham strong-financial-condition test — current ratio 1.88×, LT debt 2.1× working capital); binary on the Q3-FY26 catalyst, which is weakened by a **prior broken AI-inflection promise** (FY25 guided +3-5%, came −2.6%). Great *story*, thin risk-adjusted *edge*. Kept as a strong analytical exhibit, not the headline.
    - **AENT** — fairly-priced *as a distributor* (~8.75× EBITDA); base FV ~$7.80, **~+10% IRR**, **no asset floor**; thin deferred margin-mix option + double-edged founder take-private. Credible #3.
    - **MIND** — **PASS/AVOID at $6.91** (base FV ~$5.25 *below* price; ~−7% IRR). Re-enter sub-$5 or on a booked defense/scientific order.
    - **SWAG** — **PASS as headline pitch** (base $1.85, ~+1.4% IRR; governance flags). Small speculative position at most; revisit if Q2–Q3 FY26 confirm the inflection + clear the material weaknesses.
    - **HOUR** (Hour Loop) — **PASS / un-actionable** (deep-flowed 2026-05-30, v2 lead-reviewed). Amazon-reseller (~98% Amazon), 1.7% op margin Amazon controls, no moat/floor/catalyst, 94.8% founder control + ~5% float. Corrected bottoms-up DCF: fundamental value **~$0.34–0.50/sh vs the $1.91 quote** → not cheap, if anything overvalued on a no-price-discovery float; un-actionable every direction. Data floor: per-SKU/cohort unit economics undisclosed (the one thesis-making variable). Verifies the "too-messy-to-read" instinct — financials read clean, but no edge for an outside minority. `data/research/hour/model.md`.
    - **ARTW** (Art's-Way Mfg) — **PASS as a deal / strong analytical exhibit** (deep-flowed 2026-05-30, v2 lead-reviewed). Tested as a *carve-out*: acquire, wind down the loss-making farm-equipment segment, own **Art's-Way Scientific** (modular biocontainment/lab + animal-biosecurity buildings, ~17% op margin, backlog +103% YoY). Depth **reversed the "free gem" hope**: net debt ~$6.4M + big ag inventory mean the modular business is implied at **~6–9× standalone EBITDA inside the ~$20M EV — fair-to-full, not free**; FY25 net income is an **ERC mirage** (real op income $0.3M, OCF −$0.9M = ag inventory build). Recentered base FV **~$2.46 (−4% vs $2.58)** → **fairly-to-modestly *overvalued* on the base; entire return in the bull + a friendly-carve-out option**; whole-co acquisition at a FONR-style 31.5% premium is **underwater (0.73× MOIC base)**. Real asset floor (passes both Graham tests). Catalyst **entirely family-gated** (McConnell 51.5%, voting gate = DEAL_BREAKER, no live process). Data floor: the **research-lab vs ag-biosecurity leg split is undisclosed (est. 60/40)** — the variable the bull hangs on. Most original output = the **two-leg policy hedge** (NIH-pressured research labs vs USDA-funded animal biosecurity). `data/research/artw/model.md`.
  - **WORKING CASE-STUDY PICK = ARTW** (selected 2026-05-30 via the take-private-and-operate lens; supersedes the USNA-lead line). Framing shift to note: ARTW is pitched as an **operator/control carve-out** — the value is in the value-creation plan, NOT a pure public-mispricing buy (the deep-flow verdict is "fairly priced as-is," base FV ~$2.46 vs $2.58). USNA remains the strongest pure *public-mispricing* alternative (~+9% IRR, asset floor) if we ever revert; HCKT/AENT behind it.
  - **Deliverables on ARTW (in progress):** Excel model `ARTW_model.xlsx` built (`scripts/build_artw_xlsx.py`, gitignored/regenerable); pitch deck `mockups/pitches/artw-deck.html` built (12 slides + AI appendix, Direction-1, Buffett voice, operator-play thesis, active hyperlinks). Bull numbers reconciled across model/workbook/deck ($22.6M EV / $4.88 FV / $2.64 weighted / 0.73×–1.44× MOIC at a 31.5% premium).

- [ ] **NEXT STEPS (Aviv, 2026-05-30 — continuing in a new session):**
  1. **Iterate the ARTW deck to final shape** — "still not there." Keep tightening (tight > long), hold the voice rules in `feedback_memo_voice` (Buffett register, savvy audience so NO finance-101 glosses, NO em-dashes, active hyperlinks), keep sharpening the operator-play thesis. Open sub-items: whether to restore slide-4's competitor-fragmentation visual as a labeled table; the conviction-vs-eyes-open dial. **Verify each pass with a no-context cold-reader subagent audit.** Open the deck via `Start-Process mockups/pitches/artw-deck.html`.
  2. **Review the Excel model** `ARTW_model.xlsx` (regenerate with `python scripts/build_artw_xlsx.py`; it reads `data/research/artw/model.md` + `peer_benchmarks.csv`).
  3. **Build the one-page written memo** — the `option-a-scroll.html` companion, same Buffett voice.
  4. **Populate `docs/prompt-log.md`** and wire it to the deck's AI-disclosure appendix (required for the whole case).
  - **Model-workbook build conventions (adopted 2026-05-30, see `methodology.md`):** every `<ticker>_model.xlsx` carries (1) the Graham financial-condition test (net debt vs working capital + current ratio), (2) a Peers tab with the comp multiples, (3) an Assumptions tab decomposing each judgment input incl. a bottom-up CAPM WACC build. Reference template: `data/research/hckt/HCKT_model.xlsx` / `scripts/build_hckt_xlsx.py`.
  - **Demoted (SaaS / software-adjacent), pending deep-flow or drop:** RSSS, CDLX, SCOR. **Shallow-eliminated (revisit only if flagged):** IZEA, ACCS, NRDY, UPLD, MTRX.

- [ ] **FMP API key** — `fetch_fmp.py` works but `/v4/price-target` + competitor-comps endpoints likely need the paid Starter tier ($14/mo). Decide: pay one month, or skip the sell-side-consensus signal. (Consensus baseline is part of the Deep Flow.)

- [ ] **Friendly-transaction framework (deferred)** — founder-controlled names with active strategic reviews (a founder-led-sale setup) read as DEAL_BREAKER under the standard hostile-attack voting logic. Revisit only if the candidate field thins.

---

## Selection process & state (current)

Process: `python scripts/framework_screen.py --all-sectors` generates suspects → neutral prioritization (cheap / under-followed / the 3 escalation flags) → **the Deep Flow** (`methodology.md § The Deep Flow`) is the only verdict step. Selection criteria in `docs/public-company-pitch.md` § Selection Process.

- **Universe:** all sectors, US-listed, EV $10–500M. `data/universe_raw_allsector_full.csv` (2,912) → 1,539 operating (ex financials/funds/SPACs/pre-rev-biotech) → 512 EV-fit → **445 non-SaaS**, of which **57** are cheap+profitable+under-followed (`data/framework_filtered.csv`).
- **Unexamined:** ~70 untouched screen-passers remain (full count rerun 2026-05-30: 71 non-SaaS names pass cheap+profitable+under-followed after removing touched tickers; HOUR now deep-flowed → ~70). Prioritize any carrying the 3 escalation flags. Top untouched by neutral priority: CATO (net-cash floor, 0.20x EV/Rev), MHH (edge-fit, data/analytics staffing), BDL (clean +FCF restaurant), DLTH (fallen-angel apparel).
- **"Only-modeling-reveals-truth" scan (2026-05-30):** surfaced fresh SOTP/opaque names — INTG, NL, GENC, BH, RICK, UTMD, KPLT, HFFG. **INTG briefed in full and PASSED (not deep-flowed):** value is a SF-hotel cap-rate call + apartment cap rates → reads as a real-estate investment, outside Aviv's operating-analysis edge (preference recorded in memory `feedback_prefer_operating_not_asset_plays`). Likewise down-weight RICK (RE stub), NL (public-stake marks), BH (portfolio leg). **Operating-business fits to pursue next:** MHH (edge-fit, IT staffing + data analytics), HFFG (food-distribution roll-up, goodwill/earnout accounting noise), GENC (net-cash cyclical operator), LIVE (operating-conglomerate SOTP).
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
