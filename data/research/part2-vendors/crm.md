# CRM — Vendor Category

Compiled 2026-05-31.

## Shipped recommendation

**Attio (free to $59/seat/mo).** AI-native, ships an MCP server with **write** access, so the agent reads and maintains the pipeline directly. Affinity (~$2,000–2,700/seat/yr) has better automatic email capture but is priced for funds; HubSpot free tier is the fallback.

| Vendor | What it is | 2026 price | Agent | Verdict |
|---|---|---|---|---|
| Attio | AI-native CRM; MCP read+write | $0–$59/seat/mo | MCP ● | Recommended |
| Affinity | Category leader; best auto-capture; MCP gated to top tiers | ~$2,000–2,700/seat/yr | MCP ● | Skip (too pricey) |
| HubSpot | Generic CRM; free works, AI/automation paid | $0 / $20 per mo | API ◐ | Fallback |

---

## Original agent report

**Bottom line:** Affinity and 4Degrees (the relationship-intelligence picks the deal world cites) are quote-only and fund-priced (~$2,000–2,700/seat/yr and ~$400/seat/yr). The sweet spot for an AI-first solo searcher is **Attio** — AI-native, free tier, $29–69/user/mo, first-class official MCP server with write access.

**Profiles:**
- **Attio** — Notion-like customizable CRM. Free (3 users, 50k records); Plus $29; Pro $59 (sources differ $59/$69); Enterprise $119. Official hosted [MCP server](https://docs.attio.com/mcp/overview) with `create_record`/`update_record`/`create_note`/`create_task` (reads auto-approve, writes confirm) + REST + webhooks + OSS self-host ([kesslerio](https://github.com/kesslerio/attio-mcp-server)). Email/calendar sync auto-logs. Weakness: no native relationship-strength graph (matters less for cold owner outreach). ([attio.com](https://attio.com/); [folk on Attio pricing](https://www.folk.app/articles/attio-crm-pricing))
- **Folk** — lightweight, strong LinkedIn capture; Standard ~$20–30, Premium $40 (API gated to Premium). ([folk.app/pricing](https://www.folk.app/pricing))
- **4Degrees** — purpose-built relationship intelligence; quote-only (~$400/seat/yr estimate, conflicting); REST API, no first-party MCP. ([4degrees.ai](https://www.4degrees.ai/); [Capterra](https://www.capterra.com/p/184593/4Degrees/))
- **Affinity** — category leader, best auto-capture; ~$2,000/seat/yr ($2,700 AI-notetaking tier); official [MCP read+write](https://developer.affinity.co/pages/mcp/introduction) but gated to Scale/Advanced/Enterprise. ([prospeo](https://prospeo.io/s/affinity-pricing-reviews-pros-and-cons))
- **HubSpot Free/Starter** — generic; AI is paid-tier; robust API. Contact-tier overages a known trap at scale. ([HubSpot Starter](https://www.hubspot.com/products/crm/starter))
- Too heavy: DealCloud, Salesforce. Clay is NOT a CRM (enrichment feeder).

**Build-vs-buy:** DIY Notion+Custom Agents+MCP is the most capable custom path but weakest on reliable auto email/calendar capture, and Notion Custom Agents moved to metered credits **May 4 2026** ([Notion custom agents](https://www.notion.com/blog/introducing-custom-agents); [Notion MCP](https://developers.notion.com/guides/mcp/overview)). Airtable Omni weaker on external integrations ([Airtable Omni](https://support.airtable.com/docs/using-omni-ai-in-airtable)). Verdict: don't build from scratch, don't buy fund-grade — **buy Attio, let an agent run it**; keep HubSpot Free as fallback; ETA IQ (free, searcher-specific) as no-setup starter ([ETA IQ](https://searchfunder.com/post/introducing-eta-iq-the-first-crm-financial-modeling-platform-for-search-funds)).

**Agent read+write:** only Attio gives a solo-affordable tier AND first-class MCP write path. Affinity's MCP is equally good but enterprise-gated. Folk charges up to API.

**Community (2026):** searchers run cheap/simple — Searchfunder thread names Pipedrive, Zoho + Quickmail, not Affinity/4Degrees ([thread](https://searchfunder.com/post/what-crm-and-email-outreach-software-are-active-searchers-currently-using)). An AI-fluent searcher beats both camps with Attio at Pipedrive-class cost + MCP.

**Caveats:** Affinity/4Degrees/DealCloud/AlphaY/ETA IQ pricing not publicly listed (estimates); Attio Pro $59 vs $69 unconfirmed; whether Affinity/4Degrees sell single seats to solos unverified; Notion credit costs post-May-2026 unquantified.
