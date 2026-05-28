# Part 1 Deck — Structure & Format

**Status:** Structure + design research complete. Awaiting (a) company selection and (b) design direction pick.

## Authoring Pipeline

| Stage | Format | Tooling |
|---|---|---|
| Drafting / iteration | HTML + CSS (per-slide pages, 16:9 fixed dimensions) | Hand-authored; preview in browser |
| Final output | `.pptx` | `python-pptx` build script that reads slide content from structured source (HTML or JSON) and writes PowerPoint |
| Backup deliverable | PDF | Export from PPTX (Lunchline accepts PDF copies) |

**Why HTML for drafting:** Faster visual iteration, real text reflow, easy version control, low cost to throw away. PowerPoint editing is slow and the file format is opaque to diffs.

**Why python-pptx for final:** Lunchline brief specifies PowerPoint. python-pptx gives reproducible builds, the Excel returns model can populate slide tables/charts directly, and we can regenerate the deck without manual re-formatting.

**Open question:** Bare HTML/CSS vs. Marp vs. Reveal.js for drafting framework. Decide after design system is picked.

---

## Cross-Cutting Principles (from research)

These apply to every slide and override any section-specific guidance:

1. **Takeaway headlines, not topic labels.** "End Market Overview" is a topic. "$8B TAM growing 12% with no scaled player above 15% share" is a thesis. Every page answers "so what?" in the title bar; the body is the proof. Pershing, Trian, and PSC winners all do this.
2. **Every number has a source.** Footnotes at the bottom of the page with specific URLs/dates. "Company filings" is not a citation.
3. **Variant perception structure** — Steinhardt's "Market sees X. We see Y because Z." This is what separates an investment pitch from a sell-side note.
4. **Operator/controlling-owner framing** — for a public small-cap we don't control, the move is: "Were we a controlling owner, here's the VCP; here's why a credible activist or new management gets some of this from a minority position." This is the angle Lunchline is explicitly testing.
5. **Density discipline** — Pershing slides can have 200+ words but in one column with generous leading. Consulting decks are sparse but use 6+ visual elements per page (icons, gradients, sidebars). That visual noise is the tell. Aim for institutional density, not consulting visual layering.

---

## Slide Structure (from [case-overview.md](case-overview.md))

Total: 10-12 pages + 1-page AI appendix.

### Slide 1-3: Business Overview (2-3 pages)
**Purpose:** What the company does, how it makes money, who buys, where it operates, how it got here.

**Per-slide scaffold:**
- **Page 1 — "Company at a Glance" dashboard:** TTM revenue, EBITDA, EV, segment mix, geo mix, customer concentration, 5-yr KPI history. Single visual layout, no narrative bullets.
- **Page 2 — "How the business actually makes money":** Unit economics, revenue model, contract structure or customer cohorts.
- **Page 3 (optional) — Strategic timeline:** Use ONLY if a recent inflection (spin, new CEO, acquisition, restatement) is core to the messiness thesis. Otherwise skip.

**Anti-patterns:** Company-history narrative ("Founded in 1987 in Houston..."); logo wall as substitute for concentration data; segment descriptions copied from the 10-K; missing unit economics.

**Exemplars:** Trian's Disney white paper pp. 8–22; Pershing Square Howard Hughes 2025 proposal; PSC 2024 Valvoline winner.

---

### Slide 4: End Market Overview (1 page)
**Purpose:** TAM, growth, structure, fragmentation, secular drivers — all in ONE page.

**Per-slide scaffold:**
- Takeaway headline (full sentence)
- TAM/SAM with **named source** (not Gartner-pie-chart-no-source)
- Growth driver **decomposed** into 2-3 secular tailwinds, each with cited data
- Market structure (concentration / fragmentation) showing where the company sits
- "What's changing NOW" callout — the reason this market matters today
- Exhibit: fragmentation chart or growth decomposition (NOT McKinsey market map you didn't build)

**Anti-patterns:** TAM with no source; "growing X% CAGR" without decomposition; market description with no link to the company's specific exposure.

**Exemplars:** Starboard Salesforce / Autodesk decks (Oct 2024) — single-page market structure with quantified concentration.

---

### Slide 5: Competitive Positioning & Dynamics (1 page)
**Purpose:** Who wins, who loses, why — over the next 5 years.

**Per-slide scaffold:**
- Takeaway headline = "why this company wins the next 5 years" claim
- Positioning grid with **named competitors** (not "Tier 1 / Tier 2")
- ONE quantified moat metric (gross margin spread, NPS, retention, switching cost in $)
- "Why incumbents can't / won't / haven't" — 3 specifics
- Source footer

**Anti-patterns:** Porter's five forces spider chart; "we are the leader" without share data; checkmark-vs-X feature grid (that's a sales deck); competitor logos with no axes.

