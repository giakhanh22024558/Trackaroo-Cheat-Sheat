"""
Strip excess conditions from component badges in trackaroo-phase1-architecture.drawio.

Keeps: ID + Name + minimal architectural classification (sync type · tier · sensitivity)
       + Option A critical items (Wi-Fi battery · Satellite future purpose)

Strips: operational metrics, range numbers, throughput descriptions, use case lists,
        detailed conditions — these belong in subsystem detail docs.
"""
import re
from pathlib import Path

DRAWIO = Path(r"G:\.shortcut-targets-by-id\1fqaX3DE_KT88tT7ElgewcBM0bKzTvkZp\TRACKAROO 2026 RFT Phase 1\9 Docs\trackaroo-phase1-architecture.drawio")

# (cell_id, new_value) — new value contains only minimal text
UPDATES = {
    # ─── Hardware (MOB_HW) ─────────────────────────────────
    "HW_GNSS":   "<i>MOB-0001</i> · <b>GNSS Sensor</b>",
    "HW_BLE":    "<i>MOB-0002</i> · <b>BLE Mesh Radio</b><br/><i>Tier 1 Primary</i>",
    # Option A critical: keep Wi-Fi battery numbers
    "HW_WIFI":   "<i>MOB-0003</i> · <b>Wi-Fi Direct / MPC</b><br/><i>Tier 1 Fallback · ≤0.8%/hr aggregate</i>",
    # Option A critical: keep Satellite future purpose
    "HW_SAT":    "<i>MOB-0004</i> · <b>Satellite Relay</b>&nbsp;<span style=\"background-color:#ffe082;color:#000;padding:1px 4px;font-size:9px;\">PHASE 2</span><br/><i>Future: BackTrack Emergency Escrow</i>",

    # ─── Data stores (MOB_DATA) ────────────────────────────
    "FCACHE":    "<i>MOB-3001</i> · <b>Firestore Local Cache</b><br/><i>[CLOUD SYNC]</i>",
    "SQL":       "<i>MOB-3002</i> · <b>Encrypted SQLite + WAL</b><br/><i>[LOCAL-ONLY]</i>",
    "PRO_LOG":   "<i>MOB-3003</i> · <b>Professional Incident Log</b><br/><i>[APP 3 SENSITIVE · CONSENT-GATED SYNC]</i>",
    "MAP_CACHE": "<i>MOB-3004</i> · <b>Map Tile Cache</b><br/><i>[Mapbox SDK native]</i>",
    "HAZ_CACHE": "<i>MOB-3005</i> · <b>HazTrack Overlay Cache</b><br/><i>[Firebase-cache-only · TTL]</i>",

    # ─── SQLITE_STORE sub-container title (simplified) ────
    "SQLITE_STORE": "<b>Encrypted SQLite + WAL Store</b> · <i>Slitigenz unified</i>",
}

content = DRAWIO.read_text(encoding='utf-8')
updated = 0
not_found = []

def html_escape(s):
    """Escape HTML attributes for mxCell value attribute (drawio format)."""
    return s.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;').replace('"', '&quot;')

for cell_id, new_value in UPDATES.items():
    escaped = html_escape(new_value)
    # Match the value="..." attribute on this cell
    pattern = re.compile(
        r'(<mxCell id="' + re.escape(cell_id) + r'" value=")[^"]*(")',
        re.DOTALL
    )
    new_content, n = pattern.subn(rf'\g<1>{escaped}\g<2>', content)
    if n == 0:
        not_found.append(cell_id)
    else:
        content = new_content
        updated += n

DRAWIO.write_text(content, encoding='utf-8')

print(f"Updated {updated}/{len(UPDATES)} cell values")
if not_found:
    print(f"NOT FOUND: {not_found}")
