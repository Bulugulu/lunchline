"""
Batch-process a list of tickers through the dossier + structural-filter pipeline.

For each ticker: build_dossier -> check_voting_structure -> check_deal_status.
Skips tickers that already have a complete dossier (summary.md + voting_structure.json + deal_status.json).

Writes progress + errors to data/research/layer2_triage_2026-05-28.log.
On completion, writes data/research/layer2_triage_2026-05-28.md with the triage table.

Usage:
    python scripts/batch_triage.py
"""

import json
import subprocess
import sys
import time
from pathlib import Path

ROOT = Path(__file__).parent.parent
DATA = ROOT / "data"
DOSSIERS = DATA / "dossiers"
RESEARCH = DATA / "research"
_args = [a for a in sys.argv[1:] if not a.startswith("-")]
TAG = next((a.split("=", 1)[1] for a in sys.argv[1:] if a.startswith("--tag=")), "2026-05-28")
LOG = RESEARCH / f"layer2_triage_{TAG}.log"
TABLE = RESEARCH / f"layer2_triage_{TAG}.md"

# Full 21-candidate slate. Tickers already with dossiers will be skipped at
# the dossier-build step but still get triage-table rows from existing data.
TICKERS = [
    "DRCT", "CETX", "UONE", "CISO", "IZEA", "ZDGE", "ACCS",
    "SWAG", "SURG", "GIFT", "SNAL", "GAME", "MIND", "HIT",
    "CNVS", "CTM", "RSSS", "FLNT", "UPLD", "XBP", "BKKT",
]

if _args:
    TICKERS = [t.upper() for t in _args]

PY = sys.executable


def log(msg):
    line = f"[{time.strftime('%H:%M:%S')}] {msg}"
    print(line, flush=True)
    with open(LOG, "a", encoding="utf-8") as f:
        f.write(line + "\n")


def has_complete_dossier(ticker):
    d = DOSSIERS / ticker.lower()
    return (
        (d / "summary.md").exists()
        and (d / "voting_structure.json").exists()
        and (d / "deal_status.json").exists()
    )


def run_step(name, cmd, timeout=600):
    log(f"  -> {name}")
    try:
        r = subprocess.run(cmd, capture_output=True, text=True, timeout=timeout)
        if r.returncode != 0:
            log(f"     FAIL rc={r.returncode}: {r.stderr[-500:]}")
            return False
        return True
    except subprocess.TimeoutExpired:
        log(f"     TIMEOUT after {timeout}s")
        return False
    except Exception as e:
        log(f"     EXCEPTION: {e}")
        return False


def process_ticker(ticker):
    log(f"=== {ticker} ===")
    if has_complete_dossier(ticker):
        log(f"  already complete, skipping")
        return True

    d = DOSSIERS / ticker.lower()
    needs_dossier = not (d / "summary.md").exists()
    needs_voting = not (d / "voting_structure.json").exists()
    needs_deal = not (d / "deal_status.json").exists()

    if needs_dossier:
        if not run_step("build_dossier", [PY, "scripts/build_dossier.py", ticker], timeout=900):
            return False
    if needs_voting:
        if not run_step("check_voting_structure", [PY, "scripts/check_voting_structure.py", ticker], timeout=120):
            return False
    if needs_deal:
        if not run_step("check_deal_status", [PY, "scripts/check_deal_status.py", ticker], timeout=120):
            return False
    return True


def read_dossier_facts(ticker):
    """Pull what we need for the triage table from each dossier."""
    d = DOSSIERS / ticker.lower()
    facts = {"ticker": ticker.upper(), "name": "", "ev": "", "sector": "",
             "voting": "", "deal": "", "notes": ""}

    yfi = d / "yfinance_info.json"
    if yfi.exists():
        try:
            info = json.loads(yfi.read_text(encoding="utf-8"))
            facts["name"] = info.get("shortName") or info.get("longName") or ""
            ev = info.get("enterpriseValue")
            facts["ev"] = f"${ev/1e6:.0f}M" if isinstance(ev, (int, float)) and ev else "n/a"
            facts["sector"] = info.get("sector") or ""
        except Exception:
            pass

    vs = d / "voting_structure.json"
    if vs.exists():
        try:
            j = json.loads(vs.read_text(encoding="utf-8"))
            facts["voting"] = j.get("risk_level") or j.get("classification") or ""
        except Exception:
            pass

    ds = d / "deal_status.json"
    if ds.exists():
        try:
            j = json.loads(ds.read_text(encoding="utf-8"))
            facts["deal"] = j.get("status") or j.get("classification") or ""
        except Exception:
            pass

    return facts


def write_table():
    rows = []
    for t in TICKERS:
        f = read_dossier_facts(t)
        verdict = "SURVIVES"
        if f["voting"] == "DEAL_BREAKER":
            verdict = "KILLED"
            f["notes"] = "voting structure deal-breaker"
        elif "closed" in str(f["deal"]).lower() or "completed" in str(f["deal"]).lower():
            verdict = "KILLED"
            f["notes"] = f"deal: {f['deal']}"
        elif not f["name"]:
            verdict = "FAILED"
            f["notes"] = "dossier incomplete"
        rows.append((f, verdict))

    lines = [
        "# Layer-2 Triage — 2026-05-28",
        "",
        "Output of batch_triage.py. Each row reflects dossier + voting + deal-status checks.",
        "",
        "| Ticker | Company | EV | Sector | Voting | Deal status | Verdict | Notes |",
        "|---|---|---|---|---|---|---|---|",
    ]
    for f, v in rows:
        lines.append(
            f"| {f['ticker']} | {f['name']} | {f['ev']} | {f['sector']} | {f['voting']} | {f['deal']} | **{v}** | {f['notes']} |"
        )
    survivors = [f["ticker"] for f, v in rows if v == "SURVIVES"]
    killed = [f["ticker"] for f, v in rows if v == "KILLED"]
    failed = [f["ticker"] for f, v in rows if v == "FAILED"]
    lines += [
        "",
        f"**Survivors ({len(survivors)}):** {', '.join(survivors) or 'none'}",
        f"**Killed ({len(killed)}):** {', '.join(killed) or 'none'}",
        f"**Failed ({len(failed)}):** {', '.join(failed) or 'none'}",
    ]
    TABLE.write_text("\n".join(lines), encoding="utf-8")
    log(f"Triage table written: {TABLE}")


def main():
    RESEARCH.mkdir(parents=True, exist_ok=True)
    LOG.write_text("", encoding="utf-8")
    log(f"Starting batch triage on {len(TICKERS)} tickers")

    ok = []
    fail = []
    for t in TICKERS:
        try:
            if process_ticker(t):
                ok.append(t)
            else:
                fail.append(t)
        except KeyboardInterrupt:
            log("INTERRUPTED")
            break
        except Exception as e:
            log(f"UNCAUGHT EXCEPTION on {t}: {e}")
            fail.append(t)

    log(f"Pipeline done. OK={len(ok)} FAIL={len(fail)}")
    if fail:
        log(f"Failed tickers: {', '.join(fail)}")
    write_table()


if __name__ == "__main__":
    main()
