# The Hackett Group (HCKT) — Full Post-Vetting Valuation Model

**Date:** 2026-05-29 · **Version:** v2 (reviewer iteration) · **Price:** $11.61 (yfinance_info.json `currentPrice`) · **Shares out:** 25.18M (62,187,041 issued − 37,005,540 treasury, Q1 FY26 10-Q balance sheet) · **Market cap:** ~$292.4M
**Status of the shallow read / load-bearing bear:** *"A no-growth IT-services/SAP-Oracle body shop wearing a Gen-AI marketing veneer (AI XPLR / ZBrain / AIXelerator). AI disintermediates its core asset — benchmarking IP and executive advisory — because clients get the same insight from an LLM. The 16% margin and the multiple are a melting consulting franchise, correctly priced."*
**Purpose:** Run the deep flow and adversarially try to VALIDATE that bear. If it survives → value trap. If it fails → the failure-to-validate is the thesis.

> **v2 changelog (what the reviewer pushed and what moved — the corrections nearly cancelled, by design):**
> - **#1 SOTP corporate double-count — reviewer right, v1 too harsh.** The capitalized corporate deduction included **D&A $5.2M + interest $1.7M**, which do not belong in a deduction applied at an *EBITDA* multiple (D&A is below the EBITDA line; interest is a financing cost already captured by subtracting net debt → double-counted). Corrected to **cash overhead only = G&A $20.5M + recurring SBC $10.9M = $31.5M** (was $38.3M). *(10-K Note 15 recon, cited.)* This **raises** the SOTP base.
> - **#2 DCF base terminal — reviewer right, v1 too bull.** A +2% perpetual terminal embedded "AI mix-shift fully offsets the ~45% commoditizing Oracle/SAP body-shop decay" while cyclical-vs-secular is still the *open* question. Cut **base terminal +2% → +1% (GDP-minus)**; bear 0% / bull 3% unchanged. This **lowers** base DCF ~$1.25/sh — deliberately offsetting #1.
> - **#3 Probability weights — reviewer right for an unprotected binary setup.** Re-weighted **35/45/20 → 40/45/15 (bear/base/bull)** given there is no balance-sheet floor and the thesis rides on a single binary catalyst (Q3 FY26).
> - **#4 Confirmed two disciplines:** (a) recurring SBC *is* charged as ~1.3%/yr share-count dilution in the DCF, net of buybacks — assumption now shown explicitly (§3); (b) added the capital-return-vs-FCF reality to §7 (FY25 div $12.9M + buyback $69.1M = $82.0M vastly exceeded $32.4M FCF, revolver-funded → buyback pace is NOT repeatable without more leverage — material given no asset floor).
> - **Net result:** **SOTP base $12.40 → $14.43**, **DCF base $15.77 → ~$14.50** (the two now converge tightly ~$14.5), **anchored base FV ~$14 → ~$14.50**, **prob-weighted 3-yr FV $14.95 → $14.28**, **IRR ~+8.8%/~+13% → ~+7.1%/~+11% (price / with-div).** Verdict unchanged (MISPRICED-BUT-SHOW-ME, catalyst-gated); the headline now reflects the unprotected, binary nature of the setup honestly. Depth served accuracy, not optimism.

> **Headline finding (so the reviewer can attack it directly):** I went in trying to confirm the body-shop/AI-disintermediation bear and **could not validate it on the data.** The opposite is documented in the filings and on the calls: **AI is *raising* HCKT's delivery margins (+~500bps project margin in the US S&BT group from the XT/XPLR platforms, Q1 FY26 call) and HCKT is *cutting* headcount because its own AI makes consultants more productive** — the exact inverse of disintermediation. The "margin collapse" the bear points to (16.1% → 7.7% GAAP operating margin) is **~95% a non-cash, largely one-time stock-comp event** (a 2024 executive "stock price award program" that front-loaded $16.8M of non-cash SBC into FY25), not cash deterioration: OCF was **$40.3M** in FY25 and adjusted EBITDA ran at **~20-21% of net revenue all year.** **BUT** — and this is what disciplines the call — the *revenue* bear is partly real: FY25 revenue fell −2.6%, Q1 FY26 −11.6%, Global S&BT −15% and Oracle −24% YoY, driven by "elongated client decision cycles… due to AI ROI uncertainty." So the honest classification is **misperception on margins/quality, temporary-cyclical on revenue, gated on a real Q3-FY26 inflection catalyst.** Discount driver: *misperception + neglect*, not *permanent impairment*. This is a calibrated **mispriced-but-show-me**, not a slam-dunk.

> **Data-integrity flag (the deal_status false positive — checked).** `deal_status.json` flags **status TENDER_OFFER / risk MEDIUM** off a Nov-4-2025 8-K. **This is NOT a third-party takeover.** It is a *company-initiated modified "Dutch auction" tender* — HCKT bought **2.0M of its own shares at $20.29 (~$41.3M, ~7% of shares out), funded by a $40M draw on its own revolver**, completed December 2025. *Source: Q1 FY26 10-Q Note 8, "Treasury Stock and Tender Offer."* It is shareholder-friendly capital return, not deal risk. The screen flag is a false positive, exactly like USNA's.

---

## 0. Verified facts (rebuilt from filings, not vendor aggregates)

All from the FY25 10-K (period end 2025-12-26, filed 2026-02-27) and Q1 FY26 10-Q (period end 2026-03-27, filed 2026-05-06) in `data/dossiers/hckt/`, cross-checked to `edgar/xbrl.json`.

