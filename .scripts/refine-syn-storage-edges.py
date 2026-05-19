"""
Refine SYN → MOB_DATA generic edge into per-store edges.

V4 storage exception (extended to SYN): which MOB-3000 component receives
Firebase ingress matters for Firebase Independence audit. Only FCACHE and
HAZ_CACHE accept FB push; SQL/PRO_LOG/MAP_CACHE must NOT.

DELETE 1 generic edge:
  e_syn_to_mob_data    SYN → MOB_DATA  "scores · PCRs · profiles · cached hazard data"

ADD 2 per-store edges:
  e_syn_to_fcache      SYN → FCACHE     scores · PCRs · profiles (auto-sync · Firestore SDK)
  e_syn_to_haz_cache   SYN → HAZ_CACHE  cached hazard data (Firebase ingress EXCEPTION per §7)
"""
import re
from pathlib import Path

DRAWIO = Path(r"G:\.shortcut-targets-by-id\1fqaX3DE_KT88tT7ElgewcBM0bKzTvkZp\TRACKAROO 2026 RFT Phase 1\9 Docs\trackaroo-phase1-architecture.drawio")

PURPLE_DATA = ('style="endArrow=classic;html=1;edgeStyle=orthogonalEdgeStyle;'
               'rounded=0;jettySize=auto;orthogonalLoop=1;dashed=1;dashPattern=2 3;'
               'strokeColor=#6a1b9a;strokeWidth=2;fontColor=#6a1b9a;fontSize=11;'
               'labelBackgroundColor=#ffffff;"')

DELETE_EDGE_IDS = ["e_syn_to_mob_data"]

NEW_EDGES = [
    ("e_syn_to_fcache",
     "&lt;b&gt;scores · PCRs · profiles&lt;/b&gt;&lt;br/&gt;&lt;i&gt;(auto-sync · Firestore SDK)&lt;/i&gt;",
     "SYN", "FCACHE"),
    ("e_syn_to_haz_cache",
     "&lt;b&gt;cached hazard data&lt;/b&gt;&lt;br/&gt;&lt;i&gt;(Firebase ingress EXCEPTION per §7 · TTL refill)&lt;/i&gt;",
     "SYN", "HAZ_CACHE"),
]

content = DRAWIO.read_text(encoding="utf-8")

# Step 1: delete old generic edge
deleted = 0
for eid in DELETE_EDGE_IDS:
    pattern = re.compile(
        r'\s*<mxCell id="' + re.escape(eid) + r'"[^>]*?>\s*'
        r'<mxGeometry[^/]*?(?:/>|>.*?</mxGeometry>)\s*'
        r'</mxCell>',
        re.DOTALL,
    )
    new_content, n = pattern.subn("", content)
    if n:
        content = new_content
        deleted += n
    else:
        print(f"  WARN: edge '{eid}' not found")

# Step 2: insert new edges before </root> of Architecture page
arch_start = content.find('<diagram id="trackaroo-arch"')
arch_end = content.find('</diagram>', arch_start)
root_close_idx = content.rfind('</root>', arch_start, arch_end)

new_xml = ""
for eid, value, source, target in NEW_EDGES:
    new_xml += (
        f'                <mxCell id="{eid}" value="{value}" '
        f'{PURPLE_DATA} parent="1" source="{source}" target="{target}" edge="1">\n'
        f'                    <mxGeometry relative="1" as="geometry"/>\n'
        f'                </mxCell>\n'
    )

content = content[:root_close_idx] + new_xml + content[root_close_idx:]
DRAWIO.write_text(content, encoding="utf-8")

print(f"DELETED {deleted}/{len(DELETE_EDGE_IDS)} generic SYN→MOB_DATA edge")
print(f"INSERTED {len(NEW_EDGES)} per-store SYN edges")
