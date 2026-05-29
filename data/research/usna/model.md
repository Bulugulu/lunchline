# USANA Health Sciences (USNA) — Full Post-Vetting Valuation Model

**Date:** 2026-05-29 · **Version:** v2 (reviewer iteration) · **Price:** $18.53 · **Shares:** 18.46M · **Market cap:** ~$342M
**Status of shallow read:** "value trap" (melting China MLM, accelerating customer loss, Hiya loss-making, no catalyst)
**Purpose of this doc:** run the deep flow honestly and let the model decide whether rigor flips the verdict.

> **v2 changelog (what the reviewer pushed and what moved):**
> - **A1 TAX — reviewer was right, v1 was too optimistic.** The 72.4% rate is **mostly structural cash drag, not a non-cash artifact.** Reworked off actual *cash taxes paid* and the *domestic/foreign pretax split*. Base cash-tax assumption raised; base FV revised **down**.
> - **A2 HIYA — partially revised.** The −13%/−17% YoY is largely a *deliberate D2C→retail channel pivot* (Meta-CAC pullback), filing-supported, but I trimmed the base multiple 1.6x→1.5x and added an EBITDA-mechanic cross-check.
> - **A3 CORE TERMINAL — rebuilt with the revenue/customer bridge.** Rising spend-per-customer (+7.6% blended) is real and offsets ~half the −15% attrition, but it is not perpetual; terminal decline widened from −1.5% to a −2% to −2.5% base with explicit justification.
> - **New base case: SOTP $24.82, consolidated DCF $20.74, prob-weighted 3-yr FV ~$25, IRR ~+9–10%/yr** (was v1 $26.42 / +12%). The thesis survives but is more sober, and the bear is materially worse.
> - Added **Part B operating/driver model + tornado** and **Part C Porter's** below.

> **First, a data-integrity fix.** The layer-2 triage KILLED USNA on "deal CLOSED." That is a **false positive.** The Dec-23-2024 8-K "Agreement and Plan of Merger" that tripped the screen is the **Hiya acquisition** (USANA *buying* 78.85% of Hiya, funded partly off its credit line and an escrow), **not** a take-private of USANA. USNA is still public, filed a Q1 FY26 10-Q dated 2026-04-04, and trades at $18.53. The deep flow is warranted.
> *Source: [FY25 10-K Note B](../../dossiers/usna/edgar/filings/2026-03-16_10-K_0000896264-26-000021.htm); deal_status.json snippet "At the closing of the Merger, USANA deposited a portion of such consideration in escrow."*

---

## 0. Verified facts (rebuilt from filings, not vendor aggregates)

All from the FY25 10-K (period end 2026-01-03) and Q1 FY26 10-Q (period end 2026-04-04) in `data/dossiers/usna/`.

| Item | Value | Source |
|---|---|---|
| Consolidated revenue FY23 / FY24 / FY25 | $921.0M / $854.5M / $925.3M | 10-K XBRL `RevenueFromContractWithCustomerExcludingAssessedTax` |
| Net income to USANA FY23/24/25 | $63.8M / $42.0M / $10.8M | 10-K |
| Operating income FY23/24/25 | $93.1M / $66.3M / $37.4M | 10-K |
| Cash & equiv (Q1 FY26) | $162.8M | Q1 10-Q `CashAndCashEquivalentsAtCarryingValue` |
| Line of credit drawn (Q1 FY26) | $14.0M | Q1 10-Q balance sheet |
| Financial debt (ex-leases) | $14.0M LOC only; **no term debt** | 10-K |
| **Net financial cash** | **$148.8M** (cash $162.8M − $14.0M LOC). Gross cash $162.8M. | derived |
| Enterprise value | mkt cap $342M − net cash $148.8M ≈ **$193M** | derived |
| Core active customers (Jan-3-2026) | **387,000**, down 14.8% YoY; was 490,000 at Dec-2022 | 10-K MD&A |
| Greater China customers | 208,000 = **53.8%** of base, −15.4% YoY | 10-K |
| FY25 segment EBIT — **Core** | rev $775.5M, **EBIT +$40.5M** (5.2% margin) | 10-K Note M |
| FY25 segment EBIT — **Hiya** | rev $132.0M, **EBIT +$3.4M** *after* $18.2M intangible amort → **pre-amort ~$21.6M (~16%)** | 10-K Note M |
| FY25 segment EBIT — **Other/Rise** | rev $17.8M, **−$6.5M** | 10-K Note M |
| Q1 FY26 segment EBIT — Core / Hiya / Rise | $18.2M (+8.9%) / −$2.6M / −$1.8M | Q1 10-Q segment note |
| Hiya monthly subscribers | **186,000** (Q1 FY26) vs **224,000** (Q1 FY25), **−17% YoY** | Q1 10-Q |
| Hiya revenue Q1 FY26 | $32.2M, **−13.3% YoY** | Q1 10-Q |
| FY25 OCF / capex / FCF | $22.3M / $13.8M / **~$8.5M** | 10-K cash-flow stmt |
| Effective tax rate FY25 / FY26 guide | **72.4%** / **55–60%** | 10-K tax note; Q4'25 call |
| Buybacks FY25 / authorization left | $27.5M / ~$34.0M | 10-K |
| Redeemable NCI (the 21.15% of Hiya) | $53.2M carrying | 10-K Note O |
| Shares out: FY24 / FY25 / now | 19.06M / 18.28M / ~18.46M | 10-K |
| Hiya purchase (Dec-2024) | **$206.1M cash for 78.85%** → implied 100% EV **~$261M** (~1.6x rev); NCI fair-valued $54.2M | 10-K Note B |
| Hiya put/call | 21.15% puttable from **Apr-2028**, priced on **Hiya Adjusted EBITDA × reference multiple** | 10-K Note O |
| Ownership | Gull Global (Wentz family) ~40.1%; **single share class, one-vote-per-share** | DEF 14A / voting_structure.json |
| Coverage | **One** analyst (DA Davidson, Neutral, **$39 PT**) | analyst.json |

