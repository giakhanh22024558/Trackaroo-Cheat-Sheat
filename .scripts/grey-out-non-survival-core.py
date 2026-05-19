"""
Grey out (+ remove text from) all cells in dfd-survival-core.drawio that are NOT
related to Survival Core.

KEEP COLOR + TEXT (in-scope cells):
  - Survival Core processes (MOB-2001 to MOB-2007) and the MOB_CORE container
  - CORE_BARRIER (Immutable Separation Boundary)
  - Data stores Survival Core reads/writes: SQL (MOB-3002), HAZ_CACHE (MOB-3005), MAP_CACHE (MOB-3004)
  - External entities Survival Core directly touches:
      · HW_GNSS (MOB-0001)            — runtime position fix
      · EXT-9001a Basemap (Mapbox)    — pre-journey tile source
      · CBE-7001 Tile Server / CDN    — pre-journey baked tiles
      · SYN-7001 Firestore            — background sync source for HAZ_CACHE (only allowed FB ingress)
  - DFD_LEGEND (the overlay legend cell)

GREY OUT + EMPTY TEXT (out-of-scope cells):
  Everything else — EXT_DATA other inputs · all CBE compute/DB · OCS · SYN container ·
  MOB_APP + sub-features · MOB_G2/CAL/MTT · FCACHE · PRO_LOG · HW_BLE/WIFI/SAT · CMS · …

Grey style applied:
  - fillColor = #f5f5f5  (very light grey)
  - strokeColor = #bdbdbd
  - fontColor = #bdbdbd
  - strokeWidth = 1
  - Other style properties (shape, container, dashed, rounded, arcSize, etc.) preserved
"""
import re
from pathlib import Path

DRAWIO = Path(r"C:\Users\Admin\Desktop\Trackagroo local management\diagrams\3-flows\data-flow\dfd-survival-core.drawio")

# Cells to KEEP as-is (Survival Core scope + direct touchpoints + legend)
KEEP_IDS = {
    "52",   # EXT-9001a Basemap (Mapbox · pre-journey to BUNDLE)
    "71",   # CBE-7001 Tile Server / CDN (pre-journey baked tiles)
    "85",   # SYN-7001 Firestore (background sync to HAZ_CACHE — only allowed FB ingress)
    "96",   # CORE_BARRIER (Immutable Separation Boundary)
    "97",   # MOB-2000 Survival Core container
    "98",   # MOB-2001 NAV
    "99",   # MOB-2002 BT
    "100",  # MOB-2003 HT
    "101",  # MOB-2004 SOS
    "102",  # MOB-2005 EVT
    "103",  # MOB-2006 SAP
    "104",  # MOB-2007 BUNDLE
    "108",  # MOB-3002 SQL (Survival Core Data + Comms Queue)
    "110",  # MOB-3005 HAZ_CACHE
    "111",  # MOB-3004 MAP_CACHE
    "113",  # MOB-0001 HW_GNSS
    "DFD_LEGEND",
    "0", "1",  # drawio root cells (system)
}

# Numeric ID range present in this file (architecture cells)
# Will iterate IDs 50..118 + DFD_LEGEND; anything not in KEEP_IDS gets greyed.
ALL_CELL_IDS = [str(i) for i in range(50, 119)] + ["DFD_LEGEND"]

GREY_FILL = "#f5f5f5"
GREY_STROKE = "#bdbdbd"
GREY_FONT = "#bdbdbd"


def restyle_to_grey(style: str) -> str:
    """
    Rewrite a drawio style string to grey-out colors while preserving
    shape/container/dashed/rounded/etc. attributes.
    """
    # Parse style string "key=value;key=value;..." into ordered dict
    parts = [p for p in style.split(";") if p]
    props = {}
    order = []
    for part in parts:
        if "=" in part:
            k, v = part.split("=", 1)
            if k not in props:
                order.append(k)
            props[k] = v
        else:
            # bare attribute (no =) — keep as-is using key=part marker
            if part not in props:
                order.append(part)
            props[part] = None

    # Override color-related properties
    props["fillColor"] = GREY_FILL
    props["strokeColor"] = GREY_STROKE
    props["fontColor"] = GREY_FONT
    props["strokeWidth"] = "1"
    # Add to order if newly introduced
    for k in ("fillColor", "strokeColor", "fontColor", "strokeWidth"):
        if k not in order:
            order.append(k)

    # Rebuild
    out = []
    for k in order:
        v = props[k]
        if v is None:
            out.append(k)
        else:
            out.append(f"{k}={v}")
    return ";".join(out) + ";"


def process(content: str) -> tuple[str, int, int]:
    """Returns (new_content, n_greyed, n_kept)."""
    n_greyed = 0
    n_kept = 0

    for cid in ALL_CELL_IDS:
        # Match the opening <mxCell ...> tag for this id
        pattern = re.compile(
            r'(<mxCell id="' + re.escape(cid) + r'") value="[^"]*" style="([^"]*)"'
        )
        m = pattern.search(content)
        if not m:
            continue

        if cid in KEEP_IDS:
            n_kept += 1
            continue

        old_style = m.group(2)
        new_style = restyle_to_grey(old_style)
        # Replace value with empty string + new style
        replacement = f'{m.group(1)} value="" style="{new_style}"'
        content = content[:m.start()] + replacement + content[m.end():]
        n_greyed += 1

    return content, n_greyed, n_kept


content = DRAWIO.read_text(encoding="utf-8")
new_content, n_greyed, n_kept = process(content)
DRAWIO.write_text(new_content, encoding="utf-8")

print(f"GREYED OUT (+ text removed) : {n_greyed} cells")
print(f"KEPT (in Survival Core scope): {n_kept} cells")
