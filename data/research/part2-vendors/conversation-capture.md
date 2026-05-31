# Conversation Capture — Vendor Category (added)

Compiled 2026-05-31. New 5th category: capture every qualifying call and Google Meet, transcribe, and feed transcripts automatically into the AI repo/logs so the agent summarizes, extracts next steps, and updates the pipeline.

## Shipped recommendation

Two-tool split — no single bot-less tool captures both Google Meet on Windows AND cell calls.
- **Granola Business ($14/user/mo)** — Google Meet via system audio, **no bot**; **native Windows app** (Mac-only era over); MCP transcript access on Business tier (free tier = notes only, no API).
- **OpenPhone / Quo Business ($23/user/mo)** — softphone; native call transcription; **call-transcript webhook** pushes JSON to the repo on call end (inbound + outbound, any cell number). Doubles as the phone-outreach channel.
- Both → one ingestion endpoint (n8n/Zapier/serverless) → markdown into the repo → trigger the agent. ~$37/mo combined.
- **Alternative:** Fireflies Pro ($10) — strongest webhook/MCP, but a recorder bot joins the call (worse for sensitive owner calls).

## Comparison

| Tool | 2026 price + free tier | Meet | Phone/cell | API/MCP/webhook | Windows? | Bot-less? | Source |
|---|---|---|---|---|---|---|---|
| **Granola** | Free (limited history); Business $14/user/mo (unlimited + API + MCP); Enterprise $35 | System audio, no bot | iOS app, outbound only; no Windows/cell | API + MCP (official, Feb 2026) on Business+ | **Native Windows app** | Yes | [pricing](https://www.granola.ai/pricing) · [Meet](https://www.granola.ai/blog/granola-google-meet-integration-recording-transcription) · [phone](https://docs.granola.ai/help-center/ios/phone-calls) |
| **OpenPhone / Quo** | Starter $15; Business $23 (AI transcripts/summaries); Scale $35 | n/a (it is the phone) | **Native VoIP transcription, in/outbound, any cell** | **API all plans + call-transcript webhook** | Web/desktop/mobile | n/a | [API](https://www.openphone.com/product/api) · [transcript webhook](https://www.openphone.com/docs/mdx/api-reference/webhooks/create-a-new-webhook-for-call-transcripts) · [pricing](https://www.cloudtalk.io/blog/openphone-pricing/) |
| **Fireflies** | Free (800 min); Pro $10 (API); Business $19; Enterprise $39 | Bot joins | Dialer/uploads; no native cell tap | Strong API + official remote MCP (OAuth) | Web | No (bot) | [pricing](https://fireflies.ai/pricing) · [MCP](https://docs.fireflies.ai/getting-started/mcp-configuration) |
| Circleback | Individual $20.83; Team $25 | Bot joins | In-person; no native cell | API + webhooks + Zapier + Make + MCP | Web | No (bot) | [pricing](https://circleback.ai/pricing) |
| Otter | Free (300 min); Pro $16.99; Business $30 | Bot joins | Mobile in-person record | Otter Connect API v2 + webhooks | Web/mobile | No (bot) | [pricing](https://otter.ai/pricing) |
| Fathom | Free (5 summaries/mo); Premium $19–39 | Bot | No native cell | API all users + Zapier | Web/desktop | No (bot) | [pricing](https://www.fathom.ai/pricing) |
| tl;dv | Free (10 summaries/mo); Pro $18; Business $59 | Bot | No | No public API | Web | No (bot) | [pricing](https://tldv.io/app/pricing/) |
| Aircall | 3-seat min (~$90/mo floor); Essentials $30/Pro $50 + AI $9 | n/a | VoIP transcription (AI add-on) | API + webhooks | Web/desktop/mobile | n/a | [pricing](https://aircall.io/pricing/) |

## Architecture (least friction)
Point Granola's MCP/Fireflies webhook (Meet) and OpenPhone's transcript webhook (phone) at one ingestion endpoint → drop markdown into the repo → trigger summarize / extract-next-steps / update-pipeline agent.

## Legal
US recording law: one-party consent (federal + most states) vs all-party consent (CA, FL, WA, IL, PA, MA, others). Owner outreach crosses state lines — treat as all-party: verbally disclose recording and get a "yes" at the top of each call. Bot-less capture still records audio, so disclosure obligations are unchanged. (General guidance, not legal advice.)

## Flags / unverifiable
- Granola free-tier history cap reported inconsistently (25 notes vs 30 days); certain that free tier lacks API/MCP export.
- Fireflies MCP V1 flagged for deprecation Apr 30 2026 (V2 successor) — confirm endpoint before building.
- OpenPhone rebranded "Quo" (late 2025); pricing from third-party 2026 breakdown — verify on quo.com.
- Granola MCP appears pull-style; whether it supports server-push webhooks is ambiguous (third-party community MCP servers add HMAC webhook push). For guaranteed push, use OpenPhone (phone) + Fireflies/Circleback (Meet).
