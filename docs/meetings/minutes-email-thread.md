# Meeting Minutes — Email Thread Convention

> How Slitigenz distributes meeting minutes after every meeting, as a single running email thread.
> Per CMP-5026 §6.5.2 (minutes within 24h of meeting close · PD confirms within 2 BD · silence = confirmation).

## Thread subject (stable — do NOT change)

```
[CMP-5026] Trackaroo® Phase 1 — Meeting Minutes
```

- This subject **anchors the whole thread**. The kickoff minutes (2026-06-01) is the **first email**; every subsequent meeting's minutes is a **Reply** in the same thread.
- Keeping the subject constant means all minutes stay in **one searchable thread**. The email client shows `Re: [CMP-5026] Trackaroo® Phase 1 — Meeting Minutes` on replies — leave that as-is.
- The specific meeting type + date is identified in the **email body header**, not the subject (see below).

> **Naming-convention note:** CMP §6.5.2 names minutes `[CMP-5026] Minutes — [Meeting Type] — [Date]`. For a running thread we keep the per-meeting `[Meeting Type] — [Date]` in the body header (line 1) and hold the subject stable so the thread does not fragment. Each email body remains fully self-identifying.

## Recipients

| Field | Value |
|---|---|
| **To** | `imoore@trackaroosystems.com` (PD) + all meeting attendees |
| **CC** | `vuta@slitigenz.io` (Slitigenz Exec Sponsor) |
| **From** | Slitigenz PM — Bill (Luong Gia Khanh) |

## How to post each meeting's minutes (the body)

Every email in the thread starts with a one-line header identifying the meeting, then the minutes:

```
Minutes — [Meeting Type] — [YYYY-MM-DD]

[paste the minutes content for this meeting]

PD confirmation: silence past 2 business days = confirmation (CMP §6.5.2).
```

- Attach or paste the full minutes (decisions · actions · risks · deferred · references).
- Send **within 24 hours of meeting close** (CMP §6.5.2 / §6.4).

## First email in the thread (Kickoff)

| | |
|---|---|
| **Subject** | `[CMP-5026] Trackaroo® Phase 1 — Meeting Minutes` |
| **Body header (line 1)** | `Minutes — Project Kickoff — 2026-06-01` |
| **Body** | Content from [`2026-06-01-kickoff-minutes.md`](./2026-06-01-kickoff-minutes.md) |
| **Send by** | 2026-06-02 15:22 ICT (24h from 15:22 meeting close) |

## Subsequent meetings (examples — same thread, Reply)

| Meeting | Body header (line 1) |
|---|---|
| Weekly Status Call | `Minutes — Weekly Status Call — [date]` |
| Design & UX Review | `Minutes — Design & UX Review — [date]` |
| Architecture & Technical Review | `Minutes — Architecture & Technical Review — [date]` |
| Gate Preparation Review | `Minutes — Gate Preparation Review — [date]` |
| Issue Resolution Workshop | `Minutes — Issue Resolution Workshop — [date]` |

> All of the above go into the **same thread** by replying to the kickoff email — never start a new subject line.

## When to break out of the thread

Start a **new** email (not a reply) only for:
- **Contractual notices** (gate clearance, variation, dispute) — these need their own subject per CMP §6.3.1.
- **Incident / anomaly reports** (SEV-1, security) — separate immediate notification per CMP §6.6.2.
- **Variation proposals** — `[VAR-NNN] Variation Proposal — [Subject]`.

Minutes-only content stays in the running thread.
