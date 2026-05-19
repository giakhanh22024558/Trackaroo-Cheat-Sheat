"""
Wire NAV (MOB-2001) data-flow edges into trackaroo-phase1-architecture.drawio.

MODIFY 3 existing edges (re-source/re-target to component-level):
  e_ext_to_mob_core      → EXT_BASEMAP → BUNDLE   (basemap supply chain)
  e_cbe_dist_to_mob_core → CBE_DISTRIBUTION → BUNDLE  (baked TrackIQ tiles)
  e_gnss_to_core         → HW_GNSS → NAV          (deterministic position fix)

ADD 4 new edges:
  e_bundle_to_mapcache   BUNDLE → MAP_CACHE       (post-download write)
  e_mapcache_to_nav      MAP_CACHE → NAV          (runtime tile read)
  e_nav_to_sql           NAV → SQL                (session state · LOCAL-ONLY)
  e_nav_to_evt           NAV → EVT                (nav events)

All edges are dotted purple (data-payload style per CLAUDE.md visual rule).
"""
import re
from pathlib import Path

DRAWIO = Path(r"G:\.shortcut-targets-by-id\1fqaX3DE_KT88tT7ElgewcBM0bKzTvkZp\TRACKAROO 2026 RFT Phase 1\9 Docs\trackaroo-phase1-architecture.drawio")

PURPLE_DATA = ('style="endArrow=classic;html=1;edgeStyle=orthogonalEdgeStyle;'
               'rounded=0;jettySize=auto;orthogonalLoop=1;dashed=1;dashPattern=2 3;'
               'strokeColor=#6a1b9a;strokeWidth=2;fontColor=#6a1b9a;fontSize=11;'
               'labelBackgroundColor=#ffffff;"')

# (edge_id, value_html, source, target) — for new edges + atomic replacement of modified ones
NEW_EDGES = [
    ("e_basemap_to_bundle",
     "&lt;b&gt;Mapbox basemap tiles&lt;/b&gt;&lt;br/&gt;&lt;i&gt;(pre-journey)&lt;/i&gt;",
     "EXT_BASEMAP", "BUNDLE"),
    ("e_cbe_dist_to_bundle",
     "&lt;b&gt;baked TrackIQ tiles + manifest&lt;/b&gt;&lt;br/&gt;&lt;i&gt;(pre-journey)&lt;/i&gt;",
     "CBE_DISTRIBUTION", "BUNDLE"),
    ("e_bundle_to_mapcache",
     "&lt;b&gt;regional tile bundles&lt;/b&gt;&lt;br/&gt;&lt;i&gt;(write · post-download)&lt;/i&gt;",
     "BUNDLE", "MAP_CACHE"),
    ("e_mapcache_to_nav",
     "&lt;b&gt;OSM vector tiles&lt;/b&gt;&lt;br/&gt;&lt;i&gt;(runtime read · Mapbox SDK)&lt;/i&gt;",
     "MAP_CACHE", "NAV"),
    ("e_gnss_to_nav",
     "&lt;b&gt;GNSS position fix&lt;/b&gt;&lt;br/&gt;&lt;i&gt;(continuous · deterministic only&lt;br/&gt;no network / no dead-reckoning)&lt;/i&gt;",
     "HW_GNSS", "NAV"),
    ("e_nav_to_sql",
     "&lt;b&gt;nav session state · route plan&lt;/b&gt;&lt;br/&gt;&lt;i&gt;[LOCAL-ONLY · AES-256 · WAL]&lt;/i&gt;",
     "NAV", "SQL"),
    ("e_nav_to_evt",
     "&lt;b&gt;nav events&lt;/b&gt;&lt;br/&gt;&lt;i&gt;(session start/stop · destination · transitions)&lt;/i&gt;",
     "NAV", "EVT"),
]

# Old edge IDs to delete (they're replaced by component-level NEW_EDGES above)
DELETE_EDGE_IDS = [
    "e_ext_to_mob_core",
    "e_cbe_dist_to_mob_core",
    "e_gnss_to_core",
]

content = DRAWIO.read_text(encoding='utf-8')

# Step 1: delete old edges (atomic)
deleted = 0
for eid in DELETE_EDGE_IDS:
    # Match full mxCell block including its mxGeometry sub-block
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
        print(f"  WARN: edge '{eid}' not found")

# Step 2: insert new edges before </root></mxGraphModel></diagram> of Architecture page
# Find the Architecture page boundaries first
arch_start = content.find('<diagram id="trackaroo-arch"')
if arch_start == -1:
    raise SystemExit("Architecture page not found")
arch_end = content.find('</diagram>', arch_start)
if arch_end == -1:
    raise SystemExit("Architecture page end not found")

# Find the last </mxCell> inside Architecture page
# Insert new edges right before </root>
root_close_idx = content.rfind('</root>', arch_start, arch_end)
if root_close_idx == -1:
    raise SystemExit("</root> not found in Architecture page")

new_edge_xml = ''
for eid, value, source, target in NEW_EDGES:
    new_edge_xml += (
        f'                <mxCell id="{eid}" value="{value}" '
        f'{PURPLE_DATA} parent="1" source="{source}" target="{target}" edge="1">\n'
        f'                    <mxGeometry relative="1" as="geometry"/>\n'
        f'                </mxCell>\n'
    )

content = content[:root_close_idx] + new_edge_xml + content[root_close_idx:]

DRAWIO.write_text(content, encoding='utf-8')

print(f"DELETED {deleted}/{len(DELETE_EDGE_IDS)} old edges")
print(f"INSERTED {len(NEW_EDGES)} new edges")
