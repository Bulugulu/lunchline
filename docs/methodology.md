# Analytical Methodology

Distilled from the exemplar decks identified in [deck-structure.md](deck-structure.md). These are the analytical disciplines that separate institutional-quality pitches (Trian, Pershing Square, Starboard, PSC winners, search fund acquirers) from McKinsey-flavored repackaging. They directly inform our workstream sequencing and AI usage.

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
