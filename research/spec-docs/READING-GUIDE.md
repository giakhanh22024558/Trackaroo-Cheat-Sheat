# Trackaroo® Phase 1 — Reading Guide & Document Clustering

**Mục đích:** Hướng dẫn đọc 19 tài liệu spec theo trình tự logic để **một Project Manager** và **một System Architect** có thể nắm được bức tranh tổng quan của toàn hệ thống — không bị lạc giữa rừng cross-reference.

**Cách dùng:**
1. Đọc Section 1 (Document Clustering) để hiểu **6 nhóm nội dung** và lý do gom nhóm.
2. Theo Section 2 (PM Reading Path) hoặc Section 3 (Architect Reading Path) — tùy vai trò.
3. Section 4 (Common Cross-Cutting Concepts) — cả hai vai trò đều phải nắm.
4. Section 5 (Quick Lookup Table) — tra ngược "câu hỏi → doc nào trả lời".

---

## Section 1 — Document Clustering (6 nhóm nội dung)

### Bản đồ tổng quát

```
┌─────────────────────────────────────────────────────────────────────────┐
│  NHÓM 1 — STRATEGIC FOUNDATION  (Tầm nhìn · Phạm vi · Đối tượng)        │
│  PSB-5026  ·  UXS-5726  ·  TAA-5126  ·  FQH-5026                        │
│  "Trackaroo là gì · cho ai · làm gì · không làm gì · success là gì"     │
└─────────────────────────────────────────────────────────────────────────┘
                                  ↓
┌─────────────────────────────────────────────────────────────────────────┐
│  NHÓM 2 — SYSTEM ARCHITECTURE  (Kiến trúc tổng thể)                     │
│  AOD-5026  ·  FSD-5126  ·  CDG-5126  ·  MAS-5126                        │
│  "Dual-Layer Architecture · data classification · Mapbox engine"        │
└─────────────────────────────────────────────────────────────────────────┘
                                  ↓
┌──────────────────────────────────────┐  ┌──────────────────────────────┐
│  NHÓM 3 — SURVIVAL CORE SUBSYSTEMS   │  │  NHÓM 4 — EXPERIENCE LAYER   │
│  (Safety-critical · 100% offline)    │  │  (Map UI · Overlays · PCR)   │
│  ESF-5026 + SFD-5026 (SOS)           │  │  OSM-5026  (overlay rules)   │
│  BTF-5126 (BackTrack™)               │  │  WFD-5126  (UI states +      │
│  HFG-5026 (Hazard feeds)             │  │             build gate)      │
└──────────────────────────────────────┘  └──────────────────────────────┘
                                  ↓
┌─────────────────────────────────────────────────────────────────────────┐
│  NHÓM 5 — ACCEPTANCE, PERFORMANCE & QA  (Tiêu chí nghiệm thu)           │
│  PRD-5126  ·  TQP-5026  ·  BPS-5126                                     │
│  "Acceptance criteria · 11 validation domains · battery/perf targets"   │
└─────────────────────────────────────────────────────────────────────────┘
                                  ↓
┌─────────────────────────────────────────────────────────────────────────┐
│  NHÓM 6 — VENDOR GOVERNANCE & OPERATIONS  (Quản lý đối tác · vận hành)  │
│  VGD-5126  ·  OCS-5026                                                  │
│  "Vendor enforcement · rejection triggers · ops console nội bộ"         │
└─────────────────────────────────────────────────────────────────────────┘
```

---

### Nhóm 1 — STRATEGIC FOUNDATION (Tầm nhìn & Phạm vi)

**4 tài liệu · ~70 trang · đọc đầu tiên · cả PM và Architect đều phải đọc**

