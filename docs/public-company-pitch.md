# Part 1: Public Company Investment Pitch

## Status: Screening / Company Selection

## Selection Framework

### 1. Interpreting Lunchline's Criteria

#### "Messy" — What Qualifies

In the search fund / lower-middle-market PE context, "messy" signals complexity that creates analytical opportunity. Lunchline themselves describe their philosophy as "be willing to get your hands dirty" and "it's about getting it right, not being right." They want to see you can synthesize messy inputs into a decision.

**Situations that qualify as messy (ranked by analytical richness):**

| Messiness Type | What It Looks Like | Why It's Good for a Case |
|---|---|---|
| Active strategic alternatives / M&A process | Board announced review, hired bankers, exploring options | Event-driven catalyst, clear timeline, valuation anchor |
| Management transition / CEO turnover | New leadership <12 months, founder departure, activist-forced change | Operator angle: what would YOU do differently? |
| Revenue model transition | Legacy license-to-SaaS conversion, usage-based pivot mid-stream | Shows you can model transition economics |
| Margin compression with identifiable cause | GTM overspend, failed product line, integration costs from acquisition | Value creation plan writes itself |
| Accounting restatement / auditor change | Late filings, material weakness disclosure, new auditor | Market over-punishes; you can assess if it's structural or fixable |
| Activist involvement / proxy fight | 13D filing, board seat demands, public letter | External catalyst, someone else validating thesis |
| Segment divestiture / asset stranding | Sold a division, stub trades at discount, market hasn't re-rated | Sum-of-parts arbitrage |
| Debt overhang with viable core business | High EV vs. low market cap due to debt load | Shows capital structure literacy |
| Failed M&A / broken deal | Walked away from acquisition, deal terminated, strategic partner left | Market re-prices downward; opportunity if standalone business is fine |
| Customer concentration + loss | Lost a top-3 customer, revenue cliff feared | If you can show replacement path, thesis is contrarian |

**Ideal messiness for this case:** 2-3 overlapping situations from the above list. More complexity = more room to demonstrate analytical skill and operator judgment.

#### "Mispriced" — What Mispricing Looks Like at $10M-$500M EV

At this EV range, mispricing manifests differently than in large-cap. Key patterns:

| Mispricing Signal | Quantitative Indicator | Why It Exists |
|---|---|---|
| EV below trailing revenue | EV/Revenue < 1.0x (ideally < 0.5x) | Market pricing in decline that may not materialize |
| Trading near or below net cash | EV < cash on balance sheet; or EV/Revenue << peers | No one is looking; too small for funds |
| Broken IPO / SPAC disappointment | 70%+ decline from IPO/de-SPAC price within 24 months | Retail exit, lock-up pressure, no natural buyer base |
| Fallen angel | Once traded at 5-10x current market cap | Institutional holders sold, left over-punished stub |
| Market cap vs. EV disconnect | Market cap $20M, EV $300M (debt-heavy) or Market cap $200M, EV $80M (cash-rich) | Casual screeners miss the right picture |
| Sector misclassification | Classified as "telecom" but actually SaaS; classified as "healthcare" but actually data/analytics | Wrong comp set = wrong multiples applied |
| Multiple compression vs. peers | Trading at 3x EBITDA when peers trade at 8-12x | Company-specific discount that may be temporary |
| Insider buying at lows | Officers/directors purchasing in open market, Form 4 filings | Signal that insiders see value market doesn't |

**Best mispricing for this case:** EV/Revenue disconnect (< 1x for a growing SaaS/software company) combined with identifiable reason the market is wrong. Allows a clear "the market sees X, but the reality is Y" variant perception.

#### "Under-Followed" — Quantitative Definition

| Metric | Under-Followed Threshold | Strongly Under-Followed |
|---|---|---|
| Sell-side analyst coverage | 0-3 analysts | 0-1 analysts |
| Institutional ownership | < 40% of float | < 20% of float |
| Average daily volume | < $500K/day | < $100K/day |
| Seeking Alpha articles (trailing 12mo) | < 5 articles | 0-1 articles |
| Earnings call transcript availability | Sporadic or no call | No call / no Q&A |
| 13F filings mentioning the stock | < 50 institutions | < 20 institutions |
| Google Trends interest | Negligible relative search volume | Near zero |

**Structural reasons for under-coverage at this EV:** Sell-side economics don't support covering companies where their bank will never win an advisory mandate. Institutions managing >$100M can't build meaningful positions without moving the stock. Index exclusion means passive flows bypass them entirely.

