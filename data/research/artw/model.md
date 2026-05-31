# Art's-Way Manufacturing (ARTW) — Full Deep-Flow Carve-Out Valuation

**Date:** 2026-05-30 · **Version:** v2 (reviewer iteration) · **Price:** $2.58 · **Shares:** 5.184M (proxy, Mar-5-2026) · **Market cap:** ~$13.4M · **Net debt:** ~$6.40M · **Enterprise value:** ~$19.8M
**Fiscal year:** ends **November 30** (FY2025 = year ended 2025-11-30; FY2026 Q1 = quarter ended 2026-02-28).
**Thesis under test:** acquire ARTW, **wind down / divest the loss-making Agricultural Products (farm-equipment) segment**, and own **Art's-Way Scientific (Modular Buildings)** standalone — modeled as **two legs with divergent macro** (research/biocontainment labs vs. agricultural/animal-biosecurity buildings).

> **v2 changelog (what the reviewer pushed and what moved):**
> - **AG-DISPOSAL BASE WAS OPTIMISTIC / TUNED TO PRICE — corrected.** v1's base ag-disposal (70% inventory / 45% PP&E) netted to $8.9M and landed base FV at *exactly* $2.58 (the quote) — an anchoring red flag. **Re-centered to 60% inventory / 95% AR / 40% PP&E** (aged farm whole-goods that ARTW itself built into a slow market, with beet equipment hit by the Dec-2025 44% American Crystal Sugar payment cut, realistically recover ~55–65%, not 70%; a single-purpose rural-Iowa plant ~35–45%). **Net ag disposal base falls $8.9M → $7.72M.** Bear/bull haircut ranges kept.
> - **Base FV revised DOWN, honestly.** Blended carve-out **base FV $2.69 → $2.46 (−4% vs price)**; SOTP-multiple base $2.58 → **$2.35 (−9%)**; prob-weighted **$2.77 → $2.60 (+1%)**. **The base is now fair-to-modestly-RICH vs the $2.58 price, not "+4% fairly valued."** I did **not** re-tune other inputs to hold it at the quote.
> - **Acquisition return worse:** at the FONR 31.5% premium ($3.39), base MOIC **0.79× → 0.73×** (deeper underwater); only the bull (1.44×, see v2.1 note) clears.
> - **OCF attribution verified (strengthens the carve-out):** the FY25 −$0.904M operating cash flow is an **AG** phenomenon — ag whole-goods built +$1.778M while *modular* inventory drew down ~$0.34M, and the modular contracts/billings swing is a one-time reversal of a FY24 over-billed position, not a structural sink. **Standalone modular is asset-light and cash-generative; shedding ag removes the cash drain.** See §A6.
> - Verdict re-framed (§12): **fairly-to-modestly-OVERVALUED on the standalone base**, with the return living entirely in the bull case + the friendly-carve-out option.
>
> **v2.1 reconciliation (2026-05-30, workbook build):** the bull *modular EV* was transcribed as $21.0M in v2, but the stated bull DCF inputs (+18/+14/…, 19% margin, 12% WACC, g 3%) actually compute to **$22.6M** (the terminal PV was understated). Reconciled here and in `ARTW_model.xlsx`: bull blend → **$21.3M**, bull equity → **$25.3M**, **bull FV $4.72 → $4.88 (+89%)**, **prob-weighted $2.60 → $2.64 (+2%)**, **bull MOIC 1.39× → 1.44×**. Base ($2.46) and bear ($1.04) unchanged; verdict unchanged. The workbook is authoritative for the bull case.

> **Headline finding (read this first — it is more sober than the thesis hoped).** Unlike the USNA template (net cash + a saleable stake ≈ the whole market cap, so the gem came free), **ARTW carries net debt and a very large ag-inventory balance.** When you value the modular gem standalone and net the *realistic* (v2-recentered) ag-disposal proceeds against the ~$6.4M of debt, the implied modular business is **not free — it sits at ~6–9× standalone EBITDA inside today's EV (~7.8× base), i.e., roughly fair-to-full.** Base-case carve-out fair value is **~$2.46/share (−4%)**; the stock is **fairly-to-modestly-OVERvalued on the standalone base**, with a real **balance-sheet floor** (passes both Graham tests) and a genuine but **bull-dependent** upside (+83%). The reverse-DCF says the ~$20M EV already embeds ~7% perpetual FCF growth — the market is *not* pricing this as a dying farm-equipment microcap; it is pricing a small, lumpy, mixed-quality industrial fully. **This is a "fairly-to-modestly-rich micro-cap with bull-case + friendly-carve-out optionality," not a mispriced free gem.** I make that case honestly below and show exactly where the (bull-only) return lives.

---

## 0. Verified facts (rebuilt from filings, not vendor aggregates)

All citations from the **FY2025 10-K** (period end 2025-11-30, filed 2026-02-12, [accession 0001437749-26-003904](https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000007623&type=10-K)), the **Q1 FY26 10-Q** (period end 2026-02-28), the **prior 10-K** (FY2024, for FY2023 segment data), and the **2026 DEF 14A** (filed 2026-03-12). Local copies in `data/edgar/artw/`.

