# Memo Principles

Project-specific rules for writing investment memos in the Lunchline case study. Paired with [memo-voice.md](memo-voice.md), which is the deeper exemplar research (Buffett / Marks / Einhorn) on *how* to write. This file is the shorter *what to include and what to check* document.

**Anchor reference:** Berkshire Hathaway shareholder letters (Warren Buffett). When in doubt about voice, ask "would this sentence appear in a Buffett letter?" If not, rewrite.

**Canonical template:** `mockups/pitches/option-a-scroll.html` — the AENT memo, written to demonstrate these principles.

---

## What every memo must include

Five blocks, in order. None is optional.

1. **Headline thesis** — one sentence, a falsifiable claim with at least one number. Stated as if the reader will grade you on it.
2. **The business** — one short paragraph: what the company is, what it actually does day-to-day, who runs it. No founding history. No mission statement.
3. **Why this is a non-obvious pick** — the *Lunchline* angle. One paragraph that answers: is the situation *messy* (post-event capital structure, accounting noise, governance), *mispriced* (the operating economics are not in the multiple), or *under-followed* (no analyst coverage, no institutional float)? Often more than one — name them explicitly.
4. **Investment thesis** — written as the *gap* between what the market sees and what we see. Two paragraphs: first the consensus stated steelmanned in its own language; then the variant view with sources for every claim.
5. **Investment risks** — three risks, each written as a conditional with a measurable threshold. *Not* a bulleted list of nouns ("execution risk, regulatory risk").
6. **Value creation** — what an operator-investor would actually do, broken across four categories: **Commercial**, **Operations**, **Capital structure**, and **Mergers and acquisitions (M&A)**. One concrete move per category, each with a quantified expected impact and a named comparable transaction.
7. **What would have to be true forward** — closing paragraph. Three observations from future filings or calls that would confirm or deny the thesis. The list should be operationally testable.

