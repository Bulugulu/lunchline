"""
Build industry-aware agent prompts for the 5-specialist + adversarial +
lightweight-model scoring workflow.

Usage in conversation:
    from scripts.agent_prompts import build_prompts
    prompts = build_prompts("LPSN")
    # prompts is a dict: {messiness, value_creation, data, contrarianism,
    #                     pe_realism, adversarial, model}
    # Each value is a fully-formed prompt string ready to dispatch via Agent tool.

The module reads:
  - data/dossiers/{ticker}/yfinance_info.json (industry classification)
  - data/dossiers/{ticker}/peers/peer_table.json (peer comparables)
  - data/dossiers/{ticker}/peers/private_peers_notes.md (if exists)
  - data/dossiers/{ticker}/voting_structure.json (governance signals)
  - scripts/industry_kpis.json (canonical KPI map)
"""

import json
from pathlib import Path

SCRIPTS_DIR = Path(__file__).parent
DATA_DIR = SCRIPTS_DIR.parent / "data"
DOSSIER_DIR = DATA_DIR / "dossiers"
KPI_MAP_PATH = SCRIPTS_DIR / "industry_kpis.json"


def _load_json(path: Path):
    if path.exists():
        try:
            return json.loads(path.read_text(encoding="utf-8"))
        except Exception:
            return None
    return None


def _read_text(path: Path):
    if path.exists():
        try:
            return path.read_text(encoding="utf-8")
        except Exception:
            return ""
    return ""


def get_industry_kpis(industry: str) -> dict:
    kpi_map = _load_json(KPI_MAP_PATH) or {}
    return kpi_map.get(industry) or kpi_map.get("_default", {})


def _format_peer_table(peers: list, max_peers: int = 10) -> str:
    """Render the peer table as a markdown table for prompt injection."""
    if not peers:
        return "(no peer table available — flag this as a data gap in scoring)"

    rows = []
    rows.append("| Ticker | Name | EV ($M) | Rev TTM ($M) | EV/Rev | Op Margin | Country |")
    rows.append("|--------|------|---------|--------------|--------|-----------|---------|")
    for p in peers[:max_peers]:
        if "error" in p:
            continue
        ev = p.get("enterprise_value") or 0
        rev = p.get("revenue_ttm") or 0
        ev_rev = p.get("ev_to_revenue")
        op_m = p.get("operating_margin")
        rows.append(
            f"| {p.get('ticker','')} | {(p.get('name') or '')[:30]} | "
            f"{ev/1e6:.0f} | {rev/1e6:.0f} | "
            f"{ev_rev:.2f}x | "
            f"{op_m*100:.1f}% | "
            f"{p.get('country','')} |"
            if ev_rev is not None and op_m is not None else
            f"| {p.get('ticker','')} | {(p.get('name') or '')[:30]} | "
            f"{ev/1e6:.0f} | {rev/1e6:.0f} | N/A | N/A | {p.get('country','')} |"
        )
    return "\n".join(rows)


def _format_voting(voting: dict) -> str:
    """Render voting structure findings."""
    if not voting:
        return "(no voting structure check on file — assume single-class until verified)"
    s = voting.get("signals", {})
    lines = [
        f"- Risk level: **{voting.get('risk_level', 'UNKNOWN')}**",
        f"- Share classes: {', '.join(s.get('share_classes_detected', [])) or 'single'}",
        f"- Voting trust: {s.get('voting_trust_mentioned', False)}",
        f"- Controlled company: {s.get('controlled_company_status', False)}",
        f"- Super-voting ratios: {s.get('super_voting_ratios', [])}",
    ]
    concentrations = s.get("voting_power_concentrations", [])
    if concentrations:
        max_v = max(c["pct"] for c in concentrations)
        lines.append(f"- Max voting concentration cited: {max_v}%")
    for r in voting.get("reasoning", []):
        lines.append(f"- {r}")
    return "\n".join(lines)


def _format_kpis(kpi_data: dict) -> str:
    if not kpi_data:
        return "Use generic KPIs: revenue growth, gross margin, op margin, FCF margin, customer count, recurring %."
    kpis = kpi_data.get("kpis", [])
    bench = kpi_data.get("peer_benchmarks", {})
    lines = [f"**Industry category:** {kpi_data.get('category', 'Generic')}"]
    lines.append("**Canonical KPIs to look for in the dossier (extract if disclosed, flag if missing):**")
    for k in kpis:
        lines.append(f"  - {k}")
    if bench:
        lines.append("**Peer benchmarks for calibration:**")
        for k, v in bench.items():
            lines.append(f"  - {k}: {v}")
    return "\n".join(lines)


