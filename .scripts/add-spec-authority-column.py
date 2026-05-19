"""
Add a "Spec Authority" column to every decision table in design-decisions.md.

Each decision is mapped to the most relevant spec document(s) in the
authority stack so that during proposal review we can trace the
governing doc for any choice.
"""
import re
from pathlib import Path

FILE = Path(r"C:\Users\Admin\Desktop\Trackagroo local management\research\design-decisions.md")

# Decision ID → Spec authority citation
AUTHORITIES = {
    # --- 1. Storage & Persistence ---
    "S1":  "**CDG-5126** (data governance) · **OCS-5026** (audit mandate)",
    "S2":  "**OCS-5026** · **TQP-5026** (pipeline test history)",
    "S3":  "**CDG-5126** · **VGD-5126** (vendor proposes)",
    "S4":  "**MAS-5126** (tile distribution)",
    "S5":  "**MAS-5126** (DEM source for terrain)",

    # --- 2. Backend Architecture ---
    "B1":  "**FSD-5126** ('decoupled service')",
    "B2":  "**FSD-5126** ('source-agnostic')",
    "B3":  "**MAS-5126** (tile architecture)",
    "B4":  "**MAS-5126** · **BPS-5126** (cost / device limits)",

    # --- 3. Mobile App ---
    "M0a": "**FRM-5126** (FA tier content model) · **PSB-5026** (Core scope)",
    "M0b": "**MAS-5126** · **FSD-5126** (Core decomposition)",
    "M1":  "**FSD-5126** · **VGD-5126**",
    "M2":  "**BPS-5126** (device matrix)",
    "M3":  "**MAS-5126** · **PSB-5026** (Phase 1 scope)",
    "M4":  "**Commercial Amendment 13 Apr 2026** · **VGD-5126**",
    "M5":  "**ESF-5026** (satellite prohibition) · **FSD-5126**",
    "M6":  "**UXS-5726** (UI behaviour) · **TQP-5026** (calibration)",
    "M7":  "**PSB-5026** (Phase 2 deferral)",
    "M8":  "**FSD-5126** · **PSB-5026**",

    # --- 4. Operations Console ---
    "O1":  "**OCS-5026** · **FSD-5126**",
    "O2":  "**CDG-5126** · **OCS-5026**",
    "O3":  "*Our visual choice — not spec'd*",
    "O4":  "**OCS-5026** (audit log retention mandate)",
    "O5":  "**OCS-5026** (pipeline history)",
    "O6":  "**OCS-5026** · **UXS-5726** (alert UX)",
    "O7":  "**OCS-5026** (Tester Mgmt module)",
    "O8":  "**HFG-5026** · **OCS-5026**",

    # --- 5. Sync & Firestore ---
    "F1":  "**CDG-5126** (Firebase isolation model)",
    "F2":  "**CDG-5126** · **VGD-5126**",
    "F3":  "**OSM-5026** (PCR framework) · **CDG-5126** (write-once)",

    # --- 6. Visual / Diagrammatic ---
    "V1":  "*N/A — visual style choice*",
    "V2":  "*N/A — visual style choice*",
    "V3":  "*N/A — visual style choice*",
    "V4":  "*N/A — visual style choice*",

    # --- 7. Compliance Interpretation ---
    "C1":  "**CDG-5126** · **ESF-5026** · **FSD-5126** (Core isolation)",
    "C2":  "**HFG-5026** · spec RT-09",
    "C3":  "**CDG-5126** V-12/V-13",
}

content = FILE.read_text(encoding='utf-8')
lines = content.split('\n')
new_lines = []
updates = 0
header_updates = 0
divider_updates = 0

ROW_RE = re.compile(r'^\|\s*([A-Z]\d+[a-z]?)\s*\|')
HEADER_RE = re.compile(r'^\| # \| Decision point \|')
DIVIDER_RE = re.compile(r'^\|---\|---\|---\|---\|---\|---\|---\|\s*$')

def append_col(line, value):
    """Insert a new column value before the final '|'."""
    parts = line.split('|')
    # Markdown rows have leading '' and trailing '' around the pipes
    if parts[-1].strip() == '':
        parts.insert(-1, f' {value} ')
    else:
        parts.append(f' {value} |')
    return '|'.join(parts)

for line in lines:
    # Header row
    if HEADER_RE.match(line):
        new_lines.append(append_col(line, 'Spec Authority'))
        header_updates += 1
        continue
    # Divider row right under a header
    if DIVIDER_RE.match(line):
        new_lines.append(append_col(line, '---'))
        divider_updates += 1
        continue
    # Data row
    m = ROW_RE.match(line)
    if m:
        row_id = m.group(1)
        if row_id in AUTHORITIES:
            new_lines.append(append_col(line, AUTHORITIES[row_id]))
            updates += 1
            continue
    new_lines.append(line)

FILE.write_text('\n'.join(new_lines), encoding='utf-8')

print(f"Header rows updated: {header_updates}")
print(f"Divider rows updated: {divider_updates}")
print(f"Data rows updated: {updates}/{len(AUTHORITIES)}")
missing = set(AUTHORITIES.keys()) - {ROW_RE.match(l).group(1) for l in lines if ROW_RE.match(l)}
if missing:
    print(f"WARNING: No row found for: {sorted(missing)}")
