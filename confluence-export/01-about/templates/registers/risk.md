# Risk Register — Template

> **Parent:** [Templates index](../_index.md)
> **Sheet name (Drive):** `[CMP-5026] Register — Risk`
> **Authority:** DCA-5026 §7 (live registers, PD continuous access) · CMP-5026 §6.6.1 (weekly status integration) · §6.7 (escalation pathway)
> **Owner:** Project Manager (Luong Gia Khanh)

## Purpose

Live record of all identified risks + blockers that could impact Phase 1 delivery. Mandatory governance + administrative tool maintained throughout the engagement.

## Schema — compact (7 columns)

Minimum field set per client mandate (severity · owner · mitigation status) + 4 fields for traceability and status filtering.

| Col | Type | Required | Sample value | Notes |
|---|---|---|---|---|
| `risk_id` | RISK-NNN | Y | `RISK-001` | Sequential, never reused |
| `date_raised` | YYYY-MM-DD | Y | `2026-06-01` | Traceability + weekly-status reference |
| `description` | Text | Y | `17-day Sprint 0 window = tightest gate · no slack for re-submission · all 8 tasks must clear PD on first review` | Plain language, 1–3 sentences |
| `severity` | Low / Medium / High / Critical | Y | `High` | **Client-mandated** — current severity |
| `owner` | Name + role | Y | `Luong Gia Khanh (PM)` | **Client-mandated** — accountable for mitigation |
| `mitigation_status` | Text | Y | `Front-load all 8 tasks from Day 1, parallel across 8 owners; foundation freeze Fri 5 Jun gives 3-BD polish window` | **Client-mandated** — current mitigation or proposed resolution |
| `status` | Open / Mitigating / Closed / Watch | Y | `Open` | Filters which rows appear in weekly status "Risks & Blockers" |

> **Append-only:** never overwrite a row; update severity/status/mitigation in place. Closed rows stay in the sheet for audit.

## Maintenance requirements

| Requirement | Source | What it means |
|---|---|---|
| Live + continuously accessible to PD | DCA §7 | Drive sheet shared view-only with `imoore@trackaroosystems.com` from Week 1 |
| Traceability of all significant risks | DCA §7 | Every weekly-status "Risks & Blockers" row must reference its `risk_id` in this register |
| All material decisions in writing | DCA §7 | Severity / mitigation updates → captured in this register, not just verbal |

## Reporting integration

### Weekly Status Report (CMP §6.6.1 · Section 3)

Every Friday by 17:00 ICT, copy active rows (`status` ∈ {Open, Mitigating, Watch}) into the **Risks & Blockers** section of [`templates/01-weekly-status-report.md`](../01-weekly-status-report.md) §3:

```
Risk / Blocker  | Severity | Owner | Mitigation | Status | New this week?
```

Cross-reference the `risk_id` so PD can drill back into the register.

### Gate Preparation Review (per gate)

For every gate (Alpha · Beta-Ready · GA), identify the **3 highest-risk schedule dependencies** from this register and propose a mitigation for each. Surface in the Gate Prep Review meeting.

## Escalation pathway (CMP §6.7)

| Severity | Required action |
|---|---|
| **SEV-1 / Critical** | Immediate written notify PD (within 2 hours business hours) AND log here. WhatsApp flag acceptable, followed by email + register entry within 1 hour. |
| **SEV-2 / High** | Written notify PD within 24 hours AND log here. |
| **SEV-3 / Medium** | Raise in weekly status + log here. |
| **SEV-4 / Low** | Log here (no separate notification required). |

> The register is the **primary tool** for the SEV-4 Early Warning Protocol. For SEV-1/2 the register entry is required IN ADDITION to immediate written notification — not instead of it.

## Audit + handover

- **§22 Audit Rights** — Client may request the register at any time. Slitigenz must respond within 5 BD.
- **Schedule 7 Handover** — register is part of the mandatory handover pack upon completion or termination.

## Transparency mandate

> **Risks must be surfaced immediately, not managed silently.**
>
> Any known risk that is not disclosed promptly via this register or formal notification is treated as a **delivery management failure** — not an unavoidable event (CMP §6.7.1).

## Sprint-level compact view (read-only mirror)

In sprint planning pages, a 6-column compact view is used for readability — see [Sprint 0 — Discovery §Risk register](../../02-planning/02-sprint-0-discovery.md#risk-register). The sprint view is a snapshot; the canonical record stays in this template's sheet.
