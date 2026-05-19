"""
Add CBE-6005 pipeline_run_history cylinder to CBE_DB in trackaroo-phase1-architecture.drawio.

PREEMPTIVE STRUCTURAL COMMIT per user direction — cell visually marked PROVISIONAL
(dashed border + dim fill + warning badge in label) to signal client confirmation
needed on design-decision S2 (Pipeline run history backend choice).

Triggered by OCS-4202 audit (TrackIQ Scoring Operations spec mandates ≥90 day
pipeline run history storage; current architecture has no explicit cylinder).

Changes:
  1. Resize CBE-6001/6002/6003/6004 from 161w → 126w to fit 5 cylinders in 720w container
  2. Add new CBE-6005 cell with provisional styling (dashed border + dim grey fill + warning badge)
"""
import re
from pathlib import Path

DRAWIO = Path(r"G:\.shortcut-targets-by-id\1fqaX3DE_KT88tT7ElgewcBM0bKzTvkZp\TRACKAROO 2026 RFT Phase 1\9 Docs\trackaroo-phase1-architecture.drawio")

# Position math (CBE_DB container = 720w · 5 cells × 126w + 4 gaps × 15 = 690 + 30 padding = 720)
POSITIONS = {
    "RAW":       15,   # CBE-6001 raw_ingested_tracks
    "QUEUE":     156,  # CBE-6002 track_review_queue
    "PROD":      297,  # CBE-6003 production_tracks
    "SYS_AUDIT": 438,  # CBE-6004 system_audit_log
    "RUN_HIST":  579,  # CBE-6005 pipeline_run_history (NEW · PROVISIONAL)
}
NEW_WIDTH = 126

# Provisional style — dashed border + dim fill + warning font color
# Same shape (cylinder3) as siblings but visually distinct as PROVISIONAL
PROVISIONAL_STYLE = (
    "shape=cylinder3;whiteSpace=wrap;html=1;boundedLbl=1;backgroundOutline=1;size=10;"
    "fillColor=#fff8e1;"             # Pale amber fill (signals attention)
    "strokeColor=#f57c00;"           # Orange stroke (warning color)
    "strokeWidth=1.5;"
    "dashed=1;dashPattern=6 3;"      # Distinct dash pattern
    "fontSize=10;spacing=5;"
    "fontColor=#e65100;"             # Orange text matches stroke
)

# Label with provisional badge
PROVISIONAL_VALUE = (
    "&lt;i&gt;CBE-6005&lt;/i&gt; &#183; &lt;b&gt;pipeline_run_history&lt;/b&gt;&lt;br/&gt;"
    "&lt;span style=&quot;background-color:#ffe082;color:#000;padding:1px 4px;"
    "font-size:8px;&quot;&gt;PROVISIONAL &#183; S2 PENDING&lt;/span&gt;"
)

content = DRAWIO.read_text(encoding="utf-8")

# Step 1: resize existing 4 cylinders + reposition
n_resized = 0
for cell_id, new_x in POSITIONS.items():
    if cell_id == "RUN_HIST":
        continue  # New cell — handled in Step 2

    # Match the cell's mxGeometry — keep y=50, h=80, change x and w
    pattern = re.compile(
        r'(<mxCell id="' + re.escape(cell_id) + r'"[^>]*>\s*'
        r'<mxGeometry x=")\d+(" y="\d+" width=")\d+(" height="\d+"[^/]*/>\s*</mxCell>)'
    )
    replacement = rf'\g<1>{new_x}\g<2>{NEW_WIDTH}\g<3>'
    new_content, n = pattern.subn(replacement, content)
    if n > 0:
        content = new_content
        n_resized += n
    else:
        print(f"  WARN: cell {cell_id} geometry not matched")

# Step 2: insert new CBE-6005 cell as child of CBE_DB (parent="CBE_DB")
# Insert right after the SYS_AUDIT cell to keep visual ordering
sys_audit_end = re.compile(
    r'(<mxCell id="SYS_AUDIT"[^>]*>\s*'
    r'<mxGeometry x="\d+" y="\d+" width="\d+" height="\d+"[^/]*/>\s*</mxCell>)'
)

new_cell_xml = (
    f'\n                <mxCell id="RUN_HIST" value="{PROVISIONAL_VALUE}" '
    f'style="{PROVISIONAL_STYLE}" vertex="1" parent="CBE_DB">\n'
    f'                    <mxGeometry x="{POSITIONS["RUN_HIST"]}" y="50" '
    f'width="{NEW_WIDTH}" height="80" as="geometry"/>\n'
    f'                </mxCell>'
)

new_content, n_added = sys_audit_end.subn(r'\g<1>' + new_cell_xml, content, count=1)
if n_added == 0:
    raise SystemExit("Could not find SYS_AUDIT cell to insert after")

DRAWIO.write_text(new_content, encoding="utf-8")
print(f"Resized {n_resized}/4 existing CBE_DB cylinders to {NEW_WIDTH}w")
print(f"Added {n_added} new cell: CBE-6005 pipeline_run_history (PROVISIONAL)")
