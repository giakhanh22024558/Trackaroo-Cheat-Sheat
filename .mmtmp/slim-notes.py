"""Slim explanatory notes / prose from roadmap-milestones.md.
Keep only what visually conveys the plan: tables, gantts, checklists.
Drop: long paragraphs, blockquote notes, per-sprint Goal/Buffer/Detail prose,
B4 narrative prefix and Feature-tier bullets.
"""
from pathlib import Path

ROOT = Path(r"C:\Users\Admin\Desktop\Trackagroo local management")
FILE = ROOT / "confluence-export" / "01-about" / "02-roadmap-milestones.md"
c = FILE.read_text(encoding='utf-8')
orig_len = len(c)

# 1. Drop prose before Sprint->Gate table
c = c.replace(
    "### Sprint → Delivery goal → Client gate\n\nEach gate block now ends with a **dedicated stabilisation sprint** so feature work freezes ~2 weeks before the gate, leaving a managed risk buffer for validation/hardening/gate prep. Feature sprints are loaded harder (more parallel tracks) to absorb the pulled-forward work.\n\n",
    "### Sprint → Delivery goal → Client gate\n\n"
)

# 2. Drop blockquote after Sprint->Gate table
c = c.replace(
    "> **Gate blocks:** Sprint 0 → Discovery · Sprints 1–5 → Alpha · Sprints 6–10 → Beta-Ready · Sprint 11 → GA.\n> Day-level item durations in the per-sprint charts are **indicative** pending Story-level estimates; tracks run in parallel per the 8-workstream model.\n\n",
    ""
)

# 3. Slim Risk-buffer policy section
c = c.replace(
    "### Risk-buffer policy & parallelisation\n\n**Buffer policy — all feature work completes ~15 days before its gate:**\n\n",
    "### Risk-buffer policy\n\n"
)

# 4. Drop Discovery constraint blockquote
c = c.replace(
    "> ⚠️ **Discovery is the one constrained gate** — contract executes 29 May, gate is 15 Jun (17-day window), so a full 15-day buffer is impossible. We target foundation-complete by **10 Jun** with a **5-day acceptance buffer**. Mitigation: run all 10 foundation concerns **in parallel from day 1** (8 tracks), front-load D8/D9 audits.\n\n",
    ""
)

# 5. Drop Parallelisation prose
c = c.replace(
    "**Parallelisation:** pulled-forward work runs concurrently across the 8 tracks (see the `section` lanes in each sprint Gantt). Peak load S4 & S9 (8 features) fits 8 experts; hard dependencies still serialise within a track.\n\n",
    ""
)

# 6. Drop A2 colour convention blockquote
c = c.replace(
    "> 🎨 **Colour convention:** in every per-sprint Gantt, each `section` = one **Epic** (Sprint 0 = one **Topic**), so **all tasks of the same Epic/Topic share the same bar colour** within that chart. Non-feature activities (Legal, QA, Buffer, Release, Gate) keep their own sections. *(Mermaid cycles ~4 section colours per chart, so colours group within a chart; they are not guaranteed identical across different sprint charts.)*\n\n",
    ""
)

# 7. Drop Sprint 0 Goal/Buffer/Detail lines
c = c.replace(
    "### Sprint 0 — Foundation (29 May – 15 Jun) → Discovery Gate\n\n**Goal:** Foundation platform + 9 committed Discovery artefacts + companion website. No business features.\n**Buffer:** parallel build → foundation-complete 10 Jun; **11–15 Jun = artefact-acceptance buffer**. Validation via lab GPS-spoofing + Faraday (CLR-SLZ-001).\n**Detail:** full task list, Topic → Concern → AC breakdown in [B2](#b2-sprint-0-foundation-register) · committed artefact register in [B5](#b5-discovery-gate-deliverable-register).\n\n",
    "### Sprint 0 — Foundation (29 May – 15 Jun) → Discovery Gate\n\n"
)