def _context_block(ticker: str) -> dict:
    """Assemble the shared context that every agent prompt needs."""
    dossier_dir = DOSSIER_DIR / ticker.lower()
    info = _load_json(dossier_dir / "yfinance_info.json") or {}
    industry = info.get("industry", "")
    kpi_data = get_industry_kpis(industry)
    peers = _load_json(dossier_dir / "peers" / "peer_table.json") or []
    private_notes = _read_text(dossier_dir / "peers" / "private_peers_notes.md")
    voting = _load_json(dossier_dir / "voting_structure.json")

    return {
        "ticker": ticker.upper(),
        "name": info.get("shortName") or info.get("longName") or ticker,
        "industry": industry,
        "sector": info.get("sector", ""),
        "country": info.get("country", ""),
        "ev": info.get("enterpriseValue"),
        "mcap": info.get("marketCap"),
        "revenue": info.get("totalRevenue"),
        "fcf": info.get("freeCashflow"),
        "cash": info.get("totalCash"),
        "debt": info.get("totalDebt"),
        "op_margin": info.get("operatingMargins"),
        "ev_to_rev": info.get("enterpriseToRevenue"),
        "analysts": info.get("numberOfAnalystOpinions"),
        "inst_own": info.get("heldPercentInstitutions"),
        "price": info.get("currentPrice"),
        "high52": info.get("fiftyTwoWeekHigh"),
        "dossier_path": str(dossier_dir),
        "industry_kpi_block": _format_kpis(kpi_data),
        "peer_table_block": _format_peer_table(peers),
        "private_peers_notes": private_notes,
        "voting_block": _format_voting(voting),
    }


# ---------------- Prompts ----------------

def _shared_header(ctx: dict) -> str:
    """Front-loaded context every specialist gets."""
    return f"""You are scoring a single dimension of an investment case study for the "Lunchline Partners" search-fund case.

**Candidate company:** {ctx['name']} (ticker: {ctx['ticker']})
- Sector / Industry: {ctx['sector']} / {ctx['industry']}
- Country: {ctx['country']}
- Enterprise Value: ${(ctx['ev'] or 0)/1e6:.0f}M
- Market Cap: ${(ctx['mcap'] or 0)/1e6:.0f}M
- Revenue (TTM): ${(ctx['revenue'] or 0)/1e6:.0f}M
- EV/Revenue: {ctx['ev_to_rev']:.2f}x
- Operating Margin: {(ctx['op_margin'] or 0)*100:.1f}%
- Free Cash Flow: ${(ctx['fcf'] or 0)/1e6:.1f}M
- Cash / Debt: ${(ctx['cash'] or 0)/1e6:.0f}M / ${(ctx['debt'] or 0)/1e6:.0f}M
- Analyst coverage: {ctx['analysts']} analysts
- Institutional ownership: {(ctx['inst_own'] or 0)*100:.1f}%
- 52wk high: ${ctx['high52']:.2f} vs current ${ctx['price']:.2f}

**Dossier location (read-only):** `{ctx['dossier_path']}\\`

## Industry-specific KPIs (use these to anchor your analysis)
{ctx['industry_kpi_block']}

## Peer table (verified from external research, not just the filtered universe)
{ctx['peer_table_block']}

{f"## Private/acquired peer notes{chr(10)}{ctx['private_peers_notes']}" if ctx['private_peers_notes'] else ""}

## Governance / voting structure (early signal — already checked)
{ctx['voting_block']}
"""


