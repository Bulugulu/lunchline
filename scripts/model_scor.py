"""SCOR back-of-envelope model - sanity check math for the writeup."""

# ============= CURRENT STATE =============
current_price = 8.00
shares_basic = 9.4
shares_diluted = 15.0  # incl Series C convertible at $11.41 (6M over 3 years)

cash_post = 50.0
debt_post = 9.0
net_cash_post = cash_post - debt_post  # $41M
print(f"Mkt cap (basic 9.4M):     ${current_price * shares_basic:>6.1f}M")
print(f"Mkt cap (diluted 15M):    ${current_price * shares_diluted:>6.1f}M")
print(f"Net cash post-payoff:     ${net_cash_post:>6.1f}M")
print(f"Net cash / diluted share: ${net_cash_post / shares_diluted:>7.2f}")
print(f"Implied EV (diluted):     ${current_price * shares_diluted - net_cash_post:>6.1f}M")
print(f"Implied EV/Rev (319):     {(current_price * shares_diluted - net_cash_post)/319:>7.2f}x")

# ============= REVENUE BASE (post-Movies) =============
rev_base = 319.0
cross_platform = 50.0
syndicated = 254.0
other = rev_base - cross_platform - syndicated  # $15M


def forecast(cp_g, syn_g, oth_g, years=3):
    cp, syn, oth = cross_platform, syndicated, other
    for _ in range(years):
        cp *= 1 + cp_g
        syn *= 1 + syn_g
        oth *= 1 + oth_g
    return cp + syn + oth, cp, syn, oth


print("\n=== 3-YEAR REVENUE FORECAST ===")
# STRESS: customer disintermediation contagion, JIC fails, Syndicated collapses
stress = forecast(-0.15, -0.10, -0.08)
# BEAR: meaningful disintermediation; CP can't outrun syndicated decline
bear = forecast(-0.05, -0.07, -0.05)
# BASE: CP +5% (Q4 trend), syndicated -3%/yr secular
base = forecast(0.05, -0.03, -0.02)
# BULL: JIC tailwind, CP reaccelerates, syndicated stabilizes
bull = forecast(0.12, -0.01, 0.00)

for name, (tot, cp, syn, oth) in [
    ("STRESS (CP -15%, Syn -10%, Oth -8%)", stress),
    ("BEAR (CP -5%, Syn -7%, Oth -5%)", bear),
    ("BASE (CP +5%, Syn -3%, Oth -2%)", base),
    ("BULL (CP +12%, Syn -1%, Oth flat)", bull),
]:
    cagr = (tot/rev_base)**(1/3) - 1
    print(f"\n{name}")
    print(f"  CP ${cp:.0f}M | Syn ${syn:.0f}M | Oth ${oth:.0f}M | Total ${tot:.0f}M | CAGR {cagr*100:+.1f}%")

# ============= EXIT VALUATION =============
print("\n=== EXIT VALUATION (3 years out) ===")

# Share count: Series C only converts at price >= $11.41 (anti-dilution to holder).
# We assume conversion = bad outcome for common (more shares, lower per-share value)
# but holders rationally convert only if in-the-money. Set 9.4M if price <$11.41, else 15M.

scenarios = [
    # name, year3 rev, EV/Rev mult, net cash at exit, prob
    # Stress case: market loses confidence, distressed mult, cash burned
    ("STRESS",  stress[0], 0.25, 10, 0.10),
    ("BEAR",    bear[0],   0.40, 25, 0.30),
    ("BASE",    base[0],   0.70, 45, 0.40),
    ("BULL",    bull[0],   1.30, 75, 0.15),
    ("STRETCH", bull[0],   2.00, 80, 0.05),
]


def shares_at_price(price):
    return 15.0 if price >= 11.41 else 9.4


results = []
for name, rev, mult, nc, prob in scenarios:
    ev = rev * mult
    equity = ev + nc
    shares = 15.0
    for _ in range(5):
        price = equity / shares
        shares = shares_at_price(price)
    irr = (price / current_price) ** (1/3) - 1
    results.append((name, rev, mult, nc, shares, prob, ev, equity, price, irr))
    print(f"\n{name} (P={prob:.0%}):")
    print(f"  Y3 Rev ${rev:.0f}M x {mult:.2f}x = EV ${ev:.0f}M")
    print(f"  + Net cash ${nc}M = Equity ${equity:.0f}M / {shares}M shrs = ${price:.2f}")
    print(f"  3yr IRR from $8.00 = {irr*100:+.1f}%")

