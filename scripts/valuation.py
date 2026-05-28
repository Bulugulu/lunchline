"""
Per-company equity valuation with football-field chart + sensitivity matrix.

Seven methods (EV/EBITDA, EV/FCF, EV/Gross Profit, Rule of 40 EV/Rev, peer comp,
10-yr DCF, Path-to-Profitability DCF) with smart routing based on EBITDA sign.

# Bespoke benchmarks per company — no hardcoded multiples

Multiple-based methods (EV/EBITDA, EV/FCF, EV/GP, EV/Rev) require peer multiples
from `data/research/<ticker>/peer_benchmarks.csv`. When the file is missing or
empty, the script writes an empty schema template, prints research instructions,
and exits. This is the methodology #3 discipline ("comp-proven, not theoretical").

The CSV columns:
  peer_ticker, peer_name, inclusion, ev_ebitda, ev_revenue, ev_gross_profit,
  ev_fcf, revenue_growth_pct, gross_margin, ebitda_margin, fcf_margin,
  as_of_date, source, notes

  inclusion = "subject" | "primary" | "secondary" | "excluded"
  - subject:   the candidate itself (anchor row, for the agent's reference)
  - primary:   tight comparables — used for target/low/high computation first
  - secondary: directional comparables — used if <3 primary peers
  - excluded:  documented as considered-and-rejected with reason in notes

When an agent researches peers during a session, they should write findings to
this CSV so future runs read them instead of re-doing research. See CLAUDE.md.

Usage:
    # Auto-routed methods, peer-derived multiples
    python scripts/valuation.py EXFY

    # Write empty peer schema and exit (do this first if researching peers)
    python scripts/valuation.py EXFY --init-peers

    # CLI overrides for one-off use without peer file
    python scripts/valuation.py EXFY --target-multiple 8 --fcf-target-multiple 15

    # Use FMP comps as additional peer source
    python scripts/valuation.py EXFY --use-comps
"""

import argparse
import json
from dataclasses import dataclass, field, asdict
from pathlib import Path

import numpy as np
import pandas as pd
import yfinance as yf

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

DATA_DIR = Path(__file__).parent.parent / "data"
VAL_DIR = DATA_DIR / "valuation"
FMP_DIR = DATA_DIR / "fmp"
RESEARCH_DIR = DATA_DIR / "research"

PEER_CSV_COLUMNS = [
    "peer_ticker", "peer_name", "inclusion",
    "ev_ebitda", "ev_revenue", "ev_gross_profit", "ev_fcf",
    "revenue_growth_pct", "gross_margin", "ebitda_margin", "fcf_margin",
    "as_of_date", "source", "notes",
]

# Map our internal method metric → column name in peer_benchmarks.csv
METRIC_TO_PEER_COL = {
    "ev_ebitda": "ev_ebitda",
    "ev_fcf": "ev_fcf",
    "ev_gp": "ev_gross_profit",
    "ev_revenue": "ev_revenue",
}


def peer_csv_path(ticker: str) -> Path:
    return RESEARCH_DIR / ticker.lower() / "peer_benchmarks.csv"


def load_peer_benchmarks(ticker: str) -> pd.DataFrame | None:
    """Load peer_benchmarks.csv for a ticker. Returns None if missing/empty."""
    path = peer_csv_path(ticker)
    if not path.exists():
        return None
    try:
        df = pd.read_csv(path)
    except pd.errors.EmptyDataError:
        return None
    if df.empty or "inclusion" not in df.columns:
        return None
    return df


def compute_peer_bands(peers_df: pd.DataFrame, metric_col: str,
                        min_peers: int = 3) -> dict | None:
    """Compute target/low/high multiples from a peer benchmark column.
    Walks tiers (primary -> primary+secondary) until min_peers reached.
    Returns None if insufficient data."""
    if metric_col not in peers_df.columns:
        return None

    def collect(inclusion_set):
        sub = peers_df[peers_df["inclusion"].isin(inclusion_set)]
        vals = pd.to_numeric(sub[metric_col], errors="coerce").dropna()
        vals = vals[vals > 0]
        return sub, vals

    sub, vals = collect({"primary"})
    tier_used = "primary"
    if len(vals) < min_peers:
        sub, vals = collect({"primary", "secondary"})
        tier_used = "primary+secondary"
    if len(vals) < 2:
        return None

    peer_list = sub.loc[vals.index, "peer_ticker"].tolist()
    return {
        "target": round(float(vals.median()), 2),
        "low": round(float(vals.min()), 2),
        "high": round(float(vals.max()), 2),
        "n_peers": int(len(vals)),
        "tier_used": tier_used,
        "peer_tickers": peer_list,
    }


def write_peer_template(ticker: str, basics: dict) -> Path:
    """Write an empty peer_benchmarks.csv at the expected path with a header
    row, a worked-example comment row, and the subject anchor row pre-populated
    from yfinance."""
    path = peer_csv_path(ticker)
    path.parent.mkdir(parents=True, exist_ok=True)

    def pct(x):
        return round(x, 4) if x is not None else ""

    # Compute subject's own multiples from live data so the agent has anchors
    ev = basics.get("enterprise_value")
    ebitda = basics.get("ebitda")
    revenue = basics.get("revenue")
    gp = basics.get("gross_profit")
    fcf = basics.get("fcf")

    def safe_div(a, b):
        if a and b and b > 0:
            return round(a / b, 2)
        return ""

    subject_row = {
        "peer_ticker": ticker.upper(),
        "peer_name": basics.get("name", ""),
        "inclusion": "subject",
        "ev_ebitda": safe_div(ev, ebitda) if ebitda and ebitda > 0 else "",
        "ev_revenue": safe_div(ev, revenue),
        "ev_gross_profit": safe_div(ev, gp) if gp and gp > 0 else "",
        "ev_fcf": safe_div(ev, fcf) if fcf and fcf > 0 else "",
        "revenue_growth_pct": pct(basics.get("revenue_growth")),
        "gross_margin": pct(gp / revenue) if gp and revenue else "",
        "ebitda_margin": pct(ebitda / revenue) if ebitda and revenue else "",
        "fcf_margin": pct(fcf / revenue) if fcf and revenue else "",
        "as_of_date": pd.Timestamp.now().strftime("%Y-%m-%d"),
        "source": "yfinance (auto)",
        "notes": "Subject company anchor row — do not modify. Add peers below.",
    }

    df = pd.DataFrame([subject_row], columns=PEER_CSV_COLUMNS)
    df.to_csv(path, index=False)
    return path