def messiness_prompt(ctx: dict) -> str:
    return _shared_header(ctx) + """

## YOUR TASK: Score Situation Complexity / Messiness ONLY (1-5 scale)

### Anchors
- 1 = Clean story, no drama
- 3 = One clear issue (e.g., margin pressure)
- 5 = 2-3 overlapping issues creating analytical richness

Qualifying messiness categories (per framework, ranked by analytical richness):
- Active strategic alternatives / M&A process
- Management transition / CEO turnover
- Revenue model transition
- Margin compression with identifiable cause
- Accounting restatement / auditor change
- Activist involvement / proxy fight
- Segment divestiture / asset stranding
- Debt overhang with viable core business
- Failed M&A / broken deal
- Customer concentration + loss

### Primary evidence files (read these)
- `edgar/filings/*_10-K_*.htm` — latest 10-K Risk Factors + MD&A
- `edgar/filings/*_8-K_*.htm` — all recent 8-Ks (material events)
- `edgar/filings/*_DEF_14A_*.htm` — latest proxy (board/comp changes)
- `transcripts/*.txt` — recent earnings calls (mgmt tone, transitions)
- `news.json` — recent narrative

### Output format
```
SCORE: <1-5>
CONFIDENCE: <low|medium|high>

EVIDENCE (min 3, cite file path + exact quote):
1. ...
2. ...
3. ...

MESSINESS CATEGORIES PRESENT (from framework list):
- <category>: <specific evidence>

WHAT WOULD MAKE THIS A HIGHER SCORE: <1-2 sentences>

CALIBRATION CHECK:
- Defensible against "this is just a struggling company"? <yes/no + reason>
- Avoided conflating "stock is down" with "situation is messy"? <yes/no>
```

Critical: ground every claim in a specific document/quote. A defensible 3/5 beats an inflated 5/5.
"""


def value_creation_prompt(ctx: dict) -> str:
    return _shared_header(ctx) + """

## YOUR TASK: Score Credible Value Creation Angle ONLY (1-5 scale)

### Anchors
- 1 = No obvious levers
- 3 = Generic cost cuts possible
- 5 = Specific, named operational + commercial + capital structure levers executable in 2-3 years, EACH backed by 2-3 comparable transitions

A 5/5 requires NAMED, SPECIFIC, QUANTIFIED levers AND a "comp-proven" track record per lever.
Generic "cut costs" or "grow revenue" is 2-3, not 5.

### Comp-proven levers (per methodology lesson #3 — non-negotiable)

Every lever scoring >=4 must cite 2-3 PRIOR COMPARABLE TRANSITIONS where another company
(peer, PE-owned, or industry transformation) executed the same playbook with quantified outcome.

The activist canon's discipline: every Trian margin claim cites a peer at that margin. Every
PSC value-creation lever cites a comparable transition that already executed. "Improve margins
200bps" is amateur; "Peer X executed this exact playbook in 18 months and hit 28% margin" is
institutional.

Use the peer table above as the FIRST place to look for comparable transitions. Augment with
sector knowledge (PE take-privates, activist campaigns, industry transformations you can name).

### Industry-specific cost/efficiency lens
Use the canonical KPIs above to identify where this company is OUT OF LINE with peers.
For example, if industry benchmark is "G&A < 15% of revenue" and this company is at 30%,
that's a quantified lever — BUT you still need to cite a comp that actually moved from 30% → 15%.

### Primary evidence files
- `edgar/filings/*_10-K_*.htm` — latest 10-K MD&A (Item 7), Item 1 business segments
- `transcripts/*.txt` — mgmt commentary on initiatives, capital allocation, named programs
- `edgar/xbrl_summary.csv` — financial trends
- `peers/peer_table.json` — for benchmarking cost structure
- `yfinance_info.json` — current snapshot

### Output format
```
SCORE: <1-5>
CONFIDENCE: <low|medium|high>

NAMED LEVERS (min 3 to score >=4; each must include comp-proven precedent):

1. Operational: <specific lever>
   - Quantified impact: <$ or % delta with math>
   - Source: <file path + exact quote>
   - Peer benchmark: <X% vs this co's Y%>
   - **Comparable transitions** (min 2):
     a. <Peer co, situation, outcome, time, source>
     b. <Peer co, situation, outcome, time, source>

2. Commercial: <specific lever>
   - ... [same structure]

3. Capital structure: <specific lever>
   - ... [same structure]

(add more if warranted; min 3 to score >=4)

PUSHBACK PRE-EMPTED:
- <strongest critique of each lever + counter or acknowledgment, citing comp-proven precedent>

CALIBRATION CHECK:
- Each lever named, quantified, AND backed by 2-3 comparable transitions? <yes/no per lever>
- Could you defend each lever AND its precedent in a Lunchline interview? <yes/no + weakest>
- Levers credible *given the current situation* (e.g., voting-trust company can't execute take-private)? <yes/no>
- Have you avoided "theoretical lever" language — only included levers where a comp actually executed? <yes/no>
```

Critical: levers without comp-proven precedent CAN appear but should be flagged as "theoretical
(no precedent identified)" and cannot count toward a 4+ score. A defensible 3/5 with 3 well-evidenced
levers beats an inflated 5/5 with 5 theoretical ones.

If governance check flagged DEAL_BREAKER, factor that into executability — but do NOT double-count
vs PE Realism score.
"""


