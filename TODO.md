# TODO

Working backlog for the Lunchline Partners case study. Newest at top within each section. Resolved items move to CHANGELOG.

For analytical workstreams (per-candidate work after selection), see `docs/methodology.md` § Sequenced Analytical Workstream. This file tracks **build**, **research**, and **decision** items for the project as a whole.

---

## Decisions blocking other work

- [ ] **Company selection** — four viable candidates (CDLX, NRDY, SCOR, AENT). All landed 2.65-2.95 post-adversarial under calibration mode; framework-discrimination diagnostic (FAST control) confirmed this band reflects pool homogeneity, not framework failure. Findings-mode confirmed the four survivors and ruled out THRY (SEC investigation hidden from calls) and BZFD (Allen 51% control closed 2 days before deadline). Next step: pitch tournament across the four.
- [ ] **FMP API key** — `fetch_fmp.py` works but `/v4/price-target` and competitor-comps endpoints likely require the paid Starter tier ($14/mo). Without it, consensus price target and competitor metrics endpoints will fail. Decide: pay for one month, or skip the sell-side-consensus signal.
- [ ] **Friendly-transaction framework treatment (deferred)** — DOMO/BBGI/ANGI are founder-controlled (DEAL_BREAKER per current logic) BUT have active strategic reviews. That's a founder-led-sale setup, conceptually different from hostile-PE-attack. Decision deferred — we have 4 viable candidates under the standard framework; only revisit if the pitch tournament collapses to <2 survivors.

---

## Selection Process (next major step)

Per `docs/public-company-pitch.md` § Selection Process, the picking methodology is a 2-layer filter + fundamental analysis on every survivor — NO Layer 3 ranking by sector / size / signal density (those would import institutional bias and contradict the case mandate). Aviv's edge fit is a tiebreaker at the END, not a filter.

### Funnel state (as of 2026-05-28)

**Starting universe:** 42 investable candidates from `data/investable_candidates.csv`.

**Layer 1 mechanical exclusion (11 out):** foreign issuers (6), op margin <-100% (5), EV/Rev >3x (a few overlapped). Listed in CHANGELOG.

**Layer 2 structural exclusion — already evaluated (10):**
- Killed: EXFY (VT standstill), KPLT (closed deal), LPSN (closed deal), BBGI (founder 92% Class B), SKLZ (founder 87% Class B), TTGT (post-merger), THRY (SEC subpoena), BZFD (Allen 51% control)
- Viable: CDLX, NRDY

**Layer 2 structural exclusion — still to evaluate (21):** DRCT, CETX, UONE, CISO, IZEA, ZDGE, ACCS, SWAG, SURG, GIFT, SNAL, GAME, MIND, HIT, CNVS, CTM, RSSS, FLNT, UPLD, XBP, BKKT. Build dossier + run voting + deal status checks on each.

**Known viable externals (not in the 42):** SCOR, AENT — slipped through the screen due to industry classification edge cases. Both meet $10-500M EV / US-listed criteria. Include in tournament as documented additions.

### After structural filters, dispatch findings pipeline on every survivor

For each Layer-2 survivor, run `build_findings_prompts(ticker)` — 3 specialists + adversarial. Outputs structured findings (5 bull + 5 bear with anchors, plus 3 most material attacks). NO score. The pitchable-vs-pass decision emerges from the findings.

### Pitch tournament (only AFTER findings on all survivors)

### Pitch agent (new — per candidate)

Once pipeline outputs exist, dispatch a **pitch agent** for each ticker. Its job:
- Read all dossier artifacts (scoring outputs, adversarial review, model output, voting/deal status, peer benchmarks)
- Produce a **concise one-page pitch** for Aviv:
  - 1-sentence thesis (variant perception: "Market sees X. We see Y because Z.")
  - 3 thesis pillars with evidence anchors
  - 1 catalyst with a date
  - 3-year IRR with probability-weighted price target
  - 2 kill criteria (specific, monitorable thresholds)
  - The single strongest counter and its rebuttal