**Exemplars:** Pershing Chipotle and Howard Hughes one-page comp dashboards; Sohn Idea Contest winners (forced compression).

---

### Slide 6-7: Investment Thesis (1-2 pages)
**Purpose:** The variant perception, made explicit.

**Per-slide scaffold:**
- Headline = the one-sentence thesis
- **"Market sees X. We see Y because Z."** template, written out
- 3 thesis pillars MAX, each = one-sentence claim + 2-3 bullets of proof
- **"What we expect vs. consensus" mini-table** — your '27 EBITDA vs. street '27 EBITDA, your multiple vs. current, implied IRR
- Why the mispricing exists (no coverage / optical complexity / recent disappointment) — this maps directly to Lunchline's "messy, mispriced, under-followed"

**Anti-patterns:** Five-bullet "investment highlights" that read like an IR deck; "high-quality business at attractive valuation" with no quantified gap to consensus; missing the *why* mispriced.

**Exemplars:** PSC 2019 Hertz winner; PSC 2026 DoorDash winner. VIC's published rule: ideas must have "variant perception that couldn't have been written by a sell-sider."

---

### Slide 8: Investment Risks (1 page)
**Purpose:** The 3 things that kill the trade — with mitigation/kill-criteria framing.

**Per-slide scaffold:**
- Risk **table**, 3 columns: Risk | Why we don't think it breaks the thesis (mitigant) | What would change our mind (kill criteria)
- Sort by probability × severity, lead with the most likely to derail
- Quantify where possible: "if EBITDA margin compresses 200bps, IRR falls from 22% to 11%"

**Anti-patterns:** "Macro / execution / regulatory risk" as one-word bullets; risks without mitigants (reads like 10-K Item 1A); boilerplate risks that don't apply.

**Exemplars:** Trian Disney white paper appendix; Pershing Valeant 2014 deck is a famous *negative* example showing why kill-criteria matter.

---

### Slide 9-11: Value Creation Plan (2-3 pages) — THE CENTERPIECE

**Purpose:** Where the deck wins or loses for Lunchline. Three layers must be visible:

**Per-slide scaffold:**

1. **Value bridge waterfall** — current EV → target EV showing contribution of each lever (revenue growth +$X, margin expansion +$Y, multiple re-rating +$Z, capital return +$W). This is the single most important visual in a PE/search deck.
2. **2-4 named levers with owner-operator moves.** Not "improve margins." Instead: "consolidate 3 ERP instances → SG&A from 18% to 14% by Y2, worth ~$22M run-rate EBITDA, evidence: comparable PE-owned peer X did this in 18 months."
3. **Sequencing timeline** — first 100 days / Year 1 / Year 2-3 / exit. Use PE language ("value creation plan") not consulting language ("operating roadmap" is fine; "align stakeholders, build dashboards" is not).

**Lunchline-specific framing:** "Were we a controlling owner, here's the VCP. From a minority position, here's why a credible activist / new management / capital return policy gets some of this." This bridges search-fund operator and public-equity investor — the angle Lunchline is testing.

**Naming:** Name your VCP. Trian named theirs "Restore the Magic." It frames the whole pitch.

**Anti-patterns:** Generic "cost-cut, grow, re-rate" bullets with no quantified bridge; consultant 2x2 of "value drivers"; first-100-days that reads like a McKinsey kickoff agenda; levers with no proof point from a comparable situation.

**Exemplars:** Trian "Restore the Magic" Disney white paper; Starboard Macy's (Jan 2016) and Darden; Stanford GSB Search Fund Primer; IESE "First 100 Days: A Search Fund Launches"; AlixPartners "Speed to value — the first 100 days."

---

### Slide 12: Financial Review (1-2 pages)
**Purpose:** Historicals → forward model → valuation → returns sensitivity, all reconciled to the VCP.

