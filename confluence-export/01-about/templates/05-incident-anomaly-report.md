# [CMP-5026] Incident Report — [Type] — [YYYY-MM-DD]

> **Use for:** SEV-1 defect / release halt · security incident · credential compromise · unauthorised access · gate failure or anticipated failure · key personnel departure or substitution · force majeure · any matter with material impact on cost / schedule / quality
> **To:** `imoore@trackaroosystems.com`
> **From:** Slitigenz Project Manager (or Tech Lead / Security Lead per type)
> **Delivery timeframe:** Per CMP §6.4 — SEV-1: **within 2 hours** (business hours) · SEV-2: 24h · Others: per §6.4 table
> **Per CMP-5026 §6.6.2**

## 1. Incident metadata

| Field | Value |
|---|---|
| **Report ID** | INC-NNN |
| **Incident type** | SEV-1 defect / Release halt / Security incident / Credential compromise / Gate failure / Personnel departure / Force majeure / Material impact |
| **Severity** | SEV-1 / SEV-2 / SEV-3 / SEV-4 |
| **Detected at** | YYYY-MM-DD HH:MM ICT (HH:MM AEST) |
| **Reported at** | YYYY-MM-DD HH:MM ICT |
| **Detected by** | [Name + role] |
| **Reported by** | [Name + role] |
| **Channels notified** | Email / WhatsApp flag / Phone — list which + timestamps |

## 2. What happened

[Plain-language description, 2–5 sentences. What is the symptom / observation?]

## 3. Affected systems / components

- [Component 1 — e.g. SOS subsystem · OCS · CI/CD · production environment]
- [Component 2]
- [Survival Core impact? Y/N — flag immediately if Y]

## 4. Potential impact

| Dimension | Impact | Estimated scale |
|---|---|---|
| User safety | Y / N / Unknown | |
| Gate clearance | Blocks / At risk / None | |
| Schedule | Days impact: __ | |
| Cost | $ __ | |
| Data exposure | Y / N — categories: __ | |
| Survival Core integrity | Compromised / At risk / Intact | |

## 5. Containment actions taken

| Time | Action | Owner | Outcome |
|---|---|---|---|
| HH:MM | | | |

## 6. Root cause (preliminary — full RCA may follow)

[Best current understanding. If unknown, state so.]

## 7. Workaround in place?

- **Yes** — describe + ETA: __
- **No** — reason + ETA for workaround: __

## 8. Permanent fix plan

- **Plan within:** 24h (SEV-1) — confirm: ☐ Provided in this report / ☐ Will follow within 24h
- **Permanent fix deployed within:** 3 BD (SEV-1) — target date: YYYY-MM-DD
- **Owner:** [Key Personnel name]
- **Validation method:** [test plan / regression scope]

## 9. PD decision required

- [ ] Approve workaround
- [ ] Approve permanent fix plan
- [ ] Approve extended fix timeline (>3 BD) — justification: __
- [ ] Other: __

## 10. Communication plan

| Audience | Channel | Sent / scheduled |
|---|---|---|
| PD | Email | ✓ this report |
| Slitigenz Squad | Internal | YYYY-MM-DD HH:MM |
| External (Client legal / users / App Store) | Per PD approval only | — |

## 11. Follow-up

- **Daily status until resolved:** Y / N
- **Full RCA delivered by:** YYYY-MM-DD
- **Logged in:** Defect register · Risk register · Decision register · Security event log

---
*Source format: CMP-5026 §6.6.2 + §6.7.2 + DCA §15.1 SEV table.*