#### "Avoid Obvious Names" — What Makes Something "Obvious"

A name is "obvious" in micro/nano-cap if:
- Frequently written up on Seeking Alpha (>10 articles/year)
- Appears in popular screener default lists (Finviz "Top Gainers," etc.)
- Already a well-known turnaround story in investor Twitter/X circles
- Covered by dedicated micro-cap newsletters (MicroCapClub featured picks)
- Has been presented at major micro-cap investor conferences (LD Micro, Planet MicroCap)
- Has a widely-followed activist situation (Icahn, Starboard-level visibility)
- Appears in ETF holdings (even micro-cap ETFs like IWC)

**Test for "obvious":** If you google "[Ticker] investment thesis" and get 10+ substantive results from investment blogs/forums, it's too obvious. The ideal target returns mostly SEC filings, press releases, and maybe 1-2 obscure write-ups.

---

### 2. Candidate Selection Process

The original version of this section was a 6-criterion weighted scoring framework (Situation Complexity 20%, Value Creation 25%, Sector Fit 15%, Data 15%, Contrarianism 15%, PE Realism 10%). We ran 8 candidates through it (EXFY, SCOR, CDLX, NRDY, THRY, BZFD, AENT, plus FAST as a control) and discovered that every candidate from our pre-screened pool landed in a 2.65-2.95 band post-adversarial — the scoring layer compressed to noise *within* the pool, even though it discriminated sharply *across* archetypes (FAST 2.58 with inverse fingerprint). See `CHANGELOG.md` 2026-05-28 (late late) for the diagnostic.

**Replaced with a 2-layer filter (no Layer 3 ranking):**

**Layer 1 — Mechanical exclusion.** Reject candidates that violate the framework on their face:
- Foreign issuer (20-F regime, different disclosure depth)
- Operating margin < -100% (zombie cash burn, not a value play)
- EV/Revenue > 3x (not value-priced; framework demands < 1.5x as the messiness signal)

**Layer 2 — Structural exclusion.** Reject candidates where governance or deal status forecloses the operator-investor thesis:
- `check_voting_structure.py` → reject DEAL_BREAKER (founder super-voting majority blocks any hostile catalyst and captures all premium in friendly transactions)
- `check_deal_status.py` → reject CLOSED or DEFINITIVE target-side
- Keep MEDIUM / HIGH / EXPLORING but flag in evaluation

**No Layer 3 — fundamentals on all structural survivors.** We deliberately do NOT rank survivors by sector fit, signal density, or EV size before fundamental analysis:
- **Sector fit** is applied at the END as a tiebreaker. Filtering on it up-front means we'd reject great non-edge-zone ideas before evaluating them.
- **Signal density** (number of visible 8-K events, news catalysts) directly contradicts the "under-followed" goal. High signal density = visible catalyst = other analysts already saw it.
- **EV size floor** (e.g., "Rev > $40M for institutional credibility") directly contradicts the case's $10-500M EV mandate, which explicitly includes nano-cap.

Instead, every Layer-2 survivor gets the findings-mode pipeline (`build_findings_prompts`). The selection emerges from the *findings*: which candidate has the sharpest variant perception, the most pitchable bear case absorption, the most concrete catalyst? That's a fundamental-analysis judgment after evidence is in, not a screening shortcut.

**Tiebreaker order (applied AFTER findings are complete):**
1. **Aviv's edge fit** — primary research is realistic in gaming/AI/SaaS/data/consumer; not in industries he can't add operator value to
2. **Catalyst clarity** — does a specific, dated event force value realization within 12 months?
3. **Asymmetry of risk/reward** — is downside limited (cash floor, asset backing) while upside is 2-3x?
4. **Narrative coherence** — can the full pitch be summarized in one compelling sentence?

**Calibration scoring is still used during pipeline calibration** (see `pipeline.md` § Calibration mode). It runs ONCE per archetype to teach the system what good/bad looks like in this pool. For routine candidate evaluation, the lighter findings-mode pipeline is the standard.

---

### 3. What Makes a Great Investment Pitch (PE/Search Fund Evaluation)

#### What Separates Outstanding from Mediocre

Based on research across PE case study guides, MBA stock pitch competitions, and search fund investor expectations:

**Outstanding pitches demonstrate:**