| Item | Value | Source (10-K unless noted) |
|---|---|---|
| Consolidated sales FY23 / FY24 / FY25 | $30.281M / $24.499M / **$22.975M** (−6.2%) | Statements of Operations; XBRL `Revenues` |
| Operating income FY23 / FY24 / FY25 | $1.531M / $0.461M / **$0.289M** | Statements of Operations |
| Net income FY23 / FY24 / FY25 | $0.267M / $0.307M / **$1.035M** | Statements of Operations |
| **"Other income" FY25 (the ERC)** | **$1.514M** (vs $3K FY24) — Employee Retention Credit refunds | Statements of Operations; MD&A |
| → ERC by segment | **~$1.235M Ag + ~$0.226M Modular = ~$1.461M** | MD&A (Ag p.493, Modular p.494) |
| Pretax income FY25 | $1.437M (= $0.289M op + $1.148M other, mostly ERC less interest) | Statements of Operations |
| **Without the ERC, pretax ≈ −$0.02M to −$0.08M** (op income $0.289M − interest $0.367M + true other ≈ 0) | **near break-even / slight loss** | derived from the above |
| Income tax expense FY25 | $0.402M (28.0% book rate) | Statements of Operations; MD&A |
| **Cash income taxes PAID FY25 / FY24** | **$0.013M / $0.006M** (essentially zero) | Cash-flow stmt, supplemental disclosures |
| **Operating cash flow FY25** | **−$0.904M** (negative; inventory build + contracts-in-progress runoff) | Cash-flow stmt |
| Capex FY25 | $0.628M (PP&E) | Cash-flow stmt |
| D&A FY25 | $0.792M | Cash-flow stmt |
| **Cash (FY25 / Q1 FY26)** | **$0.0048M / $0.0029M** (near-zero) | Balance sheet; XBRL |
| Total debt FY25 | **$6.41M** = revolver $3.252M + term loans ($1.667M + $0.514M, incl. current $0.165M / LT $2.325M) + finance leases ($0.256M cur + $0.408M LT); incl. ~$0.309M SBA EIDL inside term | Balance sheet + MD&A Note 10 (p.506) |
| **Net debt** | **~$6.40M** (debt $6.41M − cash $0.005M) | derived |
| Revolver availability | $0.748M remaining on a $4.0M Bank Midwest line | MD&A (p.506) |
| Working capital / current ratio FY25 | **$8.34M / 2.30×** (FY24: $6.49M / 1.98×) | MD&A working-capital table (p.511) |
| Inventories FY25 (consolidated) | **$11.71M** (ag whole-goods up ~$1.778M YoY — built into a slow market) | Balance sheet; MD&A (p.505) |
| Shares outstanding | **5,184,084** (Mar-5-2026); 5,225,423 issued − 113,589 treasury at FY-end | DEF 14A (p.193); balance sheet |
| Control | **Marc McConnell (Chairman, President & CEO) 46.7%** (incl. McConnell Legacy Investments LLC 41.5%); directors & officers as a group **51.5%** | DEF 14A ownership table (p.554–599) |
| Coverage / float / liquidity | **0 analysts**; float ~2.04M sh (~39%); insiders ~59%; institutions ~6.7%; avg vol ~38K sh/day (~$0.1M/day) | yfinance snapshot; DEF 14A |
| 52-week range / book value | $1.69 – $4.71 / book $2.57 per share (stock ≈ **1.0× book**) | yfinance; balance sheet ($13.306M equity ÷ 5.184M) |
| Auditor | Eide Bailly LLP (PCAOB 286); ICFR effective; no material weakness | 10-K Item 9A |

### Segment financials, FY2023–FY2025 (CITED, 10-K Note 17 / prior 10-K Note)

| ($000) | FY23 | FY24 | FY25 |
|---|---|---|---|
| **Ag Products — revenue** | 22,467 | 14,663 | **12,749** (−13.1%) |
| Ag — gross profit | 6,584 | 4,155 | 2,977 (23.4% GM) |
| **Ag — operating income (loss)** | **+664** | **(1,510)** | **(1,462)** |
| Ag — total assets | 20,754 | 18,372 | **19,204** (inventory-heavy) |
| **Modular — revenue** | 7,814 | 9,836 | **10,226** (+4.0%) |
| Modular — gross profit | 2,000 | 3,155 | 3,290 (**32.2% GM**) |
| **Modular — operating income** | **+867** | **+1,971** | **+1,751** (**17.1% op margin**) |
| Modular — total assets | 2,593 | 2,869 | **3,274** (very asset-light) |
| Modular — D&A / capex FY25 | — | — | 251 / 222 |
| Consolidated op income | 1,531 | 461 | 289 |

*Read:* Modular revenue has risen **every year** (7.8 → 9.8 → 10.2) while Ag collapsed (22.5 → 14.7 → 12.7) and flipped to losses. **Modular runs ~17% operating margin on ~$3.3M of assets — a genuinely good little business. Ag is a cyclical, steel-cost-squeezed, $19M-asset anchor that lost ~$1.5M two years running.** The whole-company optics (op income $0.289M, "net income $1.035M") *entirely* mask this: the net income is an ERC artifact, and the consolidated op margin (1.3%) is the average of a 17% business and a money-loser.

### Backlog (CITED — strong leading indicator)

| As of Feb 2 | 2025 | 2026 |
|---|---|---|
| **Modular Buildings backlog** | $2,403K | **$4,882K (+103%)** |
| Ag Products net backlog | $3,486K | $3,224K (−7.5%) |

*Source: 10-K Item 1 "Backlog" (p.395).* Modular backlog **more than doubled** YoY — the single best filing-based evidence the modular momentum is real heading into FY26. Ag backlog is down slightly (beet equipment hurt by a 44% cut in American Crystal Sugar payment-per-ton announced Dec-2025; partly offset by livestock demand). The 10-K does **not** split modular backlog/revenue between the two legs — see §10 (data floor).

---

## A. Resolved / load-bearing assumptions (flagged cited vs. estimated)

### A1. The "FY25 net income $1.035M" is an ERC mirage — CITED.
The $1.035M net income is almost entirely the **$1.514M of "Other income," which is the Employee Retention Credit** ($1.235M Ag + $0.226M Modular, MD&A pp.493–494). Operating income was only **$0.289M**, and **operating cash flow was −$0.904M.** Strip the one-time ERC and ARTW was roughly **break-even to slightly loss-making** pretax in FY25. *This is the single most important normalization: do not capitalize the headline earnings.* The clean earning power is the **modular segment's $1.751M op income**, against an ag segment losing ~$1.5M and corporate cost.