# 8. Drop Sprint 1 Goal line
c = c.replace(
    "### Sprint 1 — SOS & Emergency Logging (16 – 27 Jun) → Alpha\n**Goal:** Safety-critical lead — SOS reaches acceptance first (Evidentiary Integrity early).\n\n",
    "### Sprint 1 — SOS & Emergency Logging (16 – 27 Jun) → Alpha\n\n"
)

# 9. Drop Sprint 5 "No new features" line
c = c.replace(
    "### Sprint 5 — 🛡️ STABILISATION buffer (11 – 22 Aug) → Alpha Gate\n**No new features** (Alpha freeze was 8 Aug). 14-day risk buffer: end-to-end Survival Core validation, legal/clinical close, hardening, gate evidence.\n\n",
    "### Sprint 5 — 🛡️ STABILISATION buffer (11 – 22 Aug) → Alpha Gate\n\n"
)

# 10. Drop Sprint 9 prose line
c = c.replace(
    "### Sprint 9 — OCS full + event-log + POI + Low-tier (6 – 17 Oct) → Beta-Ready · **feature freeze 17 Oct**\nAll remaining features land here (incl. the 3 Low-tier, pulled from S11) so the RC is **feature-complete by 17 Oct**.\n\n",
    "### Sprint 9 — OCS full + event-log + POI + Low-tier (6 – 17 Oct) → Beta-Ready · **feature freeze 17 Oct**\n\n"
)

# 11. Drop Sprint 10 "No new features" line
c = c.replace(
    "### Sprint 10 — 🛡️ STABILISATION buffer (20 – 30 Oct) → Beta-Ready Gate\n**No new features** (Beta freeze was 17 Oct). 13-day risk buffer: full validation suite + audits on the frozen RC.\n\n",
    "### Sprint 10 — 🛡️ STABILISATION buffer (20 – 30 Oct) → Beta-Ready Gate\n\n"
)

# 12. Drop Sprint 11 prose
c = c.replace(
    "### Sprint 11 — 🛡️ RELEASE buffer (31 Oct – 13 Nov) → GA Gate\n**No new features** — the RC is feature-complete since 17 Oct (S9). Pure release: regression on the frozen build, store submission, go/no-go. Maximum risk buffer for the hard commercial deadline.\n\n",
    "### Sprint 11 — 🛡️ RELEASE buffer (31 Oct – 13 Nov) → GA Gate\n\n"
)

# 13. Slim B4 prose
c = c.replace(
    "## B4. Delivery Gate & Priority\n\nPriority by earliest delivery gate (lower ID = higher priority). Companion mapping — not a backlog column (canonical Priority col G is filled on Story rows; Stories inherit Feature priority here).\n\n",
    "## B4. Delivery Gate & Priority\n\n"
)

# 14. Drop B4 locked-timeline paragraph + Feature-tiers bullets
c = c.replace(
    "Full locked timeline: **Contract Execution 29 May → Discovery 15 Jun → Alpha 22 Aug → Beta-Ready 30 Oct → GA 13 Nov 2026** (Slitigenz proposal §10.2 — `../../research/spec-docs/Slitigenz-Proposal-RFT5026.md`).\n\n**Feature tiers (mixed epics carry features at >1 gate):**\n\n- **High (25)** → Sprints 1–5: FEAT-001→005, 006→010, 011→014, 017→024, 025, 027, 028\n- **Medium (23)** → Sprints 6–10: FEAT-015, 026, 029→031, 033→038, 039→044, 045→049, 050\n- **Low (3)** → Sprint 11: FEAT-016 (breadcrumb export) · FEAT-032 (OCS analytics/config) · FEAT-051 (POI metadata)\n\n",
    ""
)

# Final cleanup: collapse triple newlines + dangling separators
import re
c = re.sub(r'\n{3,}', '\n\n', c)
c = c.rstrip() + '\n'

FILE.write_text(c, encoding='utf-8')
print(f'OK orig={orig_len} new={len(c)} delta={orig_len - len(c)}')
