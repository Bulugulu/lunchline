# ARTW Deck — Writing Audit (AI-tells + Buffett-voice fidelity)

**Audited file:** `mockups/pitches/artw-deck.html`
**Standard:** `docs/memo-voice.md`, `docs/memo-principles.md`, `CLAUDE.md` tone rules — Buffett/Marks/Einhorn plainness; no marketing/consulting speak; no hype; lead with the number; risks as conditionals; close with restraint.
**Scope:** prose only (headlines, subheads, body, callouts). SVG chart internals and CSS ignored.

Phrase-level find→replace so fixes survive concurrent editing. Grouped by slide.

---

## Top systemic patterns to fix (in priority order)

1. **"Marquee" + adjective hype.** The word "marquee" appears twice (Slide 3 headline + a dash-title) and is explicitly the kind of sell-side adjective the memo principles ban. Same family: "high-value asset," "clean platform," "the real difference." These are adjectives standing in for analysis — the rule (`memo-principles.md` Forbidden moves) is to replace each with the underlying number or fact. The customer logos already prove "marquee"; the word adds nothing.

2. **Imperative ad-copy headlines ("Buy control, shed the farm drag, scale the lab builder," "Buy control, divest the drag, own it debt-free," "Unlock"-style verb stacks).** Buffett headlines state a fact and then judge it; they do not bark a three-verb command. The tricolon imperative is a pitch-deck tell, not a shareholder-letter move. Convert the lead claims to "number, then meaning" form.

3. **Em-dash overuse as the default connective.** The deck leans on the em-dash to splice two clauses in nearly every subhead and callout (cover tagline, Slides 2, 5, 6, 7, 8, 11, 12). Buffett uses periods. Where a dash joins two independent statements, split into two sentences; reserve the dash for a genuine appositive.

4. **Hype/marketing vocabulary scattered throughout:** "re-rate / re-rates / re-rating" (jargon, repeated ~6×, never translated), "platform," "compounds," "playbook," "the trade in one line," "the real difference." Translate or cut per the plain-English table.

5. **Throat-clearing labels that restate the obvious:** callout labels like "The trade in one line," "Where the return comes from" (used twice), "What protects the downside," "What the margin supports for value." These are consulting-slide furniture. Most can be deleted or made factual.

---

## Slide 1 — Cover