| Element | What Great Looks Like | What Mediocre Looks Like |
|---|---|---|
| Variant perception | "The market sees X because of Y; I see Z because of specific evidence A, B, C" | "This company is cheap on multiples" (no explanation of WHY market is wrong) |
| Value creation plan | Named, sequenced operational levers with estimated impact: "Reduce churn from 18% to 12% via [specific action] = $X ARR saved" | Generic "cut costs and grow revenue" without specifics |
| Catalyst path | "Q3 2026 earnings will reveal [X] because of [Y]; strategic review concludes by [date]" | "Eventually the market will recognize the value" |
| Risk framing | "These 3 things kill the trade. Here's why #1 is mitigated, #2 is priced in, and #3 is my key monitor" | Listing risks without assessing probability, severity, or mitigation |
| Operator mindset | Thinks like someone who would RUN this business, not just own the stock | Reads like a sell-side initiation report |
| Financial model | Illuminates 2-3 key drivers; shows what has to be true for the thesis to work | 300-row DCF that obscures key assumptions |
| Conviction | Clear recommendation with target price, time horizon, and defined exit criteria | Hedged conclusion, wishy-washy "further research needed" |

#### What Lunchline Specifically Wants to See (Inferred from Their Context)

Lunchline's own philosophy ("be willing to get your hands dirty," "constantly re-underwrite," "build-up not roll-up") reveals what they'll reward:

1. **Operator-first framing:** The Value Creation Plan is the centerpiece, not an afterthought. They run businesses. Show you think like someone who would walk in Monday morning as CEO.

2. **Hands-dirty specificity:** Not "improve margins" but "renegotiate AWS contract (currently $X/mo for Y seats, market rate is Z), consolidate 3 overlapping marketing tools into HubSpot, reduce engineering headcount from 45 to 32 by sunsetting legacy product line."

3. **Lunchline formula alignment:** Their playbook is: fragmented market + operational improvement + digital transformation + talent systems. Pick a company where this playbook applies.

4. **Search fund realism:** They know you want to launch a search fund. Picking a company that looks like something you'd actually acquire (B2B services/SaaS, $5-50M revenue, fixable operations, recurring revenue) signals alignment.

5. **AI fluency as a tool, not a topic:** The prompt log appendix means they want to see you USING AI effectively in the research process, not just picking an "AI company" because it's trendy.

#### The Seven Pillars of an Institutional-Quality Pitch

1. **Variant Perception** — What do you see that the market misses? (Must be specific and evidence-backed)
2. **Thesis Clarity** — Can you state the investment thesis in one sentence, then defend it in three?
3. **Catalyst Path** — What forces the market to recognize value? When?
4. **Risk Identification** — What kills the trade? (Intellectual honesty > optimism)
5. **Model Utility** — Does your model test what matters, or just check a box?
6. **Valuation Discipline** — Is your target price grounded in defensible assumptions?
7. **Communication & Conviction** — Can you survive 10 minutes of hostile Q&A?

---

### 4. Quantitative Screening Filters

#### Primary Filters (Hard Requirements)

| Filter | Specification | Rationale |
|---|---|---|
| Exchange | NYSE or NASDAQ only | Case requirement |
| Enterprise Value | $10M - $500M | Case requirement; prefer $30M-$250M sweet spot |
| Country | US-headquartered or US-listed with significant US operations | SEC filing depth, accessibility |
| Filing status | Current on SEC filings (10-K filed within 90 days of FY end) | Need data to model; delinquent filers too risky |
| Minimum revenue | > $10M trailing twelve months | Below this, too early-stage to credibly model |
| Listing age | > 2 years public | Need financial history for trend analysis |

#### Secondary Filters (Messiness / Mispricing Signals)

| Filter | Specification | What It Captures |
|---|---|---|
| EV/Revenue | < 1.5x (ideally < 1.0x) | Revenue/valuation disconnect |
| Price decline from 52-week high | > 40% | Market punishment (fallen angel signal) |
| Price decline from all-time high | > 70% | Broken story, potential over-punishment |
| Analyst coverage | 0-3 covering analysts | Under-followed |
| Institutional ownership | < 50% of float | Not widely held; structural inefficiency |
| Recent 8-K filings | Management change, strategic alternatives, restatement, auditor change in trailing 12 months | Active "messiness" signal |
| Insider buying | Net insider purchases in trailing 6 months | Contrarian signal from people with information |
| Short interest | > 10% of float | Market betting against; creates squeeze potential if thesis is right |

#### Sector Filters — initial universe scope, not candidate-level filtering

The Finviz pull is scoped to Tech + Communication Services sectors. This is a **universe-level** scope decision (which sectors to pull from), not a candidate-level filter (which we deliberately do NOT apply per Layer 3 rationale above). Within the included sectors, we do not further discriminate by Aviv's edge fit during selection — that's a tiebreaker applied at the end.