| Doc | Vai trò | Lý do thuộc nhóm này |
|---|---|---|
| **PSB-5026** | Phase Scope Boundary | Định nghĩa **Phase 1 vs Phase 2/3** — cái gì in scope, cái gì out scope. 3 permitted Phase 2 scaffolds (BT Escrow · CAL satReady · CAL satellite pathway). Đọc trước để khỏi "lạc" sang Phase 2 features. |
| **UXS-5726** | Behavioural Authority (Priority 1 — cao nhất) | Đây là **nguồn của mọi quy tắc hành vi**: offline-first supremacy · 5-question hierarchy · ≤2-tap SOS · prohibited claims register · 6 archetypes. Mọi conflict đều resolve lên doc này. |
| **TAA-5126** | Target Archetypes + Tier Philosophy | Định nghĩa **đối tượng người dùng** (6 archetypes) + commercial framework (Free/Plus/Pro) + nguyên tắc "monetises specialisation, never survival". Universal Baseline luôn miễn phí. |
| **FQH-5026** | 5-Question Cognitive Hierarchy Visual | Chỉ 3 trang — tóm tắt **primary UX acceptance criterion**: 5 câu hỏi user phải trả lời được "without deliberation, offline, with gloves, under stress". Đọc nhanh nhưng quan trọng. |

> **Tại sao gom thành 1 nhóm:** Cả 4 doc trả lời câu hỏi *"Trackaroo là sản phẩm gì, dành cho ai, định nghĩa thành công như thế nào"*. Không thể bắt đầu phân tích kỹ thuật trước khi nắm 4 doc này.

---

### Nhóm 2 — SYSTEM ARCHITECTURE (Kiến trúc hệ thống)

**4 tài liệu · ~150 trang · đọc thứ 2 · ưu tiên Architect**

| Doc | Vai trò | Lý do thuộc nhóm này |
|---|---|---|
| **AOD-5026** | Architecture Overview Document | **Bức tranh dual-layer architecture** lớn nhất: Survival Core (100% offline, deterministic) ⇎ Experience & Intelligence Layer (online-tolerant). Component inventory. Phải đọc đầu tiên trong nhóm. |
| **FSD-5126** | Functional Specification (Priority 3) | Đặc tả **execution baseline** cho mọi subsystem: CAL state flags, transport tier stack, breadcrumb intervals (15m/20s std · 5m/5s distress), PCR framework execution model. |
| **CDG-5126** | Cloud & Data Governance | Sole authority cho **data classification**: Local-Only · Non-Syncable · Survival Core data **không bao giờ chạm Firebase**. 14 prohibited breadcrumb mutations. |
| **MAS-5126** | Mapping Architecture & Visual System | Mapbox SDK + OSM vector tiles. **Map provider agnostic** rule. PCR icon design là vendor deliverable thuộc MAS Part B. |

> **Tại sao gom thành 1 nhóm:** Cả 4 doc trả lời câu hỏi *"Hệ thống được xây dựng như thế nào về mặt kỹ thuật"*. AOD cho big picture, FSD cho execution, CDG cho data boundary, MAS cho rendering.

---

### Nhóm 3 — SURVIVAL CORE SUBSYSTEMS (Safety-critical layer)

**4 tài liệu · ~120 trang · đọc thứ 3 · ưu tiên Architect, PM đọc lướt**

| Doc | Subsystem | Lý do thuộc nhóm này |
|---|---|---|
| **ESF-5026** | Emergency Safety Framework | Quy định **SOS liability boundary**: non-dispatch posture, zero transmission, immutable log, satellite field prohibition (§8). LE-02 legal review. |
| **SFD-5026** | SOS Flow Diagram (vendor pack) | **Annotated swim-lane diagram** của SOS: 3-stage log sequence · 6 confirmation feedback elements · 12-state ≤2-tap coverage matrix. Bonus doc nhưng cực kỳ chi tiết cho dev. |
| **BTF-5126** | BackTrack™ Framework | Breadcrumb integrity · retrace ≤3 seconds · ≤3-tap access · 14 prohibited mutations · Phase 2 Emergency Escrow schema (inert). |
| **HFG-5026** | Hazard Feed Governance | Hazard ingestion rules: **5-Pillar Filter** · authority-origin rule · TTL thresholds theo source type. |

> **Tại sao gom thành 1 nhóm:** Cả 4 doc mô tả **4 subsystem của Survival Core** — phải tuân thủ chung 1 bộ rules: 100% offline · deterministic · non-adaptive · Firebase-independent · zero outbound packets. ESF+SFD đi đôi (governance + flow diagram).

---

### Nhóm 4 — EXPERIENCE & INTELLIGENCE LAYER (Map UI + Overlays)

**2 tài liệu · ~50 trang · đọc thứ 4 · cả PM và Architect**

