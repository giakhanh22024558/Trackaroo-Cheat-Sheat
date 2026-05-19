"""
Restructure MOB layer in trackaroo-phase1-architecture.drawio:
1. Change MOB_G2 parent from MOB_APP → MOB (becomes standalone row)
2. Delete APP_DIVIDER cell (no longer needed since MOB_G2 is outside MOB_APP)

This script must run BEFORE retile-architecture.py · retile only touches
geometry, not parent or cell deletion.

After this script + retile, the MOB layer will have 4 rows:
  Row 1: MOB_APP + CORE_BARRIER + MOB_CORE (top)
  Row 2: MOB_G2 standalone (Comms & Transport · full width)
  Row 3: MOB_DATA (full width)
  Row 4: MOB_HW (full width)
"""
import re
from pathlib import Path

DRAWIO = Path(r"C:/Users/Admin/Desktop/Trackagroo local management/diagrams/1-overview/trackaroo-phase1-architecture.drawio")

content = DRAWIO.read_text(encoding="utf-8")

# Step 1: change MOB_G2 parent from MOB_APP → MOB
# Match the MOB_G2 cell · update parent attribute
mob_g2_pattern = re.compile(
    r'(<mxCell id="MOB_G2"[^>]*?)parent="MOB_APP"([^>]*?>)'
)
new_content, n_parent = mob_g2_pattern.subn(r'\g<1>parent="MOB"\g<2>', content)
print(f"MOB_G2 parent change: {n_parent} match")

# Step 2: delete APP_DIVIDER cell entirely (full mxCell block)
divider_pattern = re.compile(
    r'\s*<mxCell id="APP_DIVIDER"[^>]*?>\s*'
    r'<mxGeometry[^/]*?(?:/>|>.*?</mxGeometry>)\s*'
    r'</mxCell>',
    re.DOTALL,
)
new_content2, n_divider = divider_pattern.subn("", new_content)
print(f"APP_DIVIDER deletion: {n_divider} match")

DRAWIO.write_text(new_content2, encoding="utf-8")
print(f"\nDone · run retile-architecture.py next to apply new geometry.")
