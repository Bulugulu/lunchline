"""Generate a self-contained, sortable HTML review page from the search-fund catalog CSV.

Reads data/screening/operating_catalog_searchfund_2026-05-30.csv and writes
data/screening/operating_catalog_2026-05-30.html — the full integrated board
(screen + enrichment + search-fund signals), nothing filtered out.
"""
import csv, json, os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, "data", "screening", "operating_catalog_macro_2026-05-30.csv")
OUT = os.path.join(ROOT, "data", "screening", "operating_catalog_2026-05-30.html")


def num(x, default=None):
    try:
        return float(x)
    except (TypeError, ValueError):
        return default


def esc(s):
    """HTML-escape free-text fields before they reach innerHTML."""
    return (str(s).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
            if s is not None else "")


rows = []
with open(SRC, newline="", encoding="utf-8") as f:
    for r in csv.DictReader(f):
        rows.append({
            "ticker": esc(r["ticker"]),
            "name": esc(r["name"]),
            "industry": esc(r["industry"]),
            "group": r["group"],
            "seen": r["seen"].strip().lower() == "true",
            "ev_m": num(r["ev_m"]),
            "ev_rev": num(r["ev_rev"]),
            "ev_ebitda": num(r["ev_ebitda"]),
            "op_margin": num(r["op_margin"]),
            "ind_median": num(r["ind_median"]),
            "delta_pp": num(r["delta_pp"]),
            "read": r["read"],
            "inst_pct": num(r["inst_pct"]),
            "inst_trend": esc(r["inst_trend"]),
            "float_pct": num(r["float_pct"]),
            "dollar_float_m": num(r["dollar_float_m"]),
            "thin": r["thin"].strip().upper() == "THIN",
            "rev_growth": num(r["revenueGrowth"]),
            "analysts": r["analysts"],
            "own": r["sf_own_dependence"],
            "prof": r["sf_under_prof"],
            "mna": r["sf_no_mna"],
            "invest": r["sf_under_invest"],
            "succ": r["sf_succession"],
            "sf": num(r["sf_composite"]),
            "depth": r["sf_depth"],
            "macro": r.get("macro", ""),
            "structure": r.get("structure", ""),
            "macro_note": esc(r.get("macro_note", "")),
            "macro_depth": r.get("macro_depth", ""),
            "hook": esc(r["hook"]),
            "why": esc(r["sf_why"]),
        })

# stable default sort: SF composite desc, then EV/Rev asc
rows.sort(key=lambda d: (-(d["sf"] or 0), d["ev_rev"] or 99))

DATA = json.dumps(rows)

