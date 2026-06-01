# Templates — CMP-5026 deliverables

> Pre-drafted templates for every recurring written deliverable Slitigenz must produce per CMP-5026. Fill placeholders, ship.
> **Parent:** [CMP-5026 Compliance Checklist](../12-cmp-compliance-checklist.md)

## Template index

| # | File | Used for | CMP §  | Naming convention |
|---|---|---|---|---|
| 01 | [Weekly Status Report](./01-weekly-status-report.md) | Weekly by 17:00 ICT | §6.6.1 | `[CMP-5026] Weekly Status Report — Week [N] — [Date]` |
| 02 | [Meeting Agenda](./02-meeting-agenda.md) | 24h before each meeting (48h for workshops) | §6.5.2 | `[Agenda] [Meeting Type] — [Date]` |
| 03 | [Meeting Minutes](./03-meeting-minutes.md) | Within 24h of every meeting | §6.5.2 | `[CMP-5026] Minutes — [Meeting Type] — [Date]` |
| 04 | [Variation Proposal](./04-variation-proposal.md) | Per change need | §6.8 / DCA §21.2 | `[VAR-NNN] Variation Proposal — [Subject]` |
| 05 | [Incident / Anomaly Report](./05-incident-anomaly-report.md) | SEV-1 · security · gate failure · personnel loss · force majeure · material impact | §6.6.2 | `[CMP-5026] Incident Report — [Type] — [Date]` |
| 06 | [Registers — per-register templates](./registers/) | 9 live registers (DCA §7) — each register has its own template file with schema + maintenance + reporting integration. **Risk** [split out](./registers/risk.md). Decision · Defect · Dependency · OSS · SDK · AI-tool · Change remaining in [`06-register-schemas.md`](./06-register-schemas.md) until split. | §6.10.2 / DCA §7 | `[CMP-5026] Register — [Name]` |

## Usage flow

1. **Copy** template → new file (or new email / new sheet).
2. **Replace** all `[bracketed placeholders]` with real content.
3. **Verify subject line / file name** matches the naming convention above.
4. **Send** via the channel mandated in the parent checklist (Email for formal; PM Tool / Sheet for registers).
5. **Log** in the appropriate register if material.

## Conventions across all templates

- **Timestamps:** ISO 8601 dates (`YYYY-MM-DD`), both time zones noted for meeting times (Sydney + Hanoi).
- **Language:** English (per project deliverable rule).
- **Trademark terms:** SOS, BackTrack™, TrackMate™, TrackIQ™, HazTrack™, PCR, CAL — preserve as-is.
- **No PII** in any minutes / status / variation / incident report unless explicitly Client-required + PD-approved.
- **Append-only** discipline for registers — never overwrite historical rows.