| Doc | Vai trò | Lý do thuộc nhóm này |
|---|---|---|
| **OSM-5026** | Overlay Semantics Map (sole authority) | **Sole authority** cho overlay visual rules: difficulty colours · Gold/Grey/No Shield · PCR framework (6 categories · supersession-only resolution) · 8 valid overlay states · LIR-01–06 · RG-01–11 rollback governance. |
| **WFD-5126** | Wireframe & UI State Authority + **build gate** | **Build gate** cho mọi subsystem: không có wireframe approval = không được phép code. Định nghĩa PCR-WF-01→06 · LoRa onboarding 4 states · Snow & Alpine whiteout states. |

> **Tại sao gom thành 1 nhóm:** OSM defines *"overlay visual rules là gì"*, WFD defines *"UI state nào hợp lệ và đã được approve"*. WFD §5.17 trực tiếp implement OSM §10.6. Đi đôi không tách được.

> **Tách OSM/WFD khỏi Survival Core?** Có — vì PCR và overlay UI là **Experience layer**, không phải safety-critical. Tuy nhiên PCR data persistence vẫn theo CDG-5126 rules (Local-Only base + Firestore sync cache mode).

---

### Nhóm 5 — ACCEPTANCE, PERFORMANCE & QA (Tiêu chí nghiệm thu)

**3 tài liệu · ~140 trang · đọc thứ 5 · ưu tiên PM**

| Doc | Vai trò | Lý do thuộc nhóm này |
|---|---|---|
| **PRD-5126** | Product Requirements & Acceptance Authority (Priority 2) | **22 named Rejection Triggers (RT-01→22)** · acceptance criteria · 4 commercial gates (Discovery · Alpha · Beta-Ready · GA). PM-must-read. |
| **TQP-5026** | Testing & QA Authority (Priority 4) | **11 validation domains** · exit criteria XC1–XC9 · static analysis rules · five-question hierarchy testing across 6 archetypes. |
| **BPS-5126** | Battery Performance Standard | Sole authority cho battery: ≤8%/hr nav · ≥10hr endurance · ≤20%/hr SOS distress · device matrix (current + 2 prior generations iOS/Android). |

> **Tại sao gom thành 1 nhóm:** Trả lời câu hỏi *"Đo lường thành công như thế nào · gate nào sẽ fail · vendor phải pass cái gì"*. PRD nêu **WHAT** cần pass, TQP nêu **HOW** test, BPS nêu **threshold số liệu** cụ thể nhất (battery — vì battery là exit criterion XC9).

---

### Nhóm 6 — VENDOR GOVERNANCE & OPERATIONS (Quản lý đối tác & vận hành nội bộ)

**2 tài liệu · ~80 trang · đọc thứ 6 · ưu tiên PM**

| Doc | Vai trò | Lý do thuộc nhóm này |
|---|---|---|
| **VGD-5126** | Vendor Enforcement Authority (Priority 6) | Contractual layer: **rejection triggers** liên kết với contract clauses · gate clearance discipline · written PD sign-off required. Cách Trackaroo "kẹp" vendor. |
| **OCS-5026** | Operations Console Specification | **Tool nội bộ** của Trackaroo: 9 modules · 3-role RBAC · break-glass intervention · không phải sản phẩm vendor delivery. PM của Trackaroo dùng OCS hàng ngày. |

> **Tại sao gom thành 1 nhóm:** Đây là **lớp governance + operational tooling** xung quanh sản phẩm — không phải bản thân sản phẩm. VGD nói *"vendor phải làm gì để không bị reject"*, OCS nói *"Trackaroo internal team vận hành sản phẩm bằng tool gì sau khi GA"*.

---

## Section 2 — PM Reading Path (Project Manager — 8 bước · ~3 ngày)

**Mục tiêu:** Sau khi đọc xong, PM nắm được scope, gate timeline, rejection risks, vendor governance, commercial framework.

### Bước 1 — PSB-5026 (1 giờ)
**Câu hỏi đặt trước khi đọc:** *"Phase 1 release gồm cái gì, KHÔNG gồm cái gì?"*

**Take-away phải nhớ:**
- 4 gates: Discovery (15 May/Jun) → Alpha (22 Aug) → Beta-Ready (30 Oct) → GA (13 Nov 2026)
- **3 permitted Phase 2 scaffolds** (EXHAUSTIVE list): BT Escrow schema · CAL satReady · CAL satellite pathway
- Mọi scaffold khác = **RT-09 rejection trigger**