def data_availability_prompt(ctx: dict) -> str:
    return _shared_header(ctx) + """

## YOUR TASK: Score Data Availability / Modelability ONLY (1-5 scale)

### Anchors
- 1 = Minimal public filings, no transcripts
- 3 = Standard 10-K/10-Q available
- 5 = Rich SEC filings + transcripts + segment data + insider data + peer comps

Framework data requirements:
- 3+ 10-Ks (5+ ideal), 8+ 10-Qs (12+ ideal)
- Earnings transcripts (most recent quarter min; 8+ ideal)
- Segment reporting (revenue minimum; revenue+margin ideal)
- 3+ public comps (5+ ideal)
- DEF 14A on file, Form 4 insider data

### Primary inputs
- `summary.md` — start here for the file inventory
- `edgar/filings_index.json` — filing counts by type
- `edgar/filings/*_10-K_*.htm` — check for segment reporting
- `transcripts/index.json` — transcript count + quarters
- `peers/peer_table.json` — PUBLIC peer count (penalize if direct competitors are private)
- `peers/private_peers_notes.md` — note if direct comps are private (real data gap)
- `analyst.json` — depth of analyst data

### Output format
```
SCORE: <1-5>
CONFIDENCE: <low|medium|high>

COVERAGE MAP:
- 10-K: <count> covering <range>
- 10-Q: <count> covering <quarters>
- 8-K: <count>
- DEF 14A: <count>
- Form 4: <count>
- Earnings transcripts: <count> covering <quarters>
- XBRL financials: <y/n>
- Segment reporting: <details>
- Public comps available: <list public + note private gaps>
- Analyst events: <count>

GAPS / LIMITATIONS:
- <specific data that's missing and would matter>

CALIBRATION CHECK:
- Enough for a 3-year quarterly model? <yes/no + reasoning>
- Enough public peers for meaningful relative valuation? <yes/no + reasoning>
- Could build a 10-12 page deck from this dossier alone? <yes/no>
```
"""


