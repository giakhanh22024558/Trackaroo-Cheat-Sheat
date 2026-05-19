"""
Retile the Architecture page of trackaroo-phase1-architecture.drawio with
uniform tight spacing.

- Removes constraint / compliance / performance banners (now living in spec docs)
- Updates only <mxGeometry> for vertex cells (by id)
- Edges + styles + values left untouched
"""
import re
import sys
from pathlib import Path

DRAWIO = Path(r"G:\.shortcut-targets-by-id\1fqaX3DE_KT88tT7ElgewcBM0bKzTvkZp\TRACKAROO 2026 RFT Phase 1\9 Docs\trackaroo-phase1-architecture.drawio")

# ---------------------------------------------------------------------------
# Banner / constraint cells to DELETE from the Architecture page.
# These textual constraints belong in spec documents — diagrams should be
# structural / relational only.
# ---------------------------------------------------------------------------
DELETE = [
    "EXT_MANDATE",       # Authority-Origin Mandate
    "COMPLIANCE",        # CBE RT-09
    "TILE_COST_GOV",     # Tile Cost Governance (inside CBE_DISTRIBUTION)
    "SYN_COMPLIANCE",    # Firebase Isolation V-12/V-13
    "CORE_COMPLIANCE",   # Survival Core compliance
    "NAV_PERF",          # NAV Performance Targets
]

# ---------------------------------------------------------------------------
# Geometry table (x, y, w, h) per cell id, AFTER banner removal.
# Container heights re-computed since they no longer contain banners.
# ---------------------------------------------------------------------------
# ---------------------------------------------------------------------------
# Inter-layer spacing tunables.
# Bigger gaps = more room for edge labels + future relationships.
# ---------------------------------------------------------------------------
LAYER_GAP_V = 60        # vertical gap between stacked layers
LAYER_GAP_H = 50        # horizontal gap CBE ↔ OCS in row 2
TOP_MARGIN  = 20        # page top margin

# Computed layer y-positions (cascading)
y_ext   = TOP_MARGIN
ext_h   = 290
y_row2  = y_ext + ext_h + LAYER_GAP_V              # CBE + OCS
row2_h  = 530                                       # max(CBE=530, OCS=485)
y_syn   = y_row2 + row2_h + LAYER_GAP_V
syn_h   = 205
y_mob   = y_syn + syn_h + LAYER_GAP_V
mob_h   = 790   # 4 rows: top (App+Core · 200h) · MOB_G2 standalone (160h) · MOB_DATA (145h) · MOB_HW (130h)
y_cms   = y_mob + mob_h + LAYER_GAP_V
cms_h   = 145

PAGE_HEIGHT = y_cms + cms_h + TOP_MARGIN

# ---------------------------------------------------------------------------
# Page width expanded 1780 → 2100 to accommodate Survival Core single-row
# layout (7 components × 165w + gaps). All top-level layers grow proportionally.
# ---------------------------------------------------------------------------
LAYER_W = 2100

# CBE & OCS horizontal positions — centred in wider page
cbe_w   = 750
ocs_w   = 585
combined_row2 = cbe_w + LAYER_GAP_H + ocs_w        # 1385
x_cbe   = (LAYER_W - combined_row2) // 2 + 20      # roughly centred (~358)
x_ocs   = x_cbe + cbe_w + LAYER_GAP_H