### Bước 2 — UXS-5726 (4 giờ)
**Câu hỏi:** *"Nguyên tắc bất di bất dịch nào ràng buộc cả product?"*

**Take-away:**
- 5-Question Cognitive Hierarchy = primary acceptance criterion
- Offline-first supremacy · Dual-Layer separation immutable
- Prohibited claims register (không được nói "rescue dispatched", "monitoring", v.v.)
- Liability position: **decision-support tool, NOT dispatch/monitoring/medical device**

### Bước 3 — FQH-5026 (15 phút — chỉ 3 trang)
**Câu hỏi:** *"5 câu hỏi đó là gì, subsystem nào trả lời?"*

**Take-away:** In ra giấy, treo cạnh bàn làm việc. Đây là 1-page acceptance sheet.

### Bước 4 — TAA-5126 (3 giờ)
**Câu hỏi:** *"Sản phẩm bán cho ai, thu tiền bằng cách nào, không thu tiền ở đâu?"*

**Take-away:**
- 6 archetypes (4WD · Bushwalkers · MTB · Remote Pro · Fish&Hunt · Snow&Alpine)
- Tier function matrix Free/Plus/Pro — **PCR + SOS + BackTrack active session + Universal Baseline = always free**
- Upgrade triggers must be **competence-based, never fear-based**
- Nomad sub-profile (cross-archetype)

### Bước 5 — PRD-5126 (1 ngày)
**Câu hỏi:** *"Vendor phải pass cái gì, fail ở đâu sẽ bị reject?"*

**Take-away:**
- **22 Rejection Triggers RT-01→22** — in ra danh sách, đánh dấu RT-01, RT-09, RT-13, RT-14, RT-15, RT-16, RT-22 là high-impact
- Acceptance criteria mapping theo gate
- Commercial gate timeline (cùng với PSB-5026 §gate)
- V-07 device validation matrix obligation

### Bước 6 — VGD-5126 (3 giờ)
**Câu hỏi:** *"Làm sao Trackaroo enforce vendor compliance bằng hợp đồng?"*

**Take-away:**
- Rejection triggers → contract clause links
- Written PD sign-off required mỗi gate
- WFD-5126 build gate = vendor obligation pre-development
- Fixed-price rework risk discipline

### Bước 7 — TQP-5026 (4 giờ)
**Câu hỏi:** *"QA evidence vendor phải submit ở mỗi gate là gì?"*

**Take-away:**
- 11 validation domains
- Exit criteria XC1–XC9 (battery = XC9)
- 23 QA Acceptance Register rules (QAR-01→23 — chéo với UXS-5726)
- 12 PCR test scenarios (§5.9)

### Bước 8 — OCS-5026 (3 giờ)
**Câu hỏi:** *"Sau GA, internal team vận hành sản phẩm như thế nào?"*

**Take-away:**
- 9 OCS modules (HazTrack admin · PCR admin · user support · break-glass · audit log...)
- 3-role RBAC (Founder/Admin/Operator)
- Break-glass intervention — duy nhất 1 path từ web vào hệ thống

**Sau 8 bước:** PM đã có đủ context để (a) chair vendor gate review, (b) audit deliverable submission, (c) cảnh báo PD khi vendor proposal touch vùng cấm.

---

## Section 3 — System Architect Reading Path (10 bước · ~5 ngày)

**Mục tiêu:** Sau khi đọc xong, Architect có thể design implementation, vẽ DFD/sequence diagrams, identify compliance pitfalls trước khi vendor đụng vào.

### Bước 1 — PSB-5026 (1 giờ)
**Lý do đọc đầu:** Biết boundary discipline TRƯỚC khi nhìn architecture. Tránh "vẽ Phase 2 features vào Phase 1 build".

### Bước 2 — UXS-5726 (4 giờ)
**Lý do:** Cấp 1 authority — mọi quyết định kiến trúc phải subordinate. Đặc biệt focus §3 (5-Q hierarchy) · §7 (SOS) · §13 (archetypes) · §9 (BackTrack).

### Bước 3 — AOD-5026 (3 giờ)
**Câu hỏi:** *"Dual-Layer Architecture trông như thế nào, components là gì?"*