### A2. Cash tax ≈ zero, but do NOT extrapolate a 0% forward rate — CITED then NORMALIZED.
Cash income taxes paid were **$13.4K (FY25)** and **$6.3K (FY24)** — the company shields nearly all cash tax via NOLs / a $2.06M deferred-tax asset (balance sheet). For the DCF I do **not** use 0%: I use a **15% cash rate** on standalone modular EBIT as a *normalized* assumption (NOLs are finite, and a profitable carve-out exhausts them), flagged as **normalized/judgment**. This is conservative-ish; the near-term real cash rate is lower, which is upside.

### A3. The two-leg split is ESTIMATED — this is the data floor (§10).
The 10-K gives only the modular *segment* total ($10.226M rev, $1.751M op inc) and two narrative breadcrumbs: (i) **agricultural-building sales rose ~$1.355M YoY** within modular (MD&A p.494), and (ii) "strong demand on the research side," citing xenotransplantation/cancer-research customers. The prompt's "+49%" implies an FY24 ag-building base of ~$2.77M → **FY25 ag-biosecurity leg ≈ $4.1M (~40% of modular)**, leaving **research/lab ≈ $6.1M (~60%)**. **I adopt 40/60 (ag-bio/research) as the base estimate and flag it as the key data-floor assumption.** Margins by leg are *not* disclosed; I assume research-lab carries the higher margin (complex BSL/vivarium, longer cycle) and ag-bio the lower (more standardized swine/animal buildings), but blend to the cited 32.2% segment gross margin.

### A4. Net debt is real and is carried by the modular co in the carve-out — CITED.
Unlike USNA, ARTW is **levered** (net debt ~$6.4M ≈ 48% of market cap). The revolver funds **ag inventory**, so in the carve-out the **ag-inventory liquidation is the primary source to retire that debt** — which is why the SOTP must net ag disposal *and* debt together (§1). This is the mechanical reason the gem is not "free."

