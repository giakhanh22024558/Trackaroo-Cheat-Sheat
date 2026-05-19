"""
Replace layer-level MOB_APP/MOB_CORE ↔ MOB_DATA edges with per-store edges
in trackaroo-phase1-architecture.drawio.

V4 EXCEPTION (storage relationships only): show which layer touches which
MOB-3000 component to make data-integrity boundaries explicit. All other
layer ↔ layer edges remain group-level per V4.

DELETE 2 generic edges:
  e_mob_app_data    MOB_APP ↔ MOB_DATA "R/W app data"
  e_mob_core_data   MOB_CORE ↔ MOB_DATA "R/W core data"

ADD 6 per-store edges:
  Application Layer ↔ stores:
    MOB_APP ↔ FCACHE      R/W app data (profiles · presets · PCR drafts)
    MOB_APP ↔ SQL         R/W Comms Queue (CAL outbound · per M0f)
    MOB_APP ↔ PRO_LOG     R/W Pro tier incidents (APP 3 sensitive · FA Pro)

  Survival Core ↔ stores:
    MOB_CORE ↔ SQL        R/W Core data (breadcrumbs · SOS · events · anchors)
    MOB_CORE ↔ MAP_CACHE  R/W tile bundles (BUNDLE writes · NAV reads)
    HAZ_CACHE → MOB_CORE  Reads hazard overlays (HT runtime · one-direction)
"""
import re
from pathlib import Path

DRAWIO = Path(r"G:\.shortcut-targets-by-id\1fqaX3DE_KT88tT7ElgewcBM0bKzTvkZp\TRACKAROO 2026 RFT Phase 1\9 Docs\trackaroo-phase1-architecture.drawio")

# Bidirectional solid grey (matches existing e_mob_app_data / e_mob_core_data style)
BIDIR_STYLE = ('style="endArrow=classic;startArrow=classic;html=1;'
               'edgeStyle=orthogonalEdgeStyle;rounded=0;jettySize=auto;'
               'orthogonalLoop=1;strokeColor=#555555;strokeWidth=1.5;'
               'fontSize=11;labelBackgroundColor=#ffffff;"')

# Unidirectional solid grey (for HAZ_CACHE → MOB_CORE one-way read)
UNIDIR_STYLE = ('style="endArrow=classic;html=1;'
                'edgeStyle=orthogonalEdgeStyle;rounded=0;jettySize=auto;'
                'orthogonalLoop=1;strokeColor=#555555;strokeWidth=1.5;'
                'fontSize=11;labelBackgroundColor=#ffffff;"')

# Old generic edges to delete
DELETE_EDGE_IDS = [
    "e_mob_app_data",
    "e_mob_core_data",
]

# New per-store edges (id, value_html, style, source, target)
NEW_EDGES = [
    # ─── Application Layer ↔ stores ───
    ("e_mob_app_to_fcache",
     "&lt;b&gt;R/W app data&lt;/b&gt;&lt;br/&gt;&lt;i&gt;(profiles · presets · PCR drafts)&lt;/i&gt;",
     BIDIR_STYLE, "MOB_APP", "FCACHE"),
    ("e_mob_app_to_sql",
     "&lt;b&gt;R/W Comms Queue&lt;/b&gt;&lt;br/&gt;&lt;i&gt;(CAL outbound · per M0f)&lt;/i&gt;",
     BIDIR_STYLE, "MOB_APP", "SQL"),
    ("e_mob_app_to_prolog",
     "&lt;b&gt;R/W Pro tier incidents&lt;/b&gt;&lt;br/&gt;&lt;i&gt;(APP 3 sensitive · FA Pro)&lt;/i&gt;",
     BIDIR_STYLE, "MOB_APP", "PRO_LOG"),

    # ─── Survival Core ↔ stores ───
    ("e_mob_core_to_sql",
     "&lt;b&gt;R/W Core data&lt;/b&gt;&lt;br/&gt;&lt;i&gt;(breadcrumbs · SOS · events · anchors)&lt;/i&gt;",
     BIDIR_STYLE, "MOB_CORE", "SQL"),
    ("e_mob_core_to_mapcache",
     "&lt;b&gt;R/W tile bundles&lt;/b&gt;&lt;br/&gt;&lt;i&gt;(BUNDLE writes · NAV reads)&lt;/i&gt;",
     BIDIR_STYLE, "MOB_CORE", "MAP_CACHE"),
    ("e_haz_to_mob_core",
     "&lt;b&gt;Reads hazard overlays&lt;/b&gt;&lt;br/&gt;&lt;i&gt;(HT runtime · local-only)&lt;/i&gt;",
     UNIDIR_STYLE, "HAZ_CACHE", "MOB_CORE"),
]


content = DRAWIO.read_text(encoding="utf-8")

# Step 1: delete old generic edges
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
for eid, value, style, source, target in NEW_EDGES:
    new_xml += (
        f'                <mxCell id="{eid}" value="{value}" '
        f'{style} parent="1" source="{source}" target="{target}" edge="1">\n'
        f'                    <mxGeometry relative="1" as="geometry"/>\n'
        f'                </mxCell>\n'
    )

content = content[:root_close_idx] + new_xml + content[root_close_idx:]
DRAWIO.write_text(content, encoding="utf-8")

print(f"DELETED {deleted}/{len(DELETE_EDGE_IDS)} generic layer-to-MOB_DATA edges")
print(f"INSERTED {len(NEW_EDGES)} per-store edges")