def contrarianism_prompt(ctx: dict) -> str:
    return _shared_header(ctx) + """

## YOUR TASK: Score Thesis Contrarianism ONLY (1-5 scale)

### Anchors
- 1 = Consensus agrees it's cheap (already priced in)
- 3 = Some bears, you disagree on one point
- 5 = Market consensus strongly negative; thesis requires seeing something the market demonstrably misunderstands, AND a structural reason the mispricing PERSISTS

A 5/5 requires (a) consensus EXISTS and is negative, (b) a SPECIFIC variant perception with
evidence, AND (c) a structural diagnosis of why the mispricing isn't already arbitraged away.

### Critical trap to avoid
"Ignored" ≠ "contrarian." A company with 1 analyst and 0 Seeking Alpha articles is
NOT contrarian — it's neglected. True contrarianism requires consensus + specific
counter-thesis + structural reason for persistence.

### Mispricing diagnosis (per methodology lesson #6 — REQUIRED OUTPUT)

Top decks don't say "it's cheap." They say "it's cheap because <structural reason>." The
structural reason IS the variant perception — it's what makes the trade contrarian rather
than crowded.

You must rule IN or OUT each of the 9 reasons below with specific evidence from the dossier:

| # | Reason mispricing could persist | Evidence source |
|---|---|---|
| 1 | Zero/thin sell-side coverage | analyst.json — # analysts, last initiation date |
| 2 | Lock-up / SPAC overhang | recent S-1/424, secondary offering 8-Ks, lock-up expiry |
| 3 | Sector misclassification | yfinance industry vs actual business per 10-K |
| 4 | Segment opacity | does company report by segment? Are drivers in "Other"? |
| 5 | Recent disappointment / fallen angel | % off ATH, % off 52wk high, what triggered drop |
| 6 | Retail exit (broken IPO/SPAC) | IPO/de-SPAC price vs current, retail holder % |
| 7 | Too-small-for-institutions | float size, daily $ volume vs $100M+ fund needs |
| 8 | Accounting opacity / restatement | recent restatements, auditor changes, material weakness |
| 9 | Activism vacuum | insider ownership %, blocking stake potential |

### Primary evidence
- `analyst.json` — consensus rating, PT distribution vs current, upgrade/downgrade history
- `transcripts/*.txt` — Q&A sections (what analysts are worried about)
- `news.json` — narrative tone
- `seeking_alpha.json` — retail narrative density
- `edgar/filings/*_10-K_*.htm` — Risk Factors (what management itself says is risky vs market)
- `edgar/filings/*_8-K_*.htm` — SPAC overhang, auditor changes, restatement signals
- `peers/peer_table.json` — is the multiple actually discounted vs peers, or are peers all cheap?
- `yfinance_info.json` — float, daily volume, institutional ownership

### Output format
```
SCORE: <1-5>
CONFIDENCE: <low|medium|high>

CONSENSUS STATE:
- Sell-side: <consensus + PT vs current + analyst count>
- Rating actions last 12mo: <summary>
- SA / retail narrative: <density + tone>
- Recent news tone: <bullish/mixed/bearish + examples>
- Peer multiple context: <discount to peers or in line?>

MISPRICING DIAGNOSIS (9-row checklist — rule in/out each with evidence):
| # | Reason | Applies? | Evidence |
|---|--------|----------|----------|
| 1 | Zero/thin sell-side coverage | <Y/N> | <specific> |
| 2 | Lock-up / SPAC overhang | <Y/N> | <specific> |
| 3 | Sector misclassification | <Y/N> | <specific> |
| 4 | Segment opacity | <Y/N> | <specific> |
| 5 | Fallen angel / recent disappointment | <Y/N> | <specific> |
| 6 | Retail exit (broken IPO/SPAC) | <Y/N> | <specific> |
| 7 | Too-small-for-institutions | <Y/N> | <specific> |
| 8 | Accounting opacity / restatement | <Y/N> | <specific> |
| 9 | Activism vacuum | <Y/N> | <specific> |

DOMINANT REASON(S) THE MISPRICING PERSISTS: <name 1-2 most material from above>

WHAT THE MARKET IS WORRIED ABOUT (cited from transcript Q&A or risk factors):
1. ...
2. ...
3. ...

CONTRARIAN VARIANT PERCEPTION (if any):
- Market believes: <X>
- Contrarian could argue: <Y> because <evidence Z>
- Why mispricing persists (linking to checklist above): <structural reason>
- Strength: <weak/moderate/strong>

CALIBRATION CHECK:
- Consensus actually negative, or just ignored? <distinguish>
- Variant perception SPECIFIC + EVIDENCE-BACKED, or just "cheap"? <yes/no>
- Is there at least ONE structural reason for persistence rule-in above? <yes/no>
- Could you defend the variant under hostile Q&A? <yes/no>
```

If the mispricing-diagnosis table has ZERO rules-in, the score CANNOT exceed 2 — there's no
structural reason for the alleged mispricing to persist, so consensus is probably right.
"""


