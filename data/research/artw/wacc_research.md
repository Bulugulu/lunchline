# ARTW / Art's-Way Scientific — Discount Rate (WACC) Recommendation

**Subject:** Standalone "Art's-Way Scientific" modular-buildings segment, valued as a **friendly take-private of the whole company by a control operator** who runs the modular business standalone and winds down the loss-making ag segment.
**Question pressure-tested:** Is the model's base **WACC = 13.5%** right? Hypothesis is **~12.5%**.
**Date:** 2026-05-31. **Author:** valuation research (agent build).

> **Bottom line up front:** Recommend **base WACC = 12.5%**, range **11.5%–14.0%** for the control / take-private DCF. The hypothesis holds. The current 13.5% is **modestly too high by ~100 bps**, because part of the model's "3–4% size/illiquidity premium" is a *security-marketability/minority-illiquidity* charge that a **control acquirer of the operating cash flows does not bear** and should drop. The *fundamental* size + single-plant + concentration + lumpiness risk is real and stays — which is why we do **not** go below ~11.5%. This is the **unlevered cost of capital for the DCF**, and is conceptually distinct from the **20–25% levered-equity IRR hurdle** an LBO sponsor would target (reconciled in §4).

---

## 1. Build-up table (control / private-operating-business cost of capital)

I build the operating (unlevered) cost of capital bottom-up and cross-check against CAPM and against private-market survey returns. Every line is marked **[cited]** or **[judgment]**.

| Component | Value | Basis | Cited / Judgment |
|---|---:|---|---|
| Risk-free rate | **4.3%** | 10-yr UST 4.46% (May 29 2026); Kroll normalized RF 3.5% w/ spot-20yr higher-of. We split the difference toward a long-bond ~4.3–4.5%. | [cited] inputs; [judgment] point pick |
| Equity risk premium (ERP) | **5.0%** | Kroll Recommended U.S. ERP **5.0%** (eff. Sep 2 2025); Damodaran implied ERP **4.33%** (Jan 1 2025). Use Kroll's 5.0% as the normative anchor. | [cited] |
| Beta adjustment (β·ERP vs. raw ERP) | **+1.0 to +2.0%** | Industrial/construction levered β ≈ 1.1–1.4; β·ERP ≈ 5.5–7.0% vs. raw 5.0%. The segment is project-cyclical → keep β > 1. | [judgment] from peer β |
| **Fundamental size premium** | **+3.0%** | Kroll CRSP 10th-decile size premium **4.7%** (cos. ≤ $212.6M mkt cap; ARTW ≈ $13M sits in micro-cap 10z). We **haircut to 3.0%**: the literature warns the smallest 10z firms are "small for a reason" (distress) and are poor proxies for a *healthy, ~20%-EBITDA-margin* private operator, so the raw 4.7% overstates *this* company's systematic size risk. | [cited] raw figure; [judgment] haircut |
| **Company-specific risk premium (CSRP)** | **+1.5 to +2.0%** | Single 50k-sqft plant (no redundancy), ~9% customer concentration, lumpy project revenue, no recurring revenue, 0 analyst coverage. CSRP literature range is **1%–6%**; these are textbook CSRP factors. We sit mid-low because margins are high and the niche (BSL-3 / biocontainment) is defensible. | [cited] range; [judgment] point |
| **Security-marketability / minority-illiquidity premium** | **0.0% (DROPS OUT)** | A DLOM/illiquidity charge compensates a *minority holder who cannot exit*. The premise here is a **control buyer of the whole operating business**, so this component is **not borne on the operating cash flows** (see §3). | [judgment], standard valuation theory |
| **Indicated unlevered cost of capital (build-up)** | **≈ 12.0–13.5%** | Sum of above ranges. | — |
| CAPM cross-check | 4.3 + 1.3·5.0 + 3.0 size + 1.5 CSRP ≈ **15.3% raw / ~12.5% after control adjustment** | — | [judgment] |
| Private-market survey cross-check | PE buyout target net IRR **15–25%**; that is a *levered equity hurdle*, an upper bound on a *levered* required return, not the unlevered WACC (see §4). | [cited] | — |
| **RECOMMENDED BASE WACC** | **12.5%** | Center of the converged range; control adjustment applied. | **[judgment]** |
| Recommended range | **11.5% – 14.0%** | Bull / base-stress to bear. | [judgment] |

