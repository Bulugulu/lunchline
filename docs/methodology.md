# Analytical Methodology

Distilled from the exemplar decks identified in [deck-structure.md](deck-structure.md). These are the analytical disciplines that separate institutional-quality pitches (Trian, Pershing Square, Starboard, PSC winners, search fund acquirers) from McKinsey-flavored repackaging. They directly inform our workstream sequencing and AI usage.

---

## Sourcing discipline: lead with the discount driver, then falsify the bear (added 2026-05-29)

A low multiple is an embedded market judgment, not a free lunch. "Cheap + profitable + under-followed" produces a list of *suspects*, never a thesis. The edge is never "this is good and cheap" — if that were both true and obvious, the gap would close. The edge is: **the market discounts this for a specific reason, and that reason is wrong, overblown, mismeasured, temporary, or simply un-analyzed.**

So we invert the research. For every screened candidate:

1. **State the single load-bearing bear** — the one reason the market discounts it; what the price *implies* the market believes. Not five bear points: *the* one.
2. **Classify the discount driver** — only one bin is fatal:
   - *Misperception* (wrong tag, hidden segment, accounting optics, one-time read as structural) → opportunity (bear is wrong)
   - *Temporary / cyclical* (down-cycle, transitory cost, integration year) → opportunity if the recovery is underwritable
   - *Neglect* (too small/illiquid/orphaned; nobody did the work) → opportunity *only with a catalyst*
   - *Permanent impairment* (secular decline w/ no offset, fraud, terminal governance, fake cheapness) → **value trap, avoid**
3. **Adversarially try to VALIDATE the bear** — build the strongest case that the scary thing is real and permanent (attack the bull, not the bear, to avoid confirmation bias). If the bear *survives* → trap, pass. If you genuinely *cannot* validate it → **the failure-to-validate IS the thesis.**
4. **Require a catalyst** — a disconfirmed bear with no catalyst just stays cheap. Full structure: *discount driver × is it actually true? × what forces the re-rate?*
5. **Rebuild the load-bearing numbers from filings, never data-vendor aggregates** — the "cheap" hook itself is often a data artifact (e.g., "net cash" that is customer float or already-spent; "16% margin" that is a non-GAAP / stock-comp-reversal figure).

The pitch then writes itself in the case's own voice: **"Market prices in [bear]. [Bear] is wrong/overblown because [evidence we could not break]. Re-rates on [catalyst]."**

This is the organizing step — it runs *before* the bull-case findings, and the `mispricing_diagnosis` RULE-IN/RULE-OUT tool is its instrument. **Validated 2026-05-29:** of three non-SaaS leads, the bear *survived* for **USNA** (accelerating MLM customer decline) and **MTRX** ("net cash" is customer float; 7 straight years of operating losses) → both cut as traps; the bear *failed* for **HCKT** (AI is raising its delivery margins, not disintermediating it) → advanced as the one genuine mispricing.