def print_research_instructions(ticker: str, path: Path):
    """Print a self-contained brief telling the agent what to research and how
    to fill in the CSV."""
    print(f"""
====================================================================
PEER BENCHMARK RESEARCH REQUIRED for {ticker.upper()}
====================================================================
No peer multiples found. An empty schema template has been written to:

  {path}

The subject's own multiples are populated as the anchor row.

To unlock peer-derived target/low/high multiples, an agent (Aviv or
Claude) needs to:

  1. Identify 3-7 public peer companies. Criteria:
     - Similar business model (recurring revenue / transactional / hybrid)
     - Similar growth profile (within ~10pts of subject revenue growth)
     - Similar size (within 5-10x EV)
     - Same sector/sub-vertical OR explicit cross-vertical comp (note the rationale)
     Tag the 3-5 closest as inclusion="primary"; looser comps as "secondary".
     Document considered-and-rejected peers as inclusion="excluded" with reason
     in the notes column.

  2. For each peer, pull current multiples:
     - ev_ebitda, ev_revenue, ev_gross_profit, ev_fcf
     - revenue_growth_pct, gross_margin, ebitda_margin, fcf_margin
     - Sources: yfinance .info ('enterpriseToEbitda', 'enterpriseToRevenue'),
       fetch_fmp.py, or sell-side reports. Leave blank where N/A.

  3. Optionally write peer-selection rationale to:
     data/research/{ticker.lower()}/peer_notes.md
     This is where the "comp-proven levers" methodology #3 discipline lives.

  4. Re-run: python scripts/valuation.py {ticker.upper()}

To bypass the peer file for a one-off run, pass explicit multiples:
  python scripts/valuation.py {ticker.upper()} \\
      --target-multiple X.X --fcf-target-multiple Y.Y \\
      --gp-target-multiple Z.Z --ev-rev-target-multiple W.W
====================================================================
""")



@dataclass
class ValuationResult:
    method: str
    target_price: float
    low_estimate: float
    high_estimate: float
    assumptions: dict = field(default_factory=dict)
    confidence: float = 0.5
    description: str = ""


# ---------- Data pull ----------

def pull_basics(ticker: str) -> dict:
    """Pull current price, shares out, net debt, EBITDA, revenue, FCF, gross
    profit, and revenue growth from yfinance."""
    t = yf.Ticker(ticker)
    info = t.info
    inc = t.income_stmt
    bs = t.balance_sheet
    cf = t.cashflow

    def latest(df, name, col=0):
        if df is None or df.empty or name not in df.index:
            return None
        if col >= len(df.columns):
            return None
        val = df.loc[name].iloc[col]
        return float(val) if pd.notna(val) else None

    ebitda = latest(inc, "EBITDA") or latest(inc, "Normalized EBITDA")
    revenue = latest(inc, "Total Revenue") or latest(inc, "Operating Revenue")
    prior_revenue = latest(inc, "Total Revenue", col=1) or latest(inc, "Operating Revenue", col=1)
    gross_profit = latest(inc, "Gross Profit")
    if gross_profit is None and revenue and latest(inc, "Cost Of Revenue"):
        gross_profit = revenue - latest(inc, "Cost Of Revenue")

    ocf = latest(cf, "Operating Cash Flow") or latest(cf, "Cash Flow From Continuing Operating Activities")
    capex = latest(cf, "Capital Expenditure") or 0.0  # Already negative on the statement
    fcf = (ocf + capex) if ocf is not None else info.get("freeCashflow")

    total_debt = latest(bs, "Total Debt") or 0.0
    cash = (latest(bs, "Cash And Cash Equivalents")
            or latest(bs, "Cash Cash Equivalents And Short Term Investments")
            or 0.0)
    net_debt = total_debt - cash

    revenue_growth = None
    if revenue and prior_revenue and prior_revenue > 0:
        revenue_growth = revenue / prior_revenue - 1

    return {
        "ticker": ticker,
        "name": info.get("shortName") or info.get("longName"),
        "current_price": info.get("currentPrice") or info.get("regularMarketPrice"),
        "shares_outstanding": info.get("sharesOutstanding"),
        "market_cap": info.get("marketCap"),
        "enterprise_value": info.get("enterpriseValue"),
        "ebitda": ebitda,
        "revenue": revenue,
        "prior_revenue": prior_revenue,
        "revenue_growth": revenue_growth,
        "gross_profit": gross_profit,
        "fcf": fcf,
        "total_debt": total_debt,
        "cash": cash,
        "net_debt": net_debt,
        "currency": info.get("currency", "USD"),
        "ev_to_ebitda": info.get("enterpriseToEbitda"),
        "trailing_pe": info.get("trailingPE"),
    }


# ---------- Methods ----------

def value_ev_ebitda(basics: dict, target_multiple: float,
                    low_mult: float, high_mult: float) -> ValuationResult | None:
    ebitda = basics["ebitda"]
    shares = basics["shares_outstanding"]
    net_debt = basics["net_debt"]
    if not ebitda or ebitda <= 0:
        return None
    if not shares:
        return None

    def price_at(mult):
        return (ebitda * mult - net_debt) / shares

    return ValuationResult(
        method="EV/EBITDA",
        target_price=round(price_at(target_multiple), 2),
        low_estimate=round(price_at(low_mult), 2),
        high_estimate=round(price_at(high_mult), 2),
        assumptions={
            "target_multiple": target_multiple,
            "low_multiple": low_mult,
            "high_multiple": high_mult,
            "ebitda": ebitda,
            "net_debt": net_debt,
        },
        confidence=0.55,
        description=f"EV/EBITDA at {target_multiple}x (range {low_mult}-{high_mult}x)",
    )


