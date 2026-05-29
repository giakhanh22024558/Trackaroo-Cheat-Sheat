# Trackaroo® Phase 1 — Spec Document Extracts

**Purpose:** Structured markdown extracts of **19 authoritative governance documents** from `TRACKAROO 2026 RFT Phase 1` Drive folder. Optimized for business analysis + cross-referencing during vendor delivery.

**Source folder:** `G:\.shortcut-targets-by-id\1fqaX3DE_KT88tT7ElgewcBM0bKzTvkZp\TRACKAROO 2026 RFT Phase 1\`

**Last extracted:** 2026-05-26 (Pass 2 — added UXS, OSM, WFD, BPS, TAA + bonus FQH, SFD)

> 📖 **Đọc tài liệu theo thứ tự logic?** Xem **[READING-GUIDE.md](./READING-GUIDE.md)** — bản đồ phân nhóm 19 docs + reading path riêng cho Project Manager (8 bước · ~3 ngày) và System Architect (10 bước · ~5 ngày).

---

## Authority Hierarchy (canonical order — conflicts resolve strictly upward)

| Priority | Document | Role | Local extract |
|---|---|---|---|
| **1** | **UXS-5726** | UX Strategy & Behavioural Authority (highest) | [UXS-5726.md](./UXS-5726.md) ✅ |
| **2** | **PRD-5126** | Product Requirements & Acceptance Authority | [PRD-5126.md](./PRD-5126.md) ✅ |
| **3** | **FSD-5126** | Functional Specification | [FSD-5126.md](./FSD-5126.md) ✅ |
| **4** | **TQP-5026** | Testing & QA Authority | [TQP-5026.md](./TQP-5026.md) ✅ |
| **5** | **WFD-5126** | Wireframe & UI State Authority + build gate | [WFD-5126.md](./WFD-5126.md) ✅ |
| **6** | **VGD-5126** | Vendor Guidance & Enforcement Authority | [VGD-5126.md](./VGD-5126.md) ✅ |

## Tier 2 Specialist Authorities (supporting guides)

| Doc | Domain | Local extract |
|---|---|---|
| **OSM-5026** | Overlay Semantics Map · TTL thresholds · PCR framework · LIR-01–06 · RG-01–11 · 8-state matrix | [OSM-5026.md](./OSM-5026.md) ✅ |
| **HFG-5026** | Hazard Feed Governance · 5-Pillar Filter · authority-origin rule | [HFG-5026.md](./HFG-5026.md) ✅ |
| **ESF-5026** | Emergency Safety Framework · SOS governance · satellite prohibition | [ESF-5026.md](./ESF-5026.md) ✅ |
| **CDG-5126** | Cloud & Data Governance · Local-Only classification · Firebase isolation | [CDG-5126.md](./CDG-5126.md) ✅ |
| **BPS-5126** | Battery Performance Standard · ≤8%/hr · ≥10hr · ≤20%/hr distress · device matrix | [BPS-5126.md](./BPS-5126.md) ✅ |
| **BTF-5126** | BackTrack™ Framework · breadcrumb integrity · Phase 2 Escrow pathway | [BTF-5126.md](./BTF-5126.md) ✅ |
| **TAA-5126** | Target Archetypes (6) & Activity Context Authority · tier function matrix | [TAA-5126.md](./TAA-5126.md) ✅ |
| **MAS-5126** | Mapping Architecture & Visual System Standard | [MAS-5126.md](./MAS-5126.md) ✅ |
| **FRM-5126** | First Aid Reference Framework (internal — not in Drive folder) | ⚠️ NOT IN DRIVE |

## Architecture Reference

| Doc | Domain | Local extract |
|---|---|---|
| **AOD-5026** | Architecture Overview (Dual-Layer Architecture · component reference · data isolation) | [AOD-5026.md](./AOD-5026.md) ✅ |

## Phase Scope + Operations

| Doc | Domain | Local extract |
|---|---|---|
| **PSB-5026** | Phase Scope Boundary Summary (in/out scope · Phase 2 deferrals · scaffold discipline) | [PSB-5026.md](./PSB-5026.md) ✅ |
| **OCS-5026** | Operations Console Specification (internal admin tool · 9 modules · 3-role RBAC) | [OCS-5026.md](./OCS-5026.md) ✅ |

## Operational Governance

| Doc | Domain | Local extract |
|---|---|---|
| **CAR-5026** | Central Amendment Register (single source of amendment history) | ⚠️ NOT IN DRIVE |

## Bonus Vendor-Pack Documents

| Doc | Domain | Local extract |
|---|---|---|
| **FQH-5026** | Five-Question Cognitive Hierarchy Visual · primary UX acceptance criterion vendor reference | [FQH-5026.md](./FQH-5026.md) ✅ |
| **SFD-5026** | SOS Flow Diagram · 3-stage log sequence · 6-element confirmation screen · ≤2-tap matrix · LE-02 copy structure | [SFD-5026.md](./SFD-5026.md) ✅ |

---

## Quick reference — Phase 1 commercial dates

| Gate | Target Date | Key conditions |
|---|---|---|
| **Contract Execution** | **29 May 2026** | Team mobilisation + environment setup |
| **Discovery** | **15 Jun 2026** *(locked — Slitigenz proposal §10.2)* | 9 Architectural Compliance Artefacts accepted (D1–D9) · companion website live · CAL architecture documented · WFD-5126 coverage per subsystem · SDK audit (V-12) · OSS audit (V-13) |
| **Alpha** | **22 Aug 2026** | Survival Core validated · SOS onboarding · clinical + SOS legal reviews · prohibited-capability scan clear · OCS Stage 1 ready |
| **Beta-Ready MVP** | **30 Oct 2026** | All 11 TQP-5026 validation domains · WCAG 2.1 AA · all 22 rejection triggers resolved · OCS all modules ready · RT-16 legal review complete |
| **GA / Public Launch** | **13 Nov 2026** | App Store + Google Play submissions live · written PD go/no-go sign-off |

> **Discovery gate date RESOLVED → 15 June 2026** (locked in Slitigenz proposal §10.2; supersedes the earlier 15 May/15 Jun ambiguity). The 9 committed Discovery artefacts are tracked in `docs/planning.md` §B5 → Discovery Gate Deliverable Register.

---

## Key cross-cutting concepts

### Survival Core invariants (immutable, AT ALL TIMES)
- Offline-first · Deterministic · Non-adaptive · Non-inferential · Non-escalatory · Crash-survivable · Firebase-independent

### Zero Transmission Posture (ESF-5026 + UXS-5726 §7.4)
- All Survival Core paths generate **zero outbound packets** Phase 1
- No satellite SDK · no satellite code (active or dormant) · no escalation logic · no monitoring posture
- Scope: app process boundary (OS-level services excluded)

### 3 Permitted Phase 2 Scaffolds (EXHAUSTIVE list — PSB-5026 §4)
1. **BackTrack™ Emergency Escrow data schema** — schema only · non-executable
2. **CAL `satReady` flag** — declared false · not activatable · CAL schema only (NOT in app data models)
3. **CAL satellite transport architectural pathway** — documented · not executable · extensible CAL interface only

Each scaffold must satisfy 4 QA visibility requirements: (a) visually surfaced · (b) display exactly "Inactive in Phase 1." · (c) schema-complete · (d) zero executable logic.

### Prohibited satellite-specific data field names (ESF-5026 §8 · FSD-5126 §4.4.4)
`satReady` (CAL schema ONLY, set to false — NOT in app data models) · `satelliteEndpoint` · `satTransmissionStatus` · `satellitePayload` · `transmission_status` · `satellite_endpoint` · `dispatch_channel` · `fallback_mode` · `connectivity_priority`

### Five-Question Cognitive Hierarchy (PRD-5126 §10 — primary acceptance criterion)
1. Where am I? · 2. Where am I going? · 3. What surrounds me? · 4. How do I get back? · 5. How do I call for help?

Failure of any question across any archetype / screen state = named rejection trigger.

### 22 Named Rejection Triggers (RT-01 → RT-22 — PRD-5126 §14.4)
Halt release immediately on detection. Common high-impact:
- **RT-01** Satellite SDK present/triggerable
- **RT-02** Autonomous rerouting
- **RT-03** AI inference logic
- **RT-05** Cloud breadcrumb storage
- **RT-06** Monitoring posture implied
- **RT-09** Phase 2+ scaffold triggerable
- **RT-13** Breadcrumb immutability compromised
- **RT-14** HazTrack™ alters TrackIQ™ grade
- **RT-15** SOS response time / ≤2-tap failure
- **RT-16** ESF-5026 legal review incomplete (Beta-Ready gate condition)
- **RT-17** LoRa onboarding disclosure absent
- **RT-19** PCR TTL logic present (must be supersession-only)
- **RT-22** Tier restriction applied to SOS-triggered distress mode

### 11 Overlay Rollback Governance Triggers (RG-01 → RG-11 — OSM-5026 §12)
Mandatory clear result at every gate. Halt release on detection.

### 14 Prohibited Breadcrumb Mutations (BTF-5126 §5.2, CDG-5126 §4.3)
Merge · Compaction · Reconstruction · Reordering · Map-matching · Coordinate interpolation · Gap-filling · Deduplication · Compression · Conflict resolution · Reconciliation · Coalescing · Smoothing · Correction.

Static analysis must confirm absence of all 14 before any release gate.

### CAL State Flags (4 mandatory — FSD-5126 §6.1.1)
- **`satReady`** — Declared FALSE in all Phase 1 builds. CAL schema only. Not in application data models. Not triggerable.
- **`queueEnabled`** — Active. True when TrackMate™ session active.
- **`offlineBeacon`** — Active. True when BLE Mesh broadcasting.
- **`partialSignal`** — Active. True on degraded connectivity. No automated recovery. UI must be calm.

### Transport Stack (TrackMate™ — FSD-5126 §6.2, VGD-5126 §5.2)
| Tier | Mechanism | Range | Phase |
|---|---|---|---|
| Tier 1 Primary | BLE Mesh (continuous background) | ~100m + multi-hop | Phase 1 |
| Tier 1 Fallback | Wi-Fi Direct (on-demand only) | ~200m line-of-sight | Phase 1 |
| Tier 2 | LoRa peripheral (auto-detected) | 5–15km open terrain | Phase 1 |
| Phase 2 only | Satellite relay | Global | **Phase 2 — NOT in Phase 1 build** |

### 6 Phase 1 Archetypes (TAA-5126 / PRD-5126 §5.3)
1. 4WD Explorers & Remote Long-Range Travellers
2. Bushwalkers & Hikers
3. Mountain Bikers / eBike / Motorbike
4. Remote Professionals
5. Fish & Hunt (preset Phase 1 · activity context depth Phase 2.5)
6. Snow & Alpine (preset Phase 1 · full module Phase 2.5 · whiteout wireframes mandatory Phase 1)

### 6 PCR Categories (Phase 1 — OSM-5026 §10.2, FSD-5126 §13.1)
PCR-OBS Obstruction · PCR-CLO Closure · PCR-INF Infrastructure Damage · PCR-SRF Surface Condition · PCR-WTR Water Crossing · PCR-HAZ Localised Hazard.

PCR resolution = **supersession only** (NOT TTL). Original archived NOT deleted on supersession.

### 8 Phase 1 Valid Overlay States (OSM-5026 §13, FSD-5126 §13)
Combinations of Difficulty (known/unknown) × Verification Shield (None/Grey/Gold) × PCR (none/active). 8 valid combinations. Anything else = QA failure.

### Performance Targets (PRD-5126 §6, FSD-5126 §10)
| Metric | Target |
|---|---|
| Warm start | ≤3s |
| Cold start (bundle ≤500MB) | ≤6s |
| Cold start (>500MB) | ≤8s |
| Map tile render | ≤2s |
| Overlay toggle | ≤1s |
| SOS UI response | ≤0.5s |
| SOS log write (GPS warm) | ≤3s |
| BackTrack™ retrace load | ≤3s |
| Battery (active nav) | ≤8%/hr (BPS-5126) |
| Offline endurance | ≥10 hours |
| SOS / distress mode battery | ≤20%/hr (BPS-5126 §3.5) |

### Confirmed Technology Stack (FSD-5126 §3, AOD-5026 §6)
| Component | Technology |
|---|---|
| Mobile framework | **Flutter (Dart)** — cross-platform iOS + Android |
| Mapping engine | **Mapbox SDK + OSM vector tiles** |
| Backend / cloud | **Firebase** (Firestore offline — non-Survival Core only) |
| Survival Core persistence | **Local device storage** — Firebase-independent |
| Encryption at rest | AES-256 |
| Encryption in transit | TLS 1.3 |
| Design system | Figma + WFD-5126 |

---

## Cross-document concept map

```
                            UXS-5726 (highest — behavioural)
                              ↓
                            PRD-5126 (acceptance)
                              ↓
                            FSD-5126 (functional execution)
                              ↓
                            TQP-5026 (validation)
                              ↓
                            WFD-5126 (UI states + build gate)
                              ↓
                            VGD-5126 (vendor enforcement)
                              ↓
              Tier 2 specialist (OSM/HFG/ESF/CDG/BPS/BTF/TAA/MAS/FRM)
                              ↓
                            AOD-5026 (architecture reference)
                            PSB-5026 (phase scope boundary)
                            OCS-5026 (operations console)
                              ↓
                            CAR-5026 (living amendment register)