- Tone: institutional, dense, no padding — Pershing/Trian voice (per design system Direction 1)

### Tournament round

For each pitch I receive, I attack:
- Where is the thesis weakest?
- Which kill criterion is most likely to trigger?
- Does the adversarial critique kill the pitch, or did the pitch absorb it?
- How does this pitch compare to the others?

Iterate (refine pitch / attack / surface new issues) until one candidate survives with a defensible thesis.

### Candidates with findings already in hand (not yet bracketed)

Findings produced but tournament not yet held — these go into the bracket alongside any Layer-2 survivors from the 21 unevaluated:
- **CDLX** — Cardlytics, $191M EV. Fingerprint: BofA disclosure 2-quarter delay, $172.5M convert as option-on-restructuring, covenant loosening signal, Sosin (CAS) at 9.4%. Governance clean.
- **NRDY** — Nerdy, $91M EV. Fingerprint: AI cost reset in execution (+1500bps margin) BUT CHGG bear inversion (CHGG ran same playbook while revenue collapsed -48%), Cohn buy = 3% of paper stake, 15-month true runway.
- **SCOR** — comScore, $219M EV (external add). Fingerprint: Goldman retained Aug 2025 (active strategic review); $22.4M capitalized software inflating "FCF," Cerberus standstill (cannot publicly solicit), Q4 net income from non-cash extinguishment gain.
- **AENT** — Alliance Entertainment, $410M EV (external add). Fingerprint: Paramount/MGM exclusive licensing real (movie rev +37%, GM +170bps); sector-misclassification variant fails op-margin test; 75% founder control eliminates activist. Bounded 30-50% upside, NOT 2x.