def pe_realism_prompt(ctx: dict) -> str:
    voting_section = ctx['voting_block']
    return _shared_header(ctx) + f"""

## YOUR TASK: Score PE/Search Fund Realism ONLY (1-5 scale)

### Anchors
- 1 = No PE buyer would touch this (wrong industry, wrong structure)
- 3 = Conceivable take-private
- 5 = Exactly the type of business a search fund or PE sponsor would acquire

### Ideal search-fund acquisition profile (per Lunchline philosophy)
- B2B services / B2B SaaS
- Recurring revenue
- Fragmented market
- Operational upside
- Stable / predictable cash flows
- Sub-scale to sponsor portfolio
- Manageable mgmt transition

### Disqualifiers (CRITICAL — check upstream voting structure)
- Founder voting control that blocks take-private (DEAL_BREAKER)
- Network-effect consumer plays needing scale
- Hard-tech requiring deep capex
- Heavily regulated industries without sponsor playbook
- Existing PE ownership at higher entry price

### IMPORTANT — voting structure pre-check (already verified):
{voting_section}

If risk_level is **DEAL_BREAKER** above, this score CANNOT exceed 2. The business itself
may be ideal but the corporate structure makes a sponsor-led transaction impossible.

### Primary evidence
- `edgar/filings/*_10-K_*.htm` — Item 1 business description, customer concentration, competition
- `edgar/filings/*_DEF_14A_*.htm` — voting structure verification, insider ownership, mgmt
- `transcripts/*.txt` — mgmt commentary on recurring rev, NRR, customer profile
- `peers/peer_table.json` + private notes — exit comparables (e.g., recent take-privates)
- `voting_structure.json` — already-checked governance signals

### Output format
```
SCORE: <1-5>
CONFIDENCE: <low|medium|high>

PE/SEARCH FUND FIT:
Revenue model: <SaaS / transaction / hybrid + recurring %>
Customer profile: <SMB / mid / enterprise mix + count + concentration>
Voting / capital structure: <verify from proxy — DO NOT assume>
- Implication for take-private feasibility: <high/medium/low + why>
Market structure: <fragmented / concentrated + named competitors + EXFY's positioning>
Sponsor fit:
- Search fund ($5-50M EV): <fits/too big/too small>
- LMM PE ($50-500M EV): <fits/too small/right>
- Most likely buyer type: <search fund / LMM PE / strategic / unlikely>

DEAL-BREAKERS / YELLOW FLAGS:
- <specific risk + evidence>

CALIBRATION CHECK:
- Sponsor could actually execute in 12-24 months? <yes/no + gating factor>
- Operational upside real (named) or hypothetical? <which>
- Founder voting structure verified from proxy? <yes/no>
```
"""


def adversarial_prompt(ctx: dict, specialist_summaries: str) -> str:
    return _shared_header(ctx) + f"""

## ADVERSARIAL REVIEWER

Five specialist agents have scored {ctx['ticker']}. Your job: argue every score is
0.5-1.0 TOO HIGH using REAL investment logic. This is the Lunchline interview in
dress rehearsal.

### Investment-logic frames (pick 4-6 strongest, develop with evidence)

1. **Business durability** — Is the unit-economic engine intact or hollowing out?
2. **Competitive moat erosion** — Quantify gap to peers from peer table + private notes.
3. **Management quality / capital allocation** — Look at actual capital allocation actions.
4. **Catalyst skepticism** — Has the bull catalyst slipped or been redefined?
5. **Multiple compression risk** — At current price, what stops it going lower?
6. **Accounting / quality of earnings** — SBC adds, working capital timing, non-GAAP gap.
7. **Customer concentration / retention reality** — Compare retention rates to peers.
8. **Catalyst inversion** — Could the bull case actually be a bear catalyst?
9. **Governance / sponsor blockers** — Already flagged upstream; argue impact on other scores.

### Specialist outputs to attack
{specialist_summaries}

### Required output
```
HEADLINE BEAR THESIS: <1 sentence — what kills this trade>

RANKED CRITIQUES (most potent first):
1. [Frame] <critique title>
   Case: <2-3 sentences>
   Evidence: <file path + quote>
   Quantification: <math/peer comparison>
   Score impact: <which specialist score should drop, by how much, why>
   Strength: <devastating | strong | moderate | weak>
(4-6 critiques)

SCORE-CHANGE RECOMMENDATIONS:
- Messiness: <old> → <new> because <reason>
- Value Creation: ...
- Data: ...
- Contrarianism: ...
- PE Realism: ...

BEAR CASE DOLLAR VIEW:
- Reasonable downside price: $X in <timeframe>
- Math: <FCF assumption × multiple → EV → equity → price>

WHAT WOULD CHANGE YOUR MIND: <1-2 sentences>
```

Critical: every critique must cite a specific dossier file + quote. If a specialist
score is well-supported and you can't break it, SAY SO. Weak critiques you label
"weak" are more valuable than inflated "devastating" ones.

Use the peer table above for benchmarking — that's the strongest source for moat/quality critiques.
"""