**Reconciliation to the old 13.5%:** old build was RF 4.3% + β·ERP ~7.7% + size/illiquidity ~3–4% + project-concentration premium. Two things change: (a) ERP normalized to **5.0%** (Kroll current) rather than ~5.5%, and (b) the **illiquidity slice of the 3–4% block is removed** for a control buyer. Net ≈ **−100 bps → 12.5%**.

---

## 2. Build-up specifics for a sub-$50M company (the figures)

- **Risk-free rate:** 10-yr UST **4.46%** (May 29 2026); Kroll's normalized RF is **3.5%**, applied as the *higher of* normalized or the spot 20-yr Treasury at the valuation date. Practical pick for a long-horizon DCF: **~4.3%**. [cited]
- **Equity risk premium:** **Kroll Recommended U.S. ERP = 5.0%** effective **Sep 2 2025** (it has oscillated 5.0%↔5.5% across 2024–25; was raised to 5.5% Apr 15 2025, lowered to 5.0% Sep 2 2025). **Damodaran implied ERP = 4.33%** as of Jan 1 2025 (10-yr at 4.58%). Using **5.0%** is defensible and conservative-normative. [cited]
- **Size premium (the key micro-cap figure):** Kroll CRSP Deciles Size Study **10th-decile size premium = 4.7%** for companies with market cap **≤ $212.6M**. Kroll further splits decile 10 into **10w/10x/10y/10z** (10z smallest); a **~$13M** cap like ARTW sits in **10z**, where raw premia run higher still. **Caveat (cited):** Crain's 2025 work and the Pepperdine/Journal-of-Entrepreneurial-Finance literature warn that subdividing decile 10 is statistically fragile and that the smallest listed firms are disproportionately *distressed/unprofitable* ("small for a reason"), so a raw 4.7%+ overstates the systematic size risk of a *profitable* private operator. We therefore **carry 3.0%**, not 4.7%. [cited raw / judgment haircut]
- **Company-specific risk premium:** CSRP literature range **1%–6%**; classic CSRP drivers — **customer/geographic/product concentration, single-plant/key-asset dependence, lumpy earnings, thin management depth** — are exactly ARTW Scientific's profile. Defensible CSRP here: **1.5–2.0%** (mid-low, because margins are high, niche is defensible/regulated, and some concentration risk is already in the size figure). [cited range / judgment point]

---

## 3. The core judgment: split the "3–4% size/illiquidity" block

The model lumps "size/illiquidity ~3–4%." Decompose it:

**(a) Security-marketability / minority-illiquidity component (DLOM-like).**
This compensates an investor who holds an interest that **cannot be readily sold** — the public float is illiquid, there are 0 analysts, and a minority holder is stuck. **For a control acquirer of the entire operating company, this does not belong in the operating-cash-flow discount rate.** Valuation doctrine: marketability discounts are largely a *minority-interest* phenomenon; on a **controlling interest** most practitioners apply **little or no DLOM**, and any control-level marketability discount should be far smaller than the minority one. The control owner monetizes the *business cash flows*, not a stock quote, so the day-to-day stock illiquidity premium **legitimately drops out**. → **remove ~1.5–2.0% of the old block.**

**(b) Fundamental size / operating-risk component.**
This is **not** liquidity — it is the genuine, undiversifiable reality that a tiny, single-plant, project-concentrated business has fatter downside tails (one plant fire, one lost anchor customer, one dry bidding year). A control buyer **fully bears** this on the cash flows. It **must stay.** And note a subtlety that argues *against* going too low: **the whole business is itself an illiquid asset** — a control owner of a $10M-revenue niche builder cannot exit quickly either; exit optionality is thin. So we keep a solid fundamental-size charge (**3.0%**) plus the CSRP (**~1.5–2.0%**) and resist cutting to a large-cap-like rate.

**Net of the decomposition:** drop ~150–200 bps of *marketability/minority-illiquidity*, **keep** ~4.5–5.0% of combined *fundamental size + company-specific* risk. That is the engine of the move from 13.5% → ~12.5%.

---

## 4. LBO levered-equity hurdle vs. the unlevered DCF WACC — do not conflate

The case lead asked "what WACC is used in LBOs / take-privates like this?" The honest answer is that **two different numbers** are in play and they are not interchangeable:

| | **Unlevered cost of capital / WACC** | **LBO sponsor equity-IRR hurdle** |
|---|---|---|
| What it is | The discount rate on the *business's* unlevered free cash flows (the DCF input). | The *minimum return on the sponsor's equity check*, after leverage and after the finite-horizon exit. |
| Typical level here | **~12.5%** (this memo) | **~20–25%** (PE buyout norm; 15–25% mid-market, can be higher for small/cyclical deals) |
| Why different | Prices the *asset's* systematic + fundamental risk. | Prices *subordinated, illiquid, concentrated, undiversified, finite-life* equity that sits behind acquisition debt. |

**The reconciliation (this is the part that must not be fudged):** a 20–25% hurdle is **not** evidence that the WACC should be 20–25%. The hurdle is **high precisely because of leverage and structure**, not because the underlying asset earns 20–25% unlevered. Mechanically: if a buyer puts, say, ~50% acquisition debt at a single-digit after-tax cost on a business whose *unlevered* assets require ~12.5%, the **levered** required return on the thin, subordinated equity sliver rises into the low-20s — that is just the levering-up of a ~12.5% asset return. The hurdle also embeds (i) a **finite 3–7-yr horizon** (no perpetuity to bail you out), (ii) **fund-level illiquidity and carry economics**, and (iii) **downside-protection / margin-of-safety** demands. A DCF on unlevered FCF with an unlevered ~12.5% WACC and a perpetuity terminal value is valuing the **same asset** as the LBO — it just isn't levering the equity or truncating the horizon. **Conclusion: use ~12.5% as the DCF WACC; cite the 20–25% only as the sponsor's *levered* hurdle, and state explicitly that the two are linked by leverage, not equal.** (Standard result: DCF and LBO outputs commonly diverge 20–30% for exactly these structural reasons.)

> Practical implication for our case: if we want to *also* show "what a financial sponsor would pay," that is an **ability-to-pay / LBO** exhibit run at a ~20–25% equity IRR with a leverage assumption — a **separate** analysis from the DCF, not a substitute discount rate.

---

## 5. The case FOR a lower rate vs. AGAINST (balance)

**FOR ~12.0–12.5% (or lower):**
- Control buyer doesn't bear minority/stock-illiquidity → DLOM-type premium drops.
- Current normalized ERP is only ~5.0% (Kroll) / 4.33% (Damodaran implied), not 5.5%+.
- Damodaran: a *generic* small-cap premium is not warranted; the historical premium has largely "dissipated since 1981" and is partly diversifiable / better handled in cash flows. Loading a full 4.7% raw size premium risks **double-counting** risk we also model via lumpy/haircut cash flows.
- High ~20% EBITDA margin and a regulated, defensible niche (BSL-3 / biocontainment) → not a distressed micro-cap.

**AGAINST going below ~11.5% (why a premium genuinely stays):**
- Single 50k-sqft plant = real, undiversifiable concentration (one-asset failure risk).
- ~9% customer concentration + lumpy, project-based, non-recurring revenue = fat downside tails.
- 10z micro-cap: even haircut, the empirical size premium is materially positive (4.7% raw at the decile).
- The whole business is itself **illiquid** — a control owner also cannot exit a $10M niche builder quickly, so *some* illiquidity is real even for control.
- 0 analyst coverage / thin information → estimation risk.

The recommended **12.5% base / 11.5–14.0% range** sits deliberately between these.

---

## 6. Recommendation (carry-forward)

| Scenario | WACC | Rationale |
|---|---:|---|
| Bull | **11.5%** | DLOM fully out, ERP at implied 4.33%, size premium toward 2.5%. |
| **Base** | **12.5%** | Kroll ERP 5.0%, fundamental size 3.0% (haircut from 4.7%), CSRP ~1.75%, no minority-illiquidity. **Recommended.** |
| Bear | **14.0%** | β·ERP toward 7%, full ~4%+ size, full CSRP — if you treat the asset as closer to a distressed 10z micro-cap. |