**Per-slide scaffold:**
- Historical P&L + segment EBITDA (5 yrs)
- Forward model (3-5 yrs) with **explicit assumptions tied to VCP levers** from Section 6
- **Base/Bull/Bear scenario bar chart**, each tied to specific operating outcomes (not just multiple compression)
- Implied price vs. today with IRR and MOIC
- Valuation framework: peer comp set + EV/Rev or EV/EBITDA range, DCF as cross-check (not primary)
- Source: Excel returns model

**Anti-patterns:** DCF as primary with 20 unaudited input cells; "12x because peers trade at 12x"; sensitivity tables with no story; forward model that doesn't reconcile to the VCP bridge.

**Exemplars:** Pershing Square Annual Investor Presentations (scenario-driven valuation); Stanford 2024 Search Fund Study (IRR/MOIC convention).

---

### Appendix: AI Disclosure (1 page)
- Tools used
- Prompts that worked
- Where AI helped or hurt
- Source: [docs/prompt-log.md](prompt-log.md)

---

## Design System — LOCKED: Direction 1 (Institutional Classic)

Picked 2026-05-28 after reviewing HTML mockups at `mockups/d1.html`. Directions 2 and 3 documented below for reference but not selected.

### ✅ Direction 1 — "Institutional Classic" (Pershing Square / Trian) — SELECTED

Reads like a $10B activist firm published it. Confident, dense, headline-driven.