Ruled out (findings-mode dispositions):
- ~~THRY~~ — SEC investigation into the exact SaaS-conversion narrative mgmt sells, never disclosed on calls. ABL maturity May 2028 collides with print publication end. Unpitchable.
- ~~BZFD~~ — Allen Family Digital closed 51% PIPE 2 days before deadline; circular collateral ($100M PIK note secured by BZFD shares Allen just bought); BF Island narrative absent from 10-K; going-concern. Unpitchable.
- ~~TTGT~~ — Informa merger closed Dec 2024; post-merger controlled entity.
- ~~ANGI~~ — IAC 10-vote Class B, DEAL_BREAKER under standard voting framework.
- ~~EXFY~~ — Voting Trust standstill contractually prohibits solicitation.
- ~~LPSN, KPLT~~ — closed deals (SoundHound, Aaron's+CCF).

### Out of scope for pitch tournament
- Per-candidate full mispricing diagnosis / consensus dossier / operating model — those happen AFTER selection per methodology.md workstream sequence.
- The pitch is a 1-pager, not a deck. Deck build is downstream of selection.

---

## Research items (do before related build)

- [x] **Operator-investor value creation lever framework (DONE — embedded in prompt).** The five lever categories + comp-proven discipline are encoded directly in `lever_findings_prompt`. The "framework + worked exemplars" version we discussed was overkill — the prompt enforces the discipline at use-time. Closed.

- [x] **Mispricing diagnosis framework (DONE — embedded in prompt).** The 9-row checklist with RULE-IN / RULE-OUT / INDETERMINATE classification and per-row evidence anchors is encoded in `mispricing_findings_prompt`. Validated across 8 candidates. Closed.

- [ ] **Consensus baseline dossier framework.** STILL OPEN — needed post-selection. Decide which sell-side data source is realistic without paid feeds (Visible Alpha, FactSet are paid; can scrape sell-side reports from SeekingAlpha or use FMP analyst-estimates endpoint if available on free tier). Output: a dossier template covering Street numbers + peer multiples + retail narrative + earnings Q&A themes.

---

## Build items (ready to start)

### Tooling — generic across companies

- [x] **C: IR-vs-SEC triangulation (DONE via prompt)** — implemented as `ir_sec_triangulation_prompt` in `scripts/agent_prompts.py`, used in both calibration mode and findings mode. Validated on 8 candidates; produced the THRY SEC-investigation finding and CDLX BofA-disclosure-delay finding. Standalone CLI script not needed — the prompt approach is the right abstraction.

- [x] **B: Value creation lever framework (DONE via prompt)** — implemented as `value_creation_prompt` (calibration mode) and `lever_findings_prompt` (findings mode) in `scripts/agent_prompts.py`. Comp-proven discipline enforced (2-3 peer transitions per lever). Standalone script not needed.

- [x] **A: Mispricing diagnosis 9-row checklist (DONE via prompt)** — implemented as `contrarianism_prompt` (calibration mode) and `mispricing_findings_prompt` (findings mode). Validated on all candidates; THRY produced 7/9 rule-ins.

- [ ] **D: `scripts/consensus_dossier.py`** — aggregates Street estimates + peer multiples + retail narrative + earnings Q&A themes. Not yet built; needed POST-selection for the chosen candidate (workstream #2 in methodology.md).

### Tooling — improvements to existing scripts

- [x] **E (DONE): Per-company peer benchmark CSV for `valuation.py`.** Removes hardcoded multiple bands.

- [x] **F (DONE): `check_deal_status.py` acquirer/target weighting.** Fixed THRY false positive — when every definitive_hit co-occurs with an acquirer_signal in the same 8-K, treat as acquirer-mode. Regression-safe.

- [ ] **`analyze_10k.py` enhancement** — make the section extractor handle older (pre-2020) 10-K layouts. Current heuristic is tuned for recent iXBRL filings.

- [ ] **`fetch_fmp.py` graceful free-tier handling** — currently errors when an endpoint requires Starter plan. Add a "tier probe" that reports which endpoints work on the current key.

### Tooling — new

- [ ] **`scripts/comp_transitions_library.py`** — supports methodology #3 (comp-proven levers). Given a proposed lever, search for 3-5 peers who executed it with date / outcome / source. Probably LLM-driven with web search.

- [ ] **`scripts/thesis_monitor.py`** — supports methodology #5 (kill criteria). Generates a thesis-monitor sheet template (metric / threshold / source / next data point) from a 1-paragraph thesis input.

- [ ] **`scripts/compression_test.py`** — supports methodology compression discipline. Takes a draft thesis paragraph, checks it against the five required elements (own / variant perception / catalyst / IRR-MOIC / kill criterion), flags missing ones.

### Deck pipeline

- [ ] **HTML → python-pptx export** — wire mockups/ Direction 1 HTML to a python-pptx renderer that consumes the operating model as source of truth.

---

## Methodology-adjacent open questions

- [ ] **Operating model** — where does it live? `models/<ticker>.xlsx`? Markdown alternative for version control? Need a decision before workstream #3 starts.
- [ ] **Primary research workflow** — methodology #4 says 5-10 calls. Need a system to track outreach + notes per call (Notion? simple `data/primary/<ticker>/calls.md`?).
- [ ] **Peer benchmark refresh policy** — peer_benchmarks.csv files will go stale. Decide: refresh on every run? Manual re-research on a cadence? Mark stale after N days?

---

## How agents should use this file

When you start a session:
1. Read `MEMORY.md` and project memory (auto-loaded).
2. Read this `TODO.md` to see open items.
3. If you complete a build or research item during the session, move it to `CHANGELOG.md` and remove from here.
4. If you discover a new item (research gap, missing tool, decision needed), add it to the appropriate section.
5. **Per-candidate work** (mispricing diagnosis, consensus dossier, operating model for a specific ticker) does not go in this file — see methodology.md workstream sequence and the candidate's own `data/research/<ticker>/` directory.
