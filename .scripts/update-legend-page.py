"""
Atomically extend Legend page of master architecture diagram to document
ALL style conventions currently in use.

Adds:
  ARR_EDGE6 — Orange dashed consent-gated sync edge
  ARR_EDGE7 — Purple dotted data + red exception flag

  SEC_VARIANTS section with:
    VAR_SCAFFOLD_CELL    — White cell with grey dashed border + amber inline badge
    VAR_PROVISIONAL_CELL — Orange dashed cylinder + amber badge
    VAR_EXT_SUBGROUP     — Orange dashed container (EXT sub-grouping)
    VAR_BADGE_PHASE2     — Amber inline badge text examples

Also:
  Extends pageHeight 900 -> 1300
  Extends SEC_ARROWS height 430 -> 590
  Moves SEC_COLORS y=597 -> y=760
"""
import re
from pathlib import Path

DRAWIO = Path(r"C:/Users/Admin/Desktop/Trackagroo local management/diagrams/1-overview/trackaroo-phase1-architecture.drawio")

content = DRAWIO.read_text(encoding="utf-8")

# ── 1. Page height: only on the legend-page diagram ─────────────────────────
legend_start = content.find('<diagram id="legend-page"')
if legend_start < 0:
    raise SystemExit("legend-page diagram not found")
legend_end = content.find('</diagram>', legend_start)
legend_block = content[legend_start:legend_end]

new_block = legend_block.replace('pageHeight="900"', 'pageHeight="1300"', 1)
print("  pageHeight: 900 -> 1300")

# ── 2. Extend SEC_ARROWS height ─────────────────────────────────────────────
new_block = re.sub(
    r'(<mxCell id="SEC_ARROWS"[^>]*>\s*<mxGeometry x="620" y="110" width="540" height=")430(")',
    r'\g<1>590\g<2>',
    new_block,
)
print("  SEC_ARROWS height: 430 -> 590")

# ── 3. Insert new ARR_EDGE6 + ARR_EDGE7 entries after ARR_DESC5 ─────────────
NEW_ARROWS = '''                <mxCell id="ARR_A6" value="A" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#555555;fontSize=10;" parent="SEC_ARROWS" vertex="1">
                    <mxGeometry x="30" y="415" width="30" height="30" as="geometry"/>
                </mxCell>
                <mxCell id="ARR_B6" value="B" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#555555;fontSize=10;" parent="SEC_ARROWS" vertex="1">
                    <mxGeometry x="200" y="415" width="30" height="30" as="geometry"/>
                </mxCell>
                <mxCell id="ARR_EDGE6" value="&lt;b&gt;Consent-gated&lt;/b&gt;" style="endArrow=classic;html=1;edgeStyle=orthogonalEdgeStyle;rounded=0;dashed=1;dashPattern=5 3;strokeColor=#f57c00;strokeWidth=2;fontColor=#e65100;fontSize=10;labelBackgroundColor=#ffffff;" parent="SEC_ARROWS" source="ARR_A6" target="ARR_B6" edge="1">
                    <mxGeometry relative="1" as="geometry"/>
                </mxCell>
                <mxCell id="ARR_DESC6" value="&lt;b&gt;Orange dashed arrow&lt;/b&gt; — User-consent-gated sync (opt-in only).&lt;br/&gt;&lt;i&gt;Marks data flow that requires explicit user consent before activation. e.g. &quot;PRO_LOG → SYN&quot; (APP 3 opt-in PCR sync).&lt;/i&gt;" style="text;html=1;align=left;verticalAlign=middle;whiteSpace=wrap;fontSize=11;" parent="SEC_ARROWS" vertex="1">
                    <mxGeometry x="250" y="405" width="280" height="50" as="geometry"/>
                </mxCell>
                <mxCell id="ARR_A7" value="A" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#555555;fontSize=10;" parent="SEC_ARROWS" vertex="1">
                    <mxGeometry x="30" y="485" width="30" height="30" as="geometry"/>
                </mxCell>
                <mxCell id="ARR_B7" value="B" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#555555;fontSize=10;" parent="SEC_ARROWS" vertex="1">
                    <mxGeometry x="200" y="485" width="30" height="30" as="geometry"/>
                </mxCell>
                <mxCell id="ARR_EDGE7" value="&lt;b&gt;Data + §exception&lt;/b&gt;" style="endArrow=classic;html=1;edgeStyle=orthogonalEdgeStyle;rounded=0;dashed=1;dashPattern=2 3;strokeColor=#6a1b9a;strokeWidth=2;fontColor=#c62828;fontSize=10;labelBackgroundColor=#ffffff;fontStyle=1;" parent="SEC_ARROWS" source="ARR_A7" target="ARR_B7" edge="1">
                    <mxGeometry relative="1" as="geometry"/>
                </mxCell>
                <mxCell id="ARR_DESC7" value="&lt;b&gt;Purple dotted arrow + RED label&lt;/b&gt; — Data flow under a compliance exception clause.&lt;br/&gt;&lt;i&gt;Purple = data payload; red font flags that this path is normally prohibited but authorized by a numbered §exception. e.g. &quot;SYN → HAZ_CACHE&quot; (compliance-matrix §7 cache-only exception).&lt;/i&gt;" style="text;html=1;align=left;verticalAlign=middle;whiteSpace=wrap;fontSize=11;" parent="SEC_ARROWS" vertex="1">
                    <mxGeometry x="250" y="475" width="280" height="65" as="geometry"/>
                </mxCell>
'''

