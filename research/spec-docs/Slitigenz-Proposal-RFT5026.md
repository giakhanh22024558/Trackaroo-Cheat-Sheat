# Slitigenz Proposal — RFT-5026 (Delivery & Milestone Extract)

> **Source:** Google Drive — `Slitigenz_RFT-5026_Proposal_Submission_20260508_FINAL (Excludes commercial terms)` (Google Doc `13N3hVTLnK-oen6BAmZkWdWA_HaWTnSXB5xlbR7JevqM`)
> **Owner:** vuta@slitigenz.io · **Synced:** 2026-05-28
> **Scope of this extract:** delivery-relevant sections only (build sequencing, milestones, committed Discovery artefacts, workstream/effort, clarifications). The technical-architecture chapters largely restate the Authority Stack already captured in the other `spec-docs/` extracts.

This is the **vendor's committed delivery plan**. It is the authority for *what Slitigenz will deliver and when* — distinct from the trackaroo® spec docs which define *what the product must be*.

---

## 1. Locked Project Gates (§10.2 — Milestone Commitment)

Slitigenz confirms the Revised Procurement Timeline (19 April 2026) and commits to these **locked gates**:

| Project Gate | Target Date | Mandatory Confirmation |
|---|---|---|
| **Contract Execution** | **29 May 2026** | Team mobilisation and environment setup |
| **Discovery Gate** | **15 June 2026** | **All 9 Architectural Compliance Artefacts accepted; OCS-5026 companion website live** |
| **Alpha Gate** | **22 August 2026** | Survival Core validated; SOS legal review complete; Stage 1 OCS-5026 modules ready |
| **Beta-Ready MVP** | **30 October 2026** | Full scope delivered; 11 validation domains executed; WCAG 2.1 AA audit complete |
| **GA / Public Launch** | **13 November 2026** | Hard Commercial Target. App Store / Google Play live |

> ✅ **Resolves earlier open question:** Discovery is **locked to 15 June 2026** (not 15 May). A new **Contract Execution** gate (29 May 2026) precedes it.

**High-risk dependency mitigation (remote validation):** field validation of Australian remote terrain is done from Vietnam via **GPS Spoofing + Faraday Shielding** in the CLR-SLZ-001 lab (simulates Australian signal attenuation / coordinate drift); empirical field confirmation via **Separable Portion 2**.

---

## 2. The 9 Architectural Compliance Artefacts (§2.7 — Discovery Gate deliverables)

Committed for delivery **by the Discovery Gate (15 June 2026)**. These are the empirical proof of Authority-Stack adherence — the **focus of Sprint 0**.

| # | Artefact | Content | Compliance basis |
|---|---|---|---|
| **D1** | **High-Level Architecture Diagram** | System diagram annotated with Survival Core isolation boundaries | AOD-5026 — immutable Core ⇎ Experience separation |
| **D2** | **Deterministic State Transition Matrix** | All Survival Core states & transitions (Idle, Navigating, SOS, BackTrack™) | Proves zero probabilistic variance |
| **D3** | **Offline-First Execution Explanation** | Whitepaper on 100% Survival Core function with no network | "Offline-First Supremacy" posture |
| **D4** | **Module Isolation Mapping** | Low-level dependency graph: Experience Layer cannot mutate Survival Core | CDG-5126 mutation-prevention |
| **D5** | **Breadcrumb Classification Confirmation** | Written confirmation breadcrumb = Local-Only & Non-Syncable | Forensic/legal-evidence integrity |
| **D6** | **CAL Architecture Documentation** | Full CAL spec: transport priority + 4 state flags (satReady=False, queueEnabled, offlineBeacon, partialSignal) | Transport abstraction + Phase 2 satellite pathway |
| **D7** | **PCR Architecture Documentation** | PCR framework: supersession-based resolution (NOT TTL) | OSM-5026 §10 — independent of TTL hazard/env layers |
| **D8** | **SDK Audit Declaration** | Inventory of every SDK (active/dormant); warrants **no prohibited capabilities** | No AI/ML/satellite SDKs present |
| **D9** | **OSS Licence Audit** | All OSS/third-party licences audited | Compatible with App Store / Play Store distribution |
| **+** | **Companion website live** | OCS-5026 companion website operational | Discovery gate confirmation (§10.2) |

---

## 3. Build Sequence (§10.1)

Adheres to **PRD-5126 §13**:
1. **Survival Core Supremacy** — all Survival Core subsystems (Offline Navigation, BackTrack™, HazTrack™, SOS, Local Logging) fully built/validated/accepted **before** Experience Layer features.
2. **Safety-Critical Lead** — SOS and BackTrack™ reach acceptance first (establish "Evidentiary Integrity" early).
3. **WFD-5126 Build Gates** — no subsystem development without prior written wireframe approval from the Project Director.
4. **Parallel Execution** — TrackIQ™ Pipeline + HazTrack™ Feed Ingestion start as independent backend workstreams **immediately after Discovery gate**.

---

## 4. Parallel Workstreams & Effort (§10.3) — 900 Man-Days · 8 Senior Experts