```

**Conflict resolution rule:** All conflicts escalate UPWARD. Cannot be resolved by delivery partner. Project Director = sole resolution authority.

---

## Outstanding extractions

**Pass 2 complete (2026-05-26):** UXS-5726, OSM-5026, WFD-5126, BPS-5126, TAA-5126 written. Plus bonus vendor-pack: FQH-5026, SFD-5026.

**Still NOT extracted (confirmed not in current Drive folder):**
1. **FRM-5126** — First Aid Reference Framework. Referenced as `FRM-5226` (typo? — superseded series ID) in WFD-5126 §5.9 mandatory disclaimer rule and §5.9 Universal Baseline accessibility rule (A-15). Documented as **internal authority document — not vendor-distributed**. Vendor-facing obligations fully implemented through WFD §5.9, TAA §9F, OSM-5026.
2. **CAR-5026** — Central Amendment Register. Living doc — single source of amendment history. Not in Drive folder. Should be requested separately.

**Synced delivery doc (2026-05-28):** [Slitigenz-Proposal-RFT5026.md](./Slitigenz-Proposal-RFT5026.md) — vendor delivery plan extract (locked gates · 9 Discovery artefacts · workstream/effort · clarifications). Feeds `docs/planning.md` (single planning + backlog source).

**Open mismatches flagged for Project Director resolution:**
- **7 vs 8 workstream tracks:** Slitigenz proposal §10.3 prose says "seven (7) tracks (VEG-5026 §7.3)" but the §10.3.1 effort table lists **8 tracks** (adds Track 8 OCS) and "Lean Senior Squad of 8 Experts". Also still only 7 expert names confirmed (Khanh · Tru · Khoi · Viet · Hoang · Thom · Duong). Confirm 7 vs 8.
- **VEG-5026 vs VGD-5126:** proposal §10.3 cites "VEG-5026 §7.3" but Authority Stack documents VGD-5126 as Priority 6 enforcement authority. Disambiguate.
- **FRM-5226 vs FRM-5126:** WFD-5126 §5.9 cites "FRM-5226"; TAA-5126 §8.1 cites "FRM-5126". DDS-1226 supersession convention suggests FRM-5126 is current. Confirm.
- ~~**Discovery gate date**~~ ✅ **RESOLVED → 15 June 2026** (Slitigenz proposal §10.2; Contract Execution gate 29 May added).

---

## How to use these extracts

- **For business analysis:** Read README index first → drill into specific doc by topic (e.g. "what governs SOS?" → ESF-5026 + FSD-5126 §4.4)
- **For governance traceability:** every claim in vendor responses must trace to specific doc + section. Use the Authority Hierarchy table to identify governing doc.
- **For conflict resolution:** identify both docs in conflict → resolve UPWARD per hierarchy (e.g. UXS-5726 always wins over FSD-5126).
- **For static analysis CI:** see TQP-5026 §7 + CDG-5126 §4.3 (14 prohibited breadcrumb operations) + ESF-5026 §8 (prohibited field names).

> ⚠️ These extracts are **summaries optimised for analysis**. For authoritative wording, always reference the original PDFs in the Drive folder. In any conflict between extract + original PDF, **original PDF prevails**.