**Two facts the shallow read got wrong:**
1. **"Hiya is loss-making"** — false at the segment level. Hiya posted **+$3.4M operating earnings in FY25** even after eating $18.2M of purchase-accounting amortization. On a cash/pre-amort basis Hiya did **~$21.6M EBITDA (~16% margin)** on $132M revenue. The Q1 FY26 −$2.6M is a seasonally heavy launch quarter (UK/Canada/Target go-live + Meta CAC inflation), not the run-rate.
2. **"Hiya growing 30–50%"** — also currently false. Subscribers fell 224k→186k and revenue −13% YoY in Q1 FY26 as Hiya transitions from pure Meta-driven D2C to retail. **Both the bull and the bear were sloppy about Hiya.** The honest read: Hiya is a mid-teens-EBITDA-margin D2C brand in a messy channel-mix transition, not a clean 40% compounder and not a cash incinerator.

---

## A. Resolved load-bearing assumptions (reviewer iteration)

### A1. TAX — RESOLVED: the high rate is mostly STRUCTURAL CASH DRAG, not a non-cash artifact. v1 was wrong.

The decisive evidence is the **domestic/foreign pretax split** and **actual cash taxes paid** (both cited from the FY25 10-K Note E / cash-flow statement; not estimated):

| ($M) | FY23 | FY24 | FY25 | Source |
|---|---|---|---|---|
| **US** pretax income | **(20.0)** | **(35.3)** | **(56.2)** | 10-K "United States $(56,248)…" |
| **Foreign** pretax income | 122.4 | 111.6 | 97.8 | 10-K "Foreign 97,775…" |
| Consolidated pretax | 102.5 | 76.4 | 41.5 | 10-K |
| **Cash income taxes paid** | **44.2** | **40.5** | **37.2** | cash-flow `IncomeTaxesPaid(Net)` |
| Current tax expense | 41.3 | 41.0 | 37.2 | 10-K — of which **foreign** | 40.9 / 40.7 / **36.3**; **US federal = $0** |
| Deferred (non-cash) | (2.7) | (6.7) | (7.1) | 10-K |
| Valuation-allowance change (non-cash) | +19.1 | +19.4 | **+22.0** | 10-K |
| **Implied CASH tax rate** (cash paid ÷ consolidated pretax) | **43.2%** | **53.0%** | **89.5%** | derived |

**Decomposition — what is actually going on:**
- The business earns **all** its profit abroad (~$98M foreign) and **loses money in the US** (−$56M, and the US loss is *growing*). USANA pays **~$36–46M of cash tax every year on the foreign profit** (~37% effective on the foreign base — China statutory + 20% withholding on repatriation).
- The growing US losses are **unbenefited**: they are absorbed by the rising valuation allowance (+$22M FY25, non-cash) and do not generate usable foreign tax credits (FTC limitation). So the US loss **does not shield** the foreign cash tax.
- Therefore the *cash* tax is a **near-fixed ~$36–40M dollar charge** that barely moves with consolidated pretax. As consolidated pretax collapsed $102M→$41M, the cash rate mechanically exploded 43%→**89%**. **This is structural and gets WORSE, not better, if US losses keep growing.**
- The +$22M valuation-allowance swing *is* non-cash (my v1 point), but it is a small part of the story; the dominant driver is the structural mismatch the reviewer flagged. **v1's "42% cash tax / artifact" framing is retracted.**

**Defensible go-forward assumption:** model the tax as the **structural fixed-dollar foreign cash charge (~$36–40M/yr)**, not a percentage of a shrinking pretax. Management's 55–60% *book* guide is consistent with this; on a *cash* basis the dollar charge is ~$36–40M. In the segment-level Core DCF I apply a **45% cash tax on Core EBIT** (foreign ~37% + leakage from unbenefited US overhead); in the consolidated DCF I model the **fixed ~$36M foreign charge directly** (which is harsher — see §2). **The single most important consequence: in the bear case, a near-fixed $33–36M tax on a shrinking EBIT crushes FCF to near zero.** Tax is correctly a top-3 risk.

### A2. HIYA — JUSTIFIED-then-TRIMMED: the YoY decline is mostly a deliberate channel pivot, but I de-rate the stale transaction multiple.

**Is it demand erosion or a deliberate D2C→retail transition?** The filings + transcripts say **mostly the latter** (all transcript-cited):
- Hiya grew **+26% YTD through Q3 FY25** and management "continue[d] to expect Hiya to generate double-digit sales growth for the full 2025" — FY25 landed at **$132.0M** (10-K), a record year. The decline is a *recent-quarters* phenomenon, not a year.
- On the Q3 FY25 call, asked directly why active customers declined: *"we're very confident with Hiya. We've had some slowdowns… typically their business is all DTC and they do a lot [in summer]"* (Walter Noot) — i.e., **seasonality + a deliberate pullback on Meta-driven D2C acquisition** as Meta CAC inflated (named explicitly in Q1 FY26 call: *"the higher short-term cost of acquiring a customer… on a year-over-year comparison"*).
- The pivot is **funded and real:** Q1 FY26 inventory build "reflects channel expansion, including distribution into **Target**, international expansion into **Canada and the United Kingdom**, and… **manufacturing Hiya products in-house**" (margin lever). Disney licensing partnership launched Q2 FY25.

