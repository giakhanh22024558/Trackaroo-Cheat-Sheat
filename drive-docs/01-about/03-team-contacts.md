# Team & Contacts

> **Goal:** for any issue type — know **who to contact** and **via what channel**.
> Sources: **CMP-5026** (Project Communications Protocol, 29 May 2026) · **Slitigenz Proposal §1.3** (Lean Senior Squad).

## 1. Primary contacts

| Party | Role | Name | Email |
|---|---|---|---|
| Trackaroo Systems (Client) | Project Director — Founder | **Ian Moore** | `imoore@trackaroosystems.com` (secondary: `admin@trackaroosystems.com`) |
| Slitigenz (Contractor) | Executive Sponsor | **Anh Vũ (Daniel Truong)** | `vuta@slitigenz.io` |
| Slitigenz (Contractor) | Project Manager (day-to-day delivery) | **Luong Gia Khanh** | *(per Slitigenz directory)* |

> **Contractual notices** (gate clearance, variation, dispute, termination) — valid only via `imoore@trackaroosystems.com` ↔ `vuta@slitigenz.io` (DCA-5026 Schedule 6).

## 2. Slitigenz Senior Squad — 8 Experts (who owns what)

| Name | Role | Owns / Specialist domain |
|---|---|---|
| **Dinh Ba Trung** | Tech Lead / Architect | Local-First system design · immutable schema (SQLite/WAL) · AES-256 at rest · Survival Core isolation · sync protocols · Phase 2 Emergency Escrow pathway |
| **Nguyen Huy Khoi** | Mobile Lead | Survival Core implementation · Mapbox offline SDK (≤6s cold start) · deterministic background services (iOS/Android) |
| **Nguyen Quoc Viet** | Web/Console Lead | **OCS-5026 Operations Console** · companion website · console-vs-Core architectural isolation |
| **Nguyen Viet Hoang** | Backend/DevOps Lead | **TrackIQ™ scoring pipeline** (Ingest → DEM enrichment → Scoring → Tile publish) · Firebase isolation · TLS 1.3 security for non-core sync |
| **Nguyen Thi Thom** | QA/Audit Lead | **11 TQP-5026 validation domains** · chaos testing · ≤8%/hour battery benchmark · 10-hour endurance test |
| **Nguyen Thuy Duong** | UI/UX Lead | State matrix execution (Online/Offline/Queued) · archetype-specific presets · UXS-5726 behavioural compliance |
| **Nguyen Tien Dat** | Mobile Developer | Experience Layer parallel workstreams — **TrackMate™** · First Aid Reference |
| **Luong Gia Khanh** | Project Manager | Gate-model governance · weekly risk reporting · Parallel Workstream Map · 13 Nov 2026 launch |

> **Entity:** 100% delivery by **SLI TECHNOLOGY COMPANY LIMITED (Vietnam)** — no sub-contractors, all engineering centralised in Hanoi.

## 3. Who to ask about X — issue → contact

| Issue type | Primary contact | Channel |
|---|---|---|
| Material decision / approval (any) | PD Ian Moore | Email |
| Day-to-day delivery issue | PM Luong Gia Khanh | Email (cc PD) |
| Commercial / contract / variation / dispute | PD ↔ Slitigenz Exec Sponsor (Anh Vũ) | Email (formal) |
| Architecture · data model · schema · Survival Core isolation | Tech Lead — **Dinh Ba Trung** | Architecture & Technical Review (fortnightly) + email |
| Mobile · Mapbox · Survival Core implementation | Mobile Lead — **Nguyen Huy Khoi** | Tech Review + email |
| Experience Layer / TrackMate™ / FAR mobile build | Mobile Developer — **Nguyen Tien Dat** | Tech Review + email |
| OCS Console · companion website | Web/Console Lead — **Nguyen Quoc Viet** | Tech Review + email |
| TrackIQ™ pipeline · Firebase · backend · DevOps · CI/CD | Backend/DevOps Lead — **Nguyen Viet Hoang** | Tech Review + email |
| QA · validation · TQP-5026 domains · battery / endurance / chaos tests | QA/Audit Lead — **Nguyen Thi Thom** | Email + weekly status |
| UI/UX · wireframe · state matrix · archetype presets · WCAG | UI/UX Lead — **Nguyen Thuy Duong** | Design & UX Review (fortnightly) + Figma |
| Sprint progress · risk register · gate readiness · resource allocation | PM Luong Gia Khanh | Weekly Status Call + report |
| SEV-1 defect · release halt · Survival Core breach · security incident | **PD immediately** + PM | WhatsApp flag → Email within 1 hour |
| SEV-2 (major functional failure / Gate artefact at risk / key personnel loss) | PD + PM | Email within 24 hours |
| Gate clearance request / submission / sign-off | PD | Email + Gate Clearance Meeting |
| Variation proposal (scope · cost · schedule change) | PD | Email to `imoore@trackaroosystems.com` (DCA-5026 §21.2 format) |
| Legal / compliance / clinical (SOS · First Aid · hazard liability · APPs · ToS) | **PD only** | Email + Legal & Compliance Briefing |
| Third-party platform issue (App Store · Google Play · Mapbox · Firebase account) | PD immediately (Client-owned accounts) | Email |
| Public statement / press / marketing about trackaroo® | **PD — written approval required** | Email (no public statement without approval) |
| Stack departure from named SDK (Mapbox · Firebase · Flutter) | PD before implementing | Email (proposal + rationale) |
| Documentation / artefact sharing | Per artefact owner | See §7 below |