def value_peer_comp(basics: dict, comps_path: Path) -> ValuationResult | None:
    """Use EV/EBITDA multiples from comps.csv (produced by fetch_fmp.py)."""
    if not comps_path.exists():
        return None
    df = pd.read_csv(comps_path)
    if "metric" not in df.columns or "symbol" not in df.columns:
        return None

    # Latest year is the rightmost numeric column
    year_cols = [c for c in df.columns if c.isdigit()]
    if not year_cols:
        return None
    latest_year = max(year_cols)

    peers = df[(df["metric"] == "EV/EBITDA") & (df["symbol"] != basics["ticker"])]
    mults = pd.to_numeric(peers[latest_year], errors="coerce").dropna()
    mults = mults[mults > 0]
    if len(mults) < 2:
        return None

    avg, lo, hi = float(mults.mean()), float(mults.min()), float(mults.max())
    return value_ev_ebitda_at_mults(basics, avg, lo, hi,
                                     method="Peer Comp", confidence=0.60,
                                     description=f"Peer avg EV/EBITDA = {avg:.1f}x ({len(mults)} peers, {latest_year})")


def value_ev_ebitda_at_mults(basics, target, low, high, method, confidence, description):
    ebitda = basics["ebitda"]
    shares = basics["shares_outstanding"]
    net_debt = basics["net_debt"]
    if not ebitda or ebitda <= 0 or not shares:
        return None

    def p(m):
        return (ebitda * m - net_debt) / shares

    return ValuationResult(
        method=method,
        target_price=round(p(target), 2),
        low_estimate=round(p(low), 2),
        high_estimate=round(p(high), 2),
        assumptions={"avg_multiple": target, "low": low, "high": high, "ebitda": ebitda},
        confidence=confidence,
        description=description,
    )


def value_dcf(basics: dict, growth_near: float, growth_far: float,
              terminal_growth: float, wacc: float,
              fcf_conversion: float = 0.60) -> tuple[ValuationResult | None, pd.DataFrame]:
    """10-year FCF projection. Two-phase growth (years 1-5 near, 6-10 far) +
    perpetuity terminal value. Returns (result, projection_dataframe)."""
    ebitda = basics["ebitda"]
    shares = basics["shares_outstanding"]
    net_debt = basics["net_debt"]
    if not ebitda or ebitda <= 0 or not shares:
        return None, pd.DataFrame()

    fcf_0 = ebitda * fcf_conversion
    proj = []
    fcf = fcf_0
    for year in range(1, 11):
        g = growth_near if year <= 5 else growth_far
        fcf = fcf * (1 + g)
        discount = (1 + wacc) ** year
        pv = fcf / discount
        proj.append({"year": year, "growth": g, "fcf": fcf, "discount": discount, "pv_fcf": pv})

    proj_df = pd.DataFrame(proj)
    pv_fcf_sum = proj_df["pv_fcf"].sum()

    # Perpetuity terminal value at end of year 10
    fcf_10 = proj_df["fcf"].iloc[-1]
    if wacc <= terminal_growth:
        return None, proj_df  # avoid div by zero / negative
    terminal = fcf_10 * (1 + terminal_growth) / (wacc - terminal_growth)
    pv_terminal = terminal / ((1 + wacc) ** 10)

    enterprise_value = pv_fcf_sum + pv_terminal
    equity_value = enterprise_value - net_debt
    target_price = equity_value / shares

    # Bull/bear sensitivity: ±200bps on WACC and terminal growth
    bear_price = _dcf_price(ebitda, fcf_conversion, growth_near, growth_far,
                             terminal_growth - 0.005, wacc + 0.02, net_debt, shares)
    bull_price = _dcf_price(ebitda, fcf_conversion, growth_near, growth_far,
                             terminal_growth + 0.005, wacc - 0.02, net_debt, shares)

    return ValuationResult(
        method="DCF",
        target_price=round(target_price, 2),
        low_estimate=round(bear_price, 2),
        high_estimate=round(bull_price, 2),
        assumptions={
            "fcf_conversion": fcf_conversion,
            "growth_near_5y": growth_near,
            "growth_far_5y": growth_far,
            "terminal_growth": terminal_growth,
            "wacc": wacc,
            "pv_fcf_sum_$M": round(pv_fcf_sum / 1e6, 1),
            "pv_terminal_$M": round(pv_terminal / 1e6, 1),
            "enterprise_value_$M": round(enterprise_value / 1e6, 1),
            "equity_value_$M": round(equity_value / 1e6, 1),
        },
        confidence=0.45,
        description=f"10-yr DCF, {growth_near*100:.0f}%/{growth_far*100:.0f}% growth, "
                    f"{terminal_growth*100:.1f}% terminal, {wacc*100:.0f}% WACC",
    ), proj_df


def value_ev_fcf(basics: dict, target_multiple: float,
                  low_mult: float, high_mult: float) -> ValuationResult | None:
    """EV/FCF — the cleanest metric for pre-EBITDA-but-FCF-positive SaaS.
    Bypasses the SBC add-back debate because FCF is real cash. Confidence: 0.60."""
    fcf = basics.get("fcf")
    shares = basics.get("shares_outstanding")
    net_debt = basics.get("net_debt") or 0.0
    if not fcf or fcf <= 0 or not shares:
        return None

    def p(m):
        return (fcf * m - net_debt) / shares

    return ValuationResult(
        method="EV/FCF",
        target_price=round(p(target_multiple), 2),
        low_estimate=round(p(low_mult), 2),
        high_estimate=round(p(high_mult), 2),
        assumptions={
            "target_multiple": target_multiple,
            "low_multiple": low_mult,
            "high_multiple": high_mult,
            "fcf": fcf,
            "net_debt": net_debt,
        },
        confidence=0.60,
        description=f"EV/FCF at {target_multiple}x (range {low_mult}-{high_mult}x) "
                    f"- bypasses SBC debate, real cash",
    )


