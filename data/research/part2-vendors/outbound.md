# Outbound — Vendor Category

Compiled 2026-05-31.

## Shipped recommendation

**Rent the sending rails, build the personalization.** Smartlead ($94/mo, 116-tool MCP) for email deliverability; HeyReach ($79/mo) for LinkedIn; Handwrytten (~$99/mo + per card) for pen-and-ink mail; a Claude agent + Clay write the per-owner message.

| Vendor | What it is | 2026 price | Agent | Verdict |
|---|---|---|---|---|
| Smartlead | Email send: warmup, inbox rotation, deliverability; 116-tool MCP | $94/mo (Pro) | MCP ● | Recommended |
| HeyReach | LinkedIn automation with MCP | $79/mo | MCP ● | Recommended |
| Handwrytten | Real pen-and-ink mail via API | ~$99/mo + per card | API ◐ | Recommended |

**Reply-rate reality:** ≥10% holds only multi-channel. Cold email alone ~3.4% platform-wide; a searcher who closed a deal saw 2–4% on email; postal mail most effective; LinkedIn connection acceptance ~1-in-4–5 ([Searchfunder 2-acquisition case](https://searchfunder.com/post/thought-piece-proprietary-sourcing-methods-that-delivered-2-acquisitions); [martal.ca](https://martal.ca/b2b-cold-email-statistics-lb/)). Lead with LinkedIn + mail, email as reinforcement. Human owns every reply/call.

---

## Original agent report

**Profiles (ranked for relationship-led owner outreach):**
- **Smartlead** — high-deliverability sender: unlimited mailboxes, inbox rotation, unlimited warmup, master inbox. Basic $39, Pro $94 (API+webhooks+white-label), custom ~$174. Strongest MCP story — official server, 113–116+ tools ([Smartlead MCP](https://helpcenter.smartlead.ai/en/articles/300-smartlead-mcp-server); [build guide](https://www.smartlead.ai/blog/build-ai-outbound-agent-smartlead-mcp)). Weakness: email-only, deliverability infra somewhat overkill at ~190/mo.
- **Clay** — AI-personalization brain; waterfalls 100+ providers + Claygent drafts per-owner touch. Launch $185, Growth $495 ([Clay pricing](https://www.clay.com/pricing)). Clay is an MCP *client*, not server — your external agent can't call Clay via MCP; treat as pre-processing ([Salesforge Clay MCP](https://www.salesforge.ai/blog/clay-mcp)).
- **HeyReach** — LinkedIn automation, multi-account; $79 (3 senders), $199 (unlimited). Webhooks + API + MCP server ([HeyReach pricing](https://www.heyreach.io/pricing); [puzzleinbox](https://puzzleinbox.com/compare/heyreach-pricing-review/)). LinkedIn is where older owners respond (personalized notes 30%+ acceptance). Account-restriction risk — keep volume low. Alts: Expandi $99, La Growth Machine €60–180.
- **lemlist** — multichannel single-tool (email+LinkedIn+calls), AI sequences, warmup; Multichannel Expert ~$87–109 ([costbench](https://costbench.com/software/sales-engagement/lemlist/)).
- **Instantly.ai** — high-volume email infra; Growth $47, Hypergrowth $97; MCP ~38 tools. Overkill for ~190 personalized touches; de-prioritized ([Instantly pricing](https://instantly.ai/pricing)).
- Also: **Apollo** ($49–119; ~15–20% bounce on some SMB segments — risky as sender; use as data source). **Handwrytten** — real pen-ink mail, from $3.75/card or $99/mo, full JSON API + integrations, ~$1,000 to clone your handwriting ([Handwrytten pricing](https://www.handwrytten.com/pricing/)). Highest-signal channel per searcher evidence. **Bantum** — purportedly searcher-specific multi-agent ($100–200/mo) but UNVERIFIED (single secondary source).

**Build-vs-buy:** buy the rails, build the brain. DIY sending infra (domains $10–17/yr, separate Workspace tenants, SPF/DKIM/DMARC, warmup) saves ~$50/mo but a single Google tenant lockout costs weeks of pipeline ([prospeo](https://prospeo.io/s/google-workspace-cold-email)). Rent deliverability; build personalization + orchestration. Indicative all-in ~$270/mo (Smartlead+HeyReach+Handwrytten) without Clay; ~$455–565 with Clay.

**Single-agent orchestration + human tension:** MCP lets one Claude agent control email (Smartlead) + LinkedIn (HeyReach) + mail (Handwrytten), with Clay as MCP-client pre-processing. AI does list-building, enrichment, per-owner research, drafting, scheduling, follow-up cadence, reply classification, CRM hygiene. Human does every reply, call, judgment, and the wet-ink signature. ~190/mo is small enough a human can own all replies. Community wary of over-automating owner outreach ([searcherinsights](https://searcherinsights.com/what-is-a-search-fund/); [Searchfunder proprietary outreach](https://www.searchfunder.com/post/proprietary-outreach-targeting)).

**Caveats:** pricing third-party-sourced and volatile (Clay re-architected Mar 11 2026); Bantum unverified; MCP tool counts drift; reply-rate figures are channel benchmarks, not exec-search-specific.