HTML = r"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Operating-candidate board — 2026-05-30</title>
<style>
  :root{
    --bg:#0f1115; --panel:#171a21; --line:#262b36; --ink:#e7ecf3; --mut:#8b96a8;
    --good:#1f7a4d; --goodbg:#13301f; --mid:#8a6d1a; --midbg:#2c2510; --bad:#7a2230; --badbg:#2a1418;
    --up:#3ad07f; --down:#ff6b81; --flat:#9aa6b8; --accent:#5aa0ff;
  }
  *{box-sizing:border-box}
  html,body{height:100%}
  body{margin:0;background:var(--bg);color:var(--ink);font:13px/1.45 -apple-system,Segoe UI,Roboto,Helvetica,Arial,sans-serif;display:flex;flex-direction:column;height:100vh;overflow:hidden}
  header{padding:18px 22px 10px;flex:0 0 auto}
  h1{margin:0 0 2px;font-size:19px;letter-spacing:.2px}
  .sub{color:var(--mut);font-size:12.5px;max-width:1100px}
  .sub b{color:var(--ink)}
  .controls{display:flex;gap:10px;flex-wrap:wrap;align-items:center;padding:10px 22px;background:var(--bg);border-bottom:1px solid var(--line);flex:0 0 auto}
  input,select{background:var(--panel);border:1px solid var(--line);color:var(--ink);border-radius:7px;padding:7px 10px;font-size:13px}
  input[type=search]{min-width:220px}
  label.toggle{display:inline-flex;gap:6px;align-items:center;color:var(--mut);cursor:pointer;user-select:none}
  .count{color:var(--mut);margin-left:auto}
  .wrap{padding:0 14px 24px;overflow:auto;flex:1 1 auto}
  table{border-collapse:collapse;width:100%;min-width:1180px}
  thead th{position:sticky;top:0;z-index:2;background:#11141a;color:var(--mut);font-weight:600;text-align:right;padding:9px 8px;border-bottom:1px solid var(--line);cursor:pointer;white-space:nowrap;font-size:11.5px;letter-spacing:.3px}
  thead th.l{text-align:left}
  thead th:hover{color:var(--ink)}
  thead th .ar{opacity:.4;font-size:10px}
  tbody td{padding:7px 8px;border-bottom:1px solid #1c212b;text-align:right;white-space:nowrap;font-variant-numeric:tabular-nums}
  tbody td.l{text-align:left;white-space:normal}
  tbody tr:hover{background:#141821}
  tr.seen{opacity:.5}
  .tk{font-weight:700;letter-spacing:.4px}
  .tk .sbadge{font-size:9px;color:var(--mut);border:1px solid var(--line);border-radius:4px;padding:0 4px;margin-left:5px;vertical-align:middle}
  .nm{color:var(--mut);font-size:11.5px}
  .grp{display:inline-block;width:18px;height:18px;line-height:18px;text-align:center;border-radius:5px;font-size:11px;font-weight:700;color:#0f1115}
  .gA{background:#c9a227}.gB{background:#d97b4f}.gC{background:#5aa0ff}.gD{background:#b56ad0}.gE{background:#5ec4b6}.gF{background:#8b96a8}
  .chip{display:inline-block;min-width:42px;padding:2px 7px;border-radius:20px;font-size:11px;font-weight:600;text-align:center}
  .High{background:var(--goodbg);color:var(--up);border:1px solid #1f5e3c}
  .Med{background:var(--midbg);color:#e6c14c;border:1px solid #5e4f1a}
  .Low{background:#1a1d24;color:var(--mut);border:1px solid var(--line)}
  .mac-Tailwind{background:var(--goodbg);color:var(--up);border:1px solid #1f5e3c}
  .mac-Neutral{background:#1a1d24;color:#c2cad6;border:1px solid var(--line)}
  .mac-Headwind{background:var(--badbg);color:var(--down);border:1px solid #5e2230}
  .stag{display:inline-block;padding:1px 6px;border-radius:4px;font-size:10.5px;color:#aeb8c7;border:1px solid var(--line);background:#11141a}
  .read-Above{color:var(--up)} .read-In-line{color:var(--flat)} .read-Below{color:var(--down)}
  .up{color:var(--up)} .down{color:var(--down)} .flat{color:var(--flat)} .sparse{color:#5b6678;font-style:italic}
  .thin{color:#ffb454;font-weight:600}
  .sf{font-weight:700}
  .sfbar{display:inline-block;height:6px;border-radius:3px;background:var(--accent);vertical-align:middle;margin-left:6px}
  .trend{font-size:11px}
  details.why{margin:0}
  details.why summary{cursor:pointer;color:var(--mut);font-size:11px;list-style:none}
  details.why summary::-webkit-details-marker{display:none}
  details.why summary:hover{color:var(--ink)}
  details.why p{margin:5px 0 0;color:#b7c0cf;font-size:11.5px;max-width:560px;white-space:normal}
  .legend{display:flex;gap:16px;flex-wrap:wrap;padding:8px 22px 0;color:var(--mut);font-size:11.5px}
  .legend span b{color:var(--ink)}
</style>
</head>
<body>
<header>
  <h1>Operating-candidate board <span style="color:var(--mut);font-weight:400">· 69 names · 2026-05-30</span></h1>
  <div class="sub">The <b>full</b> screened operating bucket (cheap + profitable + under-followed, non-SaaS), with every lens side-by-side:
  the core screen, the enrichment (op-margin vs industry, institutional trend, float), and the <b>take-private/operate signals</b> as
  <b>additional</b> columns — <b>nothing is filtered out</b>. A low "no-M&amp;A" score just flags a roll-up on that one axis; weigh it against cheapness, smart-money flow, and margin. Click any header to sort.</div>
  <div class="legend">
    <span><b>Groups:</b> A roll-ups · B leveraged stubs · C multi-segment · D turnarounds · E cyclicals · F clean-neglected</span>
    <span><b>SF</b> = take-private composite (0–10, higher = better operate target)</span>
    <span><b>Macro</b> = industry tailwind/headwind · <b>Struct</b> = Fragmented/Barbell/Consolidated (hover for driver; <span style="color:#5b6678">~</span> = judgment, not web-verified)</span>
    <span><b>★</b> caveats: industry median skews low (cheap universe); inst-trend "sparse" where 13F too thin; some inst% &gt; float% (vendor noise)</span>
  </div>
</header>
<div class="controls">
  <input type="search" id="q" placeholder="filter ticker / name / industry…">
  <select id="grp"><option value="">all groups</option><option>A</option><option>B</option><option>C</option><option>D</option><option>E</option><option>F</option></select>
  <select id="macro"><option value="">any macro</option><option>Tailwind</option><option>Neutral</option><option>Headwind</option></select>
  <select id="depth"><option value="">any depth</option><option value="full">full-depth only</option><option value="proxy">proxy-only</option></select>
  <label class="toggle"><input type="checkbox" id="hideseen"> hide already-seen</label>
  <label class="toggle"><input type="checkbox" id="thinonly"> hide THIN float</label>
  <span class="count" id="count"></span>
</div>
<div class="wrap">
<table>
  <thead><tr>
    <th class="l" data-k="ticker">Ticker</th>
    <th class="l" data-k="group">Grp</th>
    <th data-k="ev_m">EV $M</th>
    <th data-k="ev_rev">EV/Rev</th>
    <th data-k="ev_ebitda">EV/EBITDA</th>
    <th data-k="op_margin">Op&nbsp;m%</th>
    <th data-k="delta_pp">vs&nbsp;ind</th>
    <th data-k="rev_growth">Rev&nbsp;gr</th>
    <th data-k="inst_pct">Inst%</th>
    <th data-k="inst_trend">Inst&nbsp;trend</th>
    <th data-k="float_pct">Float%</th>
    <th data-k="dollar_float_m">$Float&nbsp;M</th>
    <th class="l" data-k="macro">Macro</th>
    <th class="l" data-k="structure">Struct</th>
    <th data-k="own">OwnDep</th>
    <th data-k="prof">UndProf</th>
    <th data-k="mna">NoM&amp;A</th>
    <th data-k="invest">UndInv</th>
    <th data-k="succ">Succ</th>
    <th data-k="sf">SF</th>
    <th class="l" data-k="why">Why / notes</th>
  </tr></thead>
  <tbody id="tb"></tbody>
</table>
</div>
<script>
const DATA = __DATA__;
const RANK = {High:3, Med:2, Low:1, "":0, unverified:0};
const MRANK = {Tailwind:3, Neutral:2, Headwind:1, "":0};
const SRANK = {Fragmented:3, Barbell:2, Consolidated:1, "":0};
let sortK = "sf", sortDir = -1;

const fmt = (v,d=2)=> v==null? "·" : v.toFixed(d);
const pct = (v,d=1)=> v==null? "·" : v.toFixed(d)+"%";
const chip = v => `<span class="chip ${v||'Low'}">${v||'?'}</span>`;
function trendCell(t){
  if(!t) return '<span class="sparse">·</span>';
  if(t==='sparse') return '<span class="sparse">sparse</span>';
  let cls = t.startsWith('↑')?'up': t.startsWith('↓')?'down':'flat';
  return `<span class="trend ${cls}">${t.replace(/^(\S+)\s*/, '$1 ')}</span>`;
}
function trendRank(t){ if(!t||t==='sparse') return -1; if(t[0]==='↑')return 2; if(t[0]==='↓')return 0; return 1; }

function row(d){
  const seen = d.seen? '<span class="sbadge">seen</span>':'';
  const thin = d.thin? ' <span class="thin">THIN</span>':'';
  const sfw = (d.sf||0)*9;
  return `<tr class="${d.seen?'seen':''}">
    <td class="l"><span class="tk">${d.ticker}</span>${seen}<div class="nm">${d.name}</div></td>
    <td class="l"><span class="grp g${d.group}" title="group ${d.group}">${d.group}</span></td>
    <td>${fmt(d.ev_m,0)}</td>
    <td>${fmt(d.ev_rev,2)}</td>
    <td>${d.ev_ebitda==null?'·':d.ev_ebitda.toFixed(1)}</td>
    <td>${fmt(d.op_margin,1)}</td>
    <td class="read-${d.read.replace(' ','-')}">${d.delta_pp>0?'+':''}${fmt(d.delta_pp,1)}</td>
    <td class="${d.rev_growth>0?'up':d.rev_growth<0?'down':'flat'}">${d.rev_growth==null?'·':(d.rev_growth*100).toFixed(0)+'%'}</td>
    <td>${pct(d.inst_pct)}</td>
    <td class="l">${trendCell(d.inst_trend)}</td>
    <td class="${d.thin?'thin':''}">${pct(d.float_pct)}${thin}</td>
    <td>${fmt(d.dollar_float_m,0)}</td>
    <td class="l" title="${d.macro_note}"><span class="chip mac-${d.macro}">${d.macro||'?'}</span></td>
    <td class="l" title="${d.macro_note}"><span class="stag">${d.structure||'·'}</span>${d.macro_depth==='judgment'?' <span style="color:#5b6678;font-size:10px">~</span>':''}</td>
    <td>${chip(d.own)}</td>
    <td>${chip(d.prof)}</td>
    <td>${chip(d.mna)}</td>
    <td>${chip(d.invest)}</td>
    <td>${chip(d.succ)}</td>
    <td class="sf">${d.sf==null?'·':d.sf}<span class="sfbar" style="width:${sfw}px"></span></td>
    <td class="l"><details class="why"><summary>${d.depth==='full'?'✓ ':''}${d.hook}</summary><p>${d.why}</p></details></td>
  </tr>`;
}

function val(d,k){
  if(["own","prof","mna","invest","succ"].includes(k)) return RANK[d[k]]??0;
  if(k==="macro") return MRANK[d[k]]??0;
  if(k==="structure") return SRANK[d[k]]??0;
  if(k==="inst_trend") return trendRank(d[k]);
  if(k==="ticker"||k==="group") return d[k];
  return d[k]==null? -1e9 : d[k];
}
function render(){
  const q=document.getElementById('q').value.toLowerCase();
  const g=document.getElementById('grp').value;
  const mc=document.getElementById('macro').value;
  const dp=document.getElementById('depth').value;
  const hs=document.getElementById('hideseen').checked;
  const to=document.getElementById('thinonly').checked;
  let r=DATA.filter(d=>
    (!q || (d.ticker+' '+d.name+' '+d.industry).toLowerCase().includes(q)) &&
    (!g || d.group===g) && (!mc || d.macro===mc) && (!dp || d.depth===dp) &&
    (!hs || !d.seen) && (!to || !d.thin));
  r.sort((a,b)=>{const x=val(a,sortK),y=val(b,sortK);
    if(typeof x==='string') return sortDir*x.localeCompare(y);
    return sortDir*(x-y);});
  document.getElementById('tb').innerHTML=r.map(row).join('');
  document.getElementById('count').textContent=`${r.length} shown`;
  document.querySelectorAll('th').forEach(th=>{const a=th.querySelector('.ar'); if(a)a.remove();
    if(th.dataset.k===sortK){const s=document.createElement('span');s.className='ar';s.textContent=sortDir<0?' ▼':' ▲';th.appendChild(s);}});
}
document.querySelectorAll('th').forEach(th=>th.addEventListener('click',()=>{
  const k=th.dataset.k; if(sortK===k) sortDir*=-1; else {sortK=k; sortDir=(["ticker","group"].includes(k))?1:-1;} render();}));
['q','grp','macro','depth','hideseen','thinonly'].forEach(id=>document.getElementById(id).addEventListener('input',render));
render();
</script>
</body>
</html>
"""

html = HTML.replace("__DATA__", DATA)
os.makedirs(os.path.dirname(OUT), exist_ok=True)
with open(OUT, "w", encoding="utf-8") as f:
    f.write(html)
print("wrote", OUT, "(", len(rows), "rows )")