| Current phrase | Suggested plain replacement |
|---|---|
| "A cyclical farm-equipment maker hides a growing, 17%-margin builder of research and animal-biosecurity labs. Buy control, divest the drag, own it debt-free." | "Art's-Way's cyclical farm-equipment segment lost money in FY24–25. Inside it sits a lab-building segment that grew sales every year to a 17% operating margin. A control buyer can sell the farm assets, repay the debt, and own the lab builder near book value." |
| "Buy control, divest the drag, own it debt-free." (the imperative tricolon) | Replace the command with the consequence: "Sold off, the farm assets repay the debt; what's left is the lab builder." |
| "hides a … builder" (personification — a company doesn't "hide" things) | "…contains a … builder" or "…sits alongside a … builder." |

---

## Slide 2 — Business Overview I

| Current phrase | Suggested plain replacement |
|---|---|
| "Two business segments are moving in opposite directions." (headline restated verbatim by the subhead and chart caption) | Lead with the number instead: "Farm-equipment sales fell to $12.7M in FY25 and lost money; lab-building sales rose to $10.2M at a 17% margin." |
| "The blended 1.3% margin masks both." | "The blended 1.3% operating margin hides both: a loss in farm, a 17% margin in labs." (keep — but "masks" → "hides" for plainness, and state the two numbers it hides) |
| "rose every year to a 17% margin on almost no assets" | "rose every year and earned a 17% operating margin on $3.3M of assets" (give the asset number rather than "almost no") |

---

## Slide 3 — Business Overview II

| Current phrase | Suggested plain replacement |
|---|---|
| "A 70-year refocus, now selling to marquee research institutions." (headline) | "Founded 1956; family-controlled since 2002. The lab unit launched in 2006 has delivered 150+ facilities to UC Davis, MD Anderson, and Stanford." |
| "marquee research institutions" / "Marquee modular customers" (dash-title) | "Named research institutions" / "Modular customers — none over 10% of sales." (the logos prove prestige; drop the adjective) |
| "A 70-year refocus" | "Seventy years of narrowing the business" (spell the number, drop the abstract noun "refocus") |
| "to concentrate on its best" | "to concentrate on its strongest segment" or just "on the lab business" (name it; "its best" is vague) |
| "Seven decades of refocusing on what works" (dash-title — restates the headline) | "What the company kept and what it exited, 1956–2024" |

---

## Slide 4 — End Market

| Current phrase | Suggested plain replacement |
|---|---|
| "An advantage: two unrelated federal budgets underpin demand" (dash-title) | "Two unrelated federal budgets fund the demand" (drop "An advantage:" throat-clearing; "underpin" → "fund") |
| "underpin demand" | "fund the demand" |
| "demand is anchored by USDA's up-to-$1B avian-flu program" | "demand comes from USDA's avian-flu program (up to $1B)" ("anchored by" is jargon) |
| "That money reaches ARTW through farmers who use the cost-share" | keep — this is good plain writing; leave as is |
| "Because the two budgets are unrelated, weakness in one leg can be offset by the other." | "Because the two budgets are unrelated, a weak year in one leg need not mean a weak year in the other." (sharper; "offset" is finance-speak) |

---

## Slide 5 — Competitive Positioning

| Current phrase | Suggested plain replacement |
|---|---|
| "We deliver a containment lab in ~6 months, not years." (headline — "deliver" + "not X" construction) | "Art's-Way builds a containment lab in about six months; an on-site build takes two to five years." (replace the marketing verb "deliver" and the "not years" tell with the actual comparison number) |
| "Speed is the real difference." (pillar 02 — "the real" is hype) | "Speed is what customers pay for." |
| "Meeting containment codes is hard to copy." | keep — plain and good. |
| "What the margin supports for value" (callout label) | "What the 17% margin is worth" or delete the label and lead with the multiple. |
| "the roughly 10-point gap reflects specialized work, not low-bid commodity building" | "the 10-point gap is specialized work, not low-bid commodity building" (cut "roughly … reflects"; the "not X" is acceptable here as a real contrast, but tighten) |

---

## Slide 6 — Investment Thesis I

| Current phrase | Suggested plain replacement |
|---|---|
| "Buy control, shed the farm drag, scale the lab builder." (headline — imperative tricolon, "drag" as noun) | "On a control basis the business is worth ~$2.80 against $2.58 today, with book value protecting the downside." (lead with the number; move the action verbs into the body) |
| "the farm drag" / "shed the … drag" | "the loss-making farm segment" / "sell the farm segment" ("drag" is slangy) |
| "an asset-protected entry, with the operator return compounding on top" | "book value protects the entry; the operator's improvements add to that return." ("compounding on top" is vague hype) |
| "Lunchline's search-fund playbook: buy a fixable niche leader from a willing family." | "The search-fund approach: buy a fixable niche leader from a family willing to sell." ("playbook" is consulting-speak; "willing family" → "family willing to sell") |
| "The building business is the high-value asset to invest behind and scale." (pillar 02) | "The building business earns 17% on $3.3M of assets and deserves the capital the farm segment now ties up." (replace "high-value asset … invest behind and scale" with the numbers) |
| "It deserves capital and focus the conglomerate denies it." | "Inside the combined company it competes for capital with a loss-making farm segment." ("the conglomerate denies it" personifies and editorializes) |
| "Today's price reflects the status quo, not the growth a focused owner could create." (pillar 03 — "not X" construction) | "At about book value, the price assumes the business stays as it is run today." |
| "The trade in one line" (navy-box label) | "In one sentence" — or delete the label. |
| "the equity return compounds as the operator sheds the drag, retires debt, and re-rates the platform." | "the equity return grows as the buyer sells the farm assets, repays the debt, and the market values the lab builder on its own." (translate "compounds," "sheds the drag," "re-rates the platform") |

---

## Slide 7 — Investment Thesis II

| Current phrase | Suggested plain replacement |
|---|---|
| "Net of farm assets, you buy the lab builder at ~7×." | keep the structure; "Net of farm assets" is acceptable, but consider "After the farm assets are subtracted, the lab builder costs about 7× operating earnings." |
| "A fair entry, with book value backstopping the downside." | "A fair price, with book value protecting the downside." ("backstopping" is jargon) |
| "A fair entry, with an asset-backed floor" (callout label) | "Book value sets a floor" |
| "Where the return comes from" (navy-box label, used again on Slides 7 and 11) | Vary or delete; on first use, "How a buyer makes money here." |
| "From operating ownership, not a cheap quote" ("not X" construction) | "The return comes from running the business, not from a cheap stock price." |
| "The catalyst is family-gated" (callout label — jargon) | "Nothing happens unless the family sells" |
| "negotiating a friendly purchase from a willing owner-family is the deal itself, not an obstacle" | "negotiating a friendly purchase from the family is the searcher's job, not an obstacle to it." ("the deal itself, not an obstacle" is the "not X but Y" tell) |

---

## Slide 8 — Investment Risks

| Current phrase | Suggested plain replacement |
|---|---|
| "Three things can break the trade — none wipe out capital." (em-dash splice) | "Three things can break the trade. None wipes out your capital, because the debt stays covered by collateral." |
| "The downside is asset-protected: the acquisition debt stays collateral-covered, so these hit the equity return, not your capital." | keep the logic; tighten: "Because the debt stays covered by collateral, each risk hits the equity return, not the capital." |
| "Each with its mitigant and trigger." (fragment + jargon "mitigant") | "Each risk below has what limits it and what would prove it real." |
| "The bull doesn't materialize — modular growth & re-rate stall" | "Modular growth and the re-rating both stall" — and translate "re-rate": "the market never values the lab builder on its own." |
| "The equity return lives here." | "This is where the upside is." ("lives here" is glib) |
| "a two-leg policy hedge (USDA biosecurity + research labs)" | "two unrelated funding sources (USDA biosecurity and research labs)" ("policy hedge" is jargon) |
| "professionalized" (in "thin, founder-dependent commercial org professionalized") | "the thin, founder-run sales organization has to be built into a real one." ("professionalized" + "commercial org" is consulting-speak) |

---

## Slide 9 — Value Creation I

| Current phrase | Suggested plain replacement |
|---|---|
| "Four levers can roughly double the building business." | keep — plain and falsifiable. ("levers" is mild jargon but established in the section.) |
| "the constraint is sales effort, not demand" ("not X" — acceptable, real contrast) | keep. |
| "Recurring service revenue earns a higher multiple than one-time project work." | keep — plain and correct. |
| "an untapped lever to add scale and service revenue" | "a way to add scale and service revenue it has never used." ("untapped lever" is consulting-speak) |

---

## Slide 10 — Value Creation II

| Current phrase | Suggested plain replacement |
|---|---|
| "Each lever: a specific action, evidence, and a sequence." (headline — label, no claim) | "Each step: what to do, the evidence it works, and when." (or lead with the end state: "Four steps over three years take the lab builder to $13–15M of sales.") |
| "Build a real sales team" | "Hire salespeople" or "Add a sales team" ("a real sales team" implies the current one is fake — say it plainly: "The sales effort is one part-time president.") |
| "convert demand into orders" | "turn that demand into orders" (fine; minor) |
| "push the unused lease option" | "use the leasing option the company has never used" (translate "push") |

---

## Slide 11 — Value Creation III / Payoff

| Current phrase | Suggested plain replacement |
|---|---|
| "Base ~12%/yr, bull ~30% — downside asset-covered." (headline, em-dash + jargon) | "Base case returns about 12% a year, the bull case about 30%; in the bear case, collateral covers the debt." |
| "the de-levered, cash-generative building business then compounds … and re-rates as a clean platform." | "with the debt repaid, the building business generates cash (about $4.5M over the hold) and is valued on its own." (translate "de-levered," "compounds," "re-rates," "clean platform") |
| "What protects the downside" (callout label) | "Why the downside is covered" — or state it: "Collateral covers the debt." |
| "Lenders stay whole even in the bear, so there is no forced sale" | keep — this is plain and concrete. |
| "a disciplined entry near book keeps the equity loss bounded — not a wipeout." (em-dash + "not X") | "buying near book value keeps the equity loss limited rather than total." |

---

## Slide 12 — Financial Review

| Current phrase | Suggested plain replacement |
|---|---|
| "Control-basis fair value ~$2.80, with an asset floor." | keep — number first, plain. Optionally spell: "with book value as a floor." |
| "How the base case adds up ($M)" | keep — plain. |
| "Assets protect the downside; Graham floor holds" (callout label) | "Assets protect the downside" (drop "Graham floor holds" — the body already states the two tests) |
| "book value $2.57 ≈ the price" | keep. |

---

## Slide 13 — AI Disclosure Appendix

| Current phrase | Suggested plain replacement |
|---|---|
| "AI accelerated research; every number rebuilt from filings." | keep — plain and factual. |
| "Running a build-then-review loop that disciplined the conclusion from a hopeful 'free gem' read to a defensible 'asset-protected operator acquisition'" | "A build-then-review loop moved the conclusion from an over-optimistic 'cheap stock' read to a defensible 'asset-protected acquisition.'" ("disciplined the conclusion," "free gem" are insidery) |
| "from modestly rich to modestly cheap" | keep — plain. |
| "The climate is cautious, not a confirmed cut." ("not X" — acceptable contrast) | keep. |

---

## Recurring words to find-and-fix globally

| Word/phrase (count) | Why it fails the standard | Replace with |
|---|---|---|
| "marquee" (×2) | Banned sell-side adjective (`memo-principles.md`) | "named" / delete (logos prove it) |
| "re-rate / re-rates / re-rating / re-rate the platform" (~6) | Untranslated jargon | "the market values the lab builder on its own" / "valued separately" |
| "platform" / "clean platform" (×3) | Consulting-speak | "the lab business" / "the building business" |
| "playbook" (×2) | Consulting-speak | "approach" / "plan" |
| "compounds / compounding" (×3) | Jargon for a slide | "grows" |
| "the drag" / "shed the drag" / "the farm drag" (×3) | Slangy noun | "the loss-making farm segment" |
| "asset-protected / asset-backed / asset-covered" (×5) | Coined compound, repetitive | "protected by collateral" / "book value protects it" (vary, don't repeat) |
| "lever / levers" (~6) | Mild consulting-speak (tolerable once defined; do not overuse) | "step" / "move" where possible |
| Em-dash clause-splices (Slides 1,2,5,6,7,8,11) | AI-writing tell | split into two sentences |
| "the real difference" / "the high-value asset" | Adjectives standing in for analysis | the underlying number |