A market-environment thesis (Marks's *Sea Change* register) belongs woven into the *Why mispriced* or *Investment thesis* sections, not as a separate block. The case brief requires both a company thesis and a market thesis; they must connect.

---

## Voice rules

The longer treatment is in [memo-voice.md](memo-voice.md). The shortlist:

1. **Lead with the number, then the meaning.** First sentence of every section contains a number with a source.
2. **Spell out every abbreviation the first time it appears.** Write "earnings before interest, taxes, depreciation, and amortization (EBITDA)" once; then EBITDA. Same with SOFR (Secured Overnight Financing Rate), 10-K, 10-Q, ABL (asset-based loan), and any acronym.
3. **No financial jargon without translation.** "Operating leverage" becomes the underlying mechanic in plain words. Translation table is in [memo-voice.md](memo-voice.md) §3.
4. **Sourcing lives inside the sentence, not in a footnote.** Pattern: prepositional phrase + named document + date. Example: "In the fiscal 2025 annual report filed September 10, 2025, the chief executive disclosed…" Every external claim is an inline hyperlink, not a footnote number.
5. **Quote management directly, dated.** When the thesis turns on what management has said, name the speaker, the venue, and the date. Then place the contradicting fact next to it.
6. **One analogy per memo.** If you need a metaphor, use it once, then move on. No restatement of the analogy in different words.
7. **Risks as conditionals with thresholds.** "If X falls below Y for Z quarters, our N estimate is wrong." Not "execution risk is elevated."
8. **No selling language.** Strike on sight: *compelling, attractive, asymmetric, world-class, best-in-class, high-conviction, high-quality*. These signal sell-side filler to the institutional reader.
9. **Close with restraint.** End on a sentence that hands judgment to the reader, not a price-target marketing line.

---

## Forbidden moves

These are presentation tricks rather than insights. Aviv has explicitly flagged each one as worth nothing to him.

- **"Wrong industry tag / GICS misclassification."** If the company is already priced inside the band of its real comparable set, re-labeling is worth a few percent of multiple, not 50%. (See the May 28, 2026 conversation that killed the AENT misclassification pillar.)
- **"Quant screens will eventually catch up."** True but small. Useful as a supporting structural point, never as a main pillar.
- **"Sum-of-the-parts says it's worth X."** Allowed only if you have an explicit catalyst (announced strategic review, activist position, controlling shareholder change) for the parts to be separated.
- **Adjectives standing in for analysis.** "Strong moat," "robust unit economics," "durable franchise." Replace each with the underlying number or mechanic.

---

## Sourcing discipline

Every claim must be auditable in under sixty seconds using only the memo text. The discipline:

- Documents are named with their date — *not* "company filings," "public reports," or "industry sources."
- Multiples and growth rates are tied to a specific filing date — *not* "trailing twelve months" as a bare phrase. The reader needs to know which TTM.
- Management quotes are dated to the call or filing they came from.
- Peer references are tied to the peer's own named filing — *not* a sector-study aggregate.

External links live inline on the words they describe. SEC EDGAR has stable URLs by CIK (company identifier); use those for filings. Yahoo Finance ticker pages are reliable for *linking to a quote page*, but see the number-verification rules below before trusting any Yahoo *figure*.

---

## Number verification (learned the hard way)

A multi-agent numbers-audit of the first eleven memos (2026-05-28) found that **every memo carried at least one wrong load-bearing number**, and several were thesis-altering. The errors clustered into four repeatable failure modes. Verify against these before any memo is pitched or built into a deck.

1. **Data-vendor aggregate fields are unreliable — compute valuation from the filed balance sheet instead.** Yahoo Finance / yfinance `marketCap`, `enterpriseValue`, `freeCashFlow`, and `totalCash` are *derived* fields that silently break on dual-class, earnout, and preferred structures. Real examples caught: AENT's market cap was reported as $704M because the field multiplied price by *implied* shares including 60M escrowed Class E earnout shares that only vest if the stock triples (true equity $323M); NRDY's enterprise value field read $91M when the balance sheet gives $137M (a ~$46M understatement); UPLD's "$36M free cash flow" was a vendor levered-FCF calc when the cash-flow statement shows $25.8M operating cash flow; SWAG's "$13.6M cash" was stale vs. the filing's $12.8M. **Rule: enterprise value, net cash/debt, and free cash flow are computed from the company's own balance sheet and cash-flow statement, with the arithmetic shown, never copied from a vendor field.**

2. **Non-GAAP metrics must be traced to the company's own reconciliation table — never inherited from an upstream analysis file.** Adjusted EBITDA, net dollar retention, ARR, segment mix, "Rule of 40," and customer-concentration percentages are not in XBRL. The worst error in the batch — IZEA adjusted EBITDA stated at $5.3M when the 10-K reconciliation shows $0.7M, a 7x overstatement that inverted the valuation conclusion — came from trusting a findings file. **Rule: every non-GAAP number is quoted from the specific reconciliation table in the 10-K/10-Q, with the period named. A number that appears only in a findings/scoring file and cannot be found in a filing does not go in the memo.**

3. **Watch for conflation — two unrelated figures of similar size summed or swapped.** This was the single most common error. Examples: IZEA's "Hoozu $5.3M write-down" was the $1.3M Hoozu goodwill *plus* an unrelated $4.0M impairment of three older acquisitions; ACCS's "$20M divestiture" was the unrelated $20M Pinnacle term-loan facility (actual price $12.5M); SCOR's "$44.3M income available to common" was an intermediate subtotal (actual $22.6M). **Rule: when two numbers in the same neighborhood are close in magnitude, confirm they are the same line item before combining or substituting them.**

4. **Watch period and share-count consistency.** Stale-period (TTM-vs-fiscal-year, especially for off-calendar fiscal years), sign-flips (a YoY decline written as growth), and per-share math on the wrong share count all recurred. SCOR's per-share targets used ~9-15M shares when fully-diluted is ~27.7M including Series C — roughly halving real per-share value. **Rule: state which period every figure covers; for per-share math, use the economic/fully-diluted share count and show it.**

**Process rule going forward:** after drafting a memo, run a dedicated verification pass that (a) checks every GAAP figure against XBRL, (b) quotes every non-GAAP figure from a reconciliation table, (c) recomputes every derived figure (multiples, per-share, IRR) for internal consistency, and (d) marks anything that genuinely requires live market data (current bond price, a peer's live multiple) with an explicit `UNVERIFIED` flag rather than inventing it. A plausible-looking number in the right ballpark is the most dangerous kind — it survives a read-through and only fails a source check.

---

## Drafting checklist

Run this against every draft before reviewing. Same as [memo-voice.md](memo-voice.md) §8, restated here for quick reference.

1. Does the first sentence of every section contain a number?
2. Is every number followed (in the same sentence) by a preposition pointing to a named source?
3. Are all abbreviations spelled out the first time they appear?
4. Are all terms of art either translated at first use or rewritten in plain language?
5. Is there exactly one analogy in the memo, used once?
6. Is there at least one direct management quote, dated and sourced?
7. Is there at least one peer cross-reference (named peer + named document)?
8. Are the risks written as conditionals with quantified thresholds, not as nouns?
9. Does the close hand judgment to the reader, or does it sell?
10. Could a teenager — with the document titles in hand — verify the three most load-bearing claims in the memo?
11. Have all instances of *compelling, attractive, asymmetric, world-class, best-in-class, high-conviction, high-quality* been deleted?
12. Are all four value-creation categories (Commercial, Operations, Capital structure, M&A) represented with one concrete move each?

---

## Length

The deliverable is a one-page memo. The HTML template at `mockups/pitches/option-a-scroll.html` is denser than a printed page but is designed to compress to one printable sheet at letter-size with quarter-inch margins. If the prose runs longer, cut — almost always the right cut is in the *what the market sees* section, where it is tempting to over-elaborate the consensus view.

The full deck (10–12 pages) is a separate deliverable per [deck-structure.md](deck-structure.md). The memo is the analytical kernel; the deck is the dressed presentation of it.