def ir_sec_triangulation_prompt(ctx: dict) -> str:
    return _shared_header(ctx) + """

## YOUR TASK: IR-vs-SEC Triangulation (no numeric score — produce a gap report)

Per the methodology's "Structural Discipline" section: compare management's IR
language (earnings call transcripts, press releases) to what the company actually
discloses in SEC filings. Find specific claim-vs-filing gaps.

This is identified as the **highest-leverage AI use case** in the entire workflow.
LLMs are very good at this triangulation; humans are slow at it. Gaps often surface
material risks (claim: "diversified customer base"; filing: "top 3 customers = 65%
of revenue") that become thesis pillars or risk-section ammunition.

### Output

This specialist does NOT produce a 1-5 score. It produces a GAP REPORT consumed by
the adversarial and aggregator steps. The report should be evidence-dense and concise.

### Methodology

1. Read the LATEST 4 earnings call transcripts (or as many as available, max 4)
2. Read the LATEST 10-K (Risk Factors + MD&A + Business + Customer Concentration sections)
3. Optionally skim 8-Ks from the same period for material event language
4. Identify SPECIFIC CLAIM-VS-FILING GAPS — places where management framing diverges
   from the filed disclosure. Examples of what counts:
   - Customer concentration ("diversified" claim vs. concentrated 10-K disclosure)
   - Recurring revenue ("subscription business" claim vs. month-to-month contracts in 10-K)
   - Margin trajectory ("expanding" claim vs. compressing in MD&A)
   - Growth driver ("AI-driven" claim vs. legacy product still 70% of revenue)
   - Customer retention ("high NRR" claim vs. logo retention in the 80s in 10-K)
   - Risk profile ("strong balance sheet" claim vs. going-concern language in Risk Factors)
   - Industry positioning ("market leader" claim vs. "we compete with X" admission)
   - Capital allocation ("returning capital" claim vs. cash burning in cash flow statement)

### Primary evidence files
- `transcripts/*.txt` — sort by quarter, read most recent 4
- `edgar/filings/*_10-K_*.htm` — latest 10-K (Item 1A Risk Factors, Item 7 MD&A, Item 1 Business)
- `edgar/filings/*_8-K_*.htm` — recent 8-Ks for press-release-language vs. filing-language
- `news.json` — IR press release headlines

### Required output format
```
TRIANGULATION REPORT — {ctx['ticker']}

GAPS IDENTIFIED (min 3 if any exist; cite both sides verbatim):

1. <Topic — e.g., "Customer concentration">
   Management says (transcript file path + exact quote): "..."
   10-K says (file path + exact quote from Item 1A or MD&A): "..."
   Gap analysis: <what the divergence reveals>
   Severity: <minor | meaningful | thesis-breaking>

2. <Topic>
   Management says: "..."
   10-K says: "..."
   Gap analysis: ...
   Severity: ...

(add more as warranted; aim for 3-6 with the strongest gaps first)

LANGUAGE ALIGNED (areas where IR language IS supported by filings):
- <1-2 examples where mgmt claims hold up under filing review — important for fairness>

THEMES:
- <1-2 sentences on the pattern. Is mgmt systematically over-selling? Aligned but
  with one blind spot? Filing-cautious / IR-aggressive? This is the meta-finding.>

IMPLICATIONS:
- For value creation thesis: <what gaps mean for executability>
- For risk section: <which gaps belong in the deck's risk table>
- For variant perception: <do any gaps support a "market is missing X" thesis?>

CONFIDENCE: <low | medium | high>
```

If you find NO material gaps after reading 4 transcripts + 10-K, report that
honestly — that itself is a signal (clean management, or alignment by coincidence
of low transparency).
"""