**Take-away:**
- Survival Core ⇎ Experience & Intelligence Layer (immutable separation)
- CAL (Comms Abstraction Layer) — 4 state flags
- Component inventory: MOB-1xxx (App Layer) · MOB-2xxx (Survival Core) · CBE-5xxx (TrackIQ Pipeline) · OCS-5xxx · SYN-7xxx
- Đối chiếu với `diagrams/1-overview/trackaroo-phase1-architecture.md`

### Bước 4 — FSD-5126 (1 ngày)
**Câu hỏi:** *"Execution-level: state transitions, intervals, parallelism như thế nào?"*

**Take-away:**
- §4.4 SOS execution detail (đọc kèm SFD-5026)
- §6.1.1 CAL state flag schema
- §6.2 Transport tier stack (BLE Mesh → Wi-Fi Direct → LoRa → [Phase 2 Sat])
- §4.3.4 PCR 90-day unconfirmed threshold (implementation parameter)
- §10 Performance targets bảng đầy đủ

### Bước 5 — CDG-5126 (3 giờ)
**Câu hỏi:** *"Data nào ở đâu, được phép sync ở đâu?"*

**Take-away:**
- **Local-Only · Non-Syncable** classification cho Survival Core data (breadcrumb, SOS log)
- Firestore offline persistence cho non-Survival Core (PCR submission cache · TrackMate group state · profile)
- **14 prohibited breadcrumb mutations** — static analysis CI rule (RT-13)
- Firebase isolation barrier diagram

### Bước 6 — MAS-5126 (2 giờ)
**Câu hỏi:** *"Map rendering hoạt động ra sao, offline tile bundle như thế nào?"*

**Take-away:**
- Mapbox SDK chỉ dùng cho rendering, **không phụ thuộc Mapbox cloud services** ở runtime
- OSM vector tiles bundled offline
- PCR icon design = vendor deliverable (Part B)
- Map provider agnostic rule — không hard-code Mapbox-specific behaviour

### Bước 7 — ESF-5026 + SFD-5026 đi cặp (4 giờ)
**Lý do đi cặp:** ESF = governance (luật pháp + non-dispatch posture), SFD = execution flow diagram (3-stage log + ≤2-tap matrix).

**Take-away:**
- 3-stage SOS log sequence (CR02 design decision 21 Mar 2026): Stage 1 timestamp+deviceID ngay tại Tap 2 không cần GPS · Stage 2 GPS pending · Stage 3 coords appended on fix
- 6 mandatory confirmation feedback elements
- 12-state ≤2-tap coverage matrix
- **Zero outbound packet rule** ở app process boundary (OS-level services ngoài scope)
- Satellite field name prohibition list (§8)
- LE-02 legal copy review pending Alpha gate

### Bước 8 — BTF-5126 (3 giờ)
**Câu hỏi:** *"Breadcrumb storage + BackTrack retrace?"*

**Take-away:**
- WAL (Write-Ahead Log) + AES-256 per-record encryption
- ≤3s retrace load · ≤3-tap access
- 14 prohibited mutations (cross-ref CDG-5126)
- Phase 2 Emergency Escrow schema = scaffold #1 (inert)
- Distress mode 5m/5s interval activates parallel với Stage 1 log

### Bước 9 — HFG-5026 (2 giờ)
**Câu hỏi:** *"Hazard feed nào được phép ingest, cache ra sao?"*

**Take-away:**
- 5-Pillar Filter (authority-origin · jurisdiction · format · TTL · sanitisation)
- Per-source-type TTL thresholds (fire/flood/closure/storm/earthquake)
- HazTrack Firebase ingress = cache-only exception (§7 cache-only rule)

### Bước 10 — OSM-5026 + WFD-5126 đi cặp (1 ngày)
**Lý do đi cặp:** OSM defines *visual semantic rules*, WFD defines *UI state implementation* — phải đọc song song.

**Take-away:**
- 8 valid overlay states (Difficulty × Shield × PCR present)
- LIR-01→06 layer independence rules
- RG-01→11 rollback governance triggers
- 6 PCR categories + supersession-only resolution
- 90-day unconfirmed muted display threshold
- PCR-WF-01→06 wireframe states (build gate prerequisite)
- TrackMate™ LoRa 4 onboarding states (RT-19)
- Snow & Alpine whiteout states (Phase 1 mandatory, full module Phase 2.5)

