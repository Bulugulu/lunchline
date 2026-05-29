# Lunchline Partners Case Study

**Candidate:** Aviv Sheriff | **Due:** June 1, 2026 EOD | **Status:** Research & Planning

## Project Structure (Router)

This file routes to domain-specific docs. Read the relevant doc before working on a task.

| Task | Doc | What's There |
|------|-----|-------------|
| Open work items (next steps) | [TODO.md](TODO.md) | Active queue: pitch tournament, build items, blocking decisions |
| Changelog & status | [CHANGELOG.md](CHANGELOG.md) | What's been done; per-session notes |
| Case requirements & email | [docs/case-overview.md](docs/case-overview.md) | Full brief, deliverables, evaluation criteria |
| Part 1: Public company pitch | [docs/public-company-pitch.md](docs/public-company-pitch.md) | Selection framework, scoring, screening filters |
| Per-candidate **evaluation = THE DEEP FLOW** | [docs/methodology.md](docs/methodology.md) § The Deep Flow | **The standard (and only) verdict-producing process.** SOTP + operating/driver model + DCF (on cash taxes) + Porter's + sensitivity tornado + consensus + VCP + kill criteria + known-unknowns, run as agent-builds → lead-reviews → iterate. |
| Dossier + structural scripts (scoring SUPERSEDED) | [docs/pipeline.md](docs/pipeline.md) | Dossier + voting/deal-status scripts (still used). The 6-criterion / findings-mode *scoring* is retired — it produced wrong conclusions; use the Deep Flow. |
| Analytical methodology | [docs/methodology.md](docs/methodology.md) | The Deep Flow; six lessons from exemplar decks; sourcing discipline (lead with the discount driver); sequenced workstreams |
| Deck structure & design | [docs/deck-structure.md](docs/deck-structure.md) | Slide scaffolds; locked design system (Direction 1); exemplar sources |
| Memo principles (what to include + checklist) | [docs/memo-principles.md](docs/memo-principles.md) | Required content blocks, voice rules, forbidden moves, drafting checklist |
| Memo voice & exemplar research | [docs/memo-voice.md](docs/memo-voice.md) | Buffett/Marks/Einhorn voice patterns, plain-English vocabulary, annotated excerpts, full skeleton |
| Canonical memo template | [mockups/pitches/option-a-scroll.html](mockups/pitches/option-a-scroll.html) | AENT memo written to demonstrate the voice principles — use as starting point for every new candidate memo |
| Part 2: Market mapping | [docs/market-mapping.md](docs/market-mapping.md) | End market selection, vendor stack, automation map |
| Data sources for screening | [docs/screening-research.md](docs/screening-research.md) | yfinance / EDGAR / Finviz reference table |
| Aviv's relevant background | [docs/background-context.md](docs/background-context.md) | Sectors of expertise, competitive advantages |
| Prompt log (required appendix) | [docs/prompt-log.md](docs/prompt-log.md) | Running log of AI prompts and their outcomes |

## Working Conventions

- **Candidate evaluation = the Deep Flow only — no shallow verdicts:** The mechanical screen (`framework_screen.py`) only *generates suspects*; it produces NO buy/avoid verdict. Every candidate we actually evaluate goes through the full **Deep Flow** (SOTP + operating/driver model + DCF on *cash* taxes from the cash-flow statement + sensitivity tornado + Porter's Five Forces + consensus baseline + value-creation plan + kill criteria + known-unknowns), run as an **agent-builds → lead-reviews → iterate** loop until we've extracted everything the data allows. The shallow single-bear "trap/keep" pass is **retired** — it produced wrong conclusions (it called USNA a value trap; the deep flow reversed it, then disciplined it to a calibrated answer). Spec: `docs/methodology.md` § The Deep Flow. Choosing *which* screened suspects get the deep flow is neutral prioritization (cheapness, under-followed, the three escalation flags — recent acquisition / net-cash-heavy / control-holder), never a shallow judgment.
- **Subagent delegation:** Use subagents for research, critiquing drafts, and independent analysis to maintain objectivity
- **Verification:** All financial data must be cross-referenced against current sources (SEC filings, earnings reports)
- **Citations:** Every claim needs a source with an active hyperlink
- **Tone:** Original thinking, specificity over polish, clear POV defended with evidence
- **AI disclosure:** Log every significant prompt interaction in prompt-log.md
- **No hardcoded benchmarks:** Per-company multiples come from peer research, not from sector-generic defaults. When you research peers for a candidate, **persist findings** to `data/research/<ticker>/peer_benchmarks.csv` (schema in `scripts/valuation.py` docstring) and write peer-selection rationale to `data/research/<ticker>/peer_notes.md`. Future sessions read these files instead of re-doing research. Mark each peer as `primary` / `secondary` / `excluded` with notes.
- **TODO and CHANGELOG:** Open work items live in `TODO.md`. Completed work moves to `CHANGELOG.md`. Per-candidate workstreams (mispricing diagnosis, consensus dossier, etc., per `docs/methodology.md`) live in `data/research/<ticker>/`, not in TODO.
