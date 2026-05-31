# ARTW — Forensic Filing Review (overlooked details)

**Reviewer pass date:** 2026-05-31 · **Analyst role:** forensic financial-statement review
**Filings read (local copies in `data/edgar/artw/`):**
- **FY2025 10-K** — period end 2025-11-30, filed 2026-02-12, accession 0001437749-26-003904 (`fy2025_10k.txt` / `filings/2026-02-12_10-K_...htm`)
- **Q1 FY26 10-Q** — period end 2026-02-28, filed 2026-04-13, accession 0001437749-26-012161 (`filings/2026-04-13_10-Q_...htm`)
- **FY2024 10-K** — filed 2024-02-28 (cross-check)
- **2026 DEF 14A** — filed 2026-03-12 (`filings/2026-03-12_DEF_14A_...htm`)
- **8-K (annual-meeting results)** — event 2026-04-21, filed 2026-04-22 (`filings/2026-04-22_8-K_...htm`)
- **Form 4s** — Jan–Apr 2026 (insider grants)

This review is scoped to surface facts that the existing `model.md` (v2.1, dated 2026-05-30) does **NOT** already capture, or that refine numbers it carries. Where the model already has the fact, it is marked *(already modeled)*. Citations give filing + note/section + the 10-K text-file line number where available.

---

## TOP 5 THINGS THAT MOVE THE NEEDLE

1. **Q1 FY26 (ended 2026-02-28) is a clean, ERC-free profitable quarter — and the model predates it.** Consolidated sales **$6.64M (+29.2% YoY)**, **net income $196K** (vs −$56K LY), **both segments profitable**, **Ag gross margin 34.5%** (vs 26.7%), and the fall early-order book **+11% overall (non-beet +62%, beet −63%)** — management explicitly calls the ag market a "recovery." This is real, no-ERC evidence the FY26 base is improving. **The model's base case ("near break-even ex-ERC," ag losing ~$1.5M) is stale and arguably too conservative.** *(NEW — not in model.)* (Q1 FY26 10-Q, MD&A "Results of Operations" / "Net income (loss)".)

2. **The near-term refinancing risk the model implies is RESOLVED and debt was repriced cheaper.** The revolver matured 2026-03-30; it was **renewed 2026-03-19, now maturing 2027-03-30**, repriced to **SOFR+2.60% (~6.27%, was WSJ prime 6.75%) — 50 bps lower**, and Bank Midwest **preapproved an extra $1.5M** of capacity. Both term loans were also amended down to **6.25%** (from 7.00% / 7.25%). This lowers interest expense and removes a liquidity overhang. *(NEW — model carries the old 6.75%/7.00%/7.25% terms and the March-2026 maturity.)* (Q1 FY26 10-Q, Note 11; FY2025 10-K Note 10, lines 998–1019.)

3. **NOL / DTA now quantified: ~$7.1M gross federal NOLs (of which ~$5.0M carry forward INDEFINITELY) + ~$109K credits, NO valuation allowance.** Tax-effected NOL+credit DTA = **$1,403,878**; total net DTA **$2,060,934**. Management expects to consume only **~$963K of NOLs in the 2025 tax year**. This robustly supports a multi-year (well beyond 3-year) **federal cash-tax shield**; the binding constraint is state tax (~3.2%) and the finite life of the *expiring* tranche ($2.13M, expires FY2036–2040). **The model's "15% normalized cash tax" is conservative; the real near-term cash rate is near zero.** *(Refines model §A2 — the model flagged ~zero cash taxes but did not quantify the NOL stock or its indefinite-carryforward split.)* (FY2025 10-K Note 14, lines 1097–1110.)

4. **Hidden real-estate value: land carried at just $70,503; buildings 66% depreciated; ~$14.3M accumulated depreciation on $19.4M gross PP&E.** Land for the 249,000 sq ft Armstrong plant + 30 acres + the Monona (50,000 sq ft) plant + a 12,000 sq ft weld shop is on the books at **$70,503 total** (unchanged YoY — 1960s/2007 cost basis). Buildings & improvements gross $7.485M, net of $14.32M accumulated depreciation across all PP&E. **This understates the ag-disposal PP&E recovery the model haircuts to 40% — replacement/market value of two owned industrial plants + land almost certainly exceeds the ~$5.08M net book.** Hidden-asset support for the SOTP floor. *(NEW detail — model assumes ~$4.5M ag PP&E at 40% recovery without noting the land is near-zero book.)* (FY2025 10-K Note 6, lines 956–966; Item 2 Properties, lines 436–437.)