# ============= EXPECTED VALUE =============
print("\n=== PROBABILITY-WEIGHTED EXPECTED VALUE ===")
total_prob = sum(r[5] for r in results)
ev_price = sum(r[5] * r[8] for r in results)
ev_irr = (ev_price / current_price) ** (1/3) - 1
ev_irr_direct = sum(r[5] * r[9] for r in results)
print(f"Total prob: {total_prob}")
print(f"EV price target (3yr): ${ev_price:.2f}")
print(f"Implied 3yr IRR from EV price: {ev_irr*100:+.1f}%")
print(f"Prob-weighted 3yr IRR (direct): {ev_irr_direct*100:+.1f}%")
print(f"20% PE hurdle: {'MEETS' if ev_irr > 0.20 else 'FAILS'}")
print(f"25% search-fund hurdle: {'MEETS' if ev_irr > 0.25 else 'FAILS'}")

# ============= DOWNSIDE / UPSIDE SKEW =============
print("\n=== ASYMMETRY CHECK ===")
loss_s = [r for r in results if r[9] < 0]
gain_s = [r for r in results if r[9] > 0]
loss_p = sum(r[5] for r in loss_s)
gain_p = sum(r[5] for r in gain_s)
exp_loss = sum(r[5] * r[9] for r in loss_s) / loss_p if loss_p > 0 else 0
exp_gain = sum(r[5] * r[9] for r in gain_s) / gain_p if gain_p > 0 else 0
print(f"P(loss): {loss_p:.0%} | Avg IRR if loss: {exp_loss*100:+.1f}%")
print(f"P(gain): {gain_p:.0%} | Avg IRR if gain: {exp_gain*100:+.1f}%")
print(f"Reward/risk ratio: {abs(exp_gain/exp_loss):.1f}x" if exp_loss < 0 else "All-gain expected outcome")

# ============= SENSITIVITY =============
print("\n=== SENSITIVITY: 3yr Revenue CAGR x Exit Multiple ===")
print("(Assumes share count toggles at $11.41, $45M net cash at exit)")
print()
print(f"{'CAGR':>10} {'Y3 Rev':>10}", end="")
for m in [0.25, 0.40, 0.60, 0.80, 1.00, 1.30, 1.50, 2.00]:
    print(f"{m:>8.2f}x", end="")
print()

for cagr in [-0.10, -0.07, -0.05, -0.02, 0.00, 0.03, 0.06]:
    rev_y3 = rev_base * (1 + cagr) ** 3
    print(f"{cagr*100:>+9.1f}% ${rev_y3:>8.0f}M", end="")
    for m in [0.25, 0.40, 0.60, 0.80, 1.00, 1.30, 1.50, 2.00]:
        ev = rev_y3 * m
        equity = ev + 45
        shares = 15.0
        for _ in range(5):
            price = equity / shares
            shares = shares_at_price(price)
        irr = (price / current_price) ** (1/3) - 1
        print(f"{irr*100:>+8.1f}%", end="")
    print()

# ============= FCF SANITY =============
print("\n=== FCF SANITY (BASE Year 3) ===")
y3_rev = base[0]
ebitda_margin = 0.085
ebitda = y3_rev * ebitda_margin
capex_pct = 0.07
capex = y3_rev * capex_pct
interest = 1.0
cash_taxes = 0
fcf = ebitda - capex - interest
print(f"Y3 Rev ${y3_rev:.0f}M | EBITDA @ 8.5% = ${ebitda:.1f}M | Capex @ 7% = ${capex:.1f}M | FCF ${fcf:.1f}M")
print(f"FCF yield on $121M mkt cap: {fcf/121*100:.1f}%")

# ============= COMPARISON =============
print("\n=== COMPARISON ===")
print("EXFY framework 2.65 | bear ~$0.65 vs $1.15 = -43%")
print(f"SCOR framework 2.85 | stress ${results[0][8]:.2f} vs $8.00 = {(results[0][8]/current_price - 1)*100:+.0f}%")
print(f"SCOR framework 2.85 | bear ${results[1][8]:.2f} vs $8.00 = {(results[1][8]/current_price - 1)*100:+.0f}%")
print(f"  -> Net cash of ${net_cash_post}M ({net_cash_post/120*100:.0f}% of mkt cap) provides floor")