**Retail traction (quantified, transcript-cited):** Target — on shelf ~2 weeks at Q1 FY26 print, "most Target stores put **end caps** in place" (too early for velocity). Canada — "exceeded the initial targets." UK — ~5 weeks in, slow start (new market, Meta-advertised). The honest read: **retail is early and unproven on velocity/reorder**, so I do *not* give it full credit.

**Mark:** I move the **base multiple 1.6x → 1.5x revenue** (the transaction is 17 months stale and pre-dates the soft quarters; I haircut it modestly rather than collapse it). Cross-checked against the **put/call EBITDA mechanic** (21.15% repriced on Hiya Adjusted EBITDA × reference multiple, puttable Apr-2028): ~$20–22M pre-amort EBITDA × 8–12x = $160–288M EV, i.e., $126–227M stake — the revenue-multiple range sits inside the EBITDA range. **Revised Hiya stake: bear $99M (1.0x) / base $154M (1.5x) / bull $221M (2.0x).**

### A3. CORE TERMINAL — RECONCILED via the revenue-per-customer bridge. Terminal decline widened.

The tension: how can a perpetual −2% terminal be consistent with −15% customer attrition? Answer: **rising spend-per-customer is offsetting roughly half the attrition — but that lever is finite.** The bridge (10-K MD&A, customers in thousands; rev/cust = segment net sales ÷ customers; *derived*):

| Region | FY25 customers | FY24 customers | Δ cust | FY25 rev/cust | FY24 rev/cust | Δ rev/cust |
|---|---|---|---|---|---|---|
| Greater China | 208k (53.8%) | 246k | **−15.4%** | $2,041 | $1,862 | **+9.6%** |
| SE Asia Pacific | 63k | 77k | −18.2% | $2,095 | $1,906 | **+9.9%** |
| North Asia | 35k | 38k | −7.9% | $2,018 | $2,058 | −2.0% |
| Americas+Europe (core) | 81k | 93k | −12.9% | $1,831 | $1,751 | +4.6% |
| **Total Core** | **387k** | **454k** | **−14.8%** | **$2,004** | **$1,863** | **+7.6%** |

**Read:** Core net sales fell only −8.3% (FY24→FY25) despite −14.8% customers because **blended spend/customer rose +7.6%** (and a 53rd week added ~+2%). So the math is: ~−15% volume + ~+8% price/mix = ~−8% revenue. **This is the classic late-MLM signature — a shrinking base of higher-spending loyalists.** It is *not* sustainable indefinitely: you cannot raise spend/customer ~8–10%/yr forever against a shrinking, aging distributor base; eventually mix-up exhausts and revenue decline converges toward the customer-decline rate.

**Justified terminal:** I model Core revenue declining ~−7% near-term fading toward **−2% to −2.5% terminal** (v1 used −1.5% — too generous). Rationale: the spend/customer offset persists 3–5 years (loyalist base, China stable per Q1 FY26 China rev −0.4% cc), then decays so terminal decline widens toward the −3% to −5% structural attrition net of a residual ~+2% price. Greater China — 54% of the base and the swing factor — showed customers −7.6% but rev −0.4% cc in Q1 FY26, i.e., stabilizing faster than the −15% FY25 headline. **Core value is highly sensitive here; the −2% to −2.5% terminal is a judgment, flagged as an estimate, and stress-tested in the §B grid (a −5% terminal is a real bear).**

---

## 1. Sum-of-the-Parts (the centerpiece) — REVISED v2

### 1a. Hiya stake
100% Hiya EV = revenue × multiple; USANA owns 78.85%. The redeemable NCI **is** the other 21.15%, so taking 78.85% of EV already nets it out — no further subtraction.

| Scenario | Hiya rev | Multiple | 100% EV | **78.85% stake** | Rationale |
|---|---|---|---|---|---|
| Bear | $125M | 1.0x | $125M | **$99M** | demand-erosion read; penalize the subscriber/revenue decline as structural |
| **Base** | $130M | **1.5x** | $195M | **$154M** | Dec-2024 transaction (1.6x) haircut for the soft quarters / 17-month staleness |
| Bull | $140M | 2.0x | $280M | **$221M** | retail (Target/Costco/UK/Canada) re-accelerates; still below Nutrafol/Olly D2C-VMS deal comps |

EBITDA cross-check (the put/call mechanic): 21.15% reprices on **Hiya Adjusted EBITDA × reference multiple**. ~$20–22M pre-amort EBITDA × 8/10/12x = $160/$216/$288M EV → $126/$170/$227M stake. The revenue-multiple range sits **inside** the EBITDA range — the two methods corroborate.

### 1b. Core Nutritional — DCF of a declining-but-cash-generative MLM (REVISED: structural cash tax + wider terminal)
Per **A1**, Core EBIT is taxed at a **45% cash rate** (foreign ~37% + unbenefited-US leakage), not v1's 42%. Per **A3**, terminal decline widened to **−2% to −2.5%** (was −1.5%). Core EBIT margin recovers modestly to ~5.5–6.5% as FY25's ~$13M one-time cost-realignment/impairment rolls off. D&A ~$13.5M, capex ~$12M.

