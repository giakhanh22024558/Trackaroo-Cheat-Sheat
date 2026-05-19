"""
Delete orphan edge `id="2"` from trackaroo-phase1-architecture.drawio.

This edge was an accidental click-drag in the Drawio app:
  - Auto-generated short ID "2"
  - Empty label (value="")
  - Bidirectional solid grey style (default Drawio)
  - Source EXT_HW → Target MOB_DATA (no valid architectural pathway)

Per audit · no spec mandate supports a direct external-peripheral-to-local-data
edge. The legitimate path is EXT_HW → MOB_G2 (CAL queue) → MOB_G2 → SQL.
"""
import re
from pathlib import Path

DRAWIO = Path(r"C:/Users/Admin/Desktop/Trackagroo local management/diagrams/1-overview/trackaroo-phase1-architecture.drawio")

content = DRAWIO.read_text(encoding="utf-8")

# Match the full mxCell block for id="2" (edge with multi-line mxGeometry inside)
pattern = re.compile(
    r'\s*<mxCell id="2" value="" [^>]*?source="EXT_HW" target="MOB_DATA"[^>]*?>\s*'
    r'<mxGeometry[^>]*>\s*'
    r'(?:<Array[^>]*>.*?</Array>\s*)?'
    r'(?:<mxPoint[^/]*/>\s*)*'
    r'</mxGeometry>\s*'
    r'</mxCell>',
    re.DOTALL,
)

new_content, n = pattern.subn("", content)
if n == 0:
    raise SystemExit("Orphan edge id=2 not found · already deleted?")

DRAWIO.write_text(new_content, encoding="utf-8")
print(f"Deleted {n} orphan edge (id=2 · EXT_HW → MOB_DATA)")