def value_ev_gp(basics: dict, target_multiple: float,
                 low_mult: float, high_mult: float) -> ValuationResult | None:
    """EV/Gross Profit — Meritech's preferred SaaS metric. GP captures business-model
    quality so a 20% GM reseller and an 80% GM SaaS don't trade off the same revenue
    multiple. Confidence: 0.55."""
    gp = basics.get("gross_profit")
    shares = basics.get("shares_outstanding")
    net_debt = basics.get("net_debt") or 0.0
    if not gp or gp <= 0 or not shares:
        return None

    def p(m):
        return (gp * m - net_debt) / shares

    return ValuationResult(
        method="EV/Gross Profit",
        target_price=round(p(target_multiple), 2),
        low_estimate=round(p(low_mult), 2),
        high_estimate=round(p(high_mult), 2),
        assumptions={
            "target_multiple": target_multiple,
            "low_multiple": low_mult,
            "high_multiple": high_mult,
            "gross_profit": gp,
            "net_debt": net_debt,
        },
        confidence=0.55,
        description=f"EV/GP at {target_multiple}x - Meritech standard for SaaS",
    )


def value_ev_revenue(basics: dict, target: float, low: float, high: float,
                      r40_context: dict | None = None) -> ValuationResult | None:
    """Peer-derived EV/Revenue valuation. If r40_context is provided, the Rule
    of 40 score for the subject is included as commentary on whether the peer
    multiple is appropriate (subject at R40 above peer median deserves the high
    end; below median deserves the low end)."""
    revenue = basics.get("revenue")
    shares = basics.get("shares_outstanding")
    net_debt = basics.get("net_debt") or 0.0
    if not revenue or not shares:
        return None

    def p(m):
        return (revenue * m - net_debt) / shares

    method_name = "EV/Revenue"
    desc = f"EV/Rev at {target}x (peer-derived range {low}-{high}x)"
    assumptions = {"target_multiple": target, "low": low, "high": high,
                   "revenue": revenue, "net_debt": net_debt}
    if r40_context:
        assumptions.update({
            "rule40_score_pct": round(r40_context["rule40_score"] * 100, 1),
            "revenue_growth_pct": round(r40_context["revenue_growth"] * 100, 1),
            "fcf_margin_pct": round(r40_context["fcf_margin"] * 100, 1),
        })
        method_name = "EV/Revenue (R40-qualified)"
        desc += f" — subject R40 = {r40_context['rule40_score']*100:+.1f}%"

    return ValuationResult(
        method=method_name,
        target_price=round(p(target), 2),
        low_estimate=round(p(low), 2),
        high_estimate=round(p(high), 2),
        assumptions=assumptions,
        confidence=0.55,
        description=desc,
    )


def compute_rule40(basics: dict) -> dict | None:
    """Standalone Rule of 40 diagnostic. Returns score components, no
    valuation."""
    revenue = basics.get("revenue")
    fcf = basics.get("fcf")
    growth = basics.get("revenue_growth")
    if not revenue or growth is None or fcf is None:
        return None
    fcf_margin = fcf / revenue
    return {
        "rule40_score": growth + fcf_margin,
        "revenue_growth": growth,
        "fcf_margin": fcf_margin,
    }


def value_path_dcf(basics: dict,
                    rev_growth_path: list[float],
                    ebitda_margin_path: list[float],
                    terminal_multiple_y5: float,
                    wacc: float,
                    fcf_conversion: float,
                    survival_prob: float
                    ) -> tuple[ValuationResult | None, pd.DataFrame]:
    """Damodaran-style path-to-profitability DCF. 5-year explicit forecast where
    each year has its own revenue growth and EBITDA margin. Terminal value at
    year 5 via EV/EBITDA multiple. Final equity value haircut by P(survival)."""
    revenue = basics.get("revenue")
    shares = basics.get("shares_outstanding")
    net_debt = basics.get("net_debt") or 0.0
    if not revenue or not shares:
        return None, pd.DataFrame()
    if len(rev_growth_path) != 5 or len(ebitda_margin_path) != 5:
        return None, pd.DataFrame()

    rev = revenue
    pv_fcf_sum = 0.0
    proj = []
    for year in range(1, 6):
        g = rev_growth_path[year - 1]
        m = ebitda_margin_path[year - 1]
        rev = rev * (1 + g)
        ebitda = rev * m
        # When EBITDA is negative, the firm is burning cash (FCF ~ EBITDA before WC swings).
        # When positive, apply conversion. This is a simplification — in a real model you'd
        # build out WC, tax, capex separately.
        fcf = ebitda if ebitda <= 0 else ebitda * fcf_conversion
        pv = fcf / ((1 + wacc) ** year)
        pv_fcf_sum += pv
        proj.append({
            "year": year, "rev_growth": g, "ebitda_margin": m,
            "revenue": rev, "ebitda": ebitda, "fcf": fcf, "pv_fcf": pv,
        })

    proj_df = pd.DataFrame(proj)
    y5_ebitda = proj_df["ebitda"].iloc[-1]
    if y5_ebitda <= 0:
        # Path doesn't reach profitability — uninvestable on this method
        return None, proj_df

    terminal_ev = y5_ebitda * terminal_multiple_y5
    pv_terminal = terminal_ev / ((1 + wacc) ** 5)
    enterprise_value = pv_fcf_sum + pv_terminal
    equity_value = enterprise_value - net_debt

    # Damodaran failure-probability adjustment: P(survive) * going-concern + P(fail) * 0
    expected_equity = equity_value * survival_prob
    target_price = expected_equity / shares

    # Range: bull = no haircut, bear = harsher haircut + bear terminal multiple
    bull_equity = equity_value
    bear_terminal = y5_ebitda * (terminal_multiple_y5 * 0.7)
    bear_pv_terminal = bear_terminal / ((1 + wacc) ** 5)
    bear_equity = (pv_fcf_sum + bear_pv_terminal - net_debt) * (survival_prob * 0.7)

    # Find profitability crossover year
    cross_year = next((p["year"] for p in proj if p["ebitda"] > 0), None)

    return ValuationResult(
        method="Path-to-Profitability DCF",
        target_price=round(target_price, 2),
        low_estimate=round(bear_equity / shares, 2),
        high_estimate=round(bull_equity / shares, 2),
        assumptions={
            "rev_growth_path": rev_growth_path,
            "ebitda_margin_path": ebitda_margin_path,
            "terminal_multiple_y5": terminal_multiple_y5,
            "wacc": wacc,
            "fcf_conversion": fcf_conversion,
            "survival_prob": survival_prob,
            "ebitda_crossover_year": cross_year,
            "y5_ebitda_$M": round(y5_ebitda / 1e6, 1),
            "pv_fcf_5y_$M": round(pv_fcf_sum / 1e6, 1),
            "pv_terminal_$M": round(pv_terminal / 1e6, 1),
            "enterprise_value_$M": round(enterprise_value / 1e6, 1),
        },
        confidence=0.40,
        description=(f"5-yr path DCF, EBITDA cross y{cross_year}, "
                     f"P(survive)={survival_prob*100:.0f}%, "
                     f"terminal {terminal_multiple_y5}x EV/EBITDA"),
    ), proj_df


