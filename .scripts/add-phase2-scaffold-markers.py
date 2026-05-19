"""
Apply Phase 2 Scaffold Zone visibility per spec (Maximal scope · M0p).

Changes:
  1. HW_SAT label — add exact "Inactive in Phase 1." text
  2. EXT_GPS label — add exact "Inactive in Phase 1." text
  3. BT cell — add "P2 ESCROW SCAFFOLD · Inactive in Phase 1." badge
  4. CAL cell — add "satReady=FALSE · Inactive in Phase 1." badge
  5. Insert new edge HW_SAT → MOB_G2 (dashed grey · "Phase 2 pathway · Inactive in Phase 1.")

Note RT-09 ID collision · deferred per M0q · this script does NOT reference
RT-09 in compliance text · only describes the mandate.
"""
import re
from pathlib import Path

DRAWIO = Path(r"C:/Users/Admin/Desktop/Trackagroo local management/diagrams/1-overview/trackaroo-phase1-architecture.drawio")

# Phase 2 badge style (amber background)
P2_BADGE_OPEN = ('&lt;span style=&quot;background-color:#ffe082;color:#000;'
                 'padding:1px 4px;font-size:9px;&quot;&gt;')
P2_SCAFFOLD_OPEN = ('&lt;span style=&quot;background-color:#ffe082;color:#000;'
                    'padding:1px 4px;font-size:8px;&quot;&gt;')
BADGE_CLOSE = '&lt;/span&gt;'

# ── New cell values ──────────────────────────────────────────────────────────

# HW_SAT: add exact "Inactive in Phase 1." mandatory text
HW_SAT_NEW_VALUE = (
    "&lt;i&gt;MOB-0004&lt;/i&gt; · &lt;b&gt;Satellite Relay&lt;/b&gt;&amp;nbsp;"
    f"{P2_BADGE_OPEN}PHASE 2{BADGE_CLOSE}"
    "&lt;br/&gt;&lt;b&gt;Inactive in Phase 1.&lt;/b&gt;&lt;br/&gt;"
    "&lt;i&gt;Future: BackTrack Emergency Escrow&lt;/i&gt;"
)

# EXT_GPS: same mandatory text
EXT_GPS_NEW_VALUE = (
    "&lt;i&gt;EXT-9006&lt;/i&gt; · &lt;b&gt;External GPS&lt;/b&gt;&amp;nbsp;"
    f"{P2_BADGE_OPEN}PHASE 2{BADGE_CLOSE}"
    "&lt;br/&gt;&lt;b&gt;Inactive in Phase 1.&lt;/b&gt;&lt;br/&gt;"
    "&lt;i&gt;Trimble · Bad Elf (Pro tier)&lt;/i&gt;"
)

# BT: add Phase 2 escrow scaffold badge
BT_NEW_VALUE = (
    "&lt;i&gt;MOB-2002&lt;/i&gt; · &lt;b&gt;BackTrack™&lt;/b&gt;&lt;br/&gt;"
    f"{P2_SCAFFOLD_OPEN}P2 ESCROW SCAFFOLD · Inactive in Phase 1.{BADGE_CLOSE}"
)

# CAL: add satReady scaffold badge
CAL_NEW_VALUE = (
    "&lt;i&gt;MOB-1101&lt;/i&gt; · &lt;b&gt;Comms Abstraction Layer&lt;/b&gt;&lt;br/&gt;"
    f"{P2_SCAFFOLD_OPEN}satReady = FALSE · Inactive in Phase 1.{BADGE_CLOSE}"
)

# Phase 2 pathway edge (HW_SAT → MOB_G2) · grey dashed
NEW_PATHWAY_EDGE = (
    '                <mxCell id="e_hw_sat_to_mob_g2" '
    'value="&lt;i&gt;Phase 2 pathway · Inactive in Phase 1.&lt;/i&gt;" '
    'style="endArrow=classic;html=1;edgeStyle=orthogonalEdgeStyle;'
    'rounded=0;jettySize=auto;orthogonalLoop=1;dashed=1;dashPattern=5 3;'
    'strokeColor=#9e9e9e;strokeWidth=1.5;fontColor=#616161;fontSize=10;'
    'labelBackgroundColor=#ffffff;" '
    'edge="1" parent="1" source="HW_SAT" target="MOB_G2">\n'
    '                    <mxGeometry relative="1" as="geometry"/>\n'
    '                </mxCell>\n'
)


def update_cell_value(content, cell_id, new_value):
    pattern = re.compile(
        r'(<mxCell id="' + re.escape(cell_id) + r'" value=")[^"]*(")'
    )
    return pattern.subn(rf'\g<1>{new_value}\g<2>', content)


content = DRAWIO.read_text(encoding="utf-8")

n_updated = 0
for cell_id, new_value in [
    ("HW_SAT", HW_SAT_NEW_VALUE),
    ("EXT_GPS", EXT_GPS_NEW_VALUE),
    ("BT", BT_NEW_VALUE),
    ("CAL", CAL_NEW_VALUE),
]:
    content, n = update_cell_value(content, cell_id, new_value)
    if n:
        n_updated += n
        print(f"  Updated {cell_id}")
    else:
        print(f"  WARN: {cell_id} not found")

# Add edge if not exists
if 'id="e_hw_sat_to_mob_g2"' in content:
    print("  Edge e_hw_sat_to_mob_g2 already exists · skipping insert")
else:
    # Insert before </root> of first diagram (Architecture page)
    root_close = content.rfind('</root>', 0, content.find('</diagram>'))
    if root_close == -1:
        raise SystemExit("</root> not found")
    content = content[:root_close] + NEW_PATHWAY_EDGE + content[root_close:]
    print("  Inserted edge: HW_SAT -> MOB_G2 (Phase 2 pathway)")

DRAWIO.write_text(content, encoding="utf-8")
print(f"\n{n_updated} cells updated · pathway edge added")