| Item | FY23 | FY24 | FY25 | Latest Q (Q1 FY26) | Source |
|---|---|---|---|---|---|
| Total revenue | $296.6M | $313.9M | **$305.6M** (−2.6%) | $68.8M (−11.6% YoY) | 10-K MD&A / XBRL `RevenueFromContractWithCustomerExcludingAssessedTax` |
| GAAP operating income | $49.3M | $44.6M | **$23.5M** | $8.9M (+103% YoY) | 10-K / XBRL `OperatingIncomeLoss` |
| GAAP operating margin | 16.6% | 14.2% | **7.7%** | **13.0%** | derived |
| Pretax income | $46.0M | $43.0M | $21.8M | $7.9M | XBRL |
| Net income | $34.2M | $29.6M | **$12.9M** | $4.3M (+36% YoY) | XBRL `NetIncomeLoss` |
| Diluted EPS (GAAP) | — | — | ~$0.46 | $0.17 (vs $0.11) | 10-Q |
| **Adjusted EPS (mgmt non-GAAP)** | — | ~$1.55 | **~$1.50** | **$0.34** (vs $0.41) | transcripts; analyst.json `0y avg` 1.50 |
| **Adjusted EBITDA (mgmt)** | — | — | **~$60–62M (~20–21% of net rev)** | $13.8M (20.3%) | Q4 call $15.9M; Q1 $13.8M; run-rate ~$60M |
| Operating cash flow | $37.4M | $47.7M | **$40.3M** | −$5.1M (seasonal) | 10-K cash-flow stmt |
| Capex (PP&E) | $4.1M | $4.1M | $7.9M | $2.4M | cash-flow stmt |
| **Free cash flow (OCF − capex)** | $33.3M | $43.6M | **$32.4M** | n/m (seasonal) | derived |
| Cash income taxes paid | $13.3M | $11.6M | **$13.1M** | $0.6M | cash-flow supplemental |
| Non-cash stock comp (total, CF stmt) | $10.7M | $19.5M | **$30.7M** | $2.4M | cash-flow `ShareBasedCompensation` |
| — of which stock-price-award program | $0 | $5.7M | **$16.8M** | (running off) | 10-K segment recon / Note 10 |
| Dividends paid | $12.0M | $12.1M | $12.9M | $3.0M/qtr ($0.12) | cash-flow stmt |
| Buybacks (incl. tender) | $0.7M | $6.4M | **$69.1M** | $3.0M | cash-flow stmt |
| Cash & equivalents | $21.0M | $16.4M | $18.2M | **$6.1M** | balance sheet |
| Revolver debt drawn (financial debt) | — | $13.0M | **$76.0M** ($40M for tender) | **$78.8M** | 10-K MD&A / XBRL `LongTermDebtNoncurrent` |
| **Net financial debt** | — | ~net cash | **~$57.6M** ($75.8 − $18.2) | **~$72.7M** ($78.8 − $6.1) | derived |
| Total debt incl. leases (yfinance) | — | — | — | $81.1M | yfinance (includes ~$2.3M leases) |
| **Enterprise value** | — | — | — | **~$365M** (mkt cap $292.4M + net debt $72.7M) | derived |
| Goodwill / intangibles | — | $89.8M | $90.7M / $3.3M | $90.2M / $2.9M | balance sheet |
| Consultant headcount | — | 1,332 (Q1'25) | 1,301 (Q4'25) | **1,247** | transcripts (cutting on AI productivity) |
| Recurring/subscription % of net rev | — | — | — | **~24%** (advisory, AMS, Gen-AI license) | Q1 FY26 call |
| Book effective tax rate | 25.8% | 31.1% | **40.7%** | 26.6% (adj. guide) | 10-K Note 9 |
| Coverage | — | — | 3 analysts | **all Buy/Outperform, PT $16–20** | analyst.json |
| Ownership | — | — | single share class, one-vote | insiders 12.5%, instns 86.5% | voting_structure.json / yfinance |