def _dcf_price(ebitda, fcf_conv, gn, gf, tg, wacc, net_debt, shares):
    fcf = ebitda * fcf_conv
    pv_sum = 0.0
    for year in range(1, 11):
        g = gn if year <= 5 else gf
        fcf *= (1 + g)
        pv_sum += fcf / (1 + wacc) ** year
    if wacc <= tg:
        return float("nan")
    terminal = fcf * (1 + tg) / (wacc - tg)
    pv_t = terminal / (1 + wacc) ** 10
    return (pv_sum + pv_t - net_debt) / shares


# ---------- Sensitivity ----------

def sensitivity_matrix(basics: dict, target_multiple: float, mode: str = "ebitda",
                       rev_range: tuple[float, float] = (-0.05, 0.05),
                       margin_range: tuple[float, float] = (-0.02, 0.02),
                       steps: int = 5) -> pd.DataFrame:
    """2D sensitivity: revenue deltas x margin deltas -> implied share price.

    mode='ebitda': uses EBITDA margin and EV/EBITDA multiple
    mode='fcf':    uses FCF margin and EV/FCF multiple (for pre-EBITDA names)
    """
    rev = basics["revenue"]
    shares = basics["shares_outstanding"]
    net_debt = basics["net_debt"]
    if not (rev and shares):
        return pd.DataFrame()

    if mode == "ebitda":
        ebitda = basics.get("ebitda")
        if not ebitda or ebitda <= 0:
            return pd.DataFrame()
        base_margin = ebitda / rev
        label = "EBITDA"
    elif mode == "fcf":
        fcf = basics.get("fcf")
        if fcf is None:
            return pd.DataFrame()
        base_margin = fcf / rev
        label = "FCF"
    else:
        return pd.DataFrame()

    rev_deltas = np.linspace(rev_range[0], rev_range[1], steps)
    margin_deltas = np.linspace(margin_range[0], margin_range[1], steps)

    rows = []
    for rd in rev_deltas:
        new_rev = rev * (1 + rd)
        row = {"Revenue_d": f"{rd*100:+.1f}%"}
        for md in margin_deltas:
            new_margin = base_margin + md
            new_cf = new_rev * new_margin
            implied_price = (new_cf * target_multiple - net_debt) / shares
            row[f"{label}m_{md*100:+.1f}%"] = round(implied_price, 2)
        rows.append(row)
    return pd.DataFrame(rows).set_index("Revenue_d")


# ---------- Football field chart ----------

def football_field(results: list[ValuationResult], basics: dict, out_path: Path):
    """Horizontal bar showing low-to-high range for each method, with current price line."""
    results = [r for r in results if r is not None]
    if not results:
        return
    current = basics.get("current_price")

    fig, ax = plt.subplots(figsize=(9, max(3, 1.0 * len(results) + 1.5)))
    y_pos = np.arange(len(results))

    for i, r in enumerate(results):
        ax.barh(i, r.high_estimate - r.low_estimate, left=r.low_estimate,
                height=0.55, color="#4a7ab8", alpha=0.7, edgecolor="#2c4f7e")
        # Target marker
        ax.plot(r.target_price, i, marker="D", markersize=9,
                color="#1f3a5f", markeredgecolor="white", markeredgewidth=1.2, zorder=5)
        # Labels at the end of each bar
        ax.text(r.high_estimate, i,
                f"  ${r.low_estimate:.2f} – ${r.high_estimate:.2f} (tgt ${r.target_price:.2f})",
                va="center", fontsize=9)

    if current:
        ax.axvline(current, color="#c0392b", linestyle="--", linewidth=1.5,
                   label=f"Current: ${current:.2f}", zorder=3)
        ax.legend(loc="lower right", fontsize=9, frameon=True)

    ax.set_yticks(y_pos)
    ax.set_yticklabels([r.method for r in results], fontsize=10)
    ax.invert_yaxis()
    ax.set_xlabel("Implied share price ($)")
    ax.set_title(f"{basics['ticker']} — Valuation Football Field",
                 fontsize=12, fontweight="bold")
    ax.grid(axis="x", alpha=0.3, linestyle=":")
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)

    # Pad x-axis so labels don't clip
    xs_max = max(r.high_estimate for r in results)
    xs_min = min(r.low_estimate for r in results)
    if current:
        xs_max = max(xs_max, current)
        xs_min = min(xs_min, current)
    pad = (xs_max - xs_min) * 0.45
    ax.set_xlim(max(0, xs_min - pad * 0.2), xs_max + pad)

    fig.tight_layout()
    fig.savefig(out_path, dpi=150)
    plt.close(fig)