## 4. Communication channels — what's valid for what

| Channel | Use for | Do NOT use for | Record obligation |
|---|---|---|---|
| **Email** (primary written) | All formal communications · decisions · directions · approvals · gate notices · variation · escalation · weekly status. **Sole valid channel for contractual notices.** | Replacing gate sign-off (which needs PD written sign-off in agreed format) | Retained by both parties; material decisions logged in project decision register |
| **Online meeting** (Zoom / Google Meet) | Status calls · design reviews · workshops · gate prep · issue resolution | Verbal directions substituting for written instruction. No meeting decision binding until confirmed in writing. | Written minutes by Slitigenz within **24 hrs** |
| **WhatsApp / IM** | Scheduling · low-urgency nudges · availability · quick non-material clarification · flag SEV-1 (followed up formally) | Any direction / decision / approval / escalation of material consequence | None — substantive content must be followed up by email within **1 Business Day** |
| **Project Management Tool** *(TBC)* | Task tracking · sprint mgmt · defect logging · register updates · build progress · doc sharing | Formal notices · gate clearance · variation approvals · anything creating contractual obligation | Slitigenz maintains all registers; PD access continuous (DCA-5026 §7) |
| **Shared Repo** (GitHub / GitLab, Client-owned) | Source code · build artefacts · CI/CD · documentation · gate evidence packages | Direct communication / decisions | Continuous PD access (DCA-5026 §8.1) |
| **Oral / Telephone** | Urgent matters · informal discussion only | Material decisions · directions · approvals · escalations | Significant oral conversations must be followed up by email within **1 Business Day** by the initiator |

## 5. Response time standards (Business Days unless stated)

| Communication | Required response | Responder |
|---|---|---|
| **SEV-1 defect / automatic release halt** | **Within 2 hours** (business hours) | Slitigenz → PD; PD acknowledgement |
| **SEV-2 escalation** | Within 24 hours | Both parties |
| Contractual notices (gate / variation / dispute) | 5 Business Days | Both parties |
| Weekly status report | By 17:00 ICT on agreed day | Slitigenz |
| Meeting minutes | Within 24 hours of meeting close | Slitigenz |
| Minute confirmation/correction | Within 2 BD of distribution | PD |
| General project query (email) | Within 1 BD | Both parties |
| Gate evidence package review | 5 BD from submission | PD |
| Variation proposal review | 5 BD | PD |
| Invoice dispute notification | 5 BD from invoice receipt (DCA-5026 §6.6) | PD |
| Audit / compliance evidence request | 5 BD (DCA-5026 §22.1) | Slitigenz |

## 6. Escalation severity → action

| Severity | Definition | Required action | Notify | Recovery plan |
|---|---|---|---|---|
| **SEV-1 / Critical** | Blocks Gate · Survival Core breach · security incident · release halt · threatens 13 Nov GA | Written notify to PD immediately. WhatsApp flag permitted, followed by email within 1 hr | **2 hours** | 5 BD |
| **SEV-2 / High** | Major functional failure · Gate artefact at risk · key personnel loss · significant schedule impact | Written notify to PD with initial assessment | **24 hours** | 5 BD |
| **SEV-3 / Medium** | Functional issue with workaround · minor schedule risk | Raise in weekly status report · flag in next weekly call | Next weekly cycle | — |
| **SEV-4 / Low** | Minor defect · cosmetic · low-consequence | Log in defect/risk register · report in weekly status | Next weekly cycle | — |

