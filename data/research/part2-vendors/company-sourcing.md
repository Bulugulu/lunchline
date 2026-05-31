# Company Research / Sourcing — Vendor Category

Compiled 2026-05-31. See `followup-grata-apollo-coverage.md` and `followup-linkedin-contact-tools.md` for the deeper coverage/cost/contact-tool follow-ups that shaped the shipped recommendation.

## Shipped recommendation

Discovery is **free** for this market — exec-search firms are web-visible (websites, named partners, LinkedIn, directories: AESC, Hunt Scanlon, BlueSteps). Scrape + structure via Claygent.
- **Clay (core, $185–495/mo)** — orchestration + AI enrichment + personalization; wraps providers (incl. Apollo via own-key); owns no target database.
- **Apollo ($79/mo Professional, own-key into Clay)** — verified personal emails + verification; bought for deliverability, not discovery; cancel after the list is enriched.
- **Grata (optional accelerator)** — discovery/mapping only; revenue/headcount are estimates; contacts thin below ~10 people; built for mid-market, not micro.
- **Bench:** Lusha free extension for manual one-click reveal on high-value partners (better US than Kaspr).

What we get per firm: name, site, location, practice/industry mix, partner names, ~headcount, emails, AI-inferred owner/succession flags. What we don't: audited financials or confirmed sale-intent (inference + the call).

---

## Original agent report

**Most important 2026 fact:** Grata and SourceScrub are now the same company (Datasite). Datasite acquired Grata early 2025 and SourceScrub (from Francisco Partners) **Aug 8 2025**, merging SourceScrub into Grata ([Datasite press](https://www.datasite.com/en/company/news/datasite-to-merge-sourcescrub-and-grata-expanding-private-market-intelligence-solutions); [Grata announcement](https://grata.com/resources/datasite-sourcescrub-acquisition); [Yahoo Finance](https://finance.yahoo.com/news/datasite-acquire-sourcescrub-expanding-private-130000309.html)). The "buy both for coverage" hedge is dead; vendor leverage drops — raising the value of building internally.

**Vendors profiled:**
- **Grata (+ SourceScrub)** — AI-native private-company search, 21M+ (Grata) + 16M (SourceScrub); founder-owned/non-sponsored focus; [Company Data API](https://grata.com/api) (enterprise add-on). Sales-gated, ~$10k–100k+/yr per third-party trackers ([G2](https://www.g2.com/products/grata/reviews); [Grata pricing](https://grata.com/pricing)). No verified search-fund-tier price; get a quote.
- **Clay** — AI enrichment/orchestration. Google Maps/LinkedIn/website scraping, waterfall owner-ID + email validation, dedup, scoring ([Clay Google Maps](https://www.clay.com/blog/google-maps-lead-generation-for-niche-leads); [Claygent](https://www.clay.com/claygent)). March 11 2026 repricing → Launch $185/mo, Growth $495/mo, data costs down 50–90% ([Clay pricing](https://www.clay.com/pricing); [Cleanlist](https://www.cleanlist.ai/blog/2026-03-12-clay-pricing-changes-2026)). MCP client + webhooks + HTTP API on Growth; no inbound API endpoint ([Synter](https://syntermedia.ai/blog/clay-integration-architecture); [Crustdata](https://crustdata.com/blog/why-clay-doesnt-work-custom-data-workflows)).
- **Inven.ai** — AI lookalike search, 28M+ companies; ~$10k/user/yr per comparison ([Inven](https://www.inven.ai/); [vs PitchBook](https://www.inven.ai/articles/deal-sourcing-platform-comparison-inven-vs-pitchbook)).
- **Apollo.io** — 230M+ contacts; $49/user/mo Basic (NOTE: API requires Professional $79 — see follow-up); covers exec-search principals well; public API ([Apollo vs ZoomInfo](https://www.apollo.io/insights/apollo-vs-zoominfo); [UpLead](https://www.uplead.com/apollo-vs-zoominfo/)).
- **ZoomInfo** — enterprise, ~$15k–40k/yr; overkill ([UpLead](https://www.uplead.com/apollo-vs-zoominfo/)).
- Also-rans: Cyndx, Udu, Data Axle Genie ($149/mo), Axial (brokered network), BizBuySell/DealStream, Phantombuster ($69–439/mo; LinkedIn ToS/account-restriction risk — [Leonar](https://www.leonar.app/blog/how-to-scrape-linkedin-recruiter/)).

**Coverage note:** exec-search market highly fragmented (no firm >5%), succession-driven ([IBISWorld 5670](https://www.ibisworld.com/united-states/industry/executive-search-recruiters/5670/); [Hunt Scanlon](https://huntscanlon.com/will-the-surging-ma-market-for-executive-search-firms-continue/)). Firms are professional-services with websites + LinkedIn + named partners → far more discoverable than typical sub-scale ETA targets → self-sourcing unusually viable.

**Build-vs-buy verdict:** Build-led hybrid. Clay-orchestrated spine (~$8–15k for the 12-mo search incl. Clay + Sales Nav + scraper + Apollo + LLM credits) vs. a single Grata seat ($10–40k+/yr). Rent one discovery DB 3–6 months to seed + catch long tail, then lapse. MCP is becoming the default agent protocol ([Atlan](https://atlan.com/know/when-to-use-mcp-vs-api/)).

**Caveats:** no verified 2026 search-fund price for Grata/Inven/Cyndx (sales-gated); post-merger Grata pricing/roadmap not public; LinkedIn scraping carries ToS/account risk.
