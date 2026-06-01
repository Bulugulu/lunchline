# Lunchline Partners — Case Study

**Candidate:** Aviv Sheriff

This repository holds the full working record for the Lunchline Partners case study — both the finished deliverables and the research, models, and AI workflow behind them.

---

## 📂 Start here — the deliverables

If you only want the finished artifacts, everything is in **[`deliverables/`](deliverables/)**:

| File | What it is |
|---|---|
| **[Part1-ARTW-pitch-deck.pdf](deliverables/Part1-ARTW-pitch-deck.pdf)** / `.pptx` | Part 1 — public-company investment pitch on **Art's-Way Manufacturing (NASDAQ: ARTW)** (11 slides) |
| **[Part1-ARTW-model.xlsx](deliverables/Part1-ARTW-model.xlsx)** | Part 1 — supporting valuation & returns model (live formulas; ties to the deck) |
| **[Part2-market-mapping-deck.pdf](deliverables/Part2-market-mapping-deck.pdf)** / `.pptx` | Part 2 — AI-enabled market mapping & sourcing strategy (executive search) |
| **[prompt-log-appendix.pdf](deliverables/prompt-log-appendix.pdf)** | Required appendix — tools used, prompts that worked, where AI helped or hurt |

> PDFs preview directly in GitHub. The `.pptx` / `.xlsx` files download on click; the Excel model is **live-formula** and recalculates on open in Excel.

---

## The two answers, in a sentence

- **Part 1 — ARTW.** A cyclical farm-equipment maker wraps a growing, ~17%-margin builder of research and biosecurity labs. The thesis is a search-fund-style operator carve-out: buy control near book value, sell off the farm equipment to clear the debt, and own the lab builder. Control-basis fair value ≈ **$2.95** vs **$2.58**, with a real asset floor.
- **Part 2 — Executive search.** A 12-month, AI-leveraged sourcing plan for acquiring a boutique retained executive-search firm: project plan, a four-category vendor stack, and a human-vs-automation map across the funnel. The vertical was chosen *by* the methodology, not assumed.

---

## How the work was done

The pitch wasn't a single guess — it came out of an all-sector screen, a multi-candidate tournament, and a deep per-company valuation process. The reasoning is documented:

- **[docs/methodology.md](docs/methodology.md)** — *The Deep Flow*: the SOTP + driver model + DCF (on cash taxes) + Porter's + sensitivity + value-creation-plan process every candidate went through.
- **[docs/prompt-log.md](docs/prompt-log.md)** — the AI workflow in seven phases (also the appendix PDF above).
- **[docs/case-overview.md](docs/case-overview.md)** — the original brief and deliverables.
- **[CHANGELOG.md](CHANGELOG.md)** — session-by-session record of what was built.

The full ARTW work — the model write-up, peer benchmarks, WACC build, filing review, and competitor comps — lives in **[`data/research/artw/`](data/research/artw/)** (start with `model.md`).

---

## Repository map

```
deliverables/            ← the finished decks, model, and appendix (start here)
docs/                     ← methodology, prompt log, memo principles, case brief
  case-overview.md          the brief
  methodology.md            the Deep Flow (the valuation process)
  prompt-log.md             AI usage appendix
data/
  research/artw/          ← ARTW model.md, peer benchmarks, WACC & filing research
  screening/              ← the candidate catalogs ARTW was selected from
  framework_filtered.csv    the all-sector screen output
mockups/pitches/         ← HTML source for the decks (the deliverable PPTX/PDF render from these)
  artw-deck.html            Part 1 pitch (source of truth)
  part2-deck.html           Part 2 market mapping (source of truth)
scripts/                 ← reproducible Python: screening, EDGAR/data pulls, model + deck builders
CLAUDE.md                ← project router / working conventions
```

The decks are authored as HTML (`mockups/pitches/`), which is the single source of truth; the PPTX/PDF in `deliverables/` are rendered from it.

---

## Reproduce

```bash
pip install -r requirements.txt

# rebuild the ARTW Excel model (live formulas, ties to the deck)
python scripts/rebuild_artw_v3.py

# render a deck (HTML → pixel-perfect PPTX + PDF)
python scripts/build_deck_artifacts.py mockups/pitches/artw-deck.html Part1-ARTW-pitch-deck

# render the prompt-log appendix (markdown → PDF)
python scripts/build_promptlog_pdf.py docs/prompt-log.md deliverables/prompt-log-appendix.pdf
```

Deck rendering uses headless Chromium via Playwright (`python -m playwright install chromium`). Data scripts read API keys from the environment (`os.environ`); none are committed.

---

## A note on AI

This case asked for *demonstrated fluency with AI as a working tool*, and the repo is meant to show that honestly — including where AI fell short. The prompt-log appendix documents the tools, the prompts that worked, and the failure modes (e.g., agents stating confident-but-wrong numbers, which a verification pass caught). Every load-bearing figure in the deck was rebuilt from the primary filings.