**Refinement (2026-05-29): the shallow pass produces false negatives — escalate to the deep flow on three setups.** Re-running USNA through the full post-vetting flow (SOTP + DCF, `data/research/usna/model.md`) *reversed* the shallow "value trap" call. The screen / one-bear pass had two hard errors — it called Hiya loss-making (it earned +$3.4M FY25 segment EBIT) and treated the 72% tax rate as structural (it's a valuation-allowance artifact, guided to 55–60%) — and it skipped the SOTP that shows net cash + the Hiya stake ≈ the entire market cap, leaving a profitable Core implied at ~0.4× EBITDA. Lesson: the screen is *systematically* wrong on (i) a **recently consolidated acquisition** distorting blended numbers, (ii) **net cash that is a large fraction of market cap**, and (iii) a **control-holder** structure. **On any candidate with one of these three flags, run the deep flow (SOTP/DCF) before ruling it out** — shallow, consolidated reading misprices exactly these.

---

## The Deep Flow — the standard (and only) candidate-evaluation process (encoded 2026-05-29)

**Decision (2026-05-29): the shallow analytical verdict is retired.** The screen-plus-single-bear "value trap / keep" call produced wrong conclusions — it labeled USNA a value trap, and modeling it reversed the verdict (then disciplined it). Going forward there is **no shallow verdict**: the mechanical screen (`framework_screen.py`) only *generates suspects*, and **every candidate we actually evaluate goes through the full deep flow below.** A buy/avoid conclusion is only ever the output of the deep flow.

*(One unavoidable bit of triage: we can't deep-flow thousands of names, so we still **prioritize** which screened suspects get the deep flow — but that prioritization is neutral (cheapness, under-followed, the three escalation flags), never a shallow buy/sell judgment.)*

**The deep flow, as run (USNA was the template — see CHANGELOG 2026-05-29):**

1. **Dossier** — `build_dossier.py <ticker>` (10-K/10-Q/8-K/DEF 14A + transcripts) and the structural gates `check_voting_structure.py` / `check_deal_status.py` (a gate, not a verdict — and double-check its flags: USNA's "deal CLOSED" was a false acquirer-side trigger).
2. **A deep-analysis agent builds the full package from the FILINGS** — never vendor aggregates (yfinance EV/cash/FCF/margins are unreliable on dual-class, earnout, acquisition, and contract-liability structures):
   - **Sum-of-the-parts** — decompose into segments/businesses + net cash and value each separately. This is the move the screen is structurally blind to; it flipped USNA (net cash + the Hiya stake ≈ the whole market cap → the profitable core implied near-free).
   - **Operating / driver model** — a driver tree to the *real* operating inputs (e.g., active customers by region × revenue/customer; subscribers × ARPU × churn × CAC) so we understand how the business runs and what moves it.
   - **DCF** — scenario-based, explicit assumptions; **tax from the cash-flow statement's "income taxes paid," not the book rate** (the USNA tax error — a fixed foreign cash tax, not the 72% book rate or a reversible artifact); WACC; terminal reconciled to the driver model.
   - **Sensitivity tornado** — rank drivers by their swing on equity value; know which 2–3 assumptions the answer hangs on (for USNA, the value rested most on the Hiya mark — the asset we had least data on).
   - **Porter's Five Forces** — per competitive arena, tied back to margin durability / terminal value / the multiple.
   - **Consensus baseline** — Street estimates + what the price implies, to locate the variant.
   - **Value-creation plan** (commercial / operations / capital structure / M&A) and **kill criteria** (monitorable thresholds).
   - **Known-unknowns** — what the data *cannot* tell us and what it would take to close (primary research / alt-data). Maps the data floor so we know when we've gone as deep as the data allows.
   - **Verdict** framed as the discount driver: is the market's reason for the discount right? + the catalyst.
3. **Review loop (mandatory)** — the lead reviews the build against everything known, challenges every estimate-vs-cited number and every internal contradiction, and the agent reconciles/iterates **until the lead is satisfied we've extracted everything the data allows.** A single pass is not trusted: USNA v1 carried its own errors (over-marked a contracting Hiya, under-taxed it); the review caught them and v2 corrected the base case down.
4. **Persist** — `data/research/<ticker>/model.md`, `peer_benchmarks.csv`, `peer_notes.md`.

**Disciplines proven on USNA:** rebuild load-bearing numbers from filings; resolve internal contradictions explicitly (the tax decomposition); **depth is for *accuracy*, not optimism** (it both rescued USNA from a false "trap" and deflated a false "+43%" to a calibrated ~+9% IRR with the error bars drawn); the review loop is non-optional.

---

## Six Core Lessons

### 1. Operating model first, deck second

Every Trian, Pershing, and PSC-winner pitch reconciles every slide number to a forward model. The VCP value bridge IS the model output. Slides are derivatives.

**Implication for us:** Build the Excel returns model as the *first* deliverable after company selection, not the last. Every slide datum cites a model cell. python-pptx becomes a "render model to deck" operation, not "type numbers into PowerPoint."

**Exemplars:** Trian Disney white paper appendix; Stanford 2024 Search Fund Study IRR/MOIC convention.

---

### 2. Consensus baseline is a prerequisite to variant perception

Top decks quote specific Street numbers ("$72M revenue Street '27E", "peer EV/EBITDA 10.0×"). You can't say "market sees X" without knowing what X is. The thesis emerges from the gap between consensus and our view — but the gap requires measuring both sides.

**Implication for us:** Before forming our own view, build a "consensus dossier":
- Sell-side estimates (FactSet / Visible Alpha if accessible; otherwise extract from sell-side reports + transcripts)
- Peer multiples table (current EV/Rev, EV/EBITDA across comp set)
- Retail / Reddit / Seeking Alpha narrative — what does the retail consensus say
- Last 2 earnings call Q&A focus areas — what is the Street asking about
- Document what the consensus *is*, then explicitly mark where we'll disagree

**Exemplars:** PSC 2019 Hertz winner (explicit consensus framing); Trian P&G white paper (specific Street disagreement quantified).

---

### 3. Comp-proven levers, not theoretical levers

Every Trian margin claim cites a peer at that margin. Every PSC value-creation lever cites a comparable transition that already executed. "Improve margins 200bps" is amateur; "Peer X executed this exact playbook in 18 months and hit 28% margin" is institutional.

**Implication for us:** Build a "comparable transitions library" — for each lever we expect to propose, identify 3-5 prior situations where peers / PE-owned cos executed similar moves. Quantified, dated, with source.

Format suggestion:

| Lever | Comp company | Situation | Outcome | Time | Source |
|---|---|---|---|---|---|
| Live-ops monetization | Take-Two (Zynga) | Battle pass intro 2023 | ARPU +27% | 14 mo | TTWO FY24 10-K |
| ... | ... | ... | ... | ... | ... |

**Exemplars:** Trian "Restore the Magic" Disney — every margin/EPS lever has a peer reference; Starboard Darden — real estate monetization framed via prior comp transactions.

---

### 4. Primary research is the actual differentiator

PSC 2026 Baker Hughes runner-up did 30+ expert calls. Hindenburg shorts run ground-truth investigations. Search fund acquirers do customer references before LOI. The reason their decks read as "I know this business" is they did the work.

**Implication for us:** Budget 5-10 primary research touches:
- LinkedIn outreach to former employees (recruiter angle works; "researching the industry" works)
- Customer reference checks (find 2-3 named customers, cold outreach or warm intros)
- Competitor checks (1-2 calls with competitor sales / product people)
- Ethnographic: Glassdoor reviews, App Store / Play Store reviews, Reddit threads, product community forums
- Expert network if budget allows (GLG, Tegus, Stream — but free outreach often gets 50% there)

For a public micro-cap this is rare and high-leverage — exactly the "specificity over polish" Lunchline wants. Also: primary research is one of the few things AI *can't* fake, which makes it disproportionately credibility-building.

**Exemplars:** PSC 2026 Baker Hughes runner-up (30+ expert calls cited); Hindenburg report archive; IESE search fund seller-call methodology.

---

### 5. Kill criteria are part of the thesis, not just the risks

"What would change our mind" must be specific, dated, monitorable — not narrative. PSC and activist decks list quantitative thresholds (DAU < X, gross margin < Y, churn > Z) and the data point that resolves each.

**Implication for us:** Build a "thesis monitor" sheet alongside the model. For each thesis pillar AND each risk: metric / threshold / source / next data point. This is what you'd hand a junior analyst saying "watch these."

Format suggestion:

| Pillar / Risk | Metric to watch | Threshold | Data source | Next data point |
|---|---|---|---|---|
| Pillar 1: Live-ops ARR | Quarterly bookings | < $32M for 2Q | 10-Q | 2026-Q4 earnings (Feb 2027) |
| Risk 1: Title #2 delay | Ship date | Slip > 6mo from Q3 FY27 | Earnings call | 2026-Q3 (Nov 2026) |
| ... | ... | ... | ... | ... |

**Exemplars:** Trian Disney risk appendix (kill criteria explicit); Pershing Valeant 2014 is the famous *negative* exemplar — they had no kill criteria, thesis broke catastrophically.

---

### 6. Diagnose WHY the mispricing persists, not just THAT it exists

Top decks don't say "it's cheap." They say "it's cheap because SPAC holders are still exiting, sell-side dropped coverage when their bank lost the IPO mandate, and segment misclassification puts it in the wrong comp screens." The structural reason IS the variant perception — it's what makes the trade contrarian rather than crowded.

**Implication for us:** Run a "mispricing diagnosis" before writing the thesis. Explicit checklist — rule in/out each with evidence:

| Reason mispricing could persist | Apply? | Evidence |
|---|---|---|
| Zero sell-side coverage | ? | # of analysts, last initiation date |
| Lock-up / SPAC overhang | ? | Lock-up expiry dates, recent secondary offerings |
| Sector misclassification | ? | GICS sector vs. actual business; comp screen output |
| Segment opacity | ? | Are key drivers buried in "Other" segment |
| Recent disappointment / fallen angel | ? | % off ATH, % off 52wk high, what triggered drop |
| Retail exit (broken IPO/SPAC) | ? | IPO/de-SPAC price vs. current, retail holder % |
| Too-small-for-institutions | ? | Float size, daily volume vs. $100M+ fund size |
| Accounting opacity / restatement | ? | Recent restatements, auditor changes, material weakness |
| Activism vacuum | ? | Insider ownership %, blocking stake potential |

**Exemplars:** PSC Hertz winner (retail SPAC exit explicitly diagnosed); broader VIC writeup tradition (always opens with "why is this mispriced").

---

## Two Structural Disciplines

### Triangulate IR rhetoric vs. SEC filings

Trian's white papers compare earnings call language to 10-K disclosures line by line. Often there are gaps — management says "diversified customer base" but 10-K says "top 3 customers = 65% of revenue." LLMs are very good at this kind of triangulation.

**Implication for us:** This is one of the highest-leverage AI use cases in our process. Pull last 4 earnings call transcripts + last 10-K, prompt an LLM to find specific claim-vs-filing gaps. Document gaps as potential thesis or risk inputs. Flag this technique in the AI appendix.

### Compression as discipline

PSC pitches force 10-15 min compression. Buffett letters compress to a page. If you can't write a 1-paragraph thesis crisply, you don't have a thesis yet — you're still researching.

**Implication for us:** Write a 1-paragraph thesis as a compression test BEFORE building slides. The paragraph must include: (a) what we own, (b) variant perception in one sentence, (c) the catalyst that forces value recognition, (d) the IRR / MOIC range, (e) the kill criterion. If any of those won't compress, keep researching.

---

## Sequenced Analytical Workstream

What this changes about our work after company selection. Replace the prior ad-hoc "next steps" with this sequence:

| # | Workstream | Output | Owner | Rough time |
|---|---|---|---|---|
| 1 | Mispricing diagnosis | Why-it-persists checklist with evidence | Aviv | 1-2 days |
| 2 | Consensus baseline dossier | Street numbers + peer multiples + retail narrative + earnings Q&A themes | Aviv + AI | 1 day |
| 3 | Operating model v0 | Excel: historicals + 3-yr forward, lever-driven, scenario-capable | Aviv | 3-5 days |
| 4 | Comparable transitions library | 3-5 prior comps per proposed lever, quantified and sourced | Aviv + AI | 2-3 days |
| 5 | Primary research outreach | 5-10 calls / customer refs / ethnographic finds | Aviv | 1-2 weeks (runs in parallel from week 1) |
| 6 | IR-vs-SEC triangulation | Documented claim gaps from last 4 transcripts vs. 10-K | AI-assisted | 0.5 day |
| 7 | Thesis synthesis + 1-paragraph compression test | Compressed thesis + thesis monitor sheet + kill criteria | Aviv | 1 day |
| 8 | Deck draft (HTML → pptx) | Final deliverable | Aviv + AI | 2-3 days |

**Total elapsed (with parallelism):** ~2.5–3 weeks from company selection to draft deck.

**Critical path:** 1 → 2 → 3 → 7 → 8. Primary research (5) runs parallel from week 1. Library (4) and triangulation (6) run parallel during model build.

---

## How This Maps to AI Usage (for the appendix)

The methodology naturally separates work where AI is high-leverage from work where AI hurts:

| Workstream | AI role | Caveat |
|---|---|---|
| Consensus dossier | High — extract from transcripts, summarize sell-side notes, scrape retail forums | Cite sources; verify quotes |
| Comparable transitions library | High — find historical comps, summarize PE press releases | Verify dates and numbers manually |
| IR-vs-SEC triangulation | Highest — LLMs excel at this | Direct quotes only; flag every gap as draft |
| Operating model | Medium — formula scaffolding, sensitivity setup | Numbers are sacred; double-check every cell |
| Mispricing diagnosis | Medium — structured prompts for each reason | Evidence requires manual verification |
| Primary research | Zero | AI cannot do this; that's why it's the moat |
| Thesis compression | Low — useful for editing, not for generating | Thesis is yours; AI should not invent perception |
| Deck draft | High — once content exists, formatting/exhibits/footnotes | Content first, render second |