**Verdict on the 12.5% hypothesis: it holds.** The old 13.5% is defensible but ~100 bps rich for a *control* buyer; 12.5% is the better central estimate. Keep 13.5%/14.0% available as the **bear** case (and note the deck's existing bear 15.0% is then a *stress* / distressed-proxy scenario, not the central case). Do **not** drop below ~11.5%, and do **not** import the 20–25% LBO hurdle into the DCF.

---

## Reference list

- [Kroll — Recommended U.S. Equity Risk Premium and Corresponding Risk-Free Rates](https://www.kroll.com/en/reports/cost-of-capital/recommended-us-equity-risk-premium-and-corresponding-risk-free-rates) — Recommended U.S. ERP 5.0% (eff. Sep 2 2025); normalized RF 3.5% / higher-of spot 20-yr.
- [Kroll lowers recommended U.S. ERP to 5.0% — Business Valuation Resources](https://www.bvresources.com/articles/bvwire/kroll-lowers-recommended-us-erp-to-50) — ERP move to 5.0%, Sep 2025.
- [Kroll increases recommended ERP to 5.5% — Business Valuation Resources](https://www.bvresources.com/articles/bvwire/kroll-increases-recommended-erp-to-55) — Apr 15 2025 increase to 5.5% (context for the oscillation).
- [Kroll — Cost of Capital (Navigator / CRSP Deciles Size Study)](https://www.kroll.com/en/tools-and-platforms/cost-of-capital) — 10th-decile size premium 4.7% for cos. ≤ $212.6M; 10w/10x/10y/10z micro-cap subdivision.
- [Aswath Damodaran — Data Update / Implied ERP 2025 (Substack)](https://aswathdamodaran.substack.com/p/data-update-2-for-2025-the-party) — Implied ERP 4.33%, 10-yr 4.58% at Jan 1 2025.
- [Aswath Damodaran — "The Small Cap Premium: Where is the beef?"](https://aswathdamodaran.blogspot.com/2015/04/the-small-cap-premium-fact-fiction-and.html) — argues against a generic small-cap premium; historical ~4.33% decile premium has dissipated post-1981; capture small-firm risk in cash flows / failure probability, not a blanket discount-rate add-on.
- [Pepperdine — Size Premium in Small Business Valuation (Journal of Entrepreneurial Finance)](https://digitalcommons.pepperdine.edu/cgi/viewcontent.cgi?article=1498&context=jef) — critique of applying public decile size premia to small private firms.
- [Pepperdine Private Capital Markets Project — 2025 Report](https://digitalcommons.pepperdine.edu/gsbm_pcm_pcmr/) and [report PDF](https://digitalcommons.pepperdine.edu/cgi/viewcontent.cgi?article=1017&context=gsbm_pcm_pcmr) — private cost of capital / required returns by capital type and deal size; senior-debt scarcity below ~$10M EBITDA.
- [WallStreetPrep — Ability-to-Pay Analysis](https://www.wallstreetprep.com/knowledge/ability-to-pay/) — LBO max-price at a 20–25% sponsor IRR hurdle.
- [Financial-Modeling.com — LBO vs. DCF Outputs: Why Valuations Diverge](https://www.financial-modeling.com/lbo-vs-dcf-outputs-why-valuations-diverge/) — why a 20–25% levered hurdle ≠ unlevered WACC; 20–30% divergence is structural.
- [AnalystPrep — LBO and VC Valuation Methods (CFA L2)](https://analystprep.com/study-notes/cfa-level-2/lbo-method-and-vc-method/) — buyout vs. VC required-return ranges (buyout ~12–18% large, 15–25% mid-market).
- [Company-specific risk premium — definition & range](https://diversification.com/term/company-specific-risk-premium) and [StableBread — Build-Up Method](https://stablebread.com/build-up-method/) — CSRP 1%–6%; concentration/single-plant/lumpy-revenue as CSRP drivers.
- [MJCPA — Evaluating Marketability When Valuing Controlling Business Interests](https://www.mjcpa.com/evaluating-marketability-when-valuing-controlling-business-interests/) and [Auxo — Control Premium vs. Minority Discount: DLOC & DLOM](https://auxocapitaladvisors.com/control-premium-vs-minority-discount/) — DLOM is primarily a minority phenomenon; little/no (and always smaller) DLOM on controlling interests.
- [U.S. Treasury — Daily Par Yield Curve (2026)](https://home.treasury.gov/resource-center/data-chart-center/interest-rates/TextView?type=daily_treasury_yield_curve&field_tdr_date_value=2026) / [Fed H.15](https://www.federalreserve.gov/releases/h15/) — 10-yr UST ≈ 4.46% (May 29 2026).