5. **Inventory reserve is large and growing — auditor's sole Critical Audit Matter.** Gross inventory **$14,100,899**; **reserve $2,392,657 (17.0% of gross, up from $1,657,002 / 13.8% in FY24)**; net $11,708,242. The reserve build (+$735K YoY) is far larger than the $56,790 "increase in obsolete reserve" shown in the cash-flow statement, implying meaningful write-offs *charged against* the reserve during the year. **The company is already marking aged ag whole-goods down — which both validates the model's disposal haircut AND means a chunk of the markdown is already taken (the net $11.7M is post-reserve).** Auditor (Eide Bailly) named inventory valuation the **only Critical Audit Matter.** *(Refines model §A1/§10 #2 — model knew net inventory $11.71M but not the $2.39M / 17% reserve or the CAM.)* (FY2025 10-K Note 4, lines 927–935; Critical Audit Matter, lines 549–556; cash-flow line 670.)

---

## 1. INCOME TAX / NOL / DTA (HIGH PRIORITY)

**Facts (FY2025 10-K Note 14, lines 1082–1112):**
- DTA composition (tax-effected): Accrued expenses $79,594; Inventory capitalization $57,115; **NOL & tax-credit carryforward $1,403,878**; Asset reserves $568,372. Total DTA **$2,108,959**; DTL (PP&E) $(48,025); **net DTA $2,060,934**. **No valuation allowance** (management says realization is more-likely-than-not).
- **Gross NOLs (from the 2024 return):** ~$2,133,000 that **expire** Nov-30 of 2036/2037/2038/2039/2040, **plus ~$4,995,000 that carry forward INDEFINITELY**, plus ~$109,000 tax-credit carryforward. → **~$7.13M gross federal NOLs + $0.109M credits.**
- Management **expects to consume ~$963,000 of NOLs for the 2025 tax year** and to utilize the remainder before expiration.
- Effective book tax rate 28.0% (FY25) / 30.3% (FY24); reconciliation: 21% federal + 3.2% state + 2.0% one-time state-rate DTA change + 1.8% permanent (line 1090–1096).
- **Cash income taxes paid: $13,371 (FY25) / $6,309 (FY24)** *(already modeled)* (cash-flow supplemental, line 711).
- **OBBBA (enacted 2025-07-04):** reinstates **100% bonus depreciation incl. manufacturing buildings**, restores favorable EBITDA-based interest-deduction limit, locks in TCJA provisions; company calls it "overall positive for agriculture" but expects "minimal" financial-statement impact (lines 1111–1112).

**So what:** The ~3-year cash-tax holiday the model wants is **comfortably supported and probably understated** — at ~$1–1.5M pretax (much lower ex-ERC), ~$7.1M of NOLs (mostly indefinite) covers many years of *federal* tax; OBBBA bonus depreciation extends it. **Raises intrinsic value vs. the model's 15% normalized cash rate** (the near-term real cash rate is ~0–3% state-only). Caveat for a carve-out: a profitable standalone modular co would consume NOLs faster, and NOLs may be subject to §382 limits on a change of control — worth a footnote in the deal model.

---

## 2. INVENTORY FOOTNOTE

**Facts (FY2025 10-K Note 4, lines 927–935; Q1 FY26 10-Q Note 7):**
- FY25 gross: Raw materials **$8,272,500**; WIP $387,332; **Finished goods $5,441,067** (up from $3,942,435 — the whole-goods build sits in finished goods, **+$1.50M**). Reserve **$(2,392,657)**; net **$11,708,242**.
- FY24 gross $11,984,915; reserve $(1,657,002); net $10,327,913.
- **Reserve = 17.0% of gross (FY25) vs 13.8% (FY24)** — rising obsolescence provision.
- Q1 FY26: gross $14,293,542; **reserve $2,223,692**; net $12,069,850 — inventory stayed elevated and the reserve came down slightly (write-offs taken).
- Costing: lower of cost or NRV, **standard cost ≈ FIFO** (no LIFO) (Note 1(f), line 737–738).
- **Critical Audit Matter = inventory valuation** — auditor flags "future salability… net realizable value by category considering retention periods, future usage, market demand" as the key subjective judgment (lines 549–556).
- No public breakout of ag vs. modular inventory, and **no inventory-aging schedule** — still the disposal data floor (model §10 #2).

**So what:** Confirms and refines the model's ag-disposal recovery debate. **A 17% reserve is already on the books**, so the net $11.7M is post-markdown — the incremental haircut to liquidation value is smaller than haircutting gross. The growing reserve + CAM is a mild red flag on the *quality* of the ag inventory build the model already penalizes. Net effect: roughly neutral-to-slightly-supportive of the base disposal mark.

---

## 3. REAL ESTATE / PP&E

**Facts (FY2025 10-K Note 6 lines 956–966; Item 2 lines 435–438):**
- Land **$70,503** (flat YoY); Buildings & improvements **$7,485,062**; CIP $103,439; Machinery & equipment $10,996,830; Trucks $590,480; Furniture $160,567. Gross $19,406,881; **accumulated depreciation $(14,324,475)**; net **$5,082,406**.
- Useful lives 3–40 years, straight-line. FY25 D&A $792,112.
- Property: Armstrong ~**249,000 sq ft** + **~30 acres** of land; Monona ~**50,000 sq ft** + a **12,000 sq ft** weld shop — *all owned* (lines 436–437). *(already modeled at a high level.)*
- **All owned real property is mortgaged to Bank Midwest** (Item 2 line 438; Note 10 line 1006 — mortgages on both Armstrong and Monona).
- **Roof:** a full Armstrong roof replacement is underway, expected completion FY2026, financed by the new $516,971 Roof Loan (see §4).

**So what:** **Hidden asset.** Land at $70K and buildings 66%+ depreciated almost certainly sit below market/replacement value for two functioning Iowa industrial plants on 30+ acres. This supports (and arguably under-marks) the model's ag-PP&E recovery and the Graham asset-floor argument. **But** the real estate is **pledged to Bank Midwest**, so in a carve-out the mortgage must be cleared before equity sees the land value — consistent with the model netting disposal against debt. Mildly raises the downside floor.

---

## 4. DEBT (revolver, term loans, EIDL, covenants, leases)

**FY2025 10-K (Note 10, lines 998–1030) — as of 2025-11-30:**
- **Revolver:** $4.0M Bank Midwest line, drawn **$3,252,437** ($747,563 available); borrowing base = 75% AR + 50% net inventory; **WSJ prime, 4.25% floor, then 6.75%**; **matured 2026-03-30**; monthly interest-only.
- **Term Loan:** $2.6M orig, bal **$1,666,762**, **7.00%**, due **2037-10-01**, USDA-guaranteed (upfront fee $62,400 + 0.5%/yr); **McConnell trust personally guarantees ~38% for a 2%/yr fee** (related party — see §5).
- **Roof Loan (NEW Oct-2025):** **$516,971**, **7.25%**, 10-yr, monthly $6,102, entered 2025-10-01 to fund the Armstrong roof. *(NEW — model lumps term loans but may not flag this as a fresh draw.)*
- **SBA EIDL:** two loans, **$309,261** total, **3.75%**, due 2050, monthly $731 each, **secured by all assets**. Cheap 30-yr money. *(already modeled inside term debt.)*
- **Covenants:** **min $4.0M working capital (tested MONTHLY)**; **min DSCR 1.25× (0.10 tolerance)**; bank approval required for equipment buys/sales **>$100K/yr**; "reasonable salaries/owner comp." **In compliance at FY25**; next annual test 2026-11-30. *(NEW specificity — model said "various covenants… in compliance" but not the 1.25× DSCR / $4.0M WC / $100K-capex-approval terms.)*
- Finance leases: $663,902 total ($255,748 current / $408,154 LT), WA rate 6.0%, WA term 30 months *(already modeled)*. Operating leases negligible ($13,774, fully run off by FY25).

**Q1 FY26 10-Q (Note 11) — SUBSEQUENT debt changes (2026-03-19):**
- Revolver **renewed, now maturing 2027-03-30**, repriced to **1-mo SOFR + 2.60% (≈6.273%), 5.00% floor**; **+$1.5M preapproved** additional capacity.
- **Term Loan repriced to 6.25%** (change-of-terms 2026-03-19); **Roof Loan repriced to 6.25%** (fixed to 2031-04-05, then 5-yr Treasury + 3.25%).
- Q1 revolver balance $3,431,937 ($568,063 available).

**So what:** **Net positive vs. the model.** (a) Removes the near-term refi overhang (revolver now 2027); (b) lowers interest expense (~50–100 bps across the stack — interest expense was already falling, $367K FY25 vs $599K FY24); (c) the **monthly $4.0M working-capital covenant** is the real constraint to watch given ARTW runs ~$8.3M WC but burns cash on ag inventory — a kill-criterion refinement. The DSCR 1.25× covenant is tight for a company with $289K operating income; it is met largely because the covenant likely adds back D&A and the ERC helped FY25 — **worth modeling covenant headroom in a downside ag year.**

---

## 5. RELATED-PARTY TRANSACTIONS (McConnell)

**Facts (FY2025 10-K Note 11 line 1031–1032; 2026 DEF 14A related-party narrative; Q1 10-Q Note 11):**
- **No related-party revenue or receivables** in FY25/FY24.
- Company buys "various supplies" from companies in which **Chairman/CEO Marc McConnell has an ownership interest and is President** — total related-party expense only **$13,021 (FY25) / $15,193 (FY24)**; $1,076 accrued payable at FY25. Immaterial.
- **Term-loan guarantee fee:** the **J. Ward McConnell Jr. Living Trust** (now referred to in the Q1 10-Q as **McConnell Legacy Investments LLC**, the >20% holder) guarantees ~38% of the $2.6M term loan for a **2%/yr fee → $13,098 (FY25) / $15,193 (FY24)** paid to the McConnell trust. *(Model §11 references control; this quantifies the only cash flowing to the family.)*

**So what:** **Clean.** No leases to, loans from, or large purchases from the family; no evidence of value extraction beyond a small arms-length-style guarantee fee that USDA *requires*. **Supports the "friendly carve-out is plausible and not conflicted" leg of the thesis** — the family is not bleeding the company, so a negotiated transaction is more about price/intent than untangling self-dealing. Lowers governance/related-party risk vs. a typical controlled micro-cap.

---

## 6. COMMITMENTS & CONTINGENCIES

**Facts:**
- **Litigation:** none material; "not currently involved in any material legal proceedings" (10-K Item 3 line 439–440; Note 16 line 1117).
- **Warranty reserve:** $225,000 (FY25), $225,186 (FY24); FY25 warranties issued $327,197, settlements $(327,383) — stable; rose to **$230,905** at Q1 FY26 (10-K Note 9 lines 987–995; Q1 10-Q Note 6).
- **Royalty commitment:** licensing/royalty agreement with **Spreader, LLC** to produce a loader-mounted spreader, royalties **until Dec-2026** (Item 1 line 417).
- **Floor-plan AR:** $412K of AR at FY25 is on 360-day floor-plan terms (down from $1,073K) — extended-term receivables to dealers (Note 1(e) line 734).
- Environmental: no expected material cost (Item 1 line 419).
- No purchase commitments, guarantees (other than the USDA term-loan guarantee), or off-balance-sheet items disclosed.

**So what:** No hidden liabilities. Warranty is small and stable. The only forward commitment of note is the **solar capex** (§7). Neutral-to-positive — confirms the balance sheet is "what you see."

---

## 7. SUBSEQUENT EVENTS

**FY2025 10-K (Note 18, line 1157–1159) — Solar (2025-12-19):**
- **Solar System Purchase Agreement, $1,402,336**, for the Armstrong HQ. Pays 5% on signing, 65% before delivery, 30% post-inspection. Estimated to **eliminate ~100% of electricity cost (~$155,000/yr) for ~30 years.**
- Eligible for **30% Investment Tax Credit** (limited by future taxable income) **and** a **USDA REAP grant (25% of eligible cost) + USDA-guaranteed loan (up to 50%)**.
- **Bank Midwest committed to fund $1,048,002** at 6.75%, 10-yr, **contingent on the REAP grant award**; deposit refundable (less expenses) if grant not awarded.

**Q1 FY26 10-Q (Note 18):** only subsequent event is the **2026-03-19 revolver renewal + term-loan change-of-terms** (see §4) — already covered.

**8-K filed 2026-04-22 (Item 5.07, annual meeting 2026-04-21):** all directors re-elected; auditor ratified; **Proposal 3 — +500,000 shares to the 2020 Equity Incentive Plan — APPROVED** (3,398,629 for / 176,936 against); say-on-pay approved. (Marc McConnell drew notably more "withheld" director votes — 253,165 — than peers, a minor governance signal.)

**So what:**
- **Solar:** a **new ~$1.4M capex / ~$1.05M new debt** not in the FY25 balance sheet, but it generates a **~$155K/yr opex saving (~11% pretax return on cost before incentives)**, a **30% ITC**, and a **25% USDA grant** — economically attractive *if* the REAP grant lands. Models should add the debt and the electricity-cost saving to FY26+; it modestly **raises** standalone modular/whole-co cash flow once operational. Watch the REAP-grant contingency. *(NEW — not in model.)*
- **Equity plan +500K shares APPROVED:** confirmed **dilution overhang of ~500,000 shares (~9.6% of 5.18M)** authorized for future grants. The model uses 5.184M shares; flag the dilution as a per-share headwind over time. *(NEW — model predates the vote.)*

---

## 8. SEGMENT FOOTNOTE (Note 17/18) & MD&A — leg-level breadcrumbs

**Disaggregation of revenue (FY2025 10-K Note 1(k), lines 791–809) — finer than the model's table:**

| FY25 ($000) | Ag Products | Modular |
|---|---|---|
| Farm equipment | 9,173 | — |
| Farm equipment service parts | **3,279** | — |
| Modular buildings | — | **10,033** |
| Modular building lease income | — | **75** |
| Other | 297 | 118 |
| **Total** | **12,749** | **10,226** |

FY24: Ag farm equipment $10,720 / parts $3,631; Modular buildings $9,386 / lease income $203.

**MD&A leg breadcrumbs:**
- FY25 10-K (line 494): within Modular, **agricultural-building sales rose ~$1,355,000 YoY**; "strong demand on the research side"; names customers "renowned for being leaders in **xenotransplantation and cancer research**." *(already modeled — basis for the 40/60 split.)*
- **Q1 FY26 10-Q adds NO explicit leg split**, but: "continued strong demand for our buildings on **both the livestock and research sides**"; Modular **gross margin fell to 21.3%** (from 32.3%) due to "selling a **warrantied agriculture modular building at cost** and project overages on site work." → confirms the two legs (livestock/ag-bio vs research) and shows the ag-bio leg can be lower-margin / warranty-exposed.

**Segment economics (Note 17, lines 1119–1156):** Modular FY25 op income $1,751K, **D&A $251K, capex $222K, interest $59K, total assets $3,274K** *(already modeled)*. Corporate expense in G&A: $420K allocated to Ag / $180K to Modular = $600K total — **useful for the standalone-corporate-cost add-back the model estimates at ~$0.45M** (the model's number looks reasonable vs. the $180K currently allocated).

**Service-parts annuity (overlooked):** Ag carries **$3.279M of high-margin aftermarket service-parts revenue** (26% of ag sales) that is far stickier and more profitable than whole-goods. **In an ag wind-down, the parts book + dealer network has standalone/strategic value the model's "liquidation" framing ignores** — a buyer of the ag line (or the parts business alone) could pay more than scrap. Mild upside to the ag-disposal mark.

**So what:** No clean research-vs-ag-bio split is disclosed — the data floor (model §10 #1) **stands**. But the disaggregation isolates **modular product revenue at $10,033K** (lease income only $75K — confirms modular is **sale**, not lease/recurring, so it does NOT deserve a WSC leasing multiple, consistent with the model). The **$3.28M ag service-parts stream** is a genuinely overlooked semi-annuity worth flagging.

---

## 9. EQUITY & OWNERSHIP

**Facts (2026 DEF 14A ownership table; FY2025 10-K cover & Note 13; Form 4s):**
- Shares: **5,225,423 issued − 113,589 treasury**; **5,177,084 o/s at 2026-02-04** (10-K cover); **5,182,084 at 2026-03-05** (proxy). *(model uses 5.184M — fine.)*
- **Marc McConnell beneficially owns 2,417,899 = 46.7%** (incl. **2,149,819 via McConnell Legacy Investments LLC = 41.5%**, of which he is managing member with voting control; + 252,500 direct; + 10,000 children; + 5,580 IRA). **Directors & officers as a group = 51.5%.** *(already modeled — but note control is concentrated in ONE person, Marc McConnell, not a diffuse "family.")*
- **NEW 5% holder: Larry M. Walther — 300,000 shares (5.8%)** per a Schedule 13G filed 2026-02-17. *(NEW — an outside ~5.8% holder appeared in early 2026; worth identifying — could be a value/activist signal in an orphan micro-cap.)*
- No preferred issued. **No dividends** (FY25/FY24). No buybacks (only $1,542 of treasury from forfeitures). 66 holders of record.
- **Stock-based comp $179,080 (FY25)**; directors get 1,000 sh/quarter + an annual grant; **no options outstanding** (last 4,000 expired FY25); **2020 Plan +500K shares approved Apr-2026** (§7). Tax deduction from SBC $154,037.
- **Insider activity (Form 4s, Jan–Apr 2026): all transaction code "A" (grants at $0) — NO open-market buys or sells.** Marc McConnell received a 30,000-share restricted grant 2026-01-21 (vests 2027–2029). *(NEW — no insider selling is mildly reassuring; but no conviction open-market buying either.)*
- **Executive comp (proxy):** CEO Marc McConnell base **$283,250** + $12K car + $15K office stipend + RSAs; CFO Michael Woods base **$158,346**. Directors ~$24–28K cash + 7,000 sh each. Audit fees $146K; tax fees $23K. **Comp is modest for a public company — no extraction red flag.**

**So what:** Control is even more concentrated than "family ~51.5%" — **one individual (Marc McConnell) holds voting control of 46.7% via an LLC he manages.** Reinforces model §11: any transaction is **entirely gated on one person.** The **new 5.8% outside holder (Walther)** and the absence of insider selling are new, mildly thesis-relevant data points (a non-family ~6% block could push for a value-realizing event). Modest comp + clean related-party = low governance-extraction risk.

---

## 10. PENSION / OPEB / OTHER LONG-TERM LIABILITIES, GOODWILL, OFF-B/S

**Facts:**
- **No pension / OPEB.** Only a **401(k)** with a 50% match up to 3% of pay (expense $97,769 FY25) — no defined-benefit obligation (Note 12, line 1033–1034).
- **No goodwill, no intangibles on the balance sheet** (intangibles are internally developed trademarks/manufacturing rights, not capitalized; Item 1 line 415–416).
- **No off-balance-sheet arrangements** disclosed.
- Other long-term liabilities = just the LT finance-lease ($408K) and LT debt ($2.325M) already in §4.
- "Other assets" $408,060 includes **finance-lease ROU $368,720**; **cloud-ERP (QAD) implementation costs fully amortized** ($0 remaining vs $61K FY24) (Note 1(h)/(m), lines 758, 827).

**So what:** **Clean.** No legacy pension/OPEB drag, no goodwill impairment risk, no hidden long-term liabilities. Supports a straightforward SOTP — there is nothing lurking below the line that the model's net-debt bridge misses.

---

## 11. OTHER RED FLAGS / HIDDEN ASSETS / THESIS-RELEVANT FACTS

- **Bill-and-hold revenue went to ZERO in FY25 (was $1,073,000 in FY24).** ARTW recognizes some ag revenue on a bill-and-hold basis (title passes before shipment). The FY24 figure was material (~4% of ag sales); **none in FY25.** This is a **quality-of-earnings positive** for FY25 (less aggressive timing) but means FY24 ag revenue was modestly flattered — relevant when using FY24 as a comp base. (10-K MD&A line 476; Note 1(j) line 784.) *(NEW.)*
- **Tools real-estate sale details (FY24):** sold Oct-2024 for **$1,800,000**, net book **$996,768**, closing costs $119,547 → **gain $683,685**. A useful real-world data point on rural-Iowa industrial real-estate realizations (sold ~1.8× book) — **supports marking the Armstrong/Monona land/plant ABOVE the $70K+depreciated book in a disposal**, i.e., the model's 40% PP&E recovery may be conservative. (10-K Note 2, line 879.) *(Refines model §1b.)*
- **Key-person / thin commercial org:** FY24 CEO stepped down (Oct-2024); Chairman Marc McConnell took over CEO; director of sales departed and was **not replaced**; long-time Modular President **Dan Palmer going part-time through Q2 FY26.** Sales responsibilities absorbed by CEO/CFO/VP-Ops. **Thin, key-person-dependent commercial bench** — execution risk for the growth case. (10-K MD&A lines 493–494.) *(already in model §8, but worth reinforcing as a risk.)*
- **Steel +26% FY25-over-FY24** crushed ag gross margin (23.4% vs 28.3%); tariffs newly incurred in FY25; **manure-spreader beaters sourced from Italy** with a FY25 reshoring project as a tariff hedge. Input-cost and tariff exposure is real and ongoing (Q1 FY26 notes steel still rising). (10-K MD&A line 492; Item 1 line 413.)
- **Customer concentration improved:** FY25 largest customer ~9% (no >10%); FY24 had **two customers at 17% and 15%.** Less concentration risk in FY25. (Note 1(d), line 730.) *(NEW — model notes 9% but not that FY24 had two ~15–17% customers.)*
- **Working-capital quality (Q1 FY26):** customer deposits jumped to **$830,578** (from $88,920) and billings-in-excess to **$879,293** — strong forward bookings funding operations; a new **$167,108 insurance-premium finance liability** appeared. Q1 OCF was positive (operating activities the primary funding source). Supports the "FY26 cash generation improving" read.

---

## RECONCILIATION TO THE MODEL — what should change

| Model item | Filing finding | Direction |
|---|---|---|
| Base case "ex-ERC near break-even, ag losing ~$1.5M" | Q1 FY26: +29% sales, $196K NI, both segments profitable, ag GM 34.5%, order book +11% | **Stale / too conservative — refresh with Q1** |
| Cash tax "15% normalized" | ~$7.1M NOLs (~$5.0M indefinite) + OBBBA bonus deprec.; ~$963K consumed/yr | **Cash tax lower → value higher (federal); §382 caveat on change of control** |
| Refi/maturity (revolver due Mar-2026 @6.75%) | Renewed to Mar-2027, repriced to SOFR+2.60% (~6.27%), +$1.5M capacity; term loans → 6.25% | **De-risked + lower interest** |
| Ag PP&E recovery 40% on ~$4.5M net book | Land $70K book; plants 66% depreciated; Tools RE sold at ~1.8× book | **PP&E recovery likely conservative → mild upside to floor** |
| Net inventory $11.71M | $2.39M (17%) reserve already taken; CAM on inventory | **Markdown partly pre-taken; neutral-to-supportive** |
| Standalone corporate add-back ~$0.45M | Only $180K corporate allocated to Modular today | **Add-back assumption reasonable** |
| Shares 5.184M | +500K equity-plan shares approved Apr-2026 | **Future dilution overhang (~9.6%)** |
| (not modeled) | Solar: $1.4M capex / ~$1.05M new debt / ~$155K-yr opex saving / 30% ITC / USDA REAP | **Add to FY26+; modest cash-flow positive** |
| (not modeled) | New 5.8% holder Larry Walther (13G Feb-2026); no insider selling | **Possible catalyst signal** |
| (not modeled) | Ag service-parts $3.28M (sticky, high-margin) | **Ag-disposal mark may understate parts/dealer value** |

*This file is a forensic read of the filings only; per instructions no other research/model files were edited.*
