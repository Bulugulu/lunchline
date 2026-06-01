"""Render docs/prompt-log.md to a publication-quality PDF.

Markdown -> styled HTML (deck aesthetic: Inter, navy headings) -> real PDF
with selectable text and page numbers, via headless Chromium's print pipeline.

Usage:
    python scripts/build_promptlog_pdf.py docs/prompt-log.md deliverables/prompt-log-appendix.pdf
"""
import sys
import tempfile
from pathlib import Path

import markdown
from playwright.sync_api import sync_playwright

TEMPLATE = """<!doctype html>
<html lang="en"><head><meta charset="utf-8">
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');
:root {{ --navy:#0A2540; --ink:#1a1a1a; --slate:#6B7280; --rule:#E5E7EB; --red:#C8102E; }}
* {{ box-sizing:border-box; }}
body {{ font-family:'Inter',-apple-system,sans-serif; color:var(--ink); font-size:10.5pt;
       line-height:1.55; margin:0; }}
.cover {{ border-bottom:2px solid var(--navy); padding-bottom:14px; margin-bottom:22px; }}
.cover .firm {{ font-size:9pt; letter-spacing:0.22em; text-transform:uppercase; color:var(--navy); font-weight:700; }}
.cover h1 {{ font-size:22pt; color:var(--navy); font-weight:500; letter-spacing:-0.02em; margin:10px 0 6px; }}
.cover .meta {{ font-size:9.5pt; color:var(--slate); }}
h1 {{ font-size:13pt; color:var(--navy); font-weight:600; margin:22px 0 4px;
      padding-top:10px; border-top:1px solid var(--rule); }}
h2 {{ font-size:12pt; color:var(--navy); font-weight:600; margin:18px 0 4px;
      page-break-after:avoid; }}
h3 {{ font-size:10.5pt; color:var(--navy); font-weight:600; margin:12px 0 3px; }}
p {{ margin:5px 0; }}
strong {{ color:var(--ink); font-weight:600; }}
em {{ color:var(--slate); }}
a {{ color:#2563eb; text-decoration:none; }}
code {{ background:#F1F3F5; padding:1px 4px; border-radius:3px; font-size:9pt;
        font-family:'SF Mono',Consolas,monospace; color:var(--navy); }}
ul,ol {{ margin:5px 0 5px 0; padding-left:20px; }}
li {{ margin:2px 0; }}
hr {{ border:none; border-top:1px solid var(--rule); margin:18px 0; }}
table {{ border-collapse:collapse; width:100%; font-size:9.5pt; margin:8px 0; }}
th,td {{ border:1px solid var(--rule); padding:5px 8px; text-align:left; }}
th {{ background:var(--navy); color:#fff; font-weight:600; }}
h2 {{ page-break-inside:avoid; }}
</style></head>
<body>
<div class="cover">
  <div class="firm">Lunchline Partners &middot; Case Study</div>
  <h1>AI Prompt Log &amp; Workflow Appendix</h1>
  <div class="meta">Aviv Sheriff &middot; how AI was used across the project &mdash; tools, prompts that worked, and where it helped or hurt</div>
</div>
{body}
</body></html>"""

FOOTER = (
    '<div style="font-family:Inter,sans-serif;font-size:8pt;color:#6B7280;'
    'width:100%;padding:0 0.6in;display:flex;justify-content:space-between;">'
    '<span>Lunchline Partners Case Study &middot; AI Prompt Log</span>'
    '<span>Page <span class="pageNumber"></span> / <span class="totalPages"></span></span>'
    "</div>"
)


def main() -> None:
    src = Path(sys.argv[1])
    out = Path(sys.argv[2])
    out.parent.mkdir(parents=True, exist_ok=True)

    md_text = src.read_text(encoding="utf-8")
    # The cover block supplies the title + subtitle, so strip the markdown's
    # own leading H1 and the first italic subtitle line to avoid duplication.
    lines = md_text.splitlines()
    i = 0
    while i < len(lines) and lines[i].strip() == "":
        i += 1
    if i < len(lines) and lines[i].startswith("# "):
        i += 1
        while i < len(lines) and lines[i].strip() == "":
            i += 1
        if i < len(lines) and lines[i].lstrip().startswith("*"):
            i += 1
    md_text = "\n".join(lines[i:])
    body = markdown.markdown(
        md_text, extensions=["extra", "sane_lists", "nl2br"]
    )
    html = TEMPLATE.format(body=body)

    with tempfile.TemporaryDirectory() as td:
        tmp_html = Path(td) / "promptlog.html"
        tmp_html.write_text(html, encoding="utf-8")
        with sync_playwright() as p:
            browser = p.chromium.launch()
            page = browser.new_page()
            page.goto(tmp_html.resolve().as_uri(), wait_until="networkidle")
            page.wait_for_timeout(800)
            page.pdf(
                path=str(out),
                format="Letter",
                print_background=True,
                display_header_footer=True,
                header_template="<div></div>",
                footer_template=FOOTER,
                margin={"top": "0.7in", "bottom": "0.8in", "left": "0.75in", "right": "0.75in"},
            )
            browser.close()
    print(f"wrote {out}")


if __name__ == "__main__":
    main()