def model_prompt(ctx: dict, scoring_summary: str) -> str:
    return _shared_header(ctx) + f"""

## LIGHTWEIGHT VALUATION AGENT — uses scripts/valuation.py

Your task: produce a per-company valuation view that turns the qualitative scoring
into a dollar return view. The project has a sophisticated 7-method valuation engine
at `scripts/valuation.py` — DO NOT reinvent a model. Your job is to:

1. Run `python scripts/valuation.py {ctx['ticker']}` and capture the output
2. Verify the peer benchmarks CSV at `data/research/{ctx['ticker'].lower()}/peer_benchmarks.csv` exists and is populated; if missing, fill it from `data/dossiers/{ctx['ticker'].lower()}/peers/peer_table.json` first
3. Interpret the football-field output + sensitivity in the context of the scoring summary
4. Produce a markdown writeup with the model output and verdict

### Scoring summary (from specialist + adversarial review)
{scoring_summary}

### Required outputs (markdown writeup)

**Valuation engine output (paste the football-field + sensitivity tables from valuation.py)**

**Method-by-method commentary:**
- Which methods apply, which don't (e.g., EV/EBITDA invalid if EBITDA negative)
- Where the football field is widest (which method is the swing variable)
- Anchor your interpretation in the peer benchmarks CSV — the multiples in that file
  are the comp-proven anchors, not theoretical bands

**Scenario translation:**
- Bear case price: derived from valuation.py low / 10th-percentile output
- Base case price: derived from valuation.py median / 50th-percentile output
- Bull case price: derived from valuation.py high / 90th-percentile output
- For each: which underlying assumption changes (revenue, margin, exit multiple)?

**Returns:**
- 3-year IRR per scenario from current ${ctx['price']:.2f}
- Probability weighting (your judgment given the scoring summary above)
- **Expected value price target:** $<weighted>
- **Expected IRR:** <%>
- Does this clear the 20-25% PE/search-fund hurdle?

**Kill criteria (per methodology lesson #5):**
- Pillar 1: <metric / threshold / data source / next data point>
- Pillar 2: <metric / threshold / data source / next data point>
- Risk 1: <metric / threshold / data source / next data point>
- Risk 2: <metric / threshold / data source / next data point>
Each entry must be DATED + MONITORABLE + SOURCED. Not narrative.

**Sanity checks:**
- Does the implied multiple in your bull case appear in the peer table? If not, flag.
- Does the implied FCF in your base case account for capitalized software / SBC dilution?
- Net cash position: ${(ctx['cash'] or 0)/1e6:.0f}M - ${(ctx['debt'] or 0)/1e6:.0f}M = ${((ctx['cash'] or 0)-(ctx['debt'] or 0))/1e6:.0f}M — does the model treat cash correctly in exit valuation?

**Verdict:**
- Risk-adjusted return relative to the framework score
- Key assumption that, if wrong, breaks the thesis
- Comparison vs. the framework score (does the IRR view agree or diverge?)

### Critical: if valuation.py fails or peer benchmarks CSV is missing
- First check `data/research/{ctx['ticker'].lower()}/peer_benchmarks.csv` exists
- If not, generate it from `data/dossiers/{ctx['ticker'].lower()}/peers/peer_table.json` using the CSV columns: peer_ticker, peer_name, inclusion (subject/primary/secondary), ev_ebitda, ev_revenue, ev_gross_profit, ev_fcf, revenue_growth_pct, gross_margin, ebitda_margin, fcf_margin, as_of_date, source, notes
- Then retry valuation.py
- If valuation.py still errors, fall back to back-of-envelope math but FLAG IT in the verdict
"""


def build_prompts(ticker: str, specialist_summaries: str = "", scoring_summary: str = "") -> dict:
    """Build all 8 agent prompts for a candidate ticker.

    Args:
        ticker: e.g. "LPSN"
        specialist_summaries: paste the 6 specialist outputs here for adversarial prompt
        scoring_summary: paste the scoring synthesis for the model prompt

    Specialists (6 in parallel):
        messiness, value_creation, data_availability, contrarianism, pe_realism,
        ir_sec_triangulation (gap report, no numeric score)
    Then sequential:
        adversarial (sees all 6 specialist outputs)
        model (uses scripts/valuation.py)
    """
    ctx = _context_block(ticker)
    return {
        "messiness": messiness_prompt(ctx),
        "value_creation": value_creation_prompt(ctx),
        "data_availability": data_availability_prompt(ctx),
        "contrarianism": contrarianism_prompt(ctx),
        "pe_realism": pe_realism_prompt(ctx),
        "ir_sec_triangulation": ir_sec_triangulation_prompt(ctx),
        "adversarial": adversarial_prompt(ctx, specialist_summaries),
        "model": model_prompt(ctx, scoring_summary),
        "_context": ctx,
    }


def main():
    import argparse
    p = argparse.ArgumentParser(description="Render scoring agent prompts for a ticker (preview).")
    p.add_argument("ticker")
    p.add_argument("--show", choices=["messiness", "value_creation", "data_availability",
                                       "contrarianism", "pe_realism", "ir_sec_triangulation",
                                       "adversarial", "model", "all"],
                   default="all")
    args = p.parse_args()
    prompts = build_prompts(args.ticker)
    if args.show == "all":
        for k, v in prompts.items():
            if k.startswith("_"):
                continue
            print(f"\n{'='*70}\n## {k.upper()}\n{'='*70}")
            print(v[:2000])
            print("..." if len(v) > 2000 else "")
    else:
        print(prompts[args.show])


if __name__ == "__main__":
    main()