> If issue not resolved by written comms within 2 BD of escalation → either party may call **Issue Resolution Workshop** (within 48 hrs for SEV-1, within 5 BD others). If still unresolved → **DCA-5026 §23 dispute resolution**.

## 7. Standing meetings — when & who leads

| Meeting | Frequency | Duration | Participants | Lead |
|---|---|---|---|---|
| **Weekly Status Call** | Weekly (agreed day, within overlap window) | 45 min | PD + Slitigenz PM + Leads as needed | Slitigenz |
| Design & UX Review | Fortnightly or at key wireframe / UI state milestones | 60–90 min | PD + Slitigenz Design Lead | Slitigenz |
| Architecture & Technical Review | Fortnightly or as required by Gate artefact delivery | 60 min | PD + Slitigenz Tech Lead | Slitigenz |
| Gate Preparation Review | 2 weeks before each Gate | 90 min | PD + Slitigenz PM + Leads | Slitigenz |
| **Gate Clearance Meeting** | At each Gate date | 60 min | PD + Slitigenz PM | **PD** |
| Issue Resolution Workshop | Ad hoc — within 48 hrs of SEV-1 / escalated risk | 90 min max | PD + Slitigenz PM + relevant Leads | Both parties |
| Legal & Compliance Briefing | Before each legal gate (LE-01..LE-08) | 45 min | PD + Slitigenz PM | **PD** |
| Ideas & Design Workshop | Ad hoc — min 5 BD advance notice | 2–3 hours | PD + Slitigenz Design + relevant Leads | **PD** |

**Minimum booking notice:** Weekly call (none — standing) · Design/Tech Review (3 BD) · Gate Prep / Gate Clearance / Workshop / Legal Briefing (5 BD) · Issue Resolution (48 hrs · immediate for SEV-1) · Ad hoc (24 hrs where practicable).

## 8. Time zone overlap window

| Season | Sydney (PD) | Hanoi (Slitigenz) | Overlap |
|---|---|---|---|
| **AEST** (Apr – Oct) | 09:00–12:00 AEST | 06:00–09:00 ICT | **3 hours** — preferred morning |
| **AEDT** (Oct – Apr) | 09:00–11:00 AEDT | 06:00–08:00 ICT | **2 hours** — confirmed morning |

> Meetings outside this window require explicit agreement from both parties **5 BD in advance**.
> Vietnam + Australian (NSW) public holidays exchanged within first BD of each calendar month.

## 9. Artefact sharing — what goes where

| Artefact | Sharing method | Naming | Approval before distribution |
|---|---|---|---|
| Gate evidence packages | Shared repo + email notify | `[GATE]-Evidence-[Date]` | No — submitted for PD review |
| Governance documents (new / amended) | Email + repo commit | Per DDS-1326 | PD confirmation before finalisation |
| Wireframes & UI states | Figma share link + email | Per WFD-5126 | **PD approval before development commences** |
| Weekly status reports | Email to `imoore@trackaroosystems.com` | `[CMP-5026] Weekly Status — Week [N] — [Date]` | No |
| Variation proposals | Email to `imoore@trackaroosystems.com` | `[VAR-NNN] Variation Proposal — [Subject]` | No — submitted for PD review |
| Third-party content (clinical / legal) | **Email only** — not in repo | Per document type | **PD approval before any user-facing exposure** |
| Meeting minutes | Email to all attendees + PD | `[CMP-5026] Minutes — [Meeting Type] — [Date]` | Confirmed by PD within 2 BD (silence = confirmation) |

## 10. Hard rules (constraints)

- All material decisions in **writing** — verbal/informal communication creates no obligation (DCA-5026 §7).
- Contractual notices only valid via the 2 designated email addresses (Schedule 6).
- **WhatsApp / IM is NOT a record** for governance purposes.
- **No public statement** about trackaroo® / the engagement / any deliverable without prior **written PD approval** (obligation survives termination).
- **Stack departure** from named SDK (Mapbox · Firebase · Flutter · etc.) requires PD approval before implementation.
- **CAL flag states** (`satReady`, `queueEnabled`, `offlineBeacon`) + Survival Core isolation = non-negotiable. Conflicts flagged immediately, not worked around.
- Failure to respond to **SEV-1 / release halt within 2 hours business hours** = breach (DCA-5026).

---
*Source: CMP-5026 §6 (Points of Contact · Channels · Response · Meetings · Escalation · Artefacts) · Slitigenz Proposal §1.3 (Lean Senior Squad).*
