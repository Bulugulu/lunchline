# Follow-up: Grata coverage floor + Apollo-inside-Clay cost mechanics

Compiled 2026-05-31. Continuation of `company-sourcing.md`.

## 1. Grata coverage floor — does it have micro, owner-operated exec-search boutiques?

**Bottom line: probably partial, and it thins out exactly at our scale ($1–20M, 5–50 people, founder-owned).** Grata markets to the *middle market* and its own materials draw the line between itself and the tools that cover sub-scale owner-operated firms.

**(a) Published size/revenue floor or web-footprint minimum?** No explicit floor. Grata "canvasses the entire digital universe to surface all investable companies," capturing pages behind registrations, and *infers* revenue/headcount/industry through "inference, triangulation, and validation" plus government records and registries ([Grata data-science engine](https://grata.com/resources/grata-ai-data-science-engine-private-market-data); [Grata markets](https://grata.com/markets)). But absence of a stated floor cuts both ways — no published guarantee a 6-person firm is in-index, no disclosed completeness-by-size. Unverifiable from public docs; confirm by demo-searching the actual buy-box.

**(b) Smallest tier reliably indexed / completeness micro vs. mid?** Grata positions itself as "specifically built for the middle market" and explicitly contrasts with "platforms like Axial and BizBuySell [that] cater to small business acquisitions" ([Grata data-science engine](https://grata.com/resources/grata-ai-data-science-engine-private-market-data)) — the coverage tell: reliable data sits above true micro-firms. Revenue/headcount for small firms is modeled/estimated, not reported — fine for screening, weak for precise filtering at $1–5M. Industry-wide, completeness degrades under ~50 employees ([Cleanlist 15-provider test](https://www.cleanlist.ai/blog/15-best-b2b-data-enrichment-providers-in-2025-ranked); [ZoomInfo private-company-data guide](https://pipeline.zoominfo.com/sales/private-company-data-providers)). Grata claims 1M+ verified executive emails ([G2](https://www.g2.com/products/grata/reviews)) — finite against 16–21M companies, so principal-email coverage for the smallest firms is patchy.

**(c) Evidence of searchers using Grata for sub-$20M owner-operated firms?** Directional, not exec-search-specific. Grata states search funds "primarily target companies with $5–$30M in revenue" and runs a search-fund case (Peterson Partners, ~50% of their searchers on Grata) and the Pineland Capital outreach case ([Peterson case](https://grata.com/case-studies/fifty-percent-of-peterson-partners-searchers-use-grata); [Pineland case](https://grata.com/case-studies/driving-business-success-through-seamless-contacts-and-information-accessibility); [Search Funds resource](https://grata.com/resources/search-funds-the-shadow-asset-class-that-went-mainstream)). A G2 searcher review: 90% of deal flow from direct email outreach with Grata as primary tool ([G2](https://www.g2.com/products/grata/reviews)). Caveats: vendor-published cases (selection bias); $5–30M sits above the bottom of the $1–20M box; Peterson case references finding "hidden verticals (companies that aren't appearing in databases just yet)" — an admission the long tail isn't fully indexed. Searchfunder practitioners note most sourcing DBs hold roughly the same companies and keyword choice matters more than tool ([Searchfunder](https://searchfunder.com/post/tools-for-sourcing-leads-in-a-search-fund)).

**(d) Better for professional-services firms (websites + LinkedIn) than tiny trades?** Yes — the genuine good news. Coverage is built on crawling millions of company websites + digital signals. Exec-search boutiques have real websites, named partners, LinkedIn pages, and trade-press visibility (Hunt Scanlon/AESC), so they index far better than a 4-person HVAC shop. Net: expect solid firm discovery and decent principal identification, but treat revenue/headcount as estimates and expect principal-email gaps below ~10 employees. Use Grata to find/map the universe; backfill contacts with Apollo/Clay.

## 2. Apollo inside Clay — availability, cost, and the own-key catch

**Confirmed: Apollo is a first-class provider in Clay's marketplace** ([Cleanlist Clay vs Apollo](https://www.cleanlist.ai/blog/2026-03-19-clay-vs-apollo); [Salesmotion](https://salesmotion.io/clay-vs-apollo)). Two cost paths:

**Path A — Apollo via Clay Data Credits (no Apollo account):** post the March 11 2026 overhaul, marketplace costs dropped 50–90%; a lookup that was ~$0.50 is now ~$0.05–$0.25, credits start at $0.05 ([Clay pricing](https://www.clay.com/pricing); [Cleanlist Clay pricing changes](https://www.cleanlist.ai/blog/2026-03-12-clay-pricing-changes-2026); [Salesforge](https://www.salesforge.ai/blog/clay-pricing)).

**Path B — Apollo via your own API key inside Clay (recommended):** connecting your own Apollo key eliminates Clay Data-Credit cost for Apollo; you pay Apollo directly and Clay only charges ~1¢ per workflow Action ([Clay docs: Actions & Data Credits](https://university.clay.com/docs/actions-data-credits); [Salesforge](https://www.salesforge.ai/blog/clay-pricing)). Apollo's own enrichment API tier is where this lives.

**Cost for ~1,500 firms' principal contacts:**
- Standalone Apollo seat: business email = 1 credit, mobile = 8, email+phone = 9 credits/contact; ~30K credits/yr on the entry tier ([Saleshandy Apollo pricing](https://www.saleshandy.com/blog/apolloio-pricing/); [UpLead](https://www.uplead.com/apollo-vs-zoominfo/)). 1,500 email lookups fits easily — effectively near-flat monthly. Cheapest per record but a separate dataset/login (CSV export).
- Apollo-via-Clay credits (Path A): ~$0.05–$0.25/record → ~$75–$375 one-off for 1,500, plus Actions. More than a seat but inside the dedup/scoring/waterfall pipeline.
- Apollo-own-key-in-Clay (Path B): Apollo's flat data cost + Clay ~1¢/step Actions (~$15–$45 for a few steps × 1,500). **Optimum** — cheap data + Clay orchestration, no Clay markup.

**Limitations (flagged):**
- Apollo ToS restricts using its data outside Apollo's platform/permitted integrations; own-key-into-Clay is the sanctioned path, but no definitive public statement blesses the flow at scale — **verify before scaling** against current Apollo API/export terms.
- Match rate differs by path; independent tests put real-world contact accuracy ~15–20 pts below vendor claims ([Cleanlist 15-provider test](https://www.cleanlist.ai/blog/15-best-b2b-data-enrichment-providers-in-2025-ranked)) — waterfall Apollo with a second source.

**Net:** run Apollo on its own key connected into Clay (Path B) as the principal-contact layer; keep Clay-credit Apollo (Path A) as a convenience fallback.

> Note: a later focused check (`followup-linkedin-contact-tools.md`) found Apollo's **API access is the $79 Professional tier**, not the $49 Basic (Basic has no API). The own-key-into-Clay path therefore costs $79/mo. This supersedes the "$49 API" figure implied above.

### Unverified / flagged
- No public Grata doc states a hard size/revenue/web-footprint floor or completeness-by-size metrics.
- Grata search-fund evidence is vendor-published and targets $5–30M, above the bottom of the $1–20M box; not exec-search-specific.
- Whether Apollo's ToS explicitly permits own-key-in-Clay at scale was not findable publicly.