| Track | Primary Owner | Man-Days | Key Deliverables |
|---|---|---|---|
| **Track 1: Survival Core** | Mobile Lead | 160 | Navigation, BackTrack™, SOS, Local Logging integrity |
| **Track 2: TrackMate™** | Mobile Developer | 140 | BLE Mesh, CAL logic, Tier 1 fallback |
| **Track 3: Mapping & Visual** | UI/UX Lead | 90 | Custom TRK styles, PCR icon system, tile budgeting |
| **Track 4: Experience Layer** | Mobile Developer | 100 | TrackIQ™ scoring display, First Aid Reference flows |
| **Track 5: Feed Integration** | Backend/DevOps Lead | 80 | HazTrack™ normalization, TrackIQ™ scoring pipeline |
| **Track 6: QA & Validation** | QA/Audit Lead | 110 | 24/7 automated testing of 11 TQP-5026 domains |
| **Track 7: Legal/Regulatory** | Project Manager | 60 | LE-01 → LE-07 coordination + gate evidence |
| **Track 8: Ops Console (OCS)** | Web/Console Lead | 160 | Staged OCS-5026 modules via unified schema |
| **TOTAL** | Senior Squad | **900** | 100% senior-level oversight |

**Efficiency levers:** (1) Unified Automation Harness compresses QA from 160 → 110 man-days; (2) strict unified type-safe schema between mobile Survival Core and OCS removes 40 man-days of integration buffer.

> ⚠️ **Open mismatch:** §10.3 prose says "**seven (7)** simultaneous tracks (VEG-5026 §7.3)" but the effort table lists **8 tracks** (adds Track 8 OCS) and "Lean Senior Squad of **8** Experts". Confirm 7 vs 8 with PD. (Earlier note also flagged 8 named experts vs 7 listed names.)

---

## 5. Clarification Register (§11) — Vendor working assumptions

| ID | Source | Question | Vendor Assumption | Risk if wrong |
|---|---|---|---|---|
| **CLR-SLZ-001** | TQP-5026 §4.1 | Will lab GPS-spoofing + Faraday simulation be accepted as primary evidence for Discovery & Alpha validation? | Yes — high-fidelity Vietnam sim env replaces AU field testing; full empirical logs matching AU coordinate envelope provided | Physical AU presence for early gates → revised mobilisation + local hiring |
| **CLR-SLZ-002** | BPS-5126 §4.1 | If iPhone 17 / Galaxy S25 unavailable in SE Asia at Alpha, can prior flagship be used with re-verify commitment? | "Reasonable efforts" for next-gen HW; latest available global versions for baseline | Battery Report (D5) delay for affected devices |
| **CLR-SLZ-003** | PRD-5126 RT-11 | WCAG 2.1 AA audit remote (staging build) or physical lab access? | Remote-capable; secure access to feature-complete build provided | Physical audit → HW shipping / AU lab |
| **CLR-SLZ-004** | FSD-5126 §4.3.2 | HazTrack™ feed "authority-origin" credential delivery format? | Standard REST/GeoJSON endpoints + API keys/OAuth | Proprietary protocols → extra normalization in TrackIQ™ pipeline |
| **CLR-SLZ-005** | OCS-5026 §6.0 | OCS hosted in same Firebase project as mobile Experience Layer? | Unified Firebase project (consolidated billing/RBAC), respecting CDG-5126 §7 isolation | Multi-project → extra DevOps cross-project config |
| **CLR-SLZ-006** | UXS-5726 §1.3.3 | Delivery format for legally cleared SOS / First Aid copy? | Structured Content Matrix (CSV/JSON) for automated integration | Manual copy-paste → human error + Prohibited-Claims scan risk |

---

## 6. Phase 2 Scaffolding Commitment (§2.6)

Confirms the 3 permitted inert scaffolds: **Emergency Escrow Schema** (versioned, forward-migration ready) + CAL `satReady` (locked false) + CAL satellite pathway — all schema-only / non-executable in Phase 1.

## 7. Selected Quantified Commitments (V-items)

- **V-01 BLE Mesh:** ≤ 0.45%/hr overhead (120-second heartbeat; event-triggered, not polling).
- **V-02 Wi-Fi Direct:** ≤ 0.8%/hr aggregate (max 2-min fallback window per 60-min traversal; auto-deactivate after burst).
- **V-03 LoRa:** < 0.1%/hr app-side; auto-detect goTenna (MFi/External Accessory) + Meshtastic (Core Bluetooth); 4 WFD-5126 UI states committed.
- **Legal gates:** LE-01 → LE-07 (clinical + legal review periods) coordinated in Track 7; aligns with ESF/SOS RT-16 and First Aid clinical review.

---

## 8. Traceability to project artifacts

| Proposal element | Project artifact it drives |
|---|---|
| §10.2 Locked gates | `docs/planning.md` §A1 master timeline + §B4 gate/priority |
| §2.7 9 Compliance Artefacts | `docs/planning.md` §B5 → Discovery Gate Deliverable Register (D1–D9) |
| §10.1 Build sequence | Story-pass ordering (Survival Core first; SOS/BackTrack lead) |
| §10.3 Workstream tracks | Resource mapping (not in backlog — delivery-org concern) |
| §11 Clarifications | Open items for PD; CLR-SLZ-001 = validation method for Discovery/Alpha |

> ⚠️ Commercial terms are excluded from this proposal version. Separable Portions referenced (1/2/3) are commercial — see the Delivery Agreement (DCA-5026) for contractual detail.
