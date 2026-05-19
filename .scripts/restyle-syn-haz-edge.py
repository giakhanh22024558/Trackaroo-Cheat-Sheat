"""
Restyle e_syn_to_haz_cache edge in trackaroo-phase1-architecture.drawio.

Forces RED font color even when drawio HTML renderer might override fontColor
attribute. Wraps the entire label content in <font color='#c62828'> tag
(more universally respected by drawio HTML label parser than CSS color).

Keeps stroke purple (still a data-flow edge) — only label text goes red as
exception flag.
"""
import re
from pathlib import Path

DRAWIO = Path(r"G:\.shortcut-targets-by-id\1fqaX3DE_KT88tT7ElgewcBM0bKzTvkZp\TRACKAROO 2026 RFT Phase 1\9 Docs\trackaroo-phase1-architecture.drawio")

content = DRAWIO.read_text(encoding="utf-8")

# Match the e_syn_to_haz_cache cell's value="..." and style="..."
pattern = re.compile(
    r'<mxCell id="e_syn_to_haz_cache" value="[^"]*" style="([^"]*)"'
)

# Wrap whole label in <font color='#c62828'> for reliable color override
# (drawio HTML renderer respects <font color> attribute even when fontColor
# style is otherwise overridden by inner <b>/<i> tags)
new_value = (
    "&lt;font color=&#39;#c62828&#39;&gt;"
    "&lt;b&gt;cached hazard data&lt;/b&gt;&lt;br/&gt;"
    "&lt;i&gt;(Firebase ingress EXCEPTION per &#167;7 &#183; "
    "TTL refill &#183; sync-when-online only)&lt;/i&gt;"
    "&lt;/font&gt;"
)


def restyle(m):
    style = m.group(1)
    # Ensure fontColor is red (belt-and-suspenders with <font> tag)
    style = re.sub(r'fontColor=#[0-9a-fA-F]+', 'fontColor=#c62828', style)
    if 'fontColor' not in style:
        style += 'fontColor=#c62828;'
    return f'<mxCell id="e_syn_to_haz_cache" value="{new_value}" style="{style}"'


new_content, n = pattern.subn(restyle, content)

if n == 0:
    raise SystemExit("Edge e_syn_to_haz_cache not found")

DRAWIO.write_text(new_content, encoding="utf-8")
print(f"Restyled {n} edge: value wrapped in <font color=red>, fontColor=#c62828 forced")
