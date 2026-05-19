"""
Update e_ocs_content_to_syn edge label in trackaroo-phase1-architecture.drawio
to include OCS-4201 audit log writes (Gap #1 from OCS-4201 audit).

Before: "Publishes PCR updates + cached hazard data"
After:  "Publishes PCR updates + cached hazard data
         + Audit log writes (OCS-5026 append-only · 7yr)"

OCS-4201 HazTrack Feed Management writes operator-action audit entries to
Firestore append-only. Gap #2 (Firestore vs PostgreSQL CBE-6004 destination
ambiguity) deferred — blocked by existing design-decision S1.
"""
import re
from pathlib import Path

DRAWIO = Path(r"G:\.shortcut-targets-by-id\1fqaX3DE_KT88tT7ElgewcBM0bKzTvkZp\TRACKAROO 2026 RFT Phase 1\9 Docs\trackaroo-phase1-architecture.drawio")

content = DRAWIO.read_text(encoding="utf-8")

# New label HTML-escaped for drawio mxCell value attribute
new_value = (
    "&lt;b&gt;Publishes PCR updates&lt;/b&gt;&lt;br/&gt;"
    "+ cached hazard data&lt;br/&gt;"
    "+ Audit log writes (OCS-5026 append-only &#183; 7yr)"
)

# Match the e_ocs_content_to_syn cell's value="..." (cell ID per existing drawio)
# Searching by likely IDs — try a few patterns
patterns_to_try = [
    r'(<mxCell id="e_ocs_content_to_syn" value=")[^"]*(")',
    r'(<mxCell id="e_ocs_to_syn" value=")[^"]*(")',
]

n_total = 0
for pat in patterns_to_try:
    pattern = re.compile(pat)
    new_content, n = pattern.subn(rf'\g<1>{new_value}\g<2>', content)
    if n > 0:
        content = new_content
        n_total += n
        print(f"Matched pattern {pat[:50]}... · {n} edge updated")
        break

if n_total == 0:
    # Fallback: find by source="OCS_CONTENT" target="SYN"
    fallback = re.compile(
        r'(<mxCell id="[^"]+" value=")[^"]*("[^>]*source="OCS_CONTENT"[^>]*target="SYN")',
    )
    new_content, n = fallback.subn(rf'\g<1>{new_value}\g<2>', content)
    if n > 0:
        content = new_content
        n_total += n
        print(f"Matched via source/target attrs · {n} edge updated")

if n_total == 0:
    raise SystemExit("Could not find OCS_CONTENT -> SYN edge")

DRAWIO.write_text(content, encoding="utf-8")
print(f"Updated {n_total} edge label: now includes OCS audit log writes")