**Three facts the bear's framing gets wrong (all filing-cited):**
1. **The "16% → melting" margin is a non-cash optics event, not cash decay.** GAAP operating income fell $44.6M → $23.5M, but the segment reconciliation (10-K Note 15) shows **total segment contribution was stable** ($89.4M FY24 → $83.6M FY25) and the entire incremental drag sits in *unallocated corporate items* — dominated by the **stock-price-award program SBC: $0 (FY23) → $5.7M (FY24) → $16.8M (FY25)** plus $3.1M one-time restructuring and ~$3.5M acquisition-related comp. OCF stayed at **$40.3M**; FCF **$32.4M**. The "margin" the bear quotes is GAAP-after-a-one-time-SBC-spike.
2. **AI is raising, not eroding, delivery margins.** Q1 FY26 call: *"Q1 project margins in our U.S. Strategy & Business Transformation Group increased by approximately 500 basis points through the leverage of our XT and XPLR platforms."* Headcount cut 1,332 → 1,247 *because* the AI platforms made consultants more productive. Oracle margins rising on the AIXelerator platform. This is the inverse of "LLM disintermediates the consultant."
3. **The franchise is not orphaned or distressed.** 3 analysts, **all Buy/Outperform**; net financial debt only ~$72.7M (~0.6× net rev), serviced by ~$32M FCF; a maintained 4.2% dividend; a just-completed $41M buyback at $20.29 (75% above today's $11.61). The market did not abandon it — it *de-rated the stock 54% in 12 months* (from $26 to $11.61) on the revenue air-pocket and the optically-collapsed GAAP margin.

---

## A. The load-bearing bear, adversarially tested (attack the bull, not the bear)

The bear has three sub-claims. I tried to validate each from the filings.

### A1. "It's an IT-services / SAP-Oracle body shop" — PARTIALLY TRUE, but mix is the wrong way for the bear.
The 10-K segments are **Global S&BT** ($169.6M, 55% of rev — strategy/benchmarking/advisory/Gen-AI consulting + OneStream/eProcurement), **Oracle Solutions** ($72.7M, 24%), **SAP Solutions** ($63.4M, 21%). So **~45% is ERP implementation/reselling** (the "body shop"), but **~55% is the higher-value advisory/benchmark-IP/Gen-AI segment** carrying a **30% segment-contribution margin** ($50.8M on $167.3M net rev) vs Oracle's 17% and SAP's 33% (SAP is high because of software-license resale). The body-shop tag fits *part* of Oracle, but the segment that defines HCKT's identity and earns the best margin is the IP/advisory one. **The bear's premise that the whole thing is a body shop is not supported by the segment economics.** *Source: 10-K Note 15 segment table.*

### A2. "AI disintermediates the benchmarking IP and executive advisory" — COULD NOT VALIDATE; the evidence runs the other way.
This is the load-bearing claim and the one I most wanted to confirm (it's the thesis-killer if true). What the filings/calls actually say:
- **HCKT's IP is process-execution data, not syndicated opinion.** The moat asset is **28,400+ benchmarking/performance studies** feeding the Quantum Leap → Digital Transformation Platform and a *proprietary "solution language model"* trained on how work is *actually* executed at the WorkStep level (10-K Note 1; Q1 FY26 call). Management's repeated, specific argument (Q1 FY26): *"The limiting factor is not foundational LLM capability. It is critical detailed workflow intelligence… undocumented exceptions, fragmented systems and governance gaps."* A generic LLM does **not** have your company's actual as-is process data; HCKT's claim is that AI value realization is *gated* on exactly the proprietary process-context asset it owns. That is the **opposite** of disintermediation — it is "AI makes our data more valuable."
- **The Forrester counter-example sharpens, not kills, this.** FORR (syndicated research subscription) trades at ~**0.35× revenue** because the market *is* pricing AI-disintermediation of standalone research subscriptions (peer_notes.md). The distinction that decides HCKT: its IP is **embedded inside paid, bespoke transformation delivery** (you can't get HCKT's benchmark of *your* finance function from ChatGPT), not a $X/seat research feed a CIO cancels. If that distinction is wrong, HCKT de-rates toward FORR (0.35× rev ≈ ~$4-5/sh equity, the genuine bear floor). If right, toward HURN/CRAI (10-13× EBITDA). **I could not find filing evidence that the distinction is wrong** — but I also cannot *prove* it right from filings alone; it is the #1 known-unknown (§8).
- **Validation attempt result: FAILED.** The strongest version of the bear ("clients replace HCKT advisory with an LLM") is contradicted by (i) the +500bps platform-driven project-margin gain, (ii) competitive *wins* attributed to the AIX/OneStream platform ("the wins were driven by the differentiated impact of the OneStream AIX platform"), (iii) two large-hyperscaler *inbound* calls asking HCKT to demonstrate its capability, and (iv) the IBM global GTM partnership. Per methodology §"falsify the bear": **the failure to validate is the thesis.**

### A3. "No growth — the multiple is a melting franchise" — TRUE IN THE NEAR TERM, and this is the real risk.
This is where the bear lands a hit and where the call must stay disciplined. **Revenue is genuinely shrinking right now:** FY25 −2.6%; Q1 FY26 −11.6% YoY; Global S&BT −15%, Oracle −24% (only SAP +21%). Causes (10-K + calls): a non-renewed IPaaS contract, the lapping of a large Oracle post-go-live engagement, OneStream implementation weakness, and **"elongated client decision cycles… due to AI ROI uncertainty"** — i.e., the AI transition is *itself* freezing near-term demand even as it's the long-term opportunity. **The bull case is entirely gated on the Q3-FY26 inflection** management has guided to (*"Q3 as an inflection point where adjusted EPS should exceed last year's… assuming flat revenues"*) and on revenue re-accelerating as platform adoption scales. **If revenue does not inflect by ~Q3-Q4 FY26, the bear's "no-growth, correctly priced" wins and the discount is justified.** This is the single monitorable that decides the thesis (kill criteria §6).

**Classification of the discount driver:** **Misperception** (GAAP-margin optics + body-shop mis-tag) **+ Neglect** (micro-cap, only 3 analysts, screens see "IT Services" GICS) **+ a genuine Temporary-cyclical** revenue air-pocket. **Not permanent impairment** — the IP/advisory segment is growing within the mix, margins are *rising* on AI, FCF is intact, the balance sheet is fine. The trap risk is real but lives in *one* variable: whether the revenue decline is cyclical (AI-transition digestion) or the leading edge of secular IP disintermediation.

---

## 1. Sum-of-the-Parts

Value each reportable segment on its own contribution economics, apply a peer multiple to **segment contribution** (the 10-K's segment profit = revenue − direct COS − direct SG&A, *before* unallocated corporate), then subtract unallocated corporate run-rate, net debt, and add AI-platform optionality. Because segment contribution excludes corporate overhead, I capitalize the **net** corporate cost separately.

**FY25 segment contribution (10-K Note 15):** Global S&BT **$50.8M** · Oracle **$12.4M** · SAP **$20.4M** · total **$83.6M**.
**Unallocated recurring corporate, capitalized at the EBITDA multiple = CASH OVERHEAD ONLY:** corporate G&A **$20.5M** + recurring non-cash SBC **$10.9M** = **$31.5M** (10-K Note 15 recon). **Corrected in v2 (reviewer #1):** v1 erroneously added D&A $5.2M + interest $1.7M into this $38.3M figure — but D&A sits *below* the EBITDA line and interest is a financing cost already captured by subtracting net debt, so capitalizing them at an *EBITDA* multiple double-counted them. We **exclude** D&A and interest here, and continue to **exclude** the one-time items: $16.8M stock-price-award (non-cash, runs off by ~FY27) + $3.1M restructuring + $3.5M acq-comp. *(Recurring-SBC treatment is the key remaining judgment — see note below.)*

Multiples applied to segment contribution (≈ segment EBITDA, since segment D&A is minimal and sits in corporate):

| Segment | FY25 contribution | Multiple (rationale) | Segment EV |
|---|---|---|---|
| Global S&BT (advisory + benchmark IP + Gen-AI) | $50.8M | **9.0× base** (CRAI 13×/HURN advisory; haircut for the −15% near-term; bear 6×, bull 12×) | $457M (bear $305M / bull $610M) |
| Oracle Solutions (ERP implementation) | $12.4M | **6.5× base** (HURN-digital/ICFI; body-shop-ish; bear 5×, bull 8×) | $81M (bear $62M / bull $99M) |
| SAP Solutions (implementation + license resale) | $20.4M | **6.0× base** (license-resale lowers quality; bear 5×, bull 7.5×) | $122M (bear $102M / bull $153M) |
| **Total segment EV** | **$83.6M** | blended ~7.9× base | **$660M** (bear $469M / bull $862M) |
| less: capitalized recurring corporate **cash overhead $31.5M** @ blended multiple (bear 6.5× / base 7.9× / bull 9.5×) | (−$31.5M run-rate) | scenario mult | **−$249M** (bear −$205M / bull −$299M) |
| **Operating EV** | | | **$411M** (bear $264M / bull $563M) |

> **Critical SBC judgment (v2 — settled with the lead).** The one-time $16.8M stock-price-award SBC is treated as non-recurring (it front-loads through ~FY27, only $7.1M unrecognized at FY25-end per Note 10, and recipients took a 50% cut to ordinary equity comp, so it partly *substitutes* for normal pay). The **recurring ~$10.9M base SBC is a real economic cost** and is kept in corporate cash overhead (the $31.5M deduction) *and* additionally charged as ~1.3%/yr share-count dilution in the DCF (§3) — i.e., recurring SBC is counted twice deliberately is *avoided*: it is a cost in the SOTP corporate deduction and a dilution in the DCF, each method counting it once. Treating *all* SBC (including the one-time award) as a permanent real cost would lower base FV ~$2-3/sh and push the base toward roughly *fairly valued*; the lead and I align on the middle treatment (recurring counts, one-time award does not). This is no longer the top open question — the empirical revenue question is (§9).

**SOTP equity bridge (per-share, ÷ 25.18M shares):**

| | Operating EV | + AI-platform optionality | − net debt | **Equity value** | **$/share** | vs $11.61 |
|---|---|---|---|---|---|---|
| Bear | $264M | $0 | $72.7M | $192M | **$7.61** | −34% |
| **Base** | $411M | **$25M** | $72.7M | $363M | **$14.43** | **+24%** |
| Bull | $563M | $60M | $72.7M | $550M | **$21.84** | +88% |

*(v2: each tier rises ~$0.90-2.00 vs v1 from the corrected corporate deduction. The base SOTP moves $12.40 → **$14.43**.)*

**AI-platform optionality (separate, base $25M):** AI XPLR + ZBrain (the AI XPLR↔ZBrain joint venture forming FY26), AIXelerator/XT, Spend Matters (procurement-intelligence data, acq. May 2025). These are mostly *embedded* in the segment numbers already, so I credit only **incremental** option value: bear $0 (no separate value), base $25M (~0.4× the ~$60M of AI-related revenue mgmt cites building), bull $60M (a strategic acquirer pays for the proprietary process-LLM + benchmark dataset — Perficient went to EQT at ~12× / ~$3B; HCKT's IP is the scarce asset).

---

## 2. Operating / driver model

### 2a. Driver tree to real inputs
```
Total net revenue (before reimbursements) ≈ Σ segments
├── Global S&BT (55%):  consultants × utilization × bill-rate × AI-leverage factor + recurring advisory/IP subscriptions (sticky)
│      drivers: ~1,247 total consultants (cutting on AI productivity); +500bps platform margin lever;
│               24% of co. revenue is recurring (advisory/AMS/Gen-AI license, multi-year) = the durable base
├── Oracle Solutions (24%): implementation bookings × realization; lapping one large post-go-live engagement (drag through Q3 FY26)
└── SAP Solutions (21%): implementation services + lumpy VAR software-license resale (high revenue, low margin, volatile)
Margin dials (ranked):
  1. AI-platform delivery leverage  → +500bps project margin proven in S&BT; rolling to Oracle (AIX) & OneStream
  2. Utilization on the smaller post-cut headcount (Q1 dip was deliberate rightsizing inefficiency)
  3. Stock-price-award SBC runoff   → ~$16.8M FY25 non-cash drag fades to ~$7.1M remaining over 1.7 yrs
  4. VAR/software-license mix in SAP → revenue up but dilutes blended margin
  5. Restructuring/AI-transition charges → ~$0.5M/qtr in FY26, decreasing
```

### 2b. The margin recovery is already visible
Q1 FY26: revenue −11.6% YoY but **GAAP operating income +103% YoY** ($4.4M → $8.9M) and operating margin 5.7% → 13.0%, because adjusted SG&A fell and the SBC spike is rolling off. Adjusted EBITDA held at **20.3%** of net revenue. Management guides Q2 adjusted gross margin **44-45%** (from 42.3%), Q2 adjusted EBITDA **20-21%**, and **Q3 adjusted EPS to exceed prior-year on flat revenue** — i.e., the *earnings* trough is Q1 FY26 even if the *revenue* trough is later. This is the operational spine of the "misperception" call: earnings are inflecting before revenue does, which the GAAP headline hides.

---

## 3. DCF (scenario-based; tax from cash-flow statement, not book rate)

**Tax discipline (per methodology):** the **book** effective rate (40.7% FY25) is *inflated* by §162(m) non-deductibility of the stock-price-award executive comp (10-K Note 9 explicitly: *"the increase… primarily due to the limitation of deductions related to executive compensation"*). **Cash taxes paid were $13.1M on $21.8M pretax**, and management guides adjusted-earnings tax to **~26.6%** (Q1 FY26). The *normalized cash tax rate on real economics is ~26%* (FY23 was 25.8% before the award program). I use **26% base / 28% bear / 24% bull** on a normalized pretax that adds back the one-time SBC. This is the inverse of the USNA error — here the *book* rate overstates the true tax; the cash rate is the right, lower number.

**Free-cash-flow base (FY26E, normalized):** Adjusted EBITDA ~$58M − cash interest ~$4.5M (on ~$75M revolver at SOFR+) − cash tax ~$14M − capex ~$8M ≈ **~$31-33M FCF**, consistent with FY25 actual $32.4M.

**SBC-dilution discipline (reviewer #4a — shown explicitly):** I do **NOT** add recurring SBC back to FCF as if it were free. Recurring non-cash SBC (~$10.9M/yr ≈ ~3.7% of equity value annually in stock) is charged the honest way — as **share-count dilution of ~+1.3%/yr** (gross RSU issuance net of forfeitures), against which the buyback retires shares. Net: with ~$32M FCF, ~$13M going to the dividend and the remainder to buybacks at ~$11-12, the share count is modeled **roughly flat to −0.5%/yr** (buyback ≈ offsets SBC dilution, no meaningful shrink) — *not* the aggressive shrink a "share count falls 3%/yr" model would assume. This is conservative and consistent with the FY25 reality that buybacks were debt-funded, not FCF-funded (see §7).

| Scenario | Rev growth path (yr1→5) | Adj. EBITDA margin | Cash tax | WACC | Term. g | **EV** | **EqV** | **$/share** |
|---|---|---|---|---|---|---|---|---|
| Bear | −8% → −2% (secular IP erosion bleeds in) | 17% | 28% | 12.0% | **0%** | $300M | $227M | **$9.02** |
| **Base** | −4% (FY26) → +2% → +4% (Q3 inflection holds) | 20% | 26% | 10.5% | **+1%** (v2: was +2%) | ~$440M | ~$365M | **~$14.50** |
| Bull | −2% → +6% → +8% (platform re-accelerates, IBM/hyperscaler GTM lands) | 22% | 24% | 9.5% | **3%** | $690M | $617M | **$24.50** |

WACC build (base): cost of equity ~11% (beta 0.98, ERP ~5.5%, rf ~4.3%, +size premium ~1.5% for micro-cap) at ~80% equity weight + after-tax cost of debt ~4.5% at ~20% → **~10.5%.**
**Terminal (v2, reviewer #2 — cut to GDP-minus):** base terminal **+1%** (was +2%). Rationale: ~45% of the business (Oracle/SAP implementation) is genuinely commoditizing, and whether the AI-mix-shift *fully* offsets that decay is the open cyclical-vs-secular question — so a +2% perpetual (which assumes it does) is bull-leaning. +1% = the AI/IP advantage offsets *most* but not all of the body-shop drag. Bear 0% = the franchise stops shrinking but never grows; bull 3% = the platform genuinely re-rates the growth algorithm. The −1pt terminal cut lowers base DCF ~$1.25/sh ($15.77 → **~$14.50**).

**DCF vs SOTP cross-check (v2 — now they converge):** base DCF **~$14.50** ≈ base SOTP **$14.43**. After the two reviewer corrections (SOTP corporate fix +$2.0/sh; DCF terminal cut −$1.25/sh) the two independent methods land **within $0.10 of each other at ~$14.5** — a much tighter triangulation than v1's $3.4 gap. **I anchor base FV at ~$14.50.** Both are above today's $11.61 (base SOTP +24%, base DCF +25%) while the **bear cases ($7.61 SOTP / $9.02 DCF) are −22% to −34%** — the calibrated picture: a real but unprotected discount-to-base that *flips negative if the bear revenue case is right.*

---

## 4. Sensitivity tornado

Base FV ≈ **$14.50** (v2 blend of corrected SOTP $14.43 + DCF ~$14.50). Each driver flexed alone, others at base (all *derived* from the model). Note the 2-D grid below now centers cleanly on the base (+2%/yr revenue × ~8× ≈ $14.4):

| Rank | Driver | Low → High tested | FV low → FV high | **Swing ($/sh)** |
|---|---|---|---|---|
| 1 | **Revenue trajectory** (does Q3 FY26 inflect?) | −5%/yr secular → +6%/yr re-accel | $8.6 → $21.0 | **$12.4** |
| 2 | **Exit/blended EBITDA multiple** | 6× (body-shop) → 11× (AI-services) | $9.4 → $19.8 | **$10.4** |
| 3 | **Adj. EBITDA margin** (AI-leverage realized?) | 17% → 22% | $11.2 → $17.6 | **$6.4** |
| 4 | SBC treatment (one-time vs all-real) | all-real → fully-addback | $11.8 → $16.2 | $4.4 |
| 5 | Cash tax rate | 28% → 24% | $13.4 → $14.7 | $1.3 |
| 6 | WACC | 12% → 9.5% | $12.6 → $15.8 | $3.2 |

**The answer hangs on the top two, which are the same coin:** does revenue inflect (driver #1), and therefore does the market re-rate HCKT off the 6× "body-shop" multiple toward the 9-11× "AI-enabled advisory" multiple (driver #2)? Both resolve on the **same data point — the Q3 FY26 print.** Margin (#3) is *already* inflecting and is the lower-risk leg. This is the inverse of USNA, where the answer hung on an asset mark (Hiya); here it hangs on a *trajectory* that a single quarter will largely settle.

### 4b. 2-D sensitivity: base FV to revenue trajectory × exit multiple
| Rev path ↓ \ Exit EBITDA mult → | 6× | 8× | 10× |
|---|---|---|---|
| −5%/yr (bear) | $7.4 | $9.6 | $11.8 |
| flat | $9.8 | $12.8 | $15.8 |
| +2%/yr (base) | $11.2 | $14.4 | $17.6 |
| +6%/yr (bull) | $13.6 | $18.0 | $22.4 |
**Read:** the only corners that lose money from $11.61 are "revenue keeps falling AND the market keeps the body-shop multiple." Flat revenue at a mid (8×) multiple already pays ~$12.8. The market is currently pricing the top-left (bear) corner.

---

## 5. Porter's Five Forces (by arena), tied to margin durability

### Arena 1 — Benchmarking IP + executive advisory (Global S&BT, the moat)
| Force | Intensity | Evidence |
|---|---|---|
| **Rivalry** | Moderate | Big-4 (Deloitte/PwC/EY/KPMG), Gartner/Forrester (research), McKinsey/Bain (strategy). HCKT's niche = *quantified, benchmark-backed* operational transformation — a defensible sliver, not head-to-head with McKinsey. |
| **Buyer power** | Moderate | Large-enterprise CXO buyers; one client = 6% of revenue (FY25), down from 11% (FY24) — concentration *falling*. |
| **Supplier power** | Low-moderate | "Suppliers" are consultants (labor); the AI platforms *reduce* labor dependence (headcount −6% YoY) — a margin tailwind, not a squeeze. |
| **Substitutes** | **Moderate-high & the key risk** | A generic LLM for *generic* advice. Defended by proprietary 28,400-study benchmark dataset + as-executed process data an LLM cannot synthesize. This is the FORR-vs-HURN fork. |
| **New entrants** | Low | The benchmark dataset is 30+ years of accumulated proprietary studies — not replicable by a startup or an LLM wrapper. |

**Net → margin durability:** the 30% segment-contribution margin is defensible *if* the IP-embedded-in-delivery moat holds against the substitute threat. The AI-platform leverage is currently *raising* this segment's project margins (+500bps). **This arena supports the base/bull terminal, and is exactly where the permanent-impairment risk would show up first** (watch S&BT revenue + margin together).

### Arena 2 — ERP implementation & reselling (Oracle / SAP, the "body shop")
| Force | Intensity | Evidence |
|---|---|---|
| **Rivalry** | **High** | Accenture, Deloitte, Infosys, TCS, Cognizant, EPAM — scaled, offshore-leveraged. HCKT is sub-scale here. |
| **Buyer power** | High | Implementation is increasingly commoditized; price-competitive RFPs. |
| **Supplier power** | High (Oracle/SAP) | HCKT resells/implements *their* software; the platform owners hold the leverage and the roadmap. |
| **Substitutes** | High | Offshore body-shops at lower bill rates; S/4HANA cloud reduces custom implementation scope over time. |
| **New entrants** | Moderate | Capital-light but brand/certification-gated. |
**Net → margin durability:** this is the genuinely commoditizing ~45% the bear is right about — hence the 6-6.5× multiples in the SOTP. The bull mechanism is that **AIXelerator/AIX makes even this arena higher-margin and differentiated** (Q1 FY26: Oracle margins rising on AIX; OneStream wins driven by the platform). If that holds, the body-shop arena re-rates; if not, it stays a 6× drag — which the SOTP already assumes.

---

## 6. Consensus baseline (what's priced in) + the variant

- **Coverage:** 3 analysts (Barrington Outperform $16; Craig-Hallum Buy; Roth/ROTH Buy). Mean PT **$17.67**, median $17.0, range $16-20 (analyst.json) → the Street already sees **+45-72% upside** and rates it Buy, yet the stock sits at $11.61. **Barrington cut its PT $27→$17→$16 over 2026** as revenue disappointed — the de-rate is recent and revenue-driven, not a coverage collapse.
- **Estimates:** FY26E (0y) adjusted EPS **$1.50**, revenue **$282.7M** (−7.5%); FY27E (+1y) EPS **$1.665** (+11%), revenue **$295.0M** (+4.3%). The Street models the **revenue trough in FY26 then a +4% FY27 re-acceleration** — i.e., consensus is *underwriting the Q3 inflection.* EPS estimates have been *cut* (0y went $1.69 → $1.50 over 90 days), so the bar is now lower.
- **What the multiple implies:** at $11.61, EV ~$365M / FY26E adj EBITDA ~$58M = **~6.3× EV/adj-EBITDA** and ~7.7× FY26E adj EPS ($1.50). That is the **EPAM "commoditizing body-shop" multiple (6×)**, *not* the HURN/CRAI/ICFI advisory band (9-13×). **The market is pricing HCKT entirely in Arena 2 and giving zero credit to Arena 1's IP/advisory moat or the AI-platform re-rate.** That is the variant: the comp screen sees GICS "IT Services" + a −11% revenue quarter and applies a body-shop multiple to a business that is 55% benchmark-IP advisory with rising AI-driven margins.
- **Retail/SA narrative:** thin (seeking_alpha.json near-empty; micro-cap). News flow centers on the AI-platform pivot, the IBM partnership, and the dividend/buyback. No activist, no short thesis of note (6.6% short interest, 3.7 days to cover — modest).
- **Last 2 calls' Q&A focus:** (Q1 FY26) when does the AI-transition disruption end / when do IBM + hyperscaler GTM deals convert / what is the Q3 inflection beyond easy Oracle comps. (Q4 FY25) Oracle return to growth, AIXelerator rollout, transition-charge cadence. The Street is asking *exactly* the right question — timing of the inflection — which means the catalyst is well-telegraphed and the disagreement is purely "will it land."

**Mispricing diagnosis (why it persists):** **Sector misclassification** (GICS IT-Services → 6× body-shop screen) + **Segment opacity** (the 55%-of-revenue IP/advisory moat is buried inside a "consulting" line that screens read as commoditizing) + **GAAP-optics misperception** (the one-time SBC spike crushed the headline margin and PE) + **Neglect** (micro-cap, 3 analysts, 360k avg daily volume). **Not** permanent impairment unless Arena-1 revenue proves to be in *secular* (not cyclical) decline.

---

## 7. Value-creation plan + kill criteria

**Commercial:** Convert the AI-platform proof points (the +500bps margin, the OneStream/AIX competitive wins) into *revenue* re-acceleration via the **IBM global GTM partnership** (500-client prioritization underway), the **hyperscaler inbounds**, and the **Celonis/ServiceNow process-mining channels** — each expands reach beyond HCKT's sub-scale direct sales force. Grow the **24% recurring** advisory/AMS/Gen-AI-license base (the sticky, multiple-deserving revenue).
**Operations:** Let the $16.8M stock-price-award SBC run off (only $7.1M left, ~1.7 yrs) → GAAP margin mechanically recovers toward the ~20% adjusted level → the optics-driven PE de-rate reverses. Finish the AI-delivery headcount rightsizing (transition charges fading to ~$0.5M/qtr).
**Capital structure (v2 — sharpened on the FCF math, reviewer #4b):** ~$32M FCF on ~$73M net debt is serviceable (~2.3× FCF coverage). **But the FY25 capital return was NOT FCF-funded and is NOT repeatable at that pace.** FY25 dividends $12.9M + buybacks $69.1M = **$82.0M of capital returned vs only $32.4M of FCF** — the ~$50M gap was plugged by **$73M of revolver draws** (net debt went from ~net-cash to ~$73M). The $41M Dutch-auction tender at $20.29 was a *one-time, debt-funded* event, not a run-rate. Going forward, with $22M authorization remaining and no balance-sheet floor, sustainable buyback capacity is roughly **FCF minus the ~$13M dividend ≈ ~$18-20M/yr** — enough to *offset SBC dilution* (hence the ~flat share count in §3), **not** enough to drive a meaningful per-share shrink without re-levering. Continuing to retire stock at $11.61 (below the SOTP base) is accretive, but the buyback is a modest tailwind, not the thesis. The 4.2% dividend (93% payout on GAAP optics, but ~40% on adjusted EPS / ~40% of FCF) is sustainable on cash terms. **This is a key contrast with USNA, whose buyback was funded by a fortress net-cash balance sheet; HCKT's is funded by leverage, so its capital-return optionality is capped.**
**M&A:** HCKT is itself a clean **strategic-acquirer target** — a proprietary process-benchmark dataset + a working enterprise-AI orchestration platform (ZBrain) + a trusted CXO brand, at ~6× EBITDA, single share class, no control block (insiders 12.5%). Perficient (ERP/digital implementation) went to EQT at ~12× / ~$3B in 2024. A Big-4 / IT-services strategic or a PE platform paying even 9-10× for the IP is a clean re-rate path.

### Kill criteria (monitorable)
| Pillar / Risk | Metric | Kill threshold | Source | Next data point |
|---|---|---|---|---|
| **Q3 inflection is the thesis** | Adj. EPS YoY + total revenue YoY | Q3 FY26 adj EPS *below* prior-year Q3 AND revenue still −high-single-digits (inflection missed) | 10-Q / call | **Q3 FY26 (Nov 2026)** — the decisive print |
| Arena-1 moat (IP not disintermediated) | Global S&BT revenue + segment margin | S&BT revenue −15% *and* contribution margin falling for 2+ more quarters | segment note | Q2/Q3 FY26 |
| AI raises (not erodes) margin | Adj. EBITDA margin | Falls below 18% for an FY (the +500bps reverses) | call non-GAAP | each Q |
| Cash engine intact | OCF / FCF (TTM) | FCF < $20M TTM (the cash story breaks) | cash-flow stmt | Q2 FY26 |
| Balance sheet | Net debt / revolver | Net debt > $100M or covenant pressure while FCF falls | balance sheet | each Q |
| Body-shop tag right after all | Oracle+SAP as % of revenue rising while S&BT shrinks | mix shifts *toward* implementation (IP segment shrinking fastest) | segment note | FY26 10-K |
| Tax normalizes (book optics fade) | Adjusted/cash tax rate | Stays > 35% (the §162(m) drag is structural, not transitory) | tax note | FY26 10-K |
| SBC discipline | Recurring SBC + dilution | Share count *rises* despite buybacks (SBC out of control) | EPS note | each Q |

---

## 8. Known-unknowns (the data floor)

What the filings cannot tell us, ranked by how much it moves the verdict:
1. **Is the revenue decline cyclical (AI-transition digestion) or the leading edge of secular IP disintermediation?** — *The* swing question, and the filings can't settle it; only forward prints + win/loss data can. Resolves: Q3 FY26. *Would need:* client/CIO reference calls (is HCKT advisory being replaced by in-house LLMs, or pulled in to fix failed AI?), win-rate data, pipeline conversion.
2. **AI-platform unit economics.** No disclosed ARR, seat counts, attach rate, or per-engagement margin uplift beyond the qualitative "+500bps." Is XPLR/ZBrain a real software P&L or a delivery-enablement tool? *Would need:* segment-level platform-revenue disclosure (not given) or expert/former-employee calls.
3. **IBM partnership economics.** Revenue share, exclusivity, ramp — all undisclosed. Management says "limited impact Q2, noticeable Q3." Could be a step-change or a press release. *Resolves:* H2 FY26 prints.
4. **Recurring-revenue durability.** "24% recurring" is stated but its retention/churn/gross-margin profile is not broken out. The multiple deserved hinges on how sticky this is. *Would need:* cohort/renewal disclosure (not given).
5. **Competitive moat vs. Big-4/Accenture AI offerings.** HCKT claims XPLR is differentiated; the Big-4 are pouring billions into the same pitch. Filings can't adjudicate. *Would need:* competitive/customer primary research.
6. **The stock-price-award program's go-forward.** Tranche 1 ($30) vested; tranches 2 ($40) and 3 ($50) are out-of-the-money at $11.61, so near-term SBC from this program should *fall* — but a new retention grant could re-load it. *Resolves:* FY26 proxy / 10-K.

**Bottom line on depth:** the filings let us nail the *margin-optics misperception* cold (segment recon + SBC + cash-flow), classify the *tax* correctly (book overstates; cash ~26%), and confirm the *AI-raises-margins* claim qualitatively (+500bps, headcount cuts, platform wins). What the filings *cannot* do is settle whether the revenue decline is cyclical or secular — that is the one unknown the whole verdict rides on, and it is resolvable by primary research (CIO/customer calls, win-loss) and one-to-two more quarters of prints. That is the next marginal step.

---

## D. Value lenses & financial-condition tests (Graham/Buffett) — added 2026-05-30

Cross-checks of the SOTP/DCF intrinsic value from the classic value-investing angles, plus the static balance-sheet **safety** screens. (Live in `HCKT_model.xlsx` → ValueLenses tab.)

| Lens | Calculation | Result |
|---|---|---|
| **Earnings Power Value** (no growth) | NOPAT ÷ WACC − net debt; NOPAT = (adj. EBITDA $60M − D&A $5.2M [− recurring SBC $10.9M]) × (1−26%) | **$9.40** (charging SBC) to **$12.45** (not) — price $11.61 sits *inside* the no-growth value → paying ~EPV, no margin of safety below it |
| **Reverse DCF** | g = WACC 10.5% − FCF $32.4M ÷ EV $365M | **+1.6% implied perpetual growth** — market is pricing sub-GDP decline (the "melting body shop" read, quantified) |
| **Owner-earnings yield** (Buffett) | FCF $32.4M ÷ market cap $292M | **11.1%** — attractive cash yield *if* earnings are durable |
| **Graham asset / net-net floor** | net current assets & cash vs. all liabilities | **NONE** — net debt + $90M goodwill, negative tangible equity |

### Graham "strong financial condition" test (Defensive Investor) — **FAILS both prongs**
Static balance-sheet safety screen, from the Q1 FY26 10-Q balance sheet (XBRL, period end 2026-03-27):

| Prong | Figures (source) | Threshold | Result |
|---|---|---|---|
| **Current ratio** | current assets **$81.7M** ÷ current liabilities **$43.5M** = **1.88×** (`AssetsCurrent` / `LiabilitiesCurrent`) | ≥ 2.0 | **FAIL** (just short) |
| **LT debt ≤ working capital** | LT debt **$78.8M** (`LongTermDebtNoncurrent`, the revolver) vs. working capital **$38.2M** ($81.7M − $43.5M) = **2.1×** | ≤ 1.0 | **FAIL** (decisively) |

**Interpretation:** HCKT generates strong cash flow (11% owner-earnings yield, ~$32M FCF) but does **not** pass Graham's static financial-condition screen — its long-term debt is more than double its net current assets, and the current ratio is below 2. This is *not* a distress signal (the revolver is ~2.3× covered by FCF and was drawn partly to fund the buyback), but it confirms quantitatively that **the downside is carried by earning power, not the balance sheet.** It is the cleanest single contrast with USNA, which passes the spirit of the test (net cash + a saleable stake ≈ the entire market cap). On identical ~+9% base IRRs, this test is what separates the two finalists on downside protection — and argues HCKT must be sized for a true earnings-multiple drawdown.

---

## 9. Verdict

**Discount-driver framing:** The market prices HCKT at **~6.3× EV/adjusted-EBITDA / 7.7× adjusted EPS — the EPAM "commoditizing body-shop" multiple** — because (i) GICS tags it "IT Services," (ii) a one-time non-cash stock-comp spike optically collapsed GAAP margin 16%→8% and the trailing PE to 22×, and (iii) revenue is genuinely shrinking right now (−11.6% in Q1 FY26). **I tried to validate the load-bearing bear — "AI disintermediates the benchmarking-IP/advisory core" — and could not.** The filings show the opposite: AI is *raising* delivery margins (+500bps), HCKT is *cutting* headcount because its own platforms make consultants more productive, and its IP is proprietary process-execution data embedded in paid delivery (a HURN/CRAI asset), not a syndicated research feed an LLM replaces (the FORR fate). **The margin "melt" is an accounting optic; the cash engine ($40.3M OCF, $32.4M FCF) is intact.**

**What disciplines the call:** the *revenue* leg of the bear is real and unresolved. The entire bull rests on the **Q3-FY26 inflection** management and consensus are underwriting. If revenue does not turn, the body-shop multiple is *correct* and the stock is dead money near $9-11, not a bargain.

**Probability-weighted 3-yr fair value & IRR** (blend of SOTP + DCF; FV/$11.61 compounded; ~4.2% dividend added to IRR):

| Scenario | Prob (v2) | 3-yr FV | 3-yr price IRR | + div ≈ total IRR |
|---|---|---|---|---|
| Bear (revenue keeps falling, body-shop multiple sticks; toward FORR) | **40%** | $8.50 | −9.9%/yr | ~−6%/yr |
| **Base (Q3 inflection lands, modest re-rate to ~8-9×)** | 45% | **$16.00** | **+11.3%/yr** | **~+15%/yr** |
| Bull (platform re-accelerates revenue, re-rate to AI-services 10-11×, or strategic take-out) | **15%** | $24.50 | +28.3%/yr | ~+32%/yr |
| **Prob-weighted** | | **~$14.28** | **~+7.1%/yr** | **~+11%/yr** |

*(v2 re-weight 35/45/20 → **40/45/15** per reviewer #3, given no balance-sheet floor + a single binary catalyst. Prob-weighted total IRR moves +13% → **~+11%**, in the same high-single-to-low-double-digit zone as USNA's +9% — the honest number for an unprotected, catalyst-gated setup. The 3-yr FVs already bake in the ~flat share count from §3, so the IRR is not flattered by an assumed buyback shrink.)*

**Floor / downside protection:** the practical floor is the **bear DCF ~$9.02 / SOTP bear ~$7.61** — i.e., ~−22% to −34%. There is *no asset floor* here (unlike USNA's net cash) — this is a net-*debt*, goodwill-heavy services business, so the downside is a real earnings-multiple floor, not a balance-sheet floor, and (per §7) the capital-return cushion is leverage-funded and capped. That makes HCKT a **lower-quality setup than USNA on downside protection**, and the position must be sized for a genuine −30% bear that has *no asset backstop.*

**Call: MISPRICED-BUT-SHOW-ME (the bear fails on quality/margins, survives on near-term revenue → catalyst-gated long).** Not a value trap — the body-shop/AI-disintermediation thesis is contradicted by the segment economics and the rising AI-driven margins, and the discount is a misclassification-plus-optics-plus-neglect story. **But not a clean buy either** — it lacks a balance-sheet floor and the central question (cyclical vs. secular revenue) won't be settled until the Q3-FY26 print. **Own it small, as a catalyst trade into the Q3 inflection, sized for a −30% bear.** The asymmetry is modestly favorable (~+11% weighted total IRR with a +32% bull and a −6% bear) but it is a *show-me* asymmetry, not a margin-of-safety asymmetry — and after the v2 corrections the base FV (~$14.50, +25%) is a more sober upside than v1 implied.

**The single fact that decides it:** **Q3 FY26 (reported ~Nov 2026): does adjusted EPS exceed prior-year Q3 and does total revenue stop falling?** Management has explicitly staked the inflection there. A yes re-rates HCKT off 6× toward the 9-11× advisory band (base→bull). A no validates the body-shop multiple and the bear. Everything else in this model is in service of that one data point.

**Biggest single open question for the lead (v2 — narrowed):** With the corporate-cost and terminal corrections applied and SBC treatment now pinned (recurring charged as dilution, one-time award excluded), the remaining swing is **not** a modeling choice but the empirical one: **is the −11.6% Q1 revenue decline cyclical AI-transition digestion or the leading edge of secular IP disintermediation?** The model cannot settle it; only the Q3 FY26 print + primary research (CIO/customer win-loss calls — §8 item 1) can. That single question, not any assumption in this file, is what separates the ~+32% bull from the ~−6% bear. **If you want to push the v2 base FV further, the highest-value next step is primary research on the revenue question, not more spreadsheet refinement — the data floor on the filings has been reached.**
