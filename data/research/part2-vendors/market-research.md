# Market Research — Vendor Category

Compiled 2026-05-31. NOTE: this category was later **reframed** (see deck + README). The original agent answered "market research = industry reports"; the locked direction is **demand-signal analysis** (hiring × industry × geography → per-firm demand-fit score), served by free labor-market APIs. The shipped recommendation is the free stack: **BLS / Census / FRED + Revelio RPLS (free) + IBISWorld (free via Searchfunder)**; paid feeds (Revelio $85k/yr, LinkedIn Talent Insights ~$6–20k/yr, Lightcast custom) are skipped. Labor-market tool pricing is in `../part2-vendors/` follow-ups and below.

## Reframed pick (shipped)

| Tool | Measures | 2026 price | Agent | Verdict |
|---|---|---|---|---|
| BLS / Census / FRED | Hiring (JOLTS), occupation & industry growth projections, employment by industry × metro | Free, public APIs | MCP/API | Recommended |
| Revelio Labs | Headcount, hiring, attrition by role × industry × geo | Free RPLS · $85,000/yr paid | API | Free tier |
| IBISWorld | Underlying-industry growth + Executive Search 5670 report | $0 via Searchfunder | Manual | One-time read |

Labor-tool detail (Revelio $85k/yr paid via AWS Marketplace; free RPLS dataset; Lightcast free Open Skills API + paid custom; LinkedIn Talent Insights ~$6–20k/yr; BLS/Census/FRED free APIs; Indeed Hiring Lab free) — sources:
- [Revelio AWS Marketplace $85k](https://aws.amazon.com/marketplace/pp/prodview-m7h5in35nozha) · [Revelio RPLS free](https://www.reveliolabs.com/public-labor-statistics/)
- [Lightcast pricing](https://lightcast.io/products/pricing) · [Lightcast free API](https://docs.lightcast.io/lightcast-api/docs/free-api-access) · [Open Skills](https://lightcast.io/open-skills/access)
- [LinkedIn Talent Insights estimate](https://valuablerecruitment.com/blog/linkedin-talent-insights-guide)
- [BLS Developers](https://www.bls.gov/developers/home.htm) · [Census API key](https://api.census.gov/data/key_signup.html) · [Official Census MCP](https://github.com/uscensusbureau/us-census-bureau-data-api-mcp) · [FRED API](https://fred.stlouisfed.org/docs/api/fred/)
- [Indeed Hiring Lab](https://www.hiringlab.org/)

**Key cross-finding:** none of the premium vendors (Revelio paid, Lightcast paid, LinkedIn TI, TalentNeuron) show documented search-fund/ETA adoption — priced for institutions. The realistic searcher stack is the free government APIs + Indeed + Lightcast free Open Skills + Revelio free RPLS.

---

## Original agent report (industry-report framing, superseded)

Scope as originally briefed: sizing the market, industry structure/fragmentation, secular drivers, fee economics, benchmarks.

**Bottom line (original):** paying list price for IBISWorld/Statista Pro/PitchBook/AlphaSense for one deal is a near-certain waste. IBISWorld is free via Searchfunder; Statista ships a native MCP; Deep Research agents (ChatGPT/Perplexity/Gemini, $20/mo) do the aggregation. AlphaSense/PitchBook/Tegus over-built for a one-deal fragmented private market — buy à la carte at most (one Tegus call in diligence).

Vendors profiled (original): IBISWorld (free via [Searchfunder](https://searchfunder.com/post/now-every-searchfunder-member-can-access-ibisworld); report 5670 = highly fragmented, no firm >5%); Statista (native [MCP server](https://www.statista.com/business/connect-mcp)); AlphaSense/Tegus ($15–20k/seat, [Tegus pay-as-you-go expert calls](https://tegus.com/experts)); PitchBook (skip); Perplexity/OpenAI/Gemini Deep Research ($20/mo, [OpenAI deep research](https://openai.com/index/introducing-deep-research/)).

Searchfunder × IBISWorld: Master License Agreement announced **Sep 1 2020** ([announcement](https://searchfunder.com/post/searchfunder-and-ibisworld-announce-partnership)); expanded to unlimited community access **Jan 9 2023** ([post](https://searchfunder.com/post/now-every-searchfunder-member-can-access-ibisworld)); ~5,132 reports; no 2024–2026 end/renewal notice found — probable-but-unverified for 2026. License prohibits download/export (manual read only).

Macro adoption: GenAI used across M&A lifecycle — ~40% of adopters for strategy/market assessment ([Deloitte 2025 M&A GenAI study](https://www.deloitte.com/us/en/what-we-do/capabilities/mergers-acquisitions-restructuring/articles/m-and-a-generative-ai-study.html)).