GEO = {
    # ========== EXT layer (no EXT_MANDATE) ==========
    "EXT":              (20, y_ext, LAYER_W, ext_h),
    "EXT_DATA":         (15, 50, 375, 225),
    "EXT_BASEMAP":      (15, 35, 165, 80),
    "EXT_TRACKDATA":    (195, 35, 165, 80),
    "EXT_DEM":          (15, 130, 165, 80),
    "EXT_HAZARD":       (195, 130, 165, 80),
    # EXT_HW back to "External peripherals only" — built-in GNSS moved to MOB_HW (on-device hardware)
    "EXT_HW":           (405, 50, 195, 225),
    "EXT_LORA":         (15, 35, 165, 80),     # Tier 2 LoRa peripheral (separate device, BLE-paired)
    "EXT_GPS":          (15, 130, 165, 80),    # Phase 2 external high-accuracy GPS dongle (inert)

    # ========== CBE layer (no COMPLIANCE banner) ==========
    # Smart fill-width applied: 4 components × 161w + 3×15 gap = 689 in 690 inner width
    "CBE":              (x_cbe, y_row2, cbe_w, 530),
    "CBE_COMPUTE":      (15, 50, 720, 145),
    "INGEST":           (15, 50, 161, 80),     # fill: 4 components in 720w container
    "DEM":              (191, 50, 161, 80),
    "SCORE":            (367, 50, 161, 80),
    "TILE":             (543, 50, 161, 80),
    "CBE_DB":           (15, 210, 720, 145),
    "RAW":              (15, 50, 161, 80),     # fill: 4 cylinders, uncapped (161 < CYLINDER_MAX 400)
    "QUEUE":            (191, 50, 161, 80),
    "PROD":             (367, 50, 161, 80),
    "SYS_AUDIT":        (543, 50, 161, 80),    # CBE-6004 immutable audit log, 7yr retention
    "CBE_DISTRIBUTION": (15, 370, 720, 145),    # no TILE_COST_GOV inside
    "CBE_CDN":          (278, 50, 165, 80),     # single component → bounded 165w, centered ((720-165)/2=278)

    # ========== OCS layer ==========
    # Smart fill-width: 2-component row fills (555w → 255 each), 3-component rows already fill at 165 each
    "OCS":              (x_ocs, y_row2, ocs_w, 485),
    "OCS_USER":         (15, 50, 555, 130),
    "ADMIN":            (15, 35, 255, 80),     # fill: 2 components in 555w (525 inner - 15 gap)/2 = 255
    "BETAADMIN":        (285, 35, 255, 80),    # fill cont.
    "OCS_CONTENT":      (15, 195, 555, 130),
    "HAZADMIN":         (15, 35, 165, 80),     # already fills at 165 (3 components)
    "TIQADMIN":         (195, 35, 165, 80),
    "PCRADMIN":         (375, 35, 165, 80),
    "OCS_GRADE":        (15, 340, 555, 130),
    "TDGA_TEXT":        (15, 35, 165, 80),     # already fills
    "FACA":             (195, 35, 165, 80),
    "AUDIT":            (375, 35, 165, 80),

    # ========== SYN layer (no SYN_COMPLIANCE banner) ==========
    # Single cylinder → bounded at MAX 400 (cylinder cap) and centered in expanded container
    "SYN":              (20, y_syn, LAYER_W, syn_h),
    "FIRESTORE":        ((LAYER_W - 400) // 2, 50, 400, 140),   # centered: (2100-400)/2 = 850

    # ========== MOB layer (MOB_CORE no longer has CORE_COMPLIANCE + NAV_PERF) ==========
    "MOB":              (20, y_mob, LAYER_W, mob_h),
    # ── Layout restructured 2026-05-19: MOB_G2 (Comms & Transport) moved OUT of
    # MOB_APP and made a STANDALONE row spanning full MOB width — positioned
    # between top row (App+Core) and MOB_DATA. Reflects CAL's role as
    # "buffer and gateway" serving BOTH App Layer (TrackMate) and (Phase-2)
    # Survival Core (BackTrack Emergency Escrow). Visual separation makes the
    # bridge role explicit.
    #
    # Row 1 · Application Layer + Survival Core side-by-side (h=200)
    "MOB_APP":          (15, 50, 720, 200),
    # Feature row: 4 components fill 720w container → 161w each + 15 gap, symmetric padding
    "TM":               (15, 50, 161, 80),
    "FA":               (191, 50, 161, 80),
    "PRESETS":          (367, 50, 161, 80),
    "PCRFW":            (543, 50, 161, 80),
    "CORE_BARRIER":     (750, 50, 30, 200),
    "MOB_CORE":         (795, 50, 1275, 200),
    # 7 components in single horizontal row — DATA-FLOW order:
    #   BUNDLE → NAV → BT → SAP → HT → SOS → EVT
    # (Bundle downloads tiles → NAV uses them → BT records breadcrumbs → SAP stores anchors
    #  → HT shows hazards → SOS triggers distress → EVT logs events)
    # 7 × 165w + 6 × 15 gap + 15 + 15 padding = 1275 (exactly fills container)
    "BUNDLE":           (15,   50, 165, 80),   # MOB-2007 · feeds NAV with regional tile bundles
    "NAV":              (195,  50, 165, 80),   # MOB-2001 · the navigation engine itself
    "BT":               (375,  50, 165, 80),   # MOB-2002 · records breadcrumbs while NAV runs
    "SAP":              (555,  50, 165, 80),   # MOB-2006 · stores safe anchor points
    "HT":               (735,  50, 165, 80),   # MOB-2003 · surfaces hazards to NAV
    "SOS":              (915,  50, 165, 80),   # MOB-2004 · emergency trigger
    "EVT":              (1095, 50, 165, 80),   # MOB-2005 · event log (sink for all of the above)

    # Row 2 · Comms & Transport standalone (full width below App+Core · above MOB_DATA)
    "MOB_G2":           (15, 280, LAYER_W - 30, 160),
    # CAL + MTT stacked vertically inside MOB_G2 · centered horizontally (bounded width)
    # MOB_G2 inner width = LAYER_W - 30 - 30 = 2040 · CAL bounded 400w centered: (2040-400)/2 = 820
    "CAL":              (820, 35, 400, 50),
    "MTT":              (820, 95, 400, 50),
    # FA_BASE (MOB-2008) REMOVED — per FRM-5126 sole authority, First Aid Reference
    # lives in Application Layer (MOB-1002). Universal Baseline content is pre-loaded
    # as immutable bundled asset, not a Survival Core structural component.
    # MOB_DATA moved from right column to BOTTOM ROW — spans full MOB width
    # to visually show it's a shared data layer that both Application Layer
    # and Survival Core can query (each via its own partitioned cylinder).
    "MOB_DATA":         (15, 470, LAYER_W - 30, 145),   # shifted up (MOB_G2 now in between)
    # Option γ hybrid: 3 outer elements (FCACHE | SQLite Store sub-container | MAP_CACHE)
    # FCACHE and MAP_CACHE = different tech (Firestore SDK / Mapbox SDK native), stay outside
    # SQLITE_STORE sub-container hosts SQL + PRO_LOG + HAZ_CACHE (Slitigenz unified)
    "FCACHE":           (15, 50, 280, 80),      # MOB-3001 Firestore SDK · [CLOUD SYNC]
    # SQLITE_STORE expanded 1100→1400 to use extra horizontal space
    "SQLITE_STORE":     (325, 25, 1400, 110),
    # Inside SQLITE_STORE (1400w): 3 cylinders, inner 1370, fill = (1370-30)/3 = 446w each
    "SQL":              (15,  30, 446, 80),     # MOB-3002 Survival Core Data + Comms Queue
    "PRO_LOG":          (476, 30, 446, 80),     # MOB-3003 Pro Incident Log · APP 3 sensitive
    "HAZ_CACHE":        (937, 30, 446, 80),     # MOB-3005 HazTrack Overlay Cache · Firebase ingress
    "MAP_CACHE":        (1755, 50, 280, 80),    # MOB-3004 Mapbox SDK · shifted right to follow SQLITE_STORE growth

    # ────────────────────────────────────────────────────────────────────────
    # MOB_HW · Device Hardware (bottom row of MOB layer)
    # Built-in sensors + transport radios on user's mobile device.
    # External peripherals (LoRa, External GPS) stay in EXT zone — they're separate physical devices.
    # ────────────────────────────────────────────────────────────────────────
    "MOB_HW":           (15, 645, LAYER_W - 30, 130),   # Full-width hardware layer · shifted up
    # 4 hardware components fill expanded 2070w: (2040 inner - 3*15 gap) / 4 = 498w each
    "HW_GNSS":          (15,   35, 498, 80),    # MOB-0001 GNSS Sensor (feeds NAV/BT/SOS)
    "HW_BLE":           (528,  35, 498, 80),    # MOB-0002 BLE Mesh Radio (Tier 1 Primary)
    "HW_WIFI":          (1041, 35, 498, 80),    # MOB-0003 Wi-Fi Direct / MPC (Tier 1 Fallback)
    "HW_SAT":           (1554, 35, 498, 80),    # MOB-0004 Satellite Relay [PHASE 2 inert]

    # ========== CMS layer ==========
    # Single component → bounded 200w, centered in 2100w
    "CMS":              (20, y_cms, LAYER_W, cms_h),
    "WEB":              ((LAYER_W - 200) // 2, 50, 200, 80),
}

content = DRAWIO.read_text(encoding='utf-8')

# Narrow scope to Architecture page only (so we don't touch Legend / CAL pages)
arch_start_re = re.compile(r'<diagram id="trackaroo-arch"[^>]*>')
arch_start_match = arch_start_re.search(content)
if not arch_start_match:
    sys.exit("Could not find Architecture page start")
arch_start = arch_start_match.end()
arch_end = content.find('</diagram>', arch_start)
if arch_end == -1:
    sys.exit("Could not find Architecture page end")

before = content[:arch_start]
arch_block = content[arch_start:arch_end]
after = content[arch_end:]

# ---------------------------------------------------------------------------
# Step 1: DELETE banner cells entirely
# ---------------------------------------------------------------------------
deleted = 0
for cell_id in DELETE:
    # Match a full <mxCell id="X" ...>...</mxCell> block (self-closing geometry inside)
    pattern = re.compile(
        r'\s*<mxCell id="' + re.escape(cell_id) + r'"[^>]*?>\s*'
        r'<mxGeometry [^/]*?/>\s*'
        r'</mxCell>',
        re.DOTALL
    )
    new_block, n = pattern.subn('', arch_block)
    if n == 0:
        print(f"DELETE: cell '{cell_id}' not found (might have been removed already)")
    else:
        arch_block = new_block
        deleted += n

# ---------------------------------------------------------------------------
# Step 2: UPDATE geometry for remaining cells
# ---------------------------------------------------------------------------
updates = 0
not_found = []
for cell_id, (x, y, w, h) in GEO.items():
    pattern = re.compile(
        r'(<mxCell id="' + re.escape(cell_id) + r'"[^>]*vertex="1"[^>]*>\s*)'
        r'<mxGeometry [^/]*?as="geometry"\s*/>',
        re.DOTALL
    )
    new_geom = f'<mxGeometry x="{x}" y="{y}" width="{w}" height="{h}" as="geometry"/>'
    new_arch, n = pattern.subn(r'\1' + new_geom, arch_block)
    if n == 0:
        not_found.append(cell_id)
    else:
        arch_block = new_arch
        updates += n

# ---------------------------------------------------------------------------
# Step 3: Update pageHeight in mxGraphModel header
# ---------------------------------------------------------------------------
page_height_re = re.compile(r'(pageWidth="1820"\s+pageHeight=")(\d+)(")')
new_arch_block, n_page = page_height_re.subn(rf'\g<1>{PAGE_HEIGHT}\g<3>', arch_block, count=1)
if n_page:
    arch_block = new_arch_block

new_content = before + arch_block + after
DRAWIO.write_text(new_content, encoding='utf-8')

print(f"DELETED {deleted}/{len(DELETE)} banner cells")
print(f"UPDATED {updates}/{len(GEO)} cell geometries")
print(f"PAGE HEIGHT set to {PAGE_HEIGHT}")
if not_found:
    print(f"NOT FOUND in update step: {not_found}")