| Dimension | Spec |
|---|---|
| Headline + body font | Neue Haas Grotesk (or free: **Inter**), one family, 3 weights (400/500/700) |
| Sizing | Headlines 24-28pt Medium; body 11pt Regular; footnotes 8pt |
| Color | Navy `#0A2540` · Ink `#111111` · Paper `#FFFFFF` · Slate `#6B7280` · Accent red `#C8102E` (thesis emphasis only) |
| Layout | 12-col grid, headline top-left full sentence, thin rule + page number footer |
| Density | High — one chart + 80-150 words per page; ~30% white space |
| Best for | Activist-flavored "things must change here" thesis. Weakest if pitch is pro-management. |
| Exemplars | [Pershing Square 2025 Annual Presentation](https://assets.pershingsquareholdings.com/2025/03/03171547/2025-Annual-Investor-Presentation_PSH_vDF.pdf) · [Trian P&G White Paper](https://trianpartners.com/wp-content/uploads/2017/01/Trian-PG-White-Paper-9.6.17-1.pdf) |

### Direction 2 — "Modern Operator" (Stripe-meets-Greenlight) — RECOMMENDED

Built for the operator-investor persona Lunchline is hiring for. Signals "I built things, I understand product" without abandoning institutional discipline. Strongest fit for "build-up not roll-up" / "get your hands dirty" voice.

| Dimension | Spec |
|---|---|
| Headline font | **Söhne** or **Inter Display** Bold/Semibold |
| Body (prose) | **Tiempos Text** or free: **Source Serif 4** — serif signals "read this carefully" |
| Body (data/tables) | **Inter** Tabular figures |
| Color | Ink `#0F1115` · Bone `#F5F2EC` (warmer than white — reads as paper) · Graphite `#3A3F47` · ONE accent: Operator Orange `#D9531E` *or* Forest `#1F4D3F` |
| Layout | 6-col asymmetric grid, 1.5x leading, generous 1in+ margins, sidebar column for footnotes and "management says vs. filings say" pull-quotes |
| Density | Medium — 2 visual elements max per page |
| Best for | Operator-investor pitches with a product or unit-economics insight. Best signal-to-noise for Lunchline brief. |
| Exemplars | Stripe Annual Letter; [Greenlight "Field of Schemes"](https://www.greenlightcapital.com/Download.aspx?ID=d46126e3-3ffa-44ae-930c-152f5d65c4c5) |

### Direction 3 — "Search Fund Minimal" (IESE / GSB primer aesthetic)

Reads as a search-fund investment memo, not a hedge-fund pitch. Maximum restraint, maximum specificity. The deck disappears so the analysis speaks. **Highest ceiling, highest risk** — no design to hide behind if the analysis is thin.

| Dimension | Spec |
|---|---|
| Font | Single family — **IBM Plex Sans** (free) or **GT America**, two weights (Regular/Medium) |
| Numbers | **IBM Plex Mono** for all tables — the mono treatment is the personality |
| Color | Black `#000000` · White `#FFFFFF` · Mid-gray `#888888` · Optional muted blue `#2D5A87` accent (<5% surface area) |
| Layout | 6-col grid, thin 1px hairline rules between sections, ~50% white space, ONE chart or table per page max |
| Density | Low — maximum restraint |
| Best for | Small, undercovered company where the thesis hinges on specific numbers that need to breathe. Matches Lunchline's "specificity over polish" most literally. |
| Exemplars | [Stanford GSB Search Fund Primer](https://www.gsb.stanford.edu/experience/about/centers-institutes/ces/research/search-funds) · IESE International Search Fund Center materials · Berkshire Hathaway annual letters (body voice) |

### Why Direction 1 was chosen

- Confident, headline-driven, density matches the activist/PE canon the Lunchline brief is steeped in
- Single-family typography (Inter) keeps the stack simple — fewer font-loading risks at pptx export
- Navy + red accent is a known-quantity institutional palette
- Reference exemplars (Pershing 2025, Trian P&G) are public and easy to cross-reference for fidelity checks

---

## Top Exemplar Decks to Study This Week

1. **Trian "Restore the Magic" (Disney) white paper** — best single source for headlines, VCP bridge, risk table. [SEC link](https://www.sec.gov/Archives/edgar/data/0001345471/000090266423000183/p23-0016_exhibit1.pdf)
2. **PSC 2024 Valvoline winner** — closest format match (MBA, 10-12 pages, public small/mid-cap with operator angle).
3. **PSC 2019 Hertz winner** — exemplary variant-perception framing. [SumZero](https://sumzero.com/headlines/automobile_and_transportation/HTZ/170-this-pitch-on-hertz-just-won-100k-at-the-pershing-square-challenge)
4. **Starboard Value deck library** — best for one-page market + competitive positioning. [10xebitda.com](https://www.10xebitda.com/hedge-fund-presentations/)
5. **Stanford GSB Search Fund Primer + IESE "First 100 Days"** — the VCP language and structure Lunchline is steeped in. [IESE PDF](https://www.iese.edu/media/research/pdfs/OP-0269-E.pdf)

## Other Source Library

- [Pershing Square deck index](https://www.slidebook.io/company/pershing-square/)
- [Pershing Square 2026 Annual Presentation](https://assets.pershingsquareholdings.com/wp-content/uploads/2026/02/11144917/2026-Annual-Investor-Presentation.pdf)
- [Pershing Square Howard Hughes 2025 proposal](https://assets.pershingsquareholdings.com/2025/01/13060332/HHH-Proposal-Letter.pdf)
- [Trian white papers index](https://trianpartners.com/white-papers/)
- [Trian GE White Paper (2015)](https://www.conference-board.org/retrievefile.cfm?filename=Panel-II---Trian-White-Paper-GE.pdf&type=subsite)
- [Hindenburg Research reports](https://hindenburgresearch.com/)
- [Sohn Idea Contest presentations](https://www.sohnconference.org/contest-presentations)
- [PSC 2026 winner recap (DoorDash)](https://www.yetanothervalueblog.com/p/pershing-square-challenge-2026-winners)
- [PSC 2026 runner-up recap (Baker Hughes)](https://www.yetanothervalueblog.com/p/pershing-square-challenge-2026-runner)
- [AlixPartners "Speed to Value"](https://www.alixpartners.com/insights/102iwgp/speed-to-valuethe-first-100-days/)
- [Berkshire Hathaway letters](https://www.berkshirehathaway.com/letters/letters.html)

---

## Open Decisions

1. ✅ ~~Design direction~~ — **LOCKED: Direction 1 (Institutional Classic)**
2. **HTML drafting framework** — bare HTML/CSS (current mockup approach) vs. Marp vs. Reveal.js. Current bare HTML works; defer.
3. **python-pptx template** — build from scratch vs. start from a designed PPTX master matching D1
4. **Chart library** — matplotlib (static, exports clean to PPTX) vs. native python-pptx charts (limited but native)
5. **Citation style** — inline superscripts vs. footer block vs. endnote slide
6. **Company selection** — BLOCKING; deck content cannot be drafted until picked
7. **VCP name** — once company is picked, name the VCP ("Restore the Magic" pattern)
