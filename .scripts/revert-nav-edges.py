"""
Revert NAV component-level edges from trackaroo-phase1-architecture.drawio.
Restores the original layer-level edges per V4 rule.

DELETE 7 component-level edges added by wire-nav-edges.py:
  e_basemap_to_bundle · e_cbe_dist_to_bundle · e_bundle_to_mapcache
  e_mapcache_to_nav · e_gnss_to_nav · e_nav_to_sql · e_nav_to_evt

ADD BACK 3 original layer-level edges:
  e_ext_to_mob_core         EXT_DATA → MOB_CORE
  e_cbe_dist_to_mob_core    CBE_DISTRIBUTION → MOB_CORE
  e_gnss_to_core            HW_GNSS → MOB_CORE
"""
import re
from pathlib import Path

DRAWIO = Path(r"G:\.shortcut-targets-by-id\1fqaX3DE_KT88tT7ElgewcBM0bKzTvkZp\TRACKAROO 2026 RFT Phase 1\9 Docs\trackaroo-phase1-architecture.drawio")

PURPLE_DATA = ('style="endArrow=classic;html=1;edgeStyle=orthogonalEdgeStyle;'
               'rounded=0;jettySize=auto;orthogonalLoop=1;dashed=1;dashPattern=2 3;'
               'strokeColor=#6a1b9a;strokeWidth=2;fontColor=#6a1b9a;fontSize=11;'
               'labelBackgroundColor=#ffffff;"')

DELETE_EDGE_IDS = [
    "e_basemap_to_bundle",
    "e_cbe_dist_to_bundle",
    "e_bundle_to_mapcache",
    "e_mapcache_to_nav",
    "e_gnss_to_nav",
    "e_nav_to_sql",
    "e_nav_to_evt",
]

RESTORE_EDGES = [
    ("e_ext_to_mob_core",
     "&lt;b&gt;basemap tiles&lt;/b&gt;&lt;br/&gt;&lt;i&gt;(pre-journey)&lt;/i&gt;",
     "EXT_DATA", "MOB_CORE"),
    ("e_cbe_dist_to_mob_core",
     "&lt;b&gt;baked tiles + manifest&lt;/b&gt;&lt;br/&gt;&lt;i&gt;(pre-journey)&lt;/i&gt;",
     "CBE_DISTRIBUTION", "MOB_CORE"),
    ("e_gnss_to_core",
     "&lt;b&gt;GNSS position fix&lt;/b&gt;&lt;br/&gt;&lt;i&gt;(continuous · used by NAV, BackTrack, SOS)&lt;/i&gt;",
     "HW_GNSS", "MOB_CORE"),
]

content = DRAWIO.read_text(encoding='utf-8')

# Step 1: delete the 7 component-level edges
deleted = 0
for eid in DELETE_EDGE_IDS:
    pattern = re.compile(
        r'\s*<mxCell id="' + re.escape(eid) + r'"[^>]*?>\s*'
        r'<mxGeometry[^/]*?(?:/>|>.*?</mxGeometry>)\s*'
        r'</mxCell>',
        re.DOTALL
    )
    new_content, n = pattern.subn('', content)
    if n:
        content = new_content
        deleted += n
    else:
        print(f"  WARN: edge '{eid}' not found (may already be removed)")

# Step 2: insert restored layer-level edges before </root> of Architecture page
arch_start = content.find('<diagram id="trackaroo-arch"')
arch_end = content.find('</diagram>', arch_start)
root_close_idx = content.rfind('</root>', arch_start, arch_end)

restored_xml = ''
for eid, value, source, target in RESTORE_EDGES:
    restored_xml += (
        f'                <mxCell id="{eid}" value="{value}" '
        f'{PURPLE_DATA} parent="1" source="{source}" target="{target}" edge="1">\n'
        f'                    <mxGeometry relative="1" as="geometry"/>\n'
        f'                </mxCell>\n'
    )

content = content[:root_close_idx] + restored_xml + content[root_close_idx:]
DRAWIO.write_text(content, encoding='utf-8')

print(f"DELETED {deleted}/{len(DELETE_EDGE_IDS)} component-level edges")
print(f"RESTORED {len(RESTORE_EDGES)} layer-level edges")