| Scenario | Decline path (yr1-5) | Margin | Cash tax | WACC | Terminal | **Core EV** |
|---|---|---|---|---|---|---|
| Bear | −10→−5% | 4.5% | 50% | 13.0% | −2% | **~$82M** |
| **Base** | −7→−2.5% | 5.5% | 45% | 11.5% | −1.5→−2% | **~$146M** |
| Bull | −4→0% | 6.5% | 40% | 10.0% | −0.5% | **~$261M** |

Peer sanity check (peer_notes.md): Core EBITDA ~$54M. Bear $82M = **1.5x EBITDA** (below NUS 3.0x). Base $146M = **2.7x** (≈NUS). Bull $261M = **4.8x** (≈HLF). Still conservative vs the declining-MLM comp band — appropriately so given the structural tax.

### 1c. Rise
Loss-making (−$1.8M Q1) but scaling (Costco weekly reorders, 500 Walmart stores, 9 more US retailers signed, $13.7M Q1 = ~$55M annualizing). Value: **$0 bear / $10M base / $35M bull** (base ≈ 0.2x run-rate; option value only).

### 1d. SOTP roll-up (REVISED v2)

| | Hiya stake | Core | Rise | Net cash | **Equity value** | **$/share** | vs $18.53 |
|---|---|---|---|---|---|---|---|
| Bear | $99M | $82M | $0 | $148.8M | $329M | **$17.81** | −4% |
| **Base** | $154M | $146M | $10M | $148.8M | $458M | **$24.82** | **+34%** |
| Bull | $221M | $261M | $35M | $148.8M | $666M | **$36.06** | +95% |

### 1e. **Is the Core implied free or negative?** (the thesis the shallow read missed — still holds)
Reverse the SOTP — strip net cash and the Hiya stake out of today's market cap:

| Hiya valued at… | Market cap − net cash − Hiya stake (− Rise) = **Implied Core** | Implied Core EV/EBITDA |
|---|---|---|
| 1.5x rev (haircut transaction) | $342M − $148.8M − $154M − $10M = **$29M** | **~0.5x** |
| 1.0x rev (harsh bear) | $342M − $148.8M − $99M = **$94M** | **~1.7x** |

**Even after de-rating Hiya to 1.5x and taxing Core at the harsher structural rate, the market still implies the entire Core business — ~$40M operating earnings, ~$54M EBITDA, 387k customers, a 34-year platform — at ~$29M, about half a turn of EBITDA.** At a distressed 1.0x-revenue Hiya, Core is implied at ~1.7x EBITDA. The mispricing is smaller than v1 said but **directionally intact**: a profitable, cash-generative Core is priced as if near-worthless.

---

## 2. Consolidated DCF (cross-check) — REVISED v2 (structural fixed-dollar tax)

Per **A1**, I model tax the *honest structural way*: a **near-fixed foreign cash charge (~$33–44M/yr)** that does NOT scale down with shrinking pretax — not a percentage. This is harsher than v1 and harsher than the SOTP, and it is the correct treatment. D&A ~$30M, rising capex as Rise/Hiya scale, small WC drag.

| Scenario | Core growth | Hiya growth | Rise (rev $M) | EBIT margin | Foreign cash tax ($M/yr) | WACC | term g | **EV** | **EqV** | **$/share** |
|---|---|---|---|---|---|---|---|---|---|---|
| Bear | −10→−5% | −5→+5% | 50→62 | 4–5% | ~33 (fixed) | 13.0% | −1% | $24M | $173M | **$9.37** |
| **Base** | −7→−2.5% | 0→+12% | 55→95 | 5.5→7.5% | 36→39 | 11.5% | +0.5% | $234M | $383M | **$20.74** |
| Bull | −4→+1% | +8→+12% | 60→130 | 6.5→9.5% | 37→44 | 10.0% | +2% | $653M | $802M | **$43.42** |

**The cross-check now reveals the real risk, not just agreement.** Base consolidated DCF **$20.74** is ~$4 *below* the SOTP base ($24.82) — the gap is the full corporate/US-overhead tax drag that the SOTP's segment-EBIT view under-weights. **Truth is between $20.74 and $24.82; I anchor base FV at ~$23.** The **bear collapses to $9.37** because a fixed ~$33M tax on a shrinking EBIT drives consolidated FCF to near zero — this is the structural-tax tail the reviewer was right to demand, and it makes the downside real (net cash + Hiya stake is the floor, ~$248M / ~$13.4/sh, not the bear DCF).

---

## 3. Scenario returns / 3-yr IRR (probability-weighted) — REVISED v2

3-yr fair-value targets blend SOTP and consolidated DCF. IRR = (FV/$18.53)^(1/3) − 1. No dividend.

| Scenario | Prob | 3-yr FV | 3-yr IRR |
|---|---|---|---|
| Bear | 30% | $14 | −8.9% |
| Base | 45% | $25 | +10.5% |
| Bull | 25% | $40 | +29.2% |
| **Prob-weighted** | | **$25.45** | **+9.4%** |

