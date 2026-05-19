"""
Convert e_ocs_content_to_syn from write-only to bidirectional R/W edge
in trackaroo-phase1-architecture.drawio.

Triggered by OCS-4203 audit (Gap #1): OCS modules need to READ from Firestore
for governance surfaces (PCR review/supersede · hazard metadata · audit log
queries). Previously only writes were modeled.

Changes:
  1. Style: add startArrow=classic (makes bidirectional)
  2. Value: expand label to include both R and W semantics
"""
import re
from pathlib import Path

DRAWIO = Path(r"G:\.shortcut-targets-by-id\1fqaX3DE_KT88tT7ElgewcBM0bKzTvkZp\TRACKAROO 2026 RFT Phase 1\9 Docs\trackaroo-phase1-architecture.drawio")

# New bidirectional label HTML-escaped for drawio mxCell value attribute
new_value = (
    "&lt;b&gt;R/W Firestore data&lt;/b&gt;&lt;br/&gt;"
    "&lt;i&gt;Writes: PCR updates &#183; cached hazard data &#183; "
    "audit log (OCS-5026 append-only &#183; 7yr)&lt;/i&gt;&lt;br/&gt;"
    "&lt;i&gt;Reads: PCRs (review/supersede surface) &#183; hazard metadata "
    "&#183; audit log queries&lt;/i&gt;"
)

content = DRAWIO.read_text(encoding="utf-8")

# Match the e_ocs_content_to_syn cell — capture value + style separately
pattern = re.compile(
    r'(<mxCell id="e_ocs_content_to_syn" value=")[^"]*(" style=")([^"]*)(")'
)


def update_edge(m):
    style = m.group(3)
    # Add startArrow=classic to make bidirectional (if not already present)
    if "startArrow" not in style:
        # Insert startArrow=classic right after endArrow=classic for consistency
        style = re.sub(r'(endArrow=classic;)', r'\1startArrow=classic;', style, count=1)
    return f'{m.group(1)}{new_value}{m.group(2)}{style}{m.group(4)}'


new_content, n = pattern.subn(update_edge, content)

if n == 0:
    raise SystemExit("Edge e_ocs_content_to_syn not found")

DRAWIO.write_text(new_content, encoding="utf-8")
print(f"Converted {n} edge to bidirectional: e_ocs_content_to_syn (now R/W)")
