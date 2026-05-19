"""
Update e_mob_app_to_sql edge label in trackaroo-phase1-architecture.drawio
to include PCR queue (Gap #1 from PCR audit).

Before: "R/W Comms Queue (CAL outbound · per M0f)"
After:  "R/W App-layer queues (CAL Comms · per M0f) + (PCR submissions · offline-queue-first)"

Both queues live in MOB-3002 SQL (Slitigenz unified) with different semantics:
  - CAL Comms Queue: Firebase-INDEPENDENT (peer mesh transport per M0f)
  - PCR Queue: Firebase-BOUND (offline-queue-first, syncs to Firestore when online)
"""
import re
from pathlib import Path

DRAWIO = Path(r"G:\.shortcut-targets-by-id\1fqaX3DE_KT88tT7ElgewcBM0bKzTvkZp\TRACKAROO 2026 RFT Phase 1\9 Docs\trackaroo-phase1-architecture.drawio")

content = DRAWIO.read_text(encoding="utf-8")

# New label HTML-escaped for drawio mxCell value attribute
# Option B (chosen): keep M0f reference + add "Firebase-independent" characterization
# so vendors reading the diagram understand the queue semantics without needing
# to consult design-decisions.md first
new_value = (
    "&lt;b&gt;R/W App-layer queues&lt;/b&gt;&lt;br/&gt;"
    "&lt;i&gt;(CAL Comms &#183; M0f Firebase-independent)&lt;br/&gt;"
    "+ (PCR submissions &#183; offline-queue-first)&lt;/i&gt;"
)

# Match the e_mob_app_to_sql cell's value="..."
pattern = re.compile(
    r'(<mxCell id="e_mob_app_to_sql" value=")[^"]*(")'
)

new_content, n = pattern.subn(rf'\g<1>{new_value}\g<2>', content)

if n == 0:
    raise SystemExit("Edge e_mob_app_to_sql not found")

DRAWIO.write_text(new_content, encoding="utf-8")
print(f"Updated {n} edge label (e_mob_app_to_sql): now includes PCR queue")
