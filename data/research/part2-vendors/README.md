# Part 2 — Vendor Stack Research

Source research behind `mockups/pitches/part2-vendor-stack.html`. Compiled 2026-05-31 via parallel category research agents + targeted follow-ups. Pricing is 2026; sales-gated figures are third-party estimates and labeled as such. All claims carry active source URLs in the per-file reports.

## Files
- `market-research.md` — Market Research category (reframed to labor-market / demand-signal analytics)
- `company-sourcing.md` — Company Research / Sourcing category
- `crm.md` — CRM category
- `outbound.md` — Outbound category
- `followup-grata-apollo-coverage.md` — Grata coverage floor at micro-scale + Apollo-inside-Clay cost mechanics
- `followup-linkedin-contact-tools.md` — Kaspr vs Lusha vs Wiza vs Apollo for the LinkedIn-native contact layer
- `outbound-pressuretest.md` — **(2026-05-31) revises the Outbound pick.** Smartlead→Apollo/Superhuman (real-domain paradigm), LinkedIn rework, adds phone, open-rate-tracking caveat. HTML rewrite deferred.
- `sourcing-channels-and-brokers.md` — **project-plan input, not vendor-stack.** Channel landscape (64% proprietary / 37% broker; 3,000→159→4→1 funnel) + broker/marketplace/referral channels for the sourcing workstream.
- `exec-search-universe-size.md` — **funnel sanity check.** US exec-search universe ~2,500–3,500 employer firms → retained acquirable boutiques only ~500–1,000 nationally (~hundreds NE). ~3,000 unique leads is NOT realistic → project-plan funnel reframed to ~750 firms at a ~20% blended reply target.

## Final recommendation (as shipped in the deck)

Guiding principles: (1) every tool feeds one AI agent via MCP/API; (2) pay only for differentiated/alpha data; (3) fit to this search (executive search, owner-operated, demand-driven), not generic subscriptions.

| Category | Pick | ~ / mo |
|---|---|---|
| Market Research | BLS / Census / FRED + Revelio RPLS + IBISWorld (all free) | $0 |
| Company Sourcing | Clay (core) + Apollo $79 (own-key into Clay); discovery free via directories + Claygent; Grata optional | $264–574 |
| CRM | Attio (AI-native, MCP read+write) | $0–59 |
| Outbound | Smartlead + HeyReach + Handwrytten; agent + Clay write messages | ~$272 |

> **Outbound revised (2026-05-31, shipped to HTML) — two tools only.** Smartlead dropped (wrong paradigm at ~190/mo). New Outbound = **Superhuman ($33, email + tracking + AI) + Handwrytten ($99, real pen-and-ink cards)**. LinkedIn worked by hand; phone on the existing OpenPhone line; Apollo sequences a $0 optional. ~$132/mo; all-in stack now ~$430–800. Open-rate tracking is broken in 2026 (Apple MPP) — judge on replies/clicks. Detail in `outbound-pressuretest.md`.

All-in ~$500–900/mo vs. $15k–120k+/yr per category for the institutional stack.

## Key resolved questions
- **Market research ≠ company research.** Reframed to demand-signal analysis (hiring × industry × geography) feeding a per-firm "demand-fit score" computed by the agent from free government APIs.
- **Clay owns no database** — it is orchestration + AI enrichment (Claygent) + a pay-per-credit marketplace wrapping other providers (incl. Apollo via own-key).
- **Grata** is built for the mid-market; data thins below ~10 employees and revenue/headcount are estimates. Useful for discovery/mapping only, not financials. Demoted to optional accelerator.
- **Apollo API is the $79 Professional tier**, not the $49 Basic (Basic has no API). Own-key-into-Clay (Path B) avoids Clay data-credit markup.
- **Kaspr** is a worse primary contact layer for a US, agent-orchestrated workflow (EU database, weak US mobiles, API only at $79, CNIL €240k fine for LinkedIn scraping). Bench it; Lusha's free extension beats it for manual US spot-checks.

## Caveats to re-verify before relying
- IBISWorld free access via Searchfunder: announced 2020, expanded Jan 2023 — confirm still live in 2026.
- All sales-gated pricing (Grata, Inven, Affinity, 4Degrees, LinkedIn Talent Insights, Lightcast paid, Revelio paid) — get live quotes.
- Apollo ToS for own-key-into-Clay at high volume — verify against current API/export terms.
- AI-vendor pricing moves monthly.
