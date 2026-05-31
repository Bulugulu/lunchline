# Follow-up: LinkedIn-native contact tools (Kaspr / Lusha / Wiza vs Apollo)

Compiled 2026-05-31. Triggered by evaluating Kaspr for the contact layer.

**Use case:** ~1,500 exec-search firms, US-based partners with rich LinkedIn profiles; need verified personal emails + direct/mobile phones + multi-channel (email/phone/mail); everything must feed one AI agent (Clay + Claude via API/MCP). So a programmatic API at a cheap tier matters more than a Chrome extension, and US data depth is the gating factor.

## Comparison

| Tool | 2026 price + free tier | API? | US email | US mobile | LinkedIn account risk | Source |
|---|---|---|---|---|---|---|
| **Kaspr** (Cognism) | Free: 5 phone + 5 direct-email + ~10 export credits/mo. Paid: Starter $49/mo (1,200 phone/yr, only 60 direct-email/yr), Business $79/mo (2,400 phone + 2,400 email/yr), Org custom. | API on Business ($79)+ (Starter API "on request" — disputed). Native HubSpot/Salesforce/Pipedrive/Zapier; can feed Clay via HTTP. | Decent globally (~75–80%) but "drops off for North American data." | Weakest US (~50–65%); EU-strong (Cognism DB). | Highest. CNIL fined Kaspr €240,000 (Dec 5 2024) for scraping LinkedIn users who restricted visibility. Core mechanic is the LinkedIn extension. | [kaspr.io/pricing](https://www.kaspr.io/pricing), [prospeo](https://prospeo.io/s/kaspr-pricing), [CNIL](https://www.cnil.fr/en/data-scraping-kaspr-fined-eu240000), [syncgtm](https://syncgtm.com/blog/kaspr-review) |
| **Lusha** | Free ~70 credits/mo, no card. Premium ~$52/user/mo annual (~$70 monthly), 5 seats. | API on Premium+; CRM sync only on Scale (custom). Phones cost 10 credits web / 5 API. | Strong US (~87% deliverable in tests vs 98% claimed). | Best US phone of the three (~62–83%). | Moderate — browser-extension on LinkedIn; no CNIL-scale enforcement on record. | [lusha.com/pricing](https://www.lusha.com/pricing/), [prospeo](https://prospeo.io/s/lusha-pricing), [salesmotion](https://salesmotion.io/blog/lusha-pricing) |
| **Wiza** | Free: 20 email + 5 phone credits/mo. Starter $49/mo, Email $99/mo, Email+Phone $199/mo (annual ~$166), Team custom. | Yes, REST API. Native Clay integration with bring-your-own-key on any paid plan — cleanest programmatic fit. Real-time verify, bounce <1%. Requires active Sales Navigator seat (~$99–150/mo). | Strong, real-time verified US emails. | Good US mobiles on Email+Phone tier. | Lower as an API workflow (Clay calls Wiza server-side); export workflow leans on your Sales Nav account. | [wiza.co/pricing](https://wiza.co/pricing), [clay.com/integrations/wiza](https://www.clay.com/integrations/data-provider/wiza), [prospeo](https://prospeo.io/s/wiza-pricing) |
| **Apollo.io** (baseline) | Free tier; Basic $49/user/mo (NO API); Professional $79/user/mo = API; Org $119. | API on Professional ($79)+. Enrich + "Retrieve Mobile Phone Numbers" endpoints; own-key-into-Clay standard. | Large US own DB. | Decent US mobiles (credit-gated). | Lowest — enriches from own DB via API; no LinkedIn extension in the agent path. | [apollo.io/pricing](https://www.apollo.io/pricing), [docs.apollo.io/api-pricing](https://docs.apollo.io/docs/api-pricing), [salesmotion](https://salesmotion.io/blog/apollo-pricing) |

## Direct answers

**Usable API at an affordable tier (agent/Clay, no human clicking)?**
- Wiza — cleanest: native Clay integration, own-key on any paid plan, server-side reveal (hidden cost: Sales Nav seat).
- Apollo — API at $79 Professional (NOT $49 Basic — common trap), own-key-into-Clay, own DB so no extension.
- Kaspr — API realistically $79 Business (Starter API disputed; don't budget on it).
- Lusha — API on Premium (~$52) but no CRM sync until Scale; phones credit-expensive.

**Best for manual browsing of high-value targets?** Kaspr or Lusha Chrome extension for one-click reveal — between them, **Lusha for US partners** (better US phone/email), Kaspr only if some targets are EU. Kaspr's free 5+5/mo is a fine zero-cost spot-check.

## Recommendation (dry)

For this US-only, agent-orchestrated workflow, **Kaspr is a worse primary contact layer than Apollo** — Cognism's European DB, US mobile ~50–65%, real API at $79, plus the only six-figure regulator fine in the set (CNIL €240k) for exactly the LinkedIn-scraping behavior this job depends on. **Apollo ($79 Professional, API + own-key into Clay) is the better programmatic baseline.** **Wiza** is the strongest LinkedIn-native complement (real-time-verified US emails/mobiles into Clay via own key) — budget ~$199 Email+Phone + a Sales Nav seat, likely overkill for 1,500 firms where deliverability matters more than perfect mobiles. **Keep Kaspr (or Lusha) only as a free/cheap manual extension fallback for individual high-value partners; Lusha beats Kaspr there for US.**

### Flagged unverifiable / disputed
- Whether Kaspr Starter $49 includes any API (kaspr.io says "limited, on request"; prospeo says Business-only). Treat $79 as the API floor.
- Lusha free-credit count (40 vs 70/mo) varies by source.
- Lusha/Apollo per-credit phone pricing from third-party teardowns, not first-party pages.
- US email/phone accuracy figures are third-party test estimates, not audited vendor numbers.