### Bước phụ — BPS-5126 (2 giờ) + TQP-5026 §7 static analysis (2 giờ)
**Trước Alpha gate:** Đọc BPS-5126 để biết test conditions chuẩn (10 parameters, airplane mode, 50% brightness, 18–24°C...). TQP §7 cho rules CI/CD static analysis.

**Sau 10 bước:** Architect đủ context để vẽ implementation DFD, design API contracts giữa CAL & Survival Core, identify Firebase isolation violation trong PR review.

---

## Section 4 — Common Cross-Cutting Concepts (cả PM và Architect phải nắm)

### A. Authority Stack — Conflict resolution rule

```
UXS-5726 (Priority 1) > PRD-5126 (2) > FSD-5126 (3) > TQP-5026 (4) > WFD-5126 (5) > VGD-5126 (6)
                                       ↓
                          Tier 2 specialists (OSM/HFG/ESF/CDG/BPS/BTF/TAA/MAS/FRM)
                                       ↓
                          Architecture & ops (AOD/PSB/OCS)
```

**Mọi conflict resolve UPWARD. Project Director là sole resolution authority. Vendor không được tự quyết.**

### B. 4 Phase 1 Commercial Gates

| Gate | Date | Vendor evidence cần submit |
|---|---|---|
| Discovery | 15 May/Jun 2026 (cần PD confirm) | 8/9 compliance artefacts · CAL doc · WFD coverage · companion site · SDK audit · OSS audit |
| Alpha | 22 Aug 2026 | Survival Core validated · SOS onboarding · clinical review · prohibited-capability scan · OCS Stage 1 ready |
| Beta-Ready | 30 Oct 2026 | 11 TQP domains · WCAG 2.1 AA · 22 RTs resolved · OCS modules · **RT-16 legal review complete** |
| GA | 13 Nov 2026 | App Store + Play submissions live · written PD go/no-go sign-off |

### C. The 5-Question Cognitive Hierarchy (acceptance floor)

User phải trả lời được 5 câu hỏi sau **WITHOUT DELIBERATION, OFFLINE, WITH GLOVES, UNDER STRESS, IN LOW LIGHT, ON FIRST USE**:

1. **Where am I?** — Navigation Engine + Offline Map
2. **Where am I going?** — Route Planning + Breadcrumb Trail
3. **What surrounds me?** — HazTrack™ + Overlays
4. **How do I get back?** — BackTrack™ (≤3 taps, ≤3 seconds)
5. **How do I call for help?** — SOS (≤2 taps)

### D. 22 Rejection Triggers (RT-01 → RT-22) — high-impact ones

| RT | Mô tả | Domain |
|---|---|---|
| RT-01 | Satellite SDK present/triggerable | ESF/CAL |
| RT-02 | Autonomous rerouting | Nav |
| RT-03 | AI inference logic | Survival Core |
| RT-05 | Cloud breadcrumb storage | BTF/CDG |
| RT-06 | Monitoring posture implied | UXS |
| RT-09 | Phase 2+ scaffold triggerable | PSB |
| RT-13 | Breadcrumb immutability compromised | BTF/CDG |
| RT-14 | HazTrack™ alters TrackIQ™ grade | OSM/LIR |
| RT-15 | SOS ≤2-tap failure | ESF/SFD |
| RT-16 | ESF legal review incomplete (Beta-Ready) | ESF |
| RT-19 | PCR TTL logic (must be supersession-only) | OSM |
| RT-22 | Tier restriction on SOS distress mode | TAA/BPS |

### E. The 3 Permitted Phase 2 Scaffolds (EXHAUSTIVE)

Mọi scaffold KHÁC = RT-09 rejection trigger.

1. **BackTrack™ Emergency Escrow data schema** — schema only · non-executable
2. **CAL `satReady` flag** — declared FALSE · NOT activatable · CAL schema only (KHÔNG được xuất hiện trong app data models)
3. **CAL satellite transport architectural pathway** — documented · NOT executable · extensible CAL interface only

Mỗi scaffold phải pass 4 QA visibility tests: (a) visually surfaced · (b) display chính xác "Inactive in Phase 1." · (c) schema-complete · (d) zero executable logic.