**Floor / downside protection:** even the bear's *DCF* ($9–14) is below the **asset floor** = net cash $148.8M + Hiya stake at a distressed 1.0x ($99M) = ~$248M ≈ **$13.4/share**, before any Core value. That floor (~−28%) is the practical downside, and it shrinks every quarter as buybacks retire stock.

**Buyback accretion (funded by net cash):** USNA bought back $27.5M FY25, ~$34M authorized. At ~$28M/yr near $20, it retires ~1.4M sh/yr → **~4.2M sh (≈23%) over three years**, shrinking the count 18.46M→~14.3M. A controlled, net-cash company buying stock at ~half of SOTP transfers Core's FCF and the Hiya stake onto fewer shares. The +9.4% weighted IRR **understates** the per-share outcome because the FVs don't fully credit the shrink.

---

## 4. Consensus baseline (what's priced in)

- **Coverage:** a single analyst (DA Davidson, **Neutral, $39 PT** — i.e., the lone covering analyst already sees ~110% upside but won't upgrade). EPS estimates **$2.12 FY26E / $2.77 FY27E**; revenue $945M FY26E / $1,002M FY27E (analyst.json).
- **What 0.2x EV/sales / ~0.5x implied-Core-EBITDA prices in:** terminal decline of Core to near-zero value, Hiya treated as a cost center, and the high tax rate read as permanent. Note (per A1): the *cash* tax drag is genuinely structural, so the market is not wrong to penalize it — the mispricing is that it ignores Hiya's stake value and the net cash, not that the tax is fake. The market is valuing USNA as a melting ice cube and giving no credit for the $206M D2C asset bolted on.
- **Retail/SA narrative:** split — one SA piece "Undervalued Turnaround" (Hiya/Rise pivot), one "Watch List But Not A Bargain Yet" (Hiya dilutes margins). No institutional sponsorship; orphaned micro-cap.
- **Earnings-call focus:** China stability, Hiya retail rollout (Target end-caps, Costco reorders), tax-rate trajectory. Q1 FY26 was a "better-than-expected" beat and management **guided the first growth year in four (+4%)**.

**Mispricing diagnosis (why it persists):** Neglect (one analyst, micro-cap, illiquid) + Segment opacity (Hiya only got its own segment line in FY25; Rise split out Q1 FY26 — comp screens still see a single declining MLM) + Misperception (the loss-making *quarter* and headline tax rate read as the whole story). This is **not** permanent impairment: Core is profitable and cash-generative even after the structural tax, Hiya is EBITDA-positive pre-amort, the balance sheet is fortress. The discount drivers are *partly* the opportunity (ignored Hiya stake + net cash) and *partly* real (structural cash tax, genuine Core attrition) — which is why this is a partial-flip, not a slam dunk.

---

## 5. Value-creation plan

**Commercial:** Scale Hiya through retail (Target/Costco/Walmart/UK/Canada) to re-accelerate the top line that D2C/Meta-CAC stalled; cross-pollinate Rise (Protein Pop) into USANA's direct-sales channel and 9 signed US retailers. Stabilize Core via product cadence (20+ in pipeline), women's/kids'/gut-health, and the omnichannel >20% mix target.
**Operations:** Let FY25's $13M one-time cost-realignment/impairment roll off (margin recovery to ~6–7% Core EBIT); in-housed China active-nutrition manufacturing lowers COGS. **Tax** is the single biggest controllable lever — the structural geographic mismatch drove the 72% rate; even normalizing to the guided 55–60% (and lower on a cash basis) is a large EPS swing on a fixed pre-tax base.
**Capital structure:** Zero term debt + $149M net cash. The highest-return use of that cash is **buying its own stock at ~0.5x implied-Core-EBITDA / ~half of SOTP** — accretion is mechanical and large. Secondary: D2C VMS tuck-ins at Hiya-like multiples to compound the segment the market already validated.
**M&A / control optionality:** Gull Global (Wentz family) owns 40.1% with a **single share class** (no super-vote). A family that just spent $206M acquiring Hiya, sitting on net cash, watching the public market price the *entire core* at ~$19M, has a clean, non-conflicted path to **take the company private** at a premium to $18.53 that would still be far below SOTP. The take-private is a credible re-rate catalyst, not a hypothetical.

---

## 6. Kill criteria (monitorable thresholds)

| Pillar / Risk | Metric | Kill threshold | Source | Next data point |
|---|---|---|---|---|
| Core not terminal | Active-customer YoY trend | Worse than −15% for 2 more quarters (no deceleration) | 10-Q MD&A | Q2 FY26 (Aug 2026) |
| Core cash engine intact | Core segment EBIT margin | < 4% for FY | segment note | FY26 10-K |
| Hiya is an asset, not a sink | Hiya segment EBIT (ex-launch) | Negative for full FY26 | segment note | FY26 10-K |
| Hiya transition resolves | Monthly subscribers | Below 170k / still falling by YE26 | 10-Q | Q3 FY26 (Nov 2026) |
| China | Greater China rev / customers | China rev decline re-accelerates past −10% cc | 10-Q | Q2 FY26 |
| Tax mismatch worsens | US pretax loss / cash taxes paid | US loss grows past −$60M, or cash taxes paid stay > $38M while pretax shrinks (cash rate worsening) | 10-K tax note + cash-flow | FY26 10-K |
| Capital allocation | Buyback pace | Buybacks stop while stock < $22 (cash hoarded, not deployed) | 10-Q cash-flow | each Q |
| Control optionality | Gull Global filings | Family *sells* into the market (signals no take-private) | Form 4 / 13D | ongoing |

---

## B. Operating model (driver-based) + sensitivity

### B1. Driver tree per segment (to real operating inputs)

**Core (direct selling)** — revenue = Σ_region (active customers × annualized rev/active customer):
```
Core revenue
├── Greater China:  208k cust × $2,041/cust  = $425M   (54% of base; -15.4% cust, +9.6% rev/cust)
├── SE Asia Pac:     63k cust × $2,095/cust  = $132M   (-18.2% cust, +9.9% rev/cust)
├── North Asia:      35k cust × $2,018/cust  = $71M    (-7.9% cust, -2.0% rev/cust)
└── Americas+Europe: 81k cust × $1,831/cust  = $148M   (-12.9% cust, +4.6% rev/cust)
                                       Total Core ≈ $775M  (387k cust, blended $2,004)
Customer flow = beginning − attrition + recruitment.  Sales mix ≈ 55% via Brand Partners (resellers),
balance Preferred Customers (10-K). Key cost lever: Brand Partner incentives = $336M = 43.3% of Core net
sales (FY25, Note M) — the largest single cost and the main margin dial.
Core gross margin ~82%; segment EBIT margin 5.2% (FY25) → 8.9% (Q1 FY26 as cost-realignment rolls off).
```
**Hiya (D2C subscription):** revenue ≈ monthly subscribers × ARPU × 12, split first-time (discounted, higher ship cost incl. glass bottle) vs recurring (better margin). Drivers: subscribers **186k** (Q1 FY26, −17% YoY) × implied ARPU ~$58–70/mo; **CAC** (Meta-driven, inflating — named headwind); **D2C-vs-retail mix** (new: Target end-caps, UK/Canada); retention/churn (subscription = recurring). FY25 segment EBIT +$3.4M post-$18.2M amort (~$21.6M pre-amort EBITDA).
**Rise (retail):** revenue ≈ doors × velocity × ARPU. Doors: 500 Walmart + Target + Costco (club) + 9 more US retailers signed for FY26. Costco reorders weekly (sell-through). Q1 FY26 $13.7M (~$55M annualizing). Segment EBIT −$1.8M (scaling losses).

### B2. Sensitivity tornado — top drivers by swing in base FV (±realistic ranges)

Base SOTP FV ≈ **$24.9**. Each driver flexed alone, others held at base (all *derived* from the model):

| Rank | Driver | Low → High range tested | FV low → FV high | **Swing ($/sh)** |
|---|---|---|---|---|
| 1 | **Hiya multiple** | 0.8x → 2.2x rev | $21.0 → $28.8 | **$7.8** |
| 2 | **Core EBIT margin** | 4.0% → 7.0% | $22.6 → $27.3 | **$4.7** |
| 3 | **Core cash-tax rate** | 55% → 37% | $23.4 → $26.2 | **$2.8** |
| 4 | Hiya revenue base | $110M → $150M | $23.6 → $26.2 | $2.6 |
| 5 | Core decline rate/yr | −8% → −1% | $23.7 → $26.0 | $2.3 |
| 6 | WACC | 13% → 10% | $24.1 → $26.0 | $1.9 |

**Correction to the reviewer's prior:** the expected top-3 was *Core customer trajectory / Core rev-per-customer / tax*. The model says the top-3 are **Hiya multiple, Core EBIT margin, Core cash-tax** — because net cash + Hiya stake is such a large share of value that the **Hiya mark dominates**, and within Core the *margin* (driven by the 43% Brand-Partner-incentive lever and the tax) moves value more than the *decline rate* within realistic ranges. Core customer trajectory matters, but ranks #5 — the rising spend/customer dampens its impact. Tax is correctly top-3, vindicating A1.

### B3. 2-D sensitivity: base FV to Core decline × Core cash tax

| Core decline/yr ↓ \ Cash tax → | 37% | 45% | 55% |
|---|---|---|---|
| −7% | $25.07 | $23.97 | $22.59 |
| −5% | $25.78 | $24.58 | $23.08 |
| −3% | $26.55 | $25.25 | $23.62 |
| −1% | $27.37 | $25.96 | $24.20 |

Even the worst corner (−7% decline, 55% cash tax) holds **$22.59 (+22%)** — because net cash + Hiya carry it. The Core assumptions are *not* able to break the thesis on their own; only a Hiya collapse + Core impairment together get you to the asset floor.

### B4. Which drivers are predictable from external data (and our directional read)

| Driver | External dataset to monitor | Our directional read |
|---|---|---|
| China direct-selling regulatory climate | China MOFCOM direct-selling license list; State Council "multi-level marketing" enforcement actions; the 2019 "100-day" health-product crackdown precedent | **Caution.** China is 54% of Core. The 2019 crackdown is the template risk. Currently stable (Q1 FY26 China rev −0.4% cc) but a single regulatory event is the largest discrete Core risk — un-modelable, hence the kill-criterion. |
| China health-supplement market growth | Euromonitor/China VMS market (~5–8% category CAGR cited by mgmt) | Category grows; USNA is **losing share** (customers −15%). The market is not the problem; recruitment is. |
| FX translation | **75.7% of net sales are non-USD** (10-K); Greater China ~46% (CNY), plus KRW/MYR/AUD. FY25 FX hit revenue by only −$3.1M | **Modest net exposure.** USNA makes product in the US and sells to subs in local currency, so costs are partly USD — a *partial natural hedge*. A 10% USD appreciation ≈ ~7.6% of revenue translated down on the top line, but EBIT impact is muted (incentives/SG&A are also foreign). Estimate: 10% USD move ≈ ±$4–7M EBIT — material but not thesis-breaking. |
| Hiya CAC (Meta/digital ad) | Meta ad-price indices; broader D2C CAC trend | **Headwind, structural.** Rising Meta CAC is *the* reason Hiya pivoted to retail. This caps D2C-only Hiya growth and pressures the multiple — a real reason to haircut (A2). |
| US mass-retail vitamin category | Nielsen/IRI VMS scanner; SPINS natural channel | Growing low-single-digits; kids' VMS faster. Supports the Hiya/Rise retail pivot if execution lands. |
| GLP-1 / wellness effect | GLP-1 scripts; protein/active-nutrition category growth | **Mixed-to-positive.** Mgmt is leaning in (Protein Pop, weight-management shakes relaunched in China). GLP-1 lifts protein/supplement demand but could pressure traditional weight-management lines. Net neutral-positive. |

---

## C. Porter's Five Forces (by arena), tied to margin durability

### Arena 1 — Direct-selling / MLM nutritional supplements (Core)
| Force | Intensity | Named evidence |
|---|---|---|
| **Rivalry** | **High** | Herbalife, Nu Skin, Amway, Melaleuca, Usana all fish the same distributor/customer pool; all shrinking in China/Asia. Competition is for *recruits*, not shelf — and recruitment is structurally falling industry-wide. |
| **Buyer power** | **High & rising** | "Buyers" are Brand Partners who can defect to a rival comp plan or to cheaper D2C/Amazon supplements. 43% of Core sales paid back as incentives = buyers extracting most of the gross margin. |
| **Supplier power** | **Low** | USNA self-manufactures (vertically integrated, owns plants) — a genuine moat vs. asset-light rivals; commodity inputs. |
| **Substitutes** | **High** | Amazon/D2C vitamins, retail VMS (the very thing Hiya/Rise are), pharmacy brands — all cheaper and friction-free vs. an MLM sign-up. This is the secular pressure. |
| **New entrants** | **Low (into MLM)** | Few want to start an MLM today; regulatory/reputational barriers. But entry into *supplements generally* is trivial — which is why substitutes, not new MLM entrants, are the threat. |

**Net read → Core margin durability:** the moat is **manufacturing + a loyal late-stage loyalist base**, not the channel. Margins are defensible in the *near* term (the 82% gross margin and the ability to dial incentives) but the **customer base is in secular decline** and buyer/substitute power is rising. **This corroborates A3:** the −2% to −2.5% terminal is appropriate, not −1.5%; a case for a worse terminal (−3% to −5%) is legitimate once the spend/customer mix-up exhausts. Core deserves a *low* multiple (NUS 3x, not NATR 8x) — which the DCF respects.

### Arena 2 — D2C + retail children's / family vitamins (Hiya / Rise)
| Force | Intensity | Named evidence |
|---|---|---|
| **Rivalry** | **High** | Kids' VMS is crowded: Olly (Unilever), Nature Made/SmartyPants (Pharmavite/Otsuka), Centrum Kids (Haleon), L'il Critters, plus store brands. Hiya's edge = subscription + "no sugar / refillable glass bottle" brand positioning. |
| **Buyer power** | **Moderate-high** | D2C consumers are one click from a substitute; subscription retention is the defense (and is what slipped). In retail, the *retailer* (Target/Costco/Walmart) holds the power over shelf and terms. |
| **Supplier power** | **Low** | Commodity gummy/vitamin contract manufacturing; USNA now in-housing Hiya production (margin lever). |
| **Substitutes** | **High** | Store-brand kids' vitamins at 1/2 the price; the premium positioning is the only defense. |
| **New entrants** | **High — and this is the key risk** | **Barriers to a new D2C VMS brand are low; the only real barrier is CAC, which is *rising* (Meta).** A well-funded entrant can replicate Hiya's playbook; the moat is brand + subscription retention + (now) retail distribution. |

**Net read → Hiya margin durability & multiple:** the Porter read is **why I haircut Hiya (A2).** Low new-entrant barriers + rising Meta CAC + retailer buyer-power mean Hiya's defensibility rests on **brand and retention**, both of which are *currently being tested* (subs −17%). That justifies marking Hiya **below** the high-growth D2C-VMS deal comps (Nutrafol ~$1B, Olly) — hence 1.5x base, not 2.5–4x. The *upside* is that retail distribution (Target/Costco) is itself a barrier once won, and a strategic acquirer (Unilever/Haleon/Pharmavite have all bought in this space) pays for shelf + subscription data — supporting the 2.0x bull and the take-out optionality.

---

## 7. Verdict (v2)

**SOTP base = $24.82/share (+34%). Consolidated DCF base = $20.74/share (+12%) — the gap is the full structural-tax drag; I anchor base FV at ~$23. Probability-weighted 3-yr FV $25.45, ~+9–10% IRR/yr — before the ~23% share shrink from net-cash-funded buybacks.** (v1 was $26.42 / +12%; the tax fix moved it down ~$1.50–2.)

**The implied Core:** even after de-rating Hiya to 1.5x and taxing Core at the structural 45% cash rate, the market values Core at **~$29M (~0.5x EBITDA)** — effectively **free**. At a distressed 1.0x Hiya, Core is **~$94M (~1.7x EBITDA)**. **Net cash + Hiya stake ($148.8M + $154M = $303M) is within ~11% of the $342M market cap**, so a profitable ~$40M-operating-earnings Core comes nearly free. The mispricing is smaller than v1 claimed but intact.

**Call: PARTIAL-FLIP (holds, slightly more cautious than v1).** The shallow "value trap" rested on one factual error (Hiya is *not* loss-making — +$3.4M FY25 segment EBIT) and one missing analysis (the SOTP). But the reviewer was right that v1 over-corrected on tax: **the high tax rate is a genuine structural cash drag, not an artifact**, and that pulls FCF and the bear down materially. So: flips from "trap, avoid" to "**mispriced on a SOTP/asset basis, but it is a deep-value asset play gated on a catalyst, not a quality compounder — own it small, sized for the structural-tax bear and a possible Hiya stall.**"

**The 2–3 swing variables (now model-confirmed by the tornado):** (1) **Hiya multiple/trajectory** — the single biggest swing ($7.8/sh); does retail re-accelerate it or is the D2C subscriber decline structural; (2) **Core EBIT margin** ($4.7/sh) — driven by the 43%-of-sales Brand-Partner-incentive lever and the structural tax; (3) **Core cash-tax** ($2.8/sh) — does the US-loss/foreign-profit mismatch ever resolve.

**The single fact that decides it:** **Hiya stake (~$154M at a haircut 1.5x) + net cash (~$149M) ≈ $303M vs a $342M market cap.** If USANA's own $206M check for Hiya 17 months ago was even roughly fair, the profitable Core is free — and a free, cash-generative Core held by a 40% family owner that is actively buying stock with net cash is not a trap. The thing that would *break* it: Hiya proves to be in structural demand decline (not a channel pivot) AND China regulation impairs Core — both at once.

**Was the depth worth it?** Yes, and v2 is the proof: the deep flow not only reached the opposite conclusion from the screen, the *reviewer's push* materially changed the numbers (tax fix moved base FV ~$2 and revealed a $9 bear). A shallow pass cannot do the domestic/foreign tax decomposition, the SOTP, or catch the "deal CLOSED" false positive. **Recommendation: run the deep flow on any screened name with (i) a recently consolidated acquisition distorting blended numbers, (ii) net cash that is a large % of market cap, or (iii) a control holder.** USNA hit all three. Not every name — but a mandatory triage flag for those three conditions.

---

## 8. What we still do NOT know (limits of the available data)

Honest list of what the dossier filings cannot tell us — i.e., where we've hit the data wall and would need primary research / paid data:

1. **Hiya's actual unit economics.** No disclosed ARPU, CAC, payback period, gross/net subscriber churn, or first-time-vs-recurring mix %. We infer ARPU (~$58–70/mo) from revenue ÷ subscribers — *estimated, not cited*. The single most important gap, since Hiya is the top swing variable. *Would need:* Hiya-specific KPIs (not broken out), expert/customer calls, or credit-card panel data (Bloomberg Second Measure / Earnest).
2. **Whether the Hiya subscriber decline is pivot or erosion.** Management says pivot (transcript-cited); the data can't yet distinguish a deliberate Meta-CAC pullback from genuine demand loss until we see FY26 retail velocity. *Resolves:* Q2–Q3 FY26 prints (Target/Costco sell-through).
3. **Retail velocity / reorder rates.** Target was ~2 weeks on shelf at last print; "end caps just placed." No sell-through data exists yet. Rise/Costco reorders are "weekly" (qualitative only). *Would need:* Nielsen/IRI/SPINS scanner data (paid).
4. **The put/call "Company Value Reference Amount."** The exact reference multiple on Hiya Adjusted EBITDA is defined in the (unfiled) LLC Agreement — we know the *mechanic* (Adj. EBITDA × multiple, puttable Apr-2028) but not the *number*. This sets the eventual NCI buyout price and is a direct Hiya-value read we can't see. *Estimated* at 8–12x.
5. **Cash-tax forward path.** We have the FY25 structure cold, but whether US losses keep growing (worsening the cash rate) or the geographic mix shifts (Hiya/Rise are US — could eventually *use* the US losses and improve the rate) is unmodelable from filings. This cuts both ways and is a genuine swing.
6. **Brand Partner cohort/recruitment data.** We see net active-customer counts by region but not gross adds vs. attrition, cohort retention, or leader (top-distributor) concentration — the leading indicators of whether Core decline inflects. *Would need:* former-employee/distributor calls.
7. **Gull Global's intent.** 40.1% family stake + net cash + a stock at half of SOTP = take-private *optionality*, but there is zero filing evidence (no 13D amendment, no special committee) that it is *imminent*. We are inferring capability, not intent. *Resolves only* via an actual filing.
8. **China regulatory trajectory.** Un-forecastable; the largest discrete tail risk to 54% of Core. Monitorable only after the fact.

**Bottom line on depth:** we have extracted essentially everything the filings allow on tax, segment economics, the customer bridge, and the SOTP. The remaining unknowns (1–4) are all **Hiya operating KPIs and retail velocity** — they are not in any USANA filing because Hiya is a consolidated sub, not a separate registrant. To go deeper than v2 requires **primary research (former Hiya/USANA employees, distributor calls) or paid alt-data (card-panel, retail scanner)** — that is the next, and final, marginal step before this is as deep as it can get.
