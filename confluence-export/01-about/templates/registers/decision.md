# Decision Register — Template

> **Parent:** [Templates index](../_index.md)
> **Sheet name (Drive):** `[CMP-5026] Register — Decision`
> **Authority:** DCA-5026 §7 (live registers, PD continuous access) · CMP-5026 §6.10.2 (Technical Decision Record + weekly status integration)
> **Owner:** Tech Lead (Dinh Ba Trung) · co-maintained by PM

## Purpose

Live record of **all material technical decisions** taken during Phase 1 — architecture choices, SDK selections, data-model changes, deviations from reference mechanisms, process decisions. Each material decision must be both recorded here AND communicated in the weekly status report (per CMP §6.10.2).

> *"A decision that is not recorded has not been made for governance purposes."* — CMP §6.10.2

## Schema — compact (9 columns)

| Col | Type | Required | Sample value | Notes |
|---|---|---|---|---|
| `decision_id` | DEC-NNN | Y | `DEC-001` | Sequential, never reused |
| `date` | YYYY-MM-DD | Y | `2026-05-29` | When decision was taken |
| `category` | Architecture / SDK / Data model / UX / Process / Other | Y | `Architecture` | Drives "significant" flag (per CMP §6.10.2: architecture · SDK · data model · spec deviation → require immediate PD notification) |
| `decision` | Text | Y | `Adopt Mapbox GL Flutter SDK with offline OSM vector-tile bundle for navigation` | The decision in 1 sentence |
| `rationale` | Text | Y | `Only SDK meeting BPS cold-start ≤6s in PoC · native offline tile bundle · matches FSD §4.1 mandate. Alternatives considered: Google Maps SDK (no offline), MapLibre (immature offline tiles).` | Why this over alternatives — keep alternatives inline |
| `taken_by` | PD / Slitigenz Tech Lead / Joint | Y | `Joint (PD + Tech Lead)` | Accountability |
| `affected` | Modules / sprints / features impacted | Y | `EPIC-001 Navigation · All map renders · Sprint 2+` | Scope of impact |
| `pd_notified` | Y/N + date | Y | `Y — 2026-05-30` | **Mandatory for significant categories** (architecture · SDK · data model · deviation). Tracks compliance with CMP §6.10.2 immediate-notification rule |
| `status` | Proposed / Approved / Superseded | Y | `Approved` | When superseded → new DEC-NNN, link in rationale of new row; keep old row as audit |

> **Append-only:** never overwrite a row. Decisions evolve via new DEC entries that supersede old ones — never edit historical decisions.

## What counts as "material" / when to log

Per CMP §6.10.2 + DCA §7:

| Category | Examples | Significance |
|---|---|---|
| **Architecture** | Dual-layer split · CAL design · component boundaries | **Significant** → immediate PD written notification |
| **SDK** | Mapbox · Firebase · Flutter package choice | **Significant** → immediate PD notification (especially stack departures) |
| **Data model** | Schema changes · field additions · classification (Local-Only vs Syncable) | **Significant** → immediate PD notification |
| **Spec deviation** | Any deviation from authority stack reference mechanism | **Significant** → immediate PD notification |
| UX | Component library choices · interaction patterns | Material — log + weekly status |
| Process | Branch model · code review process · CI choice | Material — log + weekly status |

> **Rule:** if you're unsure whether a decision is "material", **log it anyway**. Over-logging is cheap; under-logging is a delivery-management failure.

## Maintenance requirements

| Requirement | Source | What it means |
|---|---|---|
| Live + continuously accessible to PD | DCA §7 | Drive sheet shared view-only with `imoore@trackaroosystems.com` from Week 1 |
| All material decisions in writing | DCA §7 + CMP §6.10.2 | No verbal decision creates obligation. If discussed in a meeting, log here after with reference to minutes |
| Immediate PD notification for "significant" categories | CMP §6.10.2 | Email to PD same-day; log decision in register; reference notification email in `pd_notified` cell |
| All decisions communicated in weekly status | CMP §6.10.2 | Weekly status §4 "Decisions required / taken" must reference new DEC rows for the reporting week |

## Reporting integration

### Weekly Status Report (CMP §6.6.1)

Every Friday by 17:00 ICT, list **new + changed decisions this week** in the status report:
- §4 "Decisions required" — for decisions awaiting PD input (`status=Proposed`)
- §4 (or §1 Progress) — for decisions taken this week (`status=Approved`, new this week)

Cross-reference each `decision_id`.

### Architecture & Technical Review (CMP §6.5.1)

At each fortnightly Architecture & Tech Review meeting, walk through `status=Proposed` decisions for PD confirmation, and recent `status=Approved` ones for awareness.

## Cross-register flows

A decision can trigger downstream register entries:

```
Decision (DEC-NNN)
  ├─ if requires_variation → Change register (CHG-NNN) → Variation Proposal (VAR-NNN)
  ├─ if introduces new SDK → SDK register (SDK-NNN) + Dependency register (DEP-NNN)
  ├─ if uses AI tool → AI-tool register (AI-NNN)
  └─ if creates new risk → Risk register (RISK-NNN)
```

When a downstream entry is created, note the `decision_id` in its source/rationale field for traceability.

## Audit + handover

- **§22 Audit Rights** — Client may request the register at any time. Slitigenz must respond within 5 BD.
- **Schedule 7 Handover** — Decision register is part of the mandatory handover pack on completion or termination — provides the "why" behind every architectural/technical choice.

## Transparency mandate

> Material decisions must be surfaced + logged at the time they are taken, not retroactively.
>
> Logging a decision weeks after the fact (especially a significant one) is treated the same as not logging it — both prevent PD from exercising clarification or variation rights at the time the decision could still be reversed cheaply.