# Insert right after the ARR_DESC5 closing tag
anchor = '<mxCell id="ARR_DESC5"'
# Find the closing </mxCell> after the ARR_DESC5 opening
a5_start = new_block.find(anchor)
if a5_start < 0:
    raise SystemExit("ARR_DESC5 not found")
a5_close = new_block.find('</mxCell>', a5_start) + len('</mxCell>') + 1  # +1 for newline
new_block = new_block[:a5_close] + NEW_ARROWS + new_block[a5_close:]
print("  Inserted ARR_EDGE6 (consent-gated) + ARR_EDGE7 (data+exception)")

# ── 4. Shift SEC_COLORS down (y=597 -> y=760) ───────────────────────────────
new_block = re.sub(
    r'(<mxCell id="SEC_COLORS"[^>]*>\s*<mxGeometry x="40" y=")597(")',
    r'\g<1>760\g<2>',
    new_block,
)
print("  SEC_COLORS y: 597 -> 760")

# ── 5. Add SEC_VARIANTS section after SEC_COLORS closes ─────────────────────
# Find the closing </mxCell> for SEC_COLORS container — it's the LAST </mxCell> tag
# before </root>. We'll insert right before </root>.

NEW_SECTION = '''                <mxCell id="SEC_VARIANTS" value="&lt;b&gt;Cell Variants &amp;amp; Inline Badges&lt;/b&gt;&lt;br/&gt;&lt;i&gt;Border style + inline amber badge encode lifecycle / scaffold status&lt;/i&gt;" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#424242;strokeWidth=1.5;verticalAlign=top;fontSize=13;fontStyle=1;align=left;spacingLeft=10;spacingTop=6;container=1;collapsible=0;recursiveResize=0;expand=0;" parent="1" vertex="1">
                    <mxGeometry x="40" y="1080" width="1120" height="200" as="geometry"/>
                </mxCell>
                <mxCell id="VAR_SCAFFOLD_CELL" value="&lt;i&gt;MOB-1101&lt;/i&gt; · &lt;b&gt;Sample Component&lt;/b&gt;&lt;br/&gt;&lt;span style=&quot;background-color:#ffe082;color:#000;padding:1px 4px;font-size:8px;&quot;&gt;satReady = FALSE · Inactive in Phase 1.&lt;/span&gt;" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#555555;strokeWidth=1;dashed=1;dashPattern=3 2;fontSize=10;spacing=5;" parent="SEC_VARIANTS" vertex="1">
                    <mxGeometry x="20" y="60" width="220" height="60" as="geometry"/>
                </mxCell>
                <mxCell id="VAR_SCAFFOLD_DESC" value="&lt;b&gt;Phase 2 Scaffold cell&lt;/b&gt; — Live Phase 1 component with dormant Phase 2 hook.&lt;br/&gt;&lt;i&gt;Grey dashed border + amber inline badge. Badge MUST end with the exact text &quot;Inactive in Phase 1.&quot; (Placeholder Discipline #2). Used for: CAL (satReady=FALSE) · BT (P2 ESCROW SCAFFOLD).&lt;/i&gt;" style="text;html=1;align=left;verticalAlign=middle;whiteSpace=wrap;fontSize=11;" parent="SEC_VARIANTS" vertex="1">
                    <mxGeometry x="260" y="55" width="290" height="70" as="geometry"/>
                </mxCell>
                <mxCell id="VAR_PROVISIONAL_CELL" value="&lt;i&gt;CBE-6005&lt;/i&gt; · &lt;b&gt;sample_provisional_table&lt;/b&gt;&lt;br/&gt;&lt;span style=&quot;background-color:#ffe082;color:#000;padding:1px 4px;font-size:8px;&quot;&gt;PROVISIONAL · S2 PENDING&lt;/span&gt;" style="shape=cylinder3;whiteSpace=wrap;html=1;boundedLbl=1;backgroundOutline=1;size=10;fillColor=#fff8e1;strokeColor=#f57c00;strokeWidth=1.5;dashed=1;dashPattern=6 3;fontSize=10;spacing=5;fontColor=#e65100;" parent="SEC_VARIANTS" vertex="1">
                    <mxGeometry x="20" y="135" width="220" height="55" as="geometry"/>
                </mxCell>
                <mxCell id="VAR_PROVISIONAL_DESC" value="&lt;b&gt;Provisional / S2-pending cell&lt;/b&gt; — Data store reserved for Stage-2 commitment, schema-locked but not yet authoritative.&lt;br/&gt;&lt;i&gt;Orange dashed cylinder + amber &quot;PROVISIONAL · S2 PENDING&quot; badge. Used for: pipeline_run_history (CBE-6005).&lt;/i&gt;" style="text;html=1;align=left;verticalAlign=middle;whiteSpace=wrap;fontSize=11;" parent="SEC_VARIANTS" vertex="1">
                    <mxGeometry x="260" y="130" width="290" height="65" as="geometry"/>
                </mxCell>
                <mxCell id="VAR_EXT_SUBGROUP" value="&lt;b&gt;Sample Sub-group&lt;/b&gt; · &lt;i&gt;Orange dashed border&lt;/i&gt;" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#fff8e7;strokeColor=#e65100;strokeWidth=1;dashed=1;dashPattern=3 2;verticalAlign=top;fontSize=10;align=left;spacingLeft=6;spacingTop=3;container=1;collapsible=0;recursiveResize=0;expand=0;" parent="SEC_VARIANTS" vertex="1">
                    <mxGeometry x="580" y="60" width="220" height="60" as="geometry"/>
                </mxCell>
                <mxCell id="VAR_EXT_SUBGROUP_DESC" value="&lt;b&gt;EXTERNAL sub-grouping container&lt;/b&gt; — Sub-zone inside the External providers zone.&lt;br/&gt;&lt;i&gt;Pale-cream fill + orange dashed border. Used to cluster: Data Inputs (Mapbox · BOM · DEM) · External Peripherals (LoRa · ext-GPS).&lt;/i&gt;" style="text;html=1;align=left;verticalAlign=middle;whiteSpace=wrap;fontSize=11;" parent="SEC_VARIANTS" vertex="1">
                    <mxGeometry x="820" y="55" width="290" height="70" as="geometry"/>
                </mxCell>
                <mxCell id="VAR_BADGE_LIST" value="&lt;b&gt;Inline amber badge — text variants in use:&lt;/b&gt;&lt;br/&gt;• &lt;span style=&quot;background-color:#ffe082;color:#000;padding:1px 4px;font-size:9px;&quot;&gt;PHASE 2&lt;/span&gt; — Phase 2 hardware / actor (HW_SAT · EXT_GPS)&lt;br/&gt;• &lt;span style=&quot;background-color:#ffe082;color:#000;padding:1px 4px;font-size:8px;&quot;&gt;P2 ESCROW SCAFFOLD · Inactive in Phase 1.&lt;/span&gt; — BackTrack escrow schema hook&lt;br/&gt;• &lt;span style=&quot;background-color:#ffe082;color:#000;padding:1px 4px;font-size:8px;&quot;&gt;satReady = FALSE · Inactive in Phase 1.&lt;/span&gt; — CAL satReady flag hardcoded FALSE&lt;br/&gt;• &lt;span style=&quot;background-color:#ffe082;color:#000;padding:1px 4px;font-size:8px;&quot;&gt;PROVISIONAL · S2 PENDING&lt;/span&gt; — Provisional data store" style="text;html=1;align=left;verticalAlign=top;whiteSpace=wrap;fontSize=11;spacing=8;" parent="SEC_VARIANTS" vertex="1">
                    <mxGeometry x="580" y="130" width="530" height="60" as="geometry"/>
                </mxCell>
'''

# Insert NEW_SECTION right before </root> on the legend page
root_close = new_block.rfind('</root>')
if root_close < 0:
    raise SystemExit("</root> not found on legend page")
new_block = new_block[:root_close] + NEW_SECTION + new_block[root_close:]
print("  Inserted SEC_VARIANTS section")

# ── 6. Splice modified legend block back ────────────────────────────────────
content = content[:legend_start] + new_block + content[legend_end:]

DRAWIO.write_text(content, encoding="utf-8")
print("\nLegend page updated successfully.")