| Universe Includes | Universe Excludes |
|---|---|
| Application Software, SaaS/Cloud, AI/ML | Oil & Gas |
| Gaming / Interactive Entertainment | Mining / Materials |
| Internet Content & Information | Biotech / Pharma |
| Advertising Agencies / Marketing Tech | Banks / Insurance |
| Publishing, Entertainment | REITs, Utilities |
| EdTech, Data Analytics | Semiconductors / Hardware (already excluded by industry filter) |

**Aviv's edge zones for the post-findings tiebreaker** (NOT applied during filtering): gaming, AI/ML, SaaS, consumer software, data/analytics, enterprise sales. Where Aviv can do primary research credibly, the pitch is stronger; where he can't, it falls back to public-data-only analysis. This matters at the tiebreaker stage, not the screening stage.

#### Data Availability Requirements

| Requirement | Minimum | Ideal |
|---|---|---|
| Consecutive 10-K filings | 3 years | 5+ years |
| Quarterly filings (10-Q) | 8 quarters | 12+ quarters |
| Earnings call transcripts | Available for most recent quarter | 8+ quarters of transcripts |
| Segment reporting | At least revenue by segment | Revenue + gross margin by segment |
| Peer company comps | 3+ public comps identifiable | 5+ comps with similar business model |
| Management proxy (DEF 14A) | Filed | Recent, with compensation detail |

#### Liquidity / Practicality Requirements

| Metric | Minimum | Notes |
|---|---|---|
| Average daily dollar volume | > $50K/day | Below this, data may be stale/unreliable |
| Market cap | > $15M | Below this, likely compliance issues or shell risk |
| Float | > 30% of shares outstanding | Need enough float for price to be market-determined |
| SEC filing currency | Current or < 30 days late | Delinquent filers = too much uncertainty |

---

## Selection Process (Summary)

**Hard requirements (Layer 1 — case mandate + framework hygiene):**
1. NYSE or Nasdaq listed
2. Enterprise Value $10M-$500M (per case brief; no internal sweet-spot bias)
3. US-headquartered (US filing regime)
4. Operating margin > -100% (zombie cash burn excluded)
5. EV/Revenue < 3x (value-priced)
6. Universe scope: Tech + Communication Services sectors (where Aviv can credibly think about businesses)

**Structural exclusion (Layer 2 — automated filters):**
7. `check_voting_structure.py` ≠ DEAL_BREAKER (no founder super-voting majority)
8. `check_deal_status.py` ≠ CLOSED or DEFINITIVE target-side

**Evaluation (no Layer 3 filtering):**
9. Run findings-mode pipeline on every Layer-2 survivor — lever findings + mispricing diagnosis + IR-vs-SEC triangulation + adversarial review
10. Selection emerges from the *findings*: variant perception clarity, bear case absorption, catalyst concreteness — fundamental analysis, not screening shortcut

**Tiebreaker (only if multiple candidates tie on fundamentals):**
11. Aviv's edge fit (primary research is realistic in gaming/AI/SaaS/data/consumer)
12. Catalyst within 12 months that forces value recognition
13. Asymmetry of risk/reward (cash floor, 2-3x upside)
14. Narrative coherence (one-sentence thesis)

## Top Candidates

The pre-framework manual scoring (DOMO 4.35, LPSN 4.25, DH 4.00, MCHX 3.70, EGAN 3.00, MNDO 2.20) is **superseded** and not reproduced here. Several of those candidates have since failed structural filters (LPSN closed in SoundHound deal; DOMO/BBGI/SKLZ founder-controlled DEAL_BREAKERs) or scored differently under the v2 multi-agent pipeline (EXFY 2.65, SCOR 2.85 — both below 3.0 viability threshold).

**Current candidate slate and pitch tournament queue:** see [TODO.md § Pitch Tournament](../TODO.md).

**v2 scoring pipeline:** see [pipeline.md](pipeline.md).

## Selected Company
**TBD** — pending pitch tournament outcome

## Deliverables

- **Analytical workstreams** (post-selection): see [methodology.md § Sequenced Analytical Workstream](methodology.md).
- **Deck artifacts** (slide-by-slide scaffolds): see [deck-structure.md](deck-structure.md).
- **Critical path:** Selection → Mispricing diagnosis → Consensus dossier → Operating model → Thesis synthesis → Deck. Primary research, comp library, and IR-vs-SEC triangulation run parallel.