### F. Zero Transmission Boundary (ESF-5026 §4.2)

**Scope:** application process boundary.
**In scope cấm:** HTTP · HTTPS · UDP · TCP socket · SDK callback từ Survival Core path.
**Ngoài scope:** OS-level services (iOS daemons · Android push infrastructure · system telemetry).

### G. Tech Stack confirmed

| Layer | Tech |
|---|---|
| Mobile | Flutter (Dart) — cross-platform iOS 15+ / Android 13+ |
| Map | Mapbox SDK + OSM vector tiles (offline bundled) |
| Cloud (non-Survival Core only) | Firebase Firestore + offline persistence |
| Survival Core persistence | SQLite + WAL + AES-256 (local-only) |
| Encryption transit | TLS 1.3 |
| Web (OCS) | React + Firebase Auth + RBAC + TLS 1.3 |

---

## Section 5 — Quick Lookup Table (câu hỏi → doc)

| Câu hỏi nghiệp vụ thường gặp | Doc trả lời chính | Doc bổ sung |
|---|---|---|
| Sản phẩm dành cho ai? | TAA-5126 §5 | UXS-5726 §13 |
| Phase 1 gồm cái gì? | PSB-5026 | PRD-5126 §3 |
| SOS hoạt động ra sao? | SFD-5026 | ESF-5026 + FSD §4.4 |
| Battery target bao nhiêu? | BPS-5126 §3 | FSD-5126 §10 |
| PCR có ở Free tier không? | TAA-5126 §9A + §14.2 | OSM-5026 §10 |
| TrackMate transport stack? | FSD-5126 §6.2 | BPS-5126 §3.3 |
| BackTrack retrace ≤? giây? | BTF-5126 §3 | UXS-5726 §9 |
| Wireframe nào cần approve trước khi code? | WFD-5126 §9 | OSM §10.6 |
| OCS có những module gì? | OCS-5026 | (chỉ doc này) |
| Vendor reject vì lý do gì? | PRD-5126 §14.4 (22 RTs) | VGD-5126 |
| QA evidence phải submit gì? | TQP-5026 | BPS §6.2 + ESF §4.4 |
| Difficulty colour code? | OSM-5026 §5 | MAS-5126 |
| Phase 2 scaffold được phép? | PSB-5026 §4 | (chỉ doc này) |
| Hazard feed nào hợp lệ? | HFG-5026 | OSM-5026 §6 |
| Tile rendering offline? | MAS-5126 | AOD-5026 §6 |
| Data nào KHÔNG được sync lên Firebase? | CDG-5126 §3-4 | BTF §5 |
| Operations Console RBAC? | OCS-5026 §3 | (chỉ doc này) |
| Universal Baseline First Aid là gì? | WFD-5126 §5.9 (A-15) | TAA §8.1 + §9F |
| Snow & Alpine module khi nào ra? | TAA-5126 §11.2 | WFD §5.14 |
| LoRa onboarding states? | WFD-5126 §5.8 | TAA §9C |

---

## Phụ lục — Thứ tự ưu tiên đọc cho 1 buổi (4 tiếng)

Nếu chỉ có **4 tiếng** để onboard:
1. **PSB-5026** (30 phút) — biết scope
2. **FQH-5026** (15 phút) — 5-Q acceptance criterion
3. **UXS-5726** đọc §3 + §7 + §13 + §9 (1 tiếng) — behavioural floor
4. **AOD-5026** (1 tiếng) — dual-layer architecture picture
5. **PRD-5126 §14.4** (30 phút) — 22 rejection triggers
6. **README.md + READING-GUIDE.md (file này)** (15 phút) — bản đồ tổng

Còn lại 30 phút: skim README **Quick reference** table.

---

## Sign-off

> **Bản đồ này không thay thế nội dung tài liệu gốc.** Mọi extract trong `research/spec-docs/` đều là **summary tối ưu cho phân tích nghiệp vụ**. Trong mọi conflict giữa extract và PDF gốc, **PDF gốc thắng**. Trong mọi conflict giữa documents, áp dụng Authority Stack — escalate lên Project Director.

> *Maintained alongside `README.md` (index) và `CLAUDE.md` (working conventions). Cập nhật khi có doc mới được extract hoặc khi authority stack thay đổi.*