### A5. Macro framing — CORRECTED against primary sources (filings/discipline win over the brief).
- **NIH / research-lab headwind is a *proposal/uncertainty* headwind, not an enacted cut.** The Administration's FY2026/FY2027 budget *proposed* deep NIH cuts and a **15% indirect-cost cap** (which directly funds university lab/animal-facility construction). **BUT** that 15% cap was **permanently struck down — the First Circuit upheld the injunction on Jan 6, 2026** ([Holland & Knight](https://www.hklaw.com/en/insights/publications/2026/01/the-nih-proposed-15-percent-indirect-cost-rate-cap-is-out-for-now); [Congress.gov CRS IN12516](https://www.congress.gov/crs-product/IN12516)). So the research-lab leg faces **budget *uncertainty* and a chilled academic-construction climate**, not a confirmed 40% cut. The brief's "40% NIH cut / 15% cap defunds construction" is a *risk scenario*, not current law. **Mitigant (and the leg's real strength): ARTW's research customers are not only NIH-academic** — the 10-K names **private research & pharmaceutical companies, government diagnostic/public-health centers, and xenotransplantation/cancer-research leaders** as buyers (Item 1 p.379; MD&A p.494). Non-NIH demand (pharma, biodefense/DoD, private diagnostics) is the diversification lever.
- **Ag/animal-biosecurity tailwind is real and current — CITED.** USDA's **Feb 26, 2025 up-to-$1B HPAI strategy** includes **$500M for on-farm biosecurity** (USDA cost-shares **up to 75%** of the highest-risk biosecurity fixes), $400M producer relief, and $100M vaccine/R&D ([USDA press release](https://www.usda.gov/about-usda/news/press-releases/2025/02/26/usda-invests-1-billion-combat-avian-flu-and-reduce-egg-prices)). This is the macro behind ARTW's **+$1.355M (≈+49%) ag-building sales** in FY25. It is **event-driven/cyclical** (tied to the HPAI outbreak and an annual funding decision), not a secular annuity.

### A6. The FY25 negative operating cash flow is an AG phenomenon — VERIFIED (strengthens the carve-out). [v2]
The FY25 consolidated **OCF was −$0.904M**. Decomposing the working-capital swings against the segment/MD&A disclosures:
- **Inventory consumed $1.437M of cash consolidated; the *Ag* whole-goods build alone was +$1.778M** (MD&A p.505: ag inventory "up approximately $1,778,000," built deliberately "despite slow demand in anticipation of improving agricultural markets"). That implies **Modular inventory actually *drew down* ~$0.34M.** The inventory cash sink is **entirely Ag.**
- The **"contracts in progress, net" −$1.665M** swing is **Modular**, but it is a **one-time reversal of a FY24 over-billed position** — "Billings in excess of cost and profit" fell from **$1.929M (FY24) → $0.431M (FY25)** as ARTW worked off larger projects it had collected on ahead of cost. That is a **timing reversal of a prior-year cash *inflow*, not a structural sink**; MD&A explicitly expects to "utilize favorable billing schedules in our Modular Buildings segment in fiscal 2026 to help fund operations."
- **Modular is structurally asset-light and cash-generative:** $3.274M total assets, $0.222M capex, $1.751M operating income, 32.2% gross margin. **Shedding Ag removes the inventory cash drain** and leaves a business whose own cash conversion is sound. This **supports the carve-out logic** and validates the DCF's modest WC treatment (10% of *incremental* revenue) — modular WC is project-timing-driven (over/under-billing nets toward zero over a cycle), not a permanent build like ag whole-goods. *No change to the DCF WC assumption.*

---

## 1. Sum-of-the-Parts (the centerpiece) — the gem is NOT free

The carve-out value = **(Modular standalone EV) + (net Ag disposal proceeds) − (net debt at close)**. Ag disposal proceeds and net debt are netted together because the revolver funds ag inventory.

### 1a. Modular (Art's-Way Scientific) standalone EV
Standalone EBITDA = segment EBITDA $2.002M (op $1.751M + D&A $0.251M) **less ~$0.45M incremental standalone corporate/public-company cost** (only ~$0.18M corporate was allocated to modular in the segment table; a standalone registrant carries more) = **~$1.55M base standalone EBITDA** *(normalized)*. Multiples from `peer_benchmarks.csv` (project-based builder, FONR ~7–9× as the base anchor, WSC's 11.7–14.5× leasing multiple as an explicit unreachable ceiling):

| Scenario | EBITDA used | EV/EBITDA | **Modular EV** | EV/rev cross-check |
|---|---|---|---|---|
| Bear | $1.40M | 5.0× | **$7.0M** | ~0.7× |
| **Base** | $1.55M | 7.0× | **$10.9M** | ~1.1× |
| Bull | $2.00M | 10.0× | **$20.0M** | ~1.6× |

### 1b. Ag Products disposal value (orderly wind-down — Vessels/Tools precedent) [v2 RE-CENTERED]
Ag loses money → **no franchise/going-concern premium; value it as recoverable net assets.** Ag total assets $19.2M are mostly **inventory** (est. ~$9.5M of the $11.7M consolidated, whole-goods-heavy), **AR** (~$1.6M), and **PP&E** (the Armstrong plant, ~$4.5M of the $5.08M consolidated). Recovery haircuts (all **estimated**).

> **v2 re-centering of the BASE (reviewer push 1).** v1's base used 70% inventory / 45% PP&E → net $8.9M, which landed base FV at *exactly* the $2.58 quote — an anchoring red flag. Two filing-cited facts make 70% too generous: (i) ARTW itself **built ~$1.778M of ag whole-goods into a slow market** (§0/§A6), i.e., this is *aged, slow-moving* equipment, and (ii) **beet equipment was hit by the Dec-2025 44% American Crystal Sugar payment-per-ton cut** (§0 backlog note), impairing a whole product line's resale. Aged farm whole-goods through a dealer/auction channel over a 12–18-month orderly wind-down realistically recover **~55–65%, not 70%**; a single-purpose rural-Iowa (Armstrong) plant recovers **~35–45%** (the 2024 Tools real-estate sale at $1.8M is a useful but not directly comparable data point). **Base re-centered to 60% inventory / 95% AR / 40% PP&E.** Bear/bull ranges unchanged.

| Scenario | Inventory | AR | PP&E | **Gross disposal** | Wind-down cost | **Net** |
|---|---|---|---|---|---|---|
| Bear (liquidation) | 50% | 85% | 30% | $7.5M | −$2.0M | **$5.5M** |
| **Base (orderly) [v2]** | **60%** | **95%** | **40%** | **$9.0M** | **−$1.3M** | **$7.7M** |
| Bull (going-concern sale) | 75% | 100% | 55% | $11.2M | −$0.8M | **$10.4M** |

Wind-down cost = severance, lease breakage, warranty/dealer tail, transaction. **Precedent: ARTW divested Tools (2015, real estate sold 2024 for $1.8M) and Vessels (2016) to refocus** — the divest-a-segment playbook is internal and proven (10-K Note 1(a)/(b) p.724–726).

### 1c. SOTP roll-up — carve-out equity [v2 RE-CENTERED]

| | Modular EV (mult) | Net Ag disposal | − Net debt | **Equity** | **$/share** | vs $2.58 |
|---|---|---|---|---|---|---|
| Bear | $7.0M | $5.5M | $6.4M | $6.0M | **$1.16** | −55% |
| **Base** | $10.9M | $7.7M | $6.4M | $12.2M | **$2.35** | **−9%** |
| Bull | $20.0M | $10.4M | $6.4M | $24.0M | **$4.63** | +80% |

### 1d. **Is the modular gem priced free/cheap inside the ~$20M EV? — NO, it's fair-to-full.** [v2]
Reverse the SOTP — strip the **net ag disposal** out of today's EV and see what's left for modular:

| Ag valued at… | EV $19.8M − net ag disposal = **implied Modular EV** | Implied Modular EV/EBITDA |
|---|---|---|
| Base orderly ($7.7M) | **$12.1M** | **~7.8×** |
| Bull going-concern ($10.4M) | **$9.4M** | ~6.0× |
| Bear liquidation ($5.5M) | **$14.3M** | ~9.2× |

**With the recentered ag mark, the market is implying the modular business at ~6–9.2× standalone EBITDA (~7.8× base) — fair-to-full, not free.** Contrast USNA, where net cash + the Hiya stake ≈ the whole market cap and the core came free. **Here there is no cash cushion and the ag inventory, while a real asset, is largely offset by the debt it financed AND recovers at a real haircut.** *This is the honest center of the analysis and the reason the verdict is "fairly-to-modestly-rich," not "cheap."*

---

## 2. Operating / driver model — Art's-Way Scientific standalone, two legs

**Leg split is ESTIMATED (§A3, the data floor): 40% ag-biosecurity / 60% research-lab of FY25's $10.226M.**

```
Modular standalone revenue (FY25 base $10.23M)
├── RESEARCH / BIOCONTAINMENT LABS  ≈ $6.1M (60%)   [higher margin, stickier]
│     drivers: # lab projects/yr × avg contract value (BSL-3/vivarium $1–5M each; 6-mo build)
│     buyers: academic (NIH-funded) + PRIVATE pharma + gov diagnostic/public-health + biodefense/DoD
│     macro path: NEAR-TERM CHILL from NIH budget uncertainty (cap struck down Jan-2026 but climate
│                 cautious) → SECULAR TAILWIND (life sciences, biosecurity, xenotransplant/cancer research)
│     base path: flat-to-+3% near-term (academic caution), reaccelerating to +5–7% as non-NIH buyers grow
│
└── AG / ANIMAL-BIOSECURITY BUILDINGS ≈ $4.1M (40%)  [lower margin, event-driven]
      drivers: # animal-facility projects × value; swine/livestock/poultry biosecurity demand
      macro path: CURRENT TAILWIND from USDA up-to-$1B HPAI/biosecurity push ($500M cost-share @75%);
                  drove FY25 +$1.355M (+49%). CYCLICAL/EVENT-DRIVEN — fades if HPAI recedes / funding lapses.
      base path: +49% FY25 does NOT repeat; model +5% FY26 then revert toward GDP-ish +2–3%, with a
                 one-time give-back risk if USDA funding is not renewed.
Blended segment: ~32% gross margin (cited), ~17% op margin (cited), lumpy/project-based (non-recurring).
Backlog $4.88M (Feb-2026, +103% YoY) underwrites ~6 months of revenue visibility.
```

**Why the two-leg framing matters:** the legs are **negatively correlated on policy** — when the research leg is chilled by federal-science budget fights, the ag-bio leg is being *funded* by a different federal pocket (USDA biosecurity). That partial hedge is the most attractive structural feature of the standalone, and it is *not* something a single "modular farm-building" tag captures.

### 2b. Standalone modular DCF (scenario, cash taxes, explicit FCF) — the EV/equity bridge shown

WACC built for a micro-cap, project-based, illiquid, single-plant business (CAPM-style, **judgment**): rf ~4.3% + β·ERP (β~1.4, ERP ~5.5% ≈ 7.7%) + **size/illiquidity premium ~3–4%** + project-concentration premium → **base WACC 13.5%** (bear 15%, bull 12%). Cash tax 15% (§A2). D&A and capex each ~2.5% of revenue (asset-light, p.1131). 10% WC drag on incremental revenue. **Standalone modular carries NO net debt in the DCF EV (debt is retired by ag disposal — see the reconciliation in §1c/§3).**

| Scenario | Rev path (yr1→) | EBITDA margin | WACC | term g | PV(FCF yr1-7) | PV(terminal) | **Modular EV** |
|---|---|---|---|---|---|---|---|
| Bear | −10%,−5%,0,+2%… | 13% | 15.0% | 1.0% | $3.4M | $2.3M | **$5.7M** |
| **Base** | +8,+6,+5,+4,+4,+3.5,+3% | 16% | 13.5% | 2.5% | $6.0M | $6.1M | **$12.1M** |
| Bull | +18,+14,+10,+8,+6,+5,+4% | 19% | 12.0% | 3.0% | $8.6M | $14.0M | **$22.6M** |

*Year-by-year base FCF (illustrative):* yr1 rev $11.0M → FCF ~$1.0M; yr7 rev $14.2M → FCF ~$1.6M; terminal on yr7 FCF × (1.025)/(0.135−0.025). The DCF base modular EV ($12.1M) corroborates the SOTP-multiple base modular EV ($10.9M) — within ~10%, so the **base modular EV ≈ $11–12M** is robust across both methods.

---

## 3. Carve-out equity bridge — DCF and multiple reconciled (math shown, no black box)

**Bridge:** `Modular EV + (Ag gross disposal − wind-down cost) − net debt = carve-out equity.` Net debt $6.40M; shares 5.184M.

| | Modular EV (DCF) | Modular EV (mult) | **Blend** | + Net ag disp [v2] | − Net debt | **Equity** | **$/sh** | vs $2.58 |
|---|---|---|---|---|---|---|---|---|
| Bear | $5.7M | $7.0M | $6.3M | $5.5M | $6.4M | $5.4M | **$1.04** | −60% |
| **Base** | $12.1M | $10.9M | $11.5M | $7.7M | $6.4M | $12.8M | **$2.46** | **−4%** |
| Bull | $22.6M | $20.0M | $21.3M | $10.4M | $6.4M | $25.3M | **$4.88** | +89% |

**Probability-weighted (30/45/25): FV ≈ $2.64/share, +2% vs $2.58 → ~+0.8%/yr over 3 years.** Essentially **no margin of safety on the standalone base** — the return is entirely in the bull tail and the friendly-carve-out option (below). *(v1 reported $2.69 base / $2.77 prob-weighted on the now-corrected $8.9M ag mark; the recentered $7.7M mark drops base to $2.46 / prob-weighted to $2.64 [v2.1 bull reconciliation].)*

**Whole-company acquisition return (the operator's question):** an acquirer must pay a control premium. At the **FONR precedent 31.5% premium**, the buy-in is **$3.39/share (~$17.6M equity, ~$24M EV)**. Realizing the **base** carve-out FV ($2.46) is a **0.73× MOIC — underwater** (worse than v1's 0.79× on the recentered ag mark); only the **bull** ($4.88 = **1.44× MOIC**) makes the deal work; the bear (0.31×) is a wipe. **So the carve-out is *not* an attractive acquisition at a normal premium on the base case — it requires the bull (modular re-rates to ~10× as a clean, growing biocontainment platform with a doubled backlog) to clear a buyer's hurdle.** That is the disciplined conclusion, and the recentered ag mark only sharpens it.

---

## 4. Value lenses & financial-condition tests (Graham/Buffett cross-checks)

| Lens | Result | Read |
|---|---|---|
| **EPV (modular-only, no growth)** | NOPAT ~$1.32M ÷ 13.5% − net debt $6.4M = **~$0.65/sh** | After loading full net debt on modular alone, **no-growth value is well below price** → you are paying for growth + the ag asset recovery. |
| **Reverse DCF** | EV $19.8M on ~$1.2M normalized FCF implies **g ≈ 7.4% perpetual** | The market is **not** pricing decline — it embeds mid-single-digit+ growth. The stock is **not cheap on embedded expectations.** |
| **Owner-earnings yield** | Normalized FCF $1.2M ÷ mkt cap $13.4M = **~9%** | Decent cash-on-equity *if* you believe $1.2M normalized FCF (ERC-stripped, ag at breakeven). |
| **Graham NCAV (net-net)** | CA $14.78M − total liab $9.17M = $5.61M = **$1.08/sh** | Not a net-net at $2.58, but a real downside marker (~42% of price covered by net current assets alone). |
| **Graham financial-condition test** | Current ratio **2.30× (≥2.0 ✔)**; LT debt $2.73M **≤** working capital $8.34M (✔) | **PASSES BOTH.** Unlike HCKT (which failed), ARTW has a genuine static **balance-sheet floor** — the downside is partly asset-backed (inventory + plant + 1.0× book), not carried solely by earning power. |

**The lenses agree with the SOTP:** roughly fairly valued, real asset floor, upside requires growth to show up. Book value $2.57 ≈ price $2.58 — the market is paying ~1.0× book for a business that earns its cost of capital only if the modular growth continues.

---

## 5. Sensitivity tornado (swing in base FV $2.46, each driver flexed alone) [v2]

| Rank | Driver | Range tested | FV low → high | **Swing ($/sh)** |
|---|---|---|---|---|
| 1 | **Modular EBITDA multiple / re-rate** | 5× → 10× (DCF WACC 15%→12%) | $1.55 → $3.77 | **$2.22** |
| 2 | **Modular standalone EBITDA (margin × leg growth)** | $1.3M → $2.0M | $2.00 → $3.15 | **$1.15** |
| 3 | **Ag disposal value (inventory/PP&E recovery)** | $5.5M → $10.4M net | $2.03 → $2.98 | **$0.95** |
| 4 | **Net debt at close** | $7.5M → $5.0M | $2.25 → $2.73 | **$0.48** |
| 5 | **Ag wind-down cost** | $2.5M → $0.5M | $2.23 → $2.62 | **$0.39** |

**The answer hangs on the modular multiple and modular EBITDA** — i.e., *does the standalone re-rate to a clean ~7–10× biocontainment platform and does the two-leg growth show up?* The **ag-disposal swing rose to $0.95 in v2** (the wider, more honest recovery range now spans bear liquidation to bull going-concern) but is still **third** — the re-rate and EBITDA dominate. The two-leg revenue paths feed driver #2. **The whole thesis is a bet on the modular re-rate + growth, not on the ag salvage.**

---

## 6. Porter's Five Forces — specialty modular research/biocontainment niche

| Force | Intensity | Evidence |
|---|---|---|
| **Rivalry** | **Moderate** | Niche has few turnkey biocontainment specialists (CERTEK, Modular Genius; broad modular: BOXX, Vanguard, WSC). ARTW claims niche leadership (20+ vivariums, 15+ BSL-3, 150+ units; UC Davis, ADM, Stowers, etc.). Custom/relationship-driven, not price-bid commodity. |
| **Buyer power** | **Moderate-high** | Project-based, lumpy; large institutional/government buyers (universities, USDA, pharma) hold negotiating power and control funding timing. One customer = 9% of consolidated revenue (10-K p.414). Backlog lumpiness = buyer-timing risk. |
| **Supplier power** | **Low-moderate** | Steel + standard building materials; steel +26% in FY25 hit ag, less so modular (pass-through on custom contracts). Self-fabricates. |
| **Substitutes** | **Moderate** | Conventional design/build (2–5 yrs vs ARTW's ~6 mo — a real speed moat for time-critical labs), plus other modular fabricators. The speed advantage is the genuine differentiator (10-K p.411). |
| **New entrants** | **Low-moderate** | 10-K cites high barriers: established customer relationships, regulatory/code expertise (BSL containment), qualified labor, bidding-process access. But a skilled fabricator *could* adapt facilities. |

**Net read → margin durability:** the niche is **defensible enough to support the ~17% operating / ~20% EBITDA margin** (above the ~7% construction-modular norm) because of the **speed-to-delivery + containment-code expertise + reputation** moat — this is what justifies a multiple in the FONR ~7–9× band and **above** generic project-builders. It is **not** WSC-like (no recurring lease ROIC), so it does **not** deserve a 12–14× leasing multiple. The Porter read **supports the base 7× and caps the bull at ~10×.**

---

## 7. Consensus baseline (what's priced in)

- **Coverage: ZERO analysts.** Pure neglect/orphan micro-cap. Float ~2.0M sh, ~$0.1M/day volume — **un-investable for any institution**; ~6.7% institutional, ~59% insider. This is the textbook "too-small-for-institutions + activism-vacuum" mispricing setup — but neglect is only an opportunity *with a catalyst* (methodology §17), and the controlling family is the catalyst gate.
- **What the ~$20M EV implies:** per the reverse DCF, ~7% perpetual FCF growth — the market is **already** giving credit for modular growth and is **not** pricing ARTW as a melting farm-equipment microcap. The implied ~5.6–9× modular EV/EBITDA is fair. **There is no obvious gross mispricing to arbitrage; the variant, if any, is that the *quality and growth* of the standalone modular (doubled backlog, two-leg policy hedge) is better than a blended-microcap screen shows — a quality/optionality argument, not a "free asset" argument.**
- **Precedent-transaction anchor — FONR:** CEO-led take-private, Dec-2025, **$19.00/sh, 31.5% premium, ~0.94× rev / ~7–9× EBITDA, ~$98.6M** ([8-K/DEFA14A](https://www.sec.gov/Archives/edgar/data/0000355019/000173112225001734/fonar_exhibit-99.htm)). Tells us: (a) a friendly control-holder take-out of a neglected profitable health-adjacent micro-cap clears at ~7–9× EBITDA + ~31% premium, and (b) **at that premium the ARTW base case is underwater** — consistent with §3.
- **Broad-modular comps:** US modular construction ~$20.3B (2024), ~4.5–6.2% CAGR ([MBI/Technavio](https://www.technavio.com/report/us-modular-construction-market-analysis)); WSC 11.7–14.5× EV/EBITDA (leasing, not comparable). Construction sector median ~10.3× ([Statista](https://www.statista.com/statistics/1030142/)).

**Mispricing diagnosis:** Neglect (0 analysts, illiquid) + Segment opacity (a 17%-margin gem averaged with a money-loser in the headline) — both *real* — but **not** a gross undervaluation, because the reverse-DCF shows growth is already in the price. **Closest classification: neglect + opacity that compresses the *quality* perception, gated on a catalyst the family controls.** Not "misperception of a free asset."

---

## 8. Value-creation plan (the carve-out playbook)

| Lever | Action | Comp-proven / precedent |
|---|---|---|
| **Divest/wind down Ag** | Orderly exit of the loss-making farm-equipment segment; redeploy ~$8–10M of trapped ag inventory + plant to retire the revolver and fund modular capacity. | **Internal precedent:** ARTW divested **Tools (2015)** and **Vessels (2016)** to refocus, and sold Tools real estate for $1.8M (2024). The playbook is proven inside this company. |
| **Re-rate modular standalone** | Surface Art's-Way Scientific as a clean, ~17%-margin, growing biocontainment platform — a stand-alone story a buyer/market can multiple at 7–10× instead of burying it in a microcap conglomerate. | FONR ~7–9× EBITDA take-out; construction median ~10×. |
| **Diversify research-lab buyers off NIH** | Lean into **private pharma, biodefense/DoD, and private diagnostics** (already named customers) to de-risk the academic/NIH-budget headwind. | 10-K already names pharma + gov diagnostic + xenotransplant/cancer-research clients (p.379, 494). |
| **Capitalize on the USDA biosecurity window** | Press the animal-biosecurity leg while the $500M USDA cost-share (75%) is live; lock multi-year framework/repeatable contracts to smooth the lumpiness. | USDA Feb-2025 $1B HPAI plan; FY25 +49% ag-building proof. |
| **Roll up the fragmented niche** | The **untapped lever**: ARTW has *never* rolled up within modular (only divested). Tuck in small biocontainment/lab fabricators (CERTEK-type) to add scale + recurring service/lease revenue and lift the multiple toward WSC's leasing model. | WSC built its multiple via lease-fleet roll-up; ARTW already offers a lease option (p.379) — under-exploited. |
| **Professionalize commercial/sales** | FY25 lost its director of sales (not replaced) and President Dan Palmer is going part-time (p.493–494) — a thin, key-person-dependent commercial org. Build a real sales engine. | — |

---

## 9. Kill criteria (monitorable thresholds)

| Pillar / Risk | Metric | Kill threshold | Source | Next data point |
|---|---|---|---|---|
| Modular momentum real | Modular backlog (Feb each yr) | Falls back below ~$2.5M (gives back the FY26 doubling) | 10-K Item 1 Backlog | FY26 10-K (Feb 2027) |
| Research-lab leg vs NIH | Research-lab order trajectory / academic project starts | Research orders down YoY two straight quarters | 10-Q MD&A / calls | Q2–Q3 FY26 |
| USDA biosecurity tailwind | USDA HPAI/biosecurity funding renewal; ag-building sales | $500M cost-share not renewed AND ag-building sales revert below FY24 | USDA appropriations; 10-K segment narrative | FY26 appropriations / FY26 10-K |
| Ag cash burn | Ag segment operating loss + ag inventory | Ag op loss > $1.5M again AND inventory not converting to cash | 10-K Note 17 | FY26 10-K |
| Capacity / margin | Modular operating margin | < 12% for a full year (the moat eroding) | 10-K Note 17 | FY26 10-K |
| Liquidity | Revolver headroom / operating cash flow | Revolver fully drawn ($4.0M) AND OCF negative two years | Balance sheet / cash-flow | each 10-Q |
| Catalyst (control) | McConnell family / Form 4 / 8-K | Family signals no strategic action AND keeps ag indefinitely | Form 4 / 13D / 8-K | ongoing |

---

## 10. Known-unknowns / data floor

The data wall, and what would close it:
1. **The two-leg split (research-lab vs ag-biosecurity) — THE FLOOR.** Not disclosed. I estimate **40/60** from the single "+$1.355M ag-building" breadcrumb (§A3). Revenue *and* margin by leg, and backlog by leg, are unknown — and they are the #2 tornado driver. *Closes only with:* management/IR calls, or if ARTW ever breaks the legs out. **Everything in the two-leg model below the segment total is estimated.**
2. **Ag inventory composition & recoverability.** I estimate ag holds ~$9.5M of the $11.7M consolidated inventory and that it liquidates at 55–80%. The actual saleability of aged whole-goods (beet equipment hurt by the American Crystal Sugar payment cut) is the swing on disposal value. *Closes with:* inventory-aging detail (not disclosed), dealer/auction-channel checks.
3. **Standalone corporate cost.** I add ~$0.45M of incremental standalone public-company/parent cost to the modular carve-out; the true number depends on deal structure (full take-private removes public-co cost entirely — upside).
4. **Modular customer/contract concentration & pipeline.** One customer = 9% of consolidated revenue; backlog is lumpy. Named marquee clients exist but contract-level concentration within modular is not disclosed. *Closes with:* primary research (former employees, named customers like UC Davis/Stowers).
5. **Family intent (the catalyst).** 51.5% insider control + a struck-down voting-trust flag (see §11) make any outcome **family-gated.** There is **no** filing evidence of a strategic review, sale, or take-private. We are inferring *capability and logic* (FONR-style), not intent. *Closes only* via an actual 8-K/13D.

**Bottom line on depth:** the filings give us a clean segment history, backlog, balance sheet, cash taxes, and the ERC normalization cold. They do **not** give the leg-level split — that is the floor, and it is exactly the variable the upside hangs on. To go deeper requires **primary research** (IR/management on the leg mix and pipeline; former employees; named-customer reference checks) — the next marginal step.

---

## 11. Structural gates (reported honestly)

- **`check_voting_structure.py ARTW` → DEAL_BREAKER:** "Voting trust controls 67.0% of voting power — hostile/unsolicited take-private structurally impossible." The proxy confirms **McConnell 46.7% / directors-officers group 51.5%** outright majority. Whether the historical "voting trust" 67% figure is current or stale, the conclusion is the same: **a hostile deal is impossible.** Per TODO's deferred friendly-transaction framework, **the entire carve-out thesis is explicitly conditioned on a *friendly, negotiated* transaction with the McConnell family** — modeled as an assumption, flagged as the binding catalyst gate, not ignored.
- **`check_deal_status.py ARTW` → NONE / LOW:** no deal signals in trailing-24-month 8-Ks or news. No live process. Confirms the catalyst is *latent*, not imminent.

---

## 12. Verdict — framed as the discount driver

**Is the market wrong to price ARTW as a dying farm-equipment microcap, missing a tailwind-exposed + secular modular gem?** *No — and the recentered v2 numbers make that answer sharper.* The market is **not** pricing ARTW as a melting ice cube: the reverse-DCF shows the ~$20M EV already embeds ~7% perpetual FCF growth, and the implied standalone modular multiple inside the EV is **~6–9.2× EBITDA (~7.8× base) — fair-to-full, not free.** The depth here did the opposite of USNA: it *deflated* a hopeful "free gem" thesis to a calibrated "fairly-to-modestly-rich with bull-only optionality."

**What is true and good:** (i) the modular segment is a genuine ~17%-margin, asset-light, **cash-generative** (§A6) and **growing** business with a **+103% YoY backlog** and a rare **two-leg policy hedge** (USDA-funded ag-biosecurity tailwind *now* + secular research-lab demand), (ii) the headline earnings/optics **understate** modular's quality by averaging it with a money-losing ag segment and flattering net income with a one-time ERC, and (iii) the balance sheet **passes both Graham tests** — there is a real asset floor (NCAV $1.08, book $2.57 ≈ 1.0×).

**What kills the "cheap" claim:** **net debt (~$6.4M) and a large *aged* ag-inventory balance that recovers at a real haircut** mean the gem is not free once you net realistic disposal proceeds (v2: $7.7M, not $8.9M) against the debt; on the recentered base the **standalone is modestly *over* fair value (−4%)**; and at a normal control premium (FONR's 31.5%), the **base-case acquisition is underwater (0.73× MOIC).**

**Standalone Art's-Way Scientific FV (the carve-out), blended DCF + multiple [v2 recentered]:**
- **Bear $1.04 (−60%)** · **Base $2.46 (−4%)** · **Bull $4.72 (+83%)** · prob-weighted **$2.60 (+1%, ~+0.3%/yr).**

**Rough whole-company acquisition return (buy at 31.5% premium = $3.39):** base **0.73× MOIC (loss)** · bull **1.39×** · bear **0.31×.** **The deal works only on the bull** (modular re-rates to a clean ~10× biocontainment platform with the doubled backlog converting and the niche roll-up beginning).

**The catalyst:** there is no organic re-rate without action, and **all action is gated on the McConnell family (51.5%).** The credible path is a *friendly* family-led take-private or a strategic-sale of the modular unit + ag wind-down — exactly the FONR template. Absent that, neglect persists and the stock stays roughly at/above fair value.

**Call:** **FAIRLY-TO-MODESTLY OVERVALUED on the standalone base, with the entire return in the bull case + a friendly-carve-out call option.** Not a mispriced free asset (the USNA setup); not a value trap (it passes the asset-floor tests and the modular business is real and growing). **The honest position: there is no margin of safety at $2.58 on the base case — you are paying slightly above standalone fair value for a decent micro-cap, compensated only by (a) the bull tail (+83%) if the modular re-rate + two-leg growth show up, (b) a hard balance-sheet floor, and (c) the family-gated carve-out option.** The risk/reward is *asymmetric to the upside in payoff* but **negative in expectancy on the base** — you need conviction in the bull, not just the floor, to underwrite it. **The single fact that decides it:** the **leg-level split and the durability of the modular growth** (data floor, §10) — if research-lab is more resilient and ag-bio more repeatable than the lumpy history suggests, the bull is live; if the FY25 ag-building +49% was a one-time HPAI spike and research stays chilled, the base ($2.46, *below* the price) is the ceiling and the deal doesn't clear a buyer's premium.

**Was the depth worth it?** Yes — and the v2 review proved it twice over. v1 prevented a false "free gem" conclusion; the reviewer's ag-disposal push then caught that v1's base had been *tuned to the quote* ($2.58 exactly) by an over-generous 70% inventory recovery, and recentering to a defensible 60%/40% mark moved the base from "+4% fairly valued" to "**−4%, modestly rich**" — flipping the honest read from "fair" to "fair-to-rich, bull-only." The SOTP's netting of ag disposal against net debt, the ERC normalization, the reverse-DCF (growth already priced), the OCF-attribution check (the cash sink is ag, not modular — §A6), and the FONR acquisition math each independently pushed the verdict away from "cheap." The thesis survives only as a **bull-case + optionality** case, not a **mispricing** case.