# ---------- Driver ----------

ALL_METHODS = ["ev_ebitda", "ev_fcf", "ev_gp", "ev_revenue", "dcf", "path_dcf", "peer_comp"]


def parse_path(s: str, name: str, expected: int = 5) -> list[float]:
    parts = [float(x.strip()) for x in s.split(",") if x.strip()]
    if len(parts) != expected:
        raise SystemExit(f"--{name}: expected {expected} comma-separated values, got {len(parts)}")
    return parts


def resolve_multiples(metric: str, peers_df: pd.DataFrame | None,
                       cli_target: float | None, cli_low: float | None,
                       cli_high: float | None) -> tuple[dict | None, str]:
    """Decide where multiples for this metric come from.

    Priority:
      1. CLI override (--target-multiple etc.) — always wins, source='cli'
      2. Peer benchmarks CSV — source='peer'
      3. None → method is skipped, source='none'
    """
    if cli_target is not None:
        return {
            "target": cli_target,
            "low": cli_low if cli_low is not None else cli_target * 0.75,
            "high": cli_high if cli_high is not None else cli_target * 1.25,
            "n_peers": 0,
            "tier_used": "cli-override",
            "peer_tickers": [],
        }, "cli"
    if peers_df is not None:
        col = METRIC_TO_PEER_COL.get(metric)
        if col:
            bands = compute_peer_bands(peers_df, col)
            if bands:
                return bands, "peer"
    return None, "none"


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("ticker")
    parser.add_argument("--methods", default="auto",
                        help=("Comma list: " + ",".join(ALL_METHODS) + ". "
                              "'auto' picks methods based on EBITDA sign."))
    parser.add_argument("--init-peers", action="store_true",
                        help="Write empty peer_benchmarks.csv template and exit.")
    # 10-yr DCF assumptions
    parser.add_argument("--growth-near", type=float, default=0.10,
                        help="FCF growth years 1-5 in 10-yr DCF (default 10%%)")
    parser.add_argument("--growth-far", type=float, default=0.05,
                        help="FCF growth years 6-10 in 10-yr DCF (default 5%%)")
    parser.add_argument("--terminal-growth", type=float, default=0.025,
                        help="Perpetual growth past year 10 (default 2.5%%)")
    parser.add_argument("--wacc", type=float, default=0.10, help="WACC (default 10%%)")
    parser.add_argument("--fcf-conversion", type=float, default=0.60,
                        help="FCF/EBITDA conversion (default 60%%)")
    # Multiple overrides (None = use peer benchmarks)
    parser.add_argument("--target-multiple", type=float, default=None,
                        help="Override target EV/EBITDA multiple (default: from peer CSV)")
    parser.add_argument("--low-multiple", type=float, default=None)
    parser.add_argument("--high-multiple", type=float, default=None)
    parser.add_argument("--fcf-target-multiple", type=float, default=None,
                        help="Override target EV/FCF multiple (default: from peer CSV)")
    parser.add_argument("--fcf-low-multiple", type=float, default=None)
    parser.add_argument("--fcf-high-multiple", type=float, default=None)
    parser.add_argument("--gp-target-multiple", type=float, default=None,
                        help="Override target EV/GP multiple (default: from peer CSV)")
    parser.add_argument("--gp-low-multiple", type=float, default=None)
    parser.add_argument("--gp-high-multiple", type=float, default=None)
    parser.add_argument("--ev-rev-target-multiple", type=float, default=None,
                        help="Override target EV/Revenue multiple (default: from peer CSV)")
    parser.add_argument("--ev-rev-low-multiple", type=float, default=None)
    parser.add_argument("--ev-rev-high-multiple", type=float, default=None)
    # Path-to-Profitability DCF (these are assumptions, not multiples, so defaults OK)
    parser.add_argument("--rev-growth-path", default="0.15,0.12,0.10,0.08,0.06",
                        help="5-yr revenue growth path (per-company; defaults are sector-generic)")
    parser.add_argument("--ebitda-margin-path", default="-0.05,0.00,0.05,0.10,0.15",
                        help="5-yr EBITDA margin path (per-company; defaults are sector-generic)")
    parser.add_argument("--terminal-multiple-y5", type=float, default=None,
                        help="EV/EBITDA at year 5 for terminal (default: from peer CSV)")
    parser.add_argument("--survival-prob", type=float, default=0.85,
                        help="P(survive 5 years) - Damodaran failure-probability haircut (default 0.85)")
    parser.add_argument("--use-comps", action="store_true",
                        help="Add peer-comp method using data/fmp/<ticker>/comps.csv")
    args = parser.parse_args()

    ticker = args.ticker.upper()
    print(f"Pulling basics for {ticker} via yfinance...")
    basics = pull_basics(ticker)

    def fmt(v, divisor=1e6, suffix="M", precision=1):
        return f"${v/divisor:.{precision}f}{suffix}" if v else "N/A"

    print(f"  {basics['name']}")
    print(f"  price=${basics['current_price']}  shares={basics['shares_outstanding']:,}"
          if basics['shares_outstanding'] else f"  price=${basics['current_price']}")
    if basics['revenue_growth'] is not None:
        print(f"  rev={fmt(basics['revenue'])}  growth={basics['revenue_growth']*100:+.1f}%")
    else:
        print(f"  rev={fmt(basics['revenue'])}")
    print(f"  EBITDA={fmt(basics['ebitda'])}  GP={fmt(basics['gross_profit'])}  "
          f"FCF={fmt(basics['fcf'])}")
    print(f"  net_debt={fmt(basics['net_debt'])}")

    # --init-peers: write the template and exit
    if args.init_peers:
        path = write_peer_template(ticker, basics)
        print(f"\n  Wrote peer benchmark template: {path}")
        print_research_instructions(ticker, path)
        return

    # Load peer benchmarks (may be None)
    peers_df = load_peer_benchmarks(ticker)
    peer_path = peer_csv_path(ticker)
    if peers_df is None:
        print(f"\n  No peer benchmarks at {peer_path}")
    else:
        n_primary = int((peers_df["inclusion"] == "primary").sum())
        n_secondary = int((peers_df["inclusion"] == "secondary").sum())
        print(f"\n  Peer benchmarks: {peer_path.name} "
              f"({n_primary} primary, {n_secondary} secondary)")

    # Method routing
    if args.methods == "auto":
        if basics["ebitda"] and basics["ebitda"] > 0:
            methods = ["ev_ebitda", "dcf"]
        else:
            methods = ["ev_fcf", "ev_gp", "ev_revenue", "path_dcf"]
        if args.use_comps:
            methods.append("peer_comp")
        print(f"  Auto-selected methods: {','.join(methods)}")
    else:
        methods = [m.strip() for m in args.methods.split(",") if m.strip()]
        bad = [m for m in methods if m not in ALL_METHODS]
        if bad:
            raise SystemExit(f"Unknown method(s): {bad}. Options: {ALL_METHODS}")

    # Pre-flight: which methods can run given the data available?
    # Resolve multiples upfront so we can detect missing peer benchmarks early.
    multiple_specs = {}
    multiple_sources = {}
    needs_peer_research = False

    if "ev_ebitda" in methods:
        spec, src = resolve_multiples("ev_ebitda", peers_df,
                                       args.target_multiple, args.low_multiple, args.high_multiple)
        multiple_specs["ev_ebitda"] = spec
        multiple_sources["ev_ebitda"] = src
        if src == "none" and basics["ebitda"] and basics["ebitda"] > 0:
            needs_peer_research = True

    if "ev_fcf" in methods:
        spec, src = resolve_multiples("ev_fcf", peers_df,
                                       args.fcf_target_multiple,
                                       args.fcf_low_multiple, args.fcf_high_multiple)
        multiple_specs["ev_fcf"] = spec
        multiple_sources["ev_fcf"] = src
        if src == "none" and basics.get("fcf") and basics["fcf"] > 0:
            needs_peer_research = True

    if "ev_gp" in methods:
        spec, src = resolve_multiples("ev_gp", peers_df,
                                       args.gp_target_multiple,
                                       args.gp_low_multiple, args.gp_high_multiple)
        multiple_specs["ev_gp"] = spec
        multiple_sources["ev_gp"] = src
        if src == "none" and basics.get("gross_profit") and basics["gross_profit"] > 0:
            needs_peer_research = True

    if "ev_revenue" in methods:
        spec, src = resolve_multiples("ev_revenue", peers_df,
                                       args.ev_rev_target_multiple,
                                       args.ev_rev_low_multiple, args.ev_rev_high_multiple)
        multiple_specs["ev_revenue"] = spec
        multiple_sources["ev_revenue"] = src
        if src == "none" and basics.get("revenue"):
            needs_peer_research = True

    # If we need peer research and no CSV exists at all, write template + exit
    if needs_peer_research and peers_df is None:
        path = write_peer_template(ticker, basics)
        print(f"\n  Wrote peer benchmark template: {path}")
        print_research_instructions(ticker, path)
        return

    out_dir = VAL_DIR / ticker.lower()
    out_dir.mkdir(parents=True, exist_ok=True)

    results: list[ValuationResult] = []
    diagnostics: dict = {}

    def report_mult_source(method_name, spec, source):
        if source == "peer":
            print(f"  multiples from peers: target {spec['target']}x  "
                  f"range {spec['low']}-{spec['high']}x  "
                  f"(n={spec['n_peers']}, tier={spec['tier_used']})")
        elif source == "cli":
            print(f"  multiples from CLI override: target {spec['target']}x  "
                  f"range {spec['low']}-{spec['high']}x")

    if "ev_ebitda" in methods:
        print("\n[EV/EBITDA]")
        spec = multiple_specs["ev_ebitda"]
        if spec is None:
            print("  skipped (no peer EV/EBITDA data and no CLI override)")
        else:
            report_mult_source("EV/EBITDA", spec, multiple_sources["ev_ebitda"])
            r = value_ev_ebitda(basics, spec["target"], spec["low"], spec["high"])
            if r:
                print(f"  target ${r.target_price}  range ${r.low_estimate}-${r.high_estimate}")
                results.append(r)
            else:
                print("  skipped (EBITDA <= 0 or missing shares)")

    if "ev_fcf" in methods:
        print("\n[EV/FCF]")
        spec = multiple_specs["ev_fcf"]
        if spec is None:
            print("  skipped (no peer EV/FCF data and no CLI override)")
        else:
            report_mult_source("EV/FCF", spec, multiple_sources["ev_fcf"])
            r = value_ev_fcf(basics, spec["target"], spec["low"], spec["high"])
            if r:
                print(f"  target ${r.target_price}  range ${r.low_estimate}-${r.high_estimate}")
                results.append(r)
            else:
                print("  skipped (FCF <= 0 or missing)")

    if "ev_gp" in methods:
        print("\n[EV/Gross Profit]")
        spec = multiple_specs["ev_gp"]
        if spec is None:
            print("  skipped (no peer EV/GP data and no CLI override)")
        else:
            report_mult_source("EV/GP", spec, multiple_sources["ev_gp"])
            r = value_ev_gp(basics, spec["target"], spec["low"], spec["high"])
            if r:
                print(f"  target ${r.target_price}  range ${r.low_estimate}-${r.high_estimate}")
                results.append(r)
            else:
                print("  skipped (Gross Profit <= 0 or missing)")

    if "ev_revenue" in methods:
        print("\n[EV/Revenue]")
        spec = multiple_specs["ev_revenue"]
        r40 = compute_rule40(basics)
        if r40:
            print(f"  R40 = {r40['rule40_score']*100:+.1f}%  "
                  f"(growth {r40['revenue_growth']*100:+.1f}%, "
                  f"FCF margin {r40['fcf_margin']*100:+.1f}%)")
            diagnostics["rule40"] = {k: round(v, 4) for k, v in r40.items()}
        if spec is None:
            print("  skipped (no peer EV/Rev data and no CLI override)")
        else:
            report_mult_source("EV/Rev", spec, multiple_sources["ev_revenue"])
            r = value_ev_revenue(basics, spec["target"], spec["low"], spec["high"],
                                  r40_context=r40)
            if r:
                print(f"  target ${r.target_price}  range ${r.low_estimate}-${r.high_estimate}")
                results.append(r)
            else:
                print("  skipped (missing revenue or shares)")

    if "peer_comp" in methods:
        print("\n[Peer Comp (FMP)]")
        comps_path = FMP_DIR / ticker.lower() / "comps.csv"
        r = value_peer_comp(basics, comps_path)
        if r:
            print(f"  target ${r.target_price}  range ${r.low_estimate}-${r.high_estimate}")
            print(f"  ({r.description})")
            results.append(r)
        else:
            print(f"  no comps at {comps_path}")

    if "dcf" in methods:
        print("\n[10-yr DCF]")
        r, proj_df = value_dcf(basics, args.growth_near, args.growth_far,
                                args.terminal_growth, args.wacc, args.fcf_conversion)
        if r:
            print(f"  target ${r.target_price}  range ${r.low_estimate}-${r.high_estimate}")
            results.append(r)
            proj_df.to_csv(out_dir / "dcf_projection.csv", index=False)
        else:
            print("  skipped (EBITDA <= 0 or WACC <= terminal growth)")

    if "path_dcf" in methods:
        print("\n[Path-to-Profitability DCF]")
        rev_path = parse_path(args.rev_growth_path, "rev-growth-path")
        mgn_path = parse_path(args.ebitda_margin_path, "ebitda-margin-path")
        # Terminal y5 multiple: CLI override -> peer EV/EBITDA median -> skip
        terminal_y5 = args.terminal_multiple_y5
        if terminal_y5 is None and peers_df is not None:
            bands = compute_peer_bands(peers_df, "ev_ebitda")
            if bands:
                terminal_y5 = bands["target"]
                print(f"  terminal y5 multiple from peers: {terminal_y5}x")
        if terminal_y5 is None:
            print("  skipped (no terminal multiple — provide --terminal-multiple-y5 or peer EV/EBITDA)")
        else:
            r, proj_df = value_path_dcf(basics, rev_path, mgn_path, terminal_y5,
                                         args.wacc, args.fcf_conversion, args.survival_prob)
            if r:
                print(f"  target ${r.target_price}  range ${r.low_estimate}-${r.high_estimate}")
                print(f"  ({r.description})")
                results.append(r)
                proj_df.to_csv(out_dir / "path_dcf_projection.csv", index=False)
            else:
                print("  skipped (no positive EBITDA in year 5 of path)")

    # Sensitivity matrix
    print("\n[Sensitivity matrix]")
    if basics["ebitda"] and basics["ebitda"] > 0 and "ev_ebitda" in multiple_specs:
        sens_spec = multiple_specs["ev_ebitda"]
        if sens_spec:
            sens = sensitivity_matrix(basics, sens_spec["target"], mode="ebitda")
            sens_label = f"EV/EBITDA at {sens_spec['target']}x"
        else:
            sens = pd.DataFrame()
            sens_label = ""
    elif "ev_fcf" in multiple_specs and multiple_specs["ev_fcf"]:
        sens_spec = multiple_specs["ev_fcf"]
        sens = sensitivity_matrix(basics, sens_spec["target"], mode="fcf")
        sens_label = f"EV/FCF at {sens_spec['target']}x"
    else:
        sens = pd.DataFrame()
        sens_label = ""
    if not sens.empty:
        print(f"  ({sens_label})")
        print(sens.to_string())
        sens.to_csv(out_dir / "sensitivity.csv")
    else:
        print("  skipped (no multiple resolved for sensitivity anchor)")

    # Football field
    print("\n[Football field]")
    ff_path = out_dir / "football_field.png"
    if results:
        football_field(results, basics, ff_path)
        print(f"  saved: {ff_path}")
    else:
        print("  skipped (no valid valuation results)")

    # Summary + blended target
    current = basics.get("current_price")
    summary = {
        "ticker": ticker,
        "name": basics["name"],
        "current_price": current,
        "methods_run": methods,
        "multiple_sources": multiple_sources,
        "peer_benchmarks_file": str(peer_path) if peers_df is not None else None,
        "diagnostics": diagnostics,
        "results": [asdict(r) for r in results],
    }
    if current and results:
        weights = np.array([r.confidence for r in results])
        prices = np.array([r.target_price for r in results])
        blended = float(np.average(prices, weights=weights))
        summary["blended_target"] = round(blended, 2)
        summary["upside_pct"] = round((blended / current - 1) * 100, 1)
        print(f"\n  Blended target: ${blended:.2f}  "
              f"({summary['upside_pct']:+.1f}% vs current ${current:.2f})")

    (out_dir / "summary.json").write_text(json.dumps(summary, indent=2, default=str))
    print(f"\nAll outputs in {out_dir}/")


if __name__ == "__main__":
    main()
