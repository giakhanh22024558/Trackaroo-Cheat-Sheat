# trackaroo® Phase 1 — Deterministic State Transition Matrix

This document satisfies the Discovery-Gate prerequisite cited in **FEAT-1.1**, **FEAT-2.1**, **FEAT-3.1**, **FEAT-4.4** and **FEAT-6.1** (AOD-5026 §7). It contains:

1. Six state-machine diagrams — one per Survival Core subsystem plus a cross-cutting crash-recovery overlay.
2. An inter-layer isolation diagram proving that Experience-Layer events cannot mutate Survival Core state.
3. A prohibition register listing the negative-space transitions (the things that must *never* happen) and how each is enforced.

---

## How to import into draw.io

1. Open <https://app.diagrams.net/> (or your desktop draw.io).
2. **Extras → Edit Diagram…** (alternatively **Arrange → Insert → Advanced → Mermaid**).
3. Copy a single ```` ```mermaid ```` block below (the code only, without the fences).
4. Paste into the Mermaid dialog and click **Insert**.
5. Repeat for each diagram. Each is independent and self-contained.

---

## 1. Offline Navigation Engine — FEAT-1.1

The largest state space. Every transition is triggered by a single deterministic input (user action, OS-level GPS boolean, or geometric point-in-polygon test). No probabilistic, AI, or telemetry-weighted transitions exist.

```mermaid
graph TD
    START(("●")) --> OFF["🔌 OFF<br/>App not running"]
    OFF -->|"Cold launch"| WARM_READY["✅ WARM_READY<br/>Map loaded · idle"]
    WARM_READY -->|"Warm resume"| WARM_READY
    WARM_READY -->|"User selects destination"| NAVIGATING["🧭 NAVIGATING<br/>Turn-by-turn active"]
    NAVIGATING -->|"GPS signal lost"| GPS_LOST["📡 GPS_LOST<br/>No fix"]
    GPS_LOST -->|"GPS fix reacquired"| NAVIGATING
    NAVIGATING -->|"Cross region boundary"| OUT_OF_REGION["🗺️ OUT_OF_REGION<br/>Outside tile set"]
    OUT_OF_REGION -->|"Re-enter region"| NAVIGATING
    NAVIGATING -->|"Stop-detect (10min, &lt;15m)"| STOPPED["⏸️ STOPPED<br/>Movement halted"]
    STOPPED -->|"User dismisses or resumes"| NAVIGATING
    NAVIGATING -->|"HazTrack hazard intersects route"| NOTIFIED["⚠️ NOTIFIED<br/>Hazard on route"]
    NOTIFIED -->|"User accepts / declines alternate"| NAVIGATING

    N_OFF["📝 Cold launch ≤6s (≤500MB) / ≤8s (&gt;500MB)<br/>Warm resume ≤3s · Ref CQR-5026, BPS-5126 §6.1"]
    N_NAV["📝 From ANY state: SOS ≤2 taps · BackTrack ≤3 taps<br/>Dest: map tap | regional POI | Safe Anchor | lat-long<br/>External address search PROHIBITED"]
    N_NOTIFIED["📝 5-step Declarative Consent Model<br/>NO autonomous reroute — RT-02 · Ref HFG-5026 §5.4"]
    N_GPS["📝 Last known position + staleness indicator<br/>Breadcrumb capture PAUSES · gap = void (no interpolation)"]
    N_OOR["📝 Tiles render BLANK · GPS + breadcrumb CONTINUE<br/>Turn-by-turn CEASES · Ref CQR-5026 (CR04 Q3)"]

    OFF -.- N_OFF
    NAVIGATING -.- N_NAV
    NOTIFIED -.- N_NOTIFIED
    GPS_LOST -.- N_GPS
    OUT_OF_REGION -.- N_OOR

    classDef startEnd fill:#263238,stroke:#263238,stroke-width:2px,color:#fff
    classDef idle fill:#ECEFF1,stroke:#607D8B,stroke-width:2px,color:#263238
    classDef ready fill:#E3F2FD,stroke:#1976D2,stroke-width:2px,color:#0D47A1
    classDef active fill:#E8F5E9,stroke:#2E7D32,stroke-width:3px,color:#1B5E20
    classDef warning fill:#FFF8E1,stroke:#F9A825,stroke-width:2px,color:#F57F17
    classDef alert fill:#FFF3E0,stroke:#EF6C00,stroke-width:2px,color:#E65100
    classDef note fill:#FFFDE7,stroke:#CBC693,stroke-width:1px,color:#5D4037

    class START startEnd
    class OFF idle
    class WARM_READY ready
    class STOPPED ready
    class NAVIGATING active
    class GPS_LOST warning
    class OUT_OF_REGION warning
    class NOTIFIED alert
    class N_OFF,N_NAV,N_NOTIFIED,N_GPS,N_OOR note

    linkStyle 0,1,3 stroke:#2E7D32,stroke-width:2.5px
    linkStyle 2 stroke:#607D8B,stroke-width:1.5px
    linkStyle 4,6 stroke:#F9A825,stroke-width:2.5px
    linkStyle 5,7,9,11 stroke:#1976D2,stroke-width:2.5px
    linkStyle 8 stroke:#607D8B,stroke-width:2px
    linkStyle 10 stroke:#EF6C00,stroke-width:2.5px
    linkStyle 12,13,14,15,16 stroke:#CBC693,stroke-width:1px,stroke-dasharray:4
```

---

## 2. BackTrack™ Breadcrumbs — FEAT-1.2

Three operational states with a one-way Distress lock that can only be set by SOS confirmation and cannot be reverted within a session — this is the most safety-critical determinism property of the subsystem.

```mermaid
graph TD
    START(("●")) --> INACTIVE["🟢 INACTIVE<br/>Standard capture mode"]
    INACTIVE -->|"Standard capture event (15m OR 20s)"| INACTIVE
    INACTIVE -->|"User opens BackTrack (≤3 taps)"| RETRACE["🔁 RETRACE<br/>Reviewing trail"]
    RETRACE -->|"User exits BackTrack view"| INACTIVE
    INACTIVE -->|"SOS Tap 2 confirmed"| DISTRESS["🆘 DISTRESS<br/>One-way locked"]
    RETRACE -->|"SOS Tap 2 confirmed"| DISTRESS
    DISTRESS -->|"Distress capture event (5m OR 5s)"| DISTRESS
    DISTRESS -->|"Session ends → next session begins"| INACTIVE

    N_INACTIVE["📝 Standard Dual-Trigger: 15m distance OR 20s time<br/>WAL committed before ack · Ref BTF-5126 §6.1.2"]
    N_DISTRESS["📝 ONE-WAY LOCK for session · Capture 5m OR 5s<br/>SOS deactivation does NOT revert to standard mode<br/>Next session starts INACTIVE · Ref BTF-5126 §6.1.4–5"]
    N_RETRACE["📝 Render ≤3s up to 10h trips / ≤6s for &gt;10h (interactive ≤1.5s)<br/>Forward route cleared · yellow-dash animated retrace · Ref BTF-5126 §6.1.3"]

    INACTIVE -.- N_INACTIVE
    DISTRESS -.- N_DISTRESS
    RETRACE -.- N_RETRACE

    classDef startEnd fill:#263238,stroke:#263238,stroke-width:2px,color:#fff
    classDef idle fill:#ECEFF1,stroke:#607D8B,stroke-width:2px,color:#263238
    classDef active fill:#E8F5E9,stroke:#2E7D32,stroke-width:3px,color:#1B5E20
    classDef critical fill:#FFEBEE,stroke:#C62828,stroke-width:3px,color:#B71C1C
    classDef note fill:#FFFDE7,stroke:#CBC693,stroke-width:1px,color:#5D4037

    class START startEnd
    class INACTIVE idle
    class RETRACE active
    class DISTRESS critical
    class N_INACTIVE,N_DISTRESS,N_RETRACE note

    linkStyle 0,2 stroke:#2E7D32,stroke-width:2.5px
    linkStyle 1,6 stroke:#607D8B,stroke-width:1.5px
    linkStyle 3,7 stroke:#1976D2,stroke-width:2.5px
    linkStyle 4,5 stroke:#C62828,stroke-width:3px
    linkStyle 8,9,10 stroke:#CBC693,stroke-width:1px,stroke-dasharray:4
```

---

## 3. SOS Emergency Logging — FEAT-1.3

The 3-Stage Log Sequence is the only state machine in the system where timing constraints are mandatory acceptance criteria (≤0.5s UI transition, ≤3s log completion). Zero outbound network packets in any state.

```mermaid
graph TD
    START(("●")) --> INACTIVE["⚪ INACTIVE<br/>No emergency"]
    INACTIVE -->|"Tap 1"| TRIGGER_PENDING["⏱️ TRIGGER_PENDING<br/>Awaiting confirm"]
    TRIGGER_PENDING -->|"Cancel"| INACTIVE
    TRIGGER_PENDING -->|"Tap 2 confirm"| STAGE1["🆘 STAGE1<br/>Local WAL committed"]
    STAGE1 -->|"GPS warm"| LOG_COMPLETE["✅ LOG_COMPLETE<br/>Immutable record"]
    STAGE1 -->|"GPS cold"| GPS_PENDING["📡 GPS_PENDING<br/>Awaiting fix"]
    GPS_PENDING -->|"GPS fix acquired"| LOG_COMPLETE
    LOG_COMPLETE -->|"User deactivates"| INACTIVE

    N_STAGE1["📝 Stage 1 commit: Timestamp + Device ID · AES-256 local WAL<br/>UI transition ≤0.5s · Ref SFD-5026 §3.2, BPS-5126 §6.1"]
    N_LOG["📝 Stage 3 — coordinates appended · Full record ≤3s (GPS warm)<br/>Record immutable after write · BackTrack DISTRESS persists on deactivate"]
    N_INACTIVE["📝 STATE INVARIANT (all states): Zero outbound packets<br/>(HTTP/HTTPS/UDP/TCP/SDK) · Runtime audit · Ref ESF-5026 §4.2"]

    STAGE1 -.- N_STAGE1
    LOG_COMPLETE -.- N_LOG
    INACTIVE -.- N_INACTIVE

    classDef startEnd fill:#263238,stroke:#263238,stroke-width:2px,color:#fff
    classDef idle fill:#ECEFF1,stroke:#607D8B,stroke-width:2px,color:#263238
    classDef warning fill:#FFF8E1,stroke:#F9A825,stroke-width:2px,color:#F57F17
    classDef critical fill:#FFEBEE,stroke:#C62828,stroke-width:3px,color:#B71C1C
    classDef done fill:#E0F2F1,stroke:#00897B,stroke-width:3px,color:#004D40
    classDef note fill:#FFFDE7,stroke:#CBC693,stroke-width:1px,color:#5D4037

    class START startEnd
    class INACTIVE idle
    class TRIGGER_PENDING warning
    class STAGE1 critical
    class GPS_PENDING warning
    class LOG_COMPLETE done
    class N_STAGE1,N_LOG,N_INACTIVE note

    linkStyle 0 stroke:#607D8B,stroke-width:2px
    linkStyle 1 stroke:#EF6C00,stroke-width:2.5px
    linkStyle 2,7 stroke:#1976D2,stroke-width:2.5px
    linkStyle 3 stroke:#C62828,stroke-width:3px
    linkStyle 4,6 stroke:#2E7D32,stroke-width:2.5px
    linkStyle 5 stroke:#F9A825,stroke-width:2.5px
    linkStyle 8,9,10 stroke:#CBC693,stroke-width:1px,stroke-dasharray:4
```

---

## 4. HazTrack™ Freshness — FEAT-1.4

State machine per feed item. Transitions are pure integer arithmetic: `(now − ingest_timestamp)` compared against fixed per-category constants. No adaptive decay curves.

```mermaid
graph TD
    START(("●")) --> NO_DATA["⚪ NO_DATA<br/>No feed item yet"]
    NO_DATA -->|"Authority feed ingest"| FRESH_GOLD["🥇 FRESH_GOLD<br/>Within Gold TTL"]
    FRESH_GOLD -->|"Gold TTL elapsed"| AGEING_GREY["🪨 AGEING_GREY<br/>Within Grey TTL"]
    AGEING_GREY -->|"Grey TTL elapsed"| NO_INDICATOR["🚫 NO_INDICATOR<br/>Silently expired"]
    FRESH_GOLD -->|"New authority data"| FRESH_GOLD
    AGEING_GREY -->|"New authority data"| FRESH_GOLD
    NO_INDICATOR -->|"New authority data"| FRESH_GOLD

    N_GOLD["📝 Gold TTL: Fire/Flood ≤6h · Weather ≤6h<br/>Closure ≤12h · General ≤12h · Ref OSM-5026 §8.2"]
    N_GREY["📝 Grey TTL upper bounds: Fire/Flood ≤12h · Weather ≤18h<br/>Closure ≤24h · General ≤24h"]
    N_NOIND["📝 Silent transition · No user alarm<br/>Feed timeouts → freshness indicator only (silent failure) · Ref HFG-5026 §6"]

    FRESH_GOLD -.- N_GOLD
    AGEING_GREY -.- N_GREY
    NO_INDICATOR -.- N_NOIND

    classDef startEnd fill:#263238,stroke:#263238,stroke-width:2px,color:#fff
    classDef idle fill:#ECEFF1,stroke:#607D8B,stroke-width:2px,color:#263238
    classDef gold fill:#FFF8E1,stroke:#F9A825,stroke-width:3px,color:#F57F17
    classDef ageing fill:#ECEFF1,stroke:#90A4AE,stroke-width:2px,color:#455A64
    classDef faded fill:#FAFAFA,stroke:#BDBDBD,stroke-width:1px,color:#9E9E9E
    classDef note fill:#FFFDE7,stroke:#CBC693,stroke-width:1px,color:#5D4037

    class START startEnd
    class NO_DATA idle
    class FRESH_GOLD gold
    class AGEING_GREY ageing
    class NO_INDICATOR faded
    class N_GOLD,N_GREY,N_NOIND note

    linkStyle 0 stroke:#607D8B,stroke-width:2px
    linkStyle 1,4,5,6 stroke:#2E7D32,stroke-width:2.5px
    linkStyle 2 stroke:#F9A825,stroke-width:2.5px
    linkStyle 3 stroke:#9E9E9E,stroke-width:2px
    linkStyle 7,8,9 stroke:#CBC693,stroke-width:1px,stroke-dasharray:4
```

---

## 5. Safe Anchor Points — FEAT-1.5

Two states with strict isolation invariants: no cloud sync of anchor data, and anchor navigation must never overwrite an active BackTrack trail (verified by TQP §5.5.2).

```mermaid
graph TD
    START(("●")) --> NO_ANCHOR["📍 NO_ANCHOR<br/>Idle / managing anchors"]
    NO_ANCHOR -->|"Create anchor at current location"| NO_ANCHOR
    NO_ANCHOR -->|"Select anchor as destination"| ANCHOR_NAV["🧭 ANCHOR_NAV<br/>Navigating to anchor"]
    ANCHOR_NAV -->|"User cancels"| NO_ANCHOR
    ANCHOR_NAV -->|"Arrival (geometric proximity)"| NO_ANCHOR

    N_NO["📝 Persistence: AES-256 encrypted local · Firebase-INDEPENDENT<br/>Local-Only / Non-Syncable · Survives force-kill (TQP §5.5.1) · Ref FEAT-1.5"]
    N_NAV["📝 PROHIBITED transitions:<br/>• Overwrite active BackTrack (TQP §5.5.2)<br/>• Cloud sync of anchor data (CDG-5126 §6.1)"]

    NO_ANCHOR -.- N_NO
    ANCHOR_NAV -.- N_NAV

    classDef startEnd fill:#263238,stroke:#263238,stroke-width:2px,color:#fff
    classDef idle fill:#ECEFF1,stroke:#607D8B,stroke-width:2px,color:#263238
    classDef active fill:#E8F5E9,stroke:#2E7D32,stroke-width:3px,color:#1B5E20
    classDef note fill:#FFFDE7,stroke:#CBC693,stroke-width:1px,color:#5D4037

    class START startEnd
    class NO_ANCHOR idle
    class ANCHOR_NAV active
    class N_NO,N_NAV note

    linkStyle 0 stroke:#607D8B,stroke-width:2px
    linkStyle 1 stroke:#607D8B,stroke-width:1.5px
    linkStyle 2 stroke:#2E7D32,stroke-width:2.5px
    linkStyle 3 stroke:#1976D2,stroke-width:2.5px
    linkStyle 4 stroke:#2E7D32,stroke-width:2.5px
    linkStyle 5,6 stroke:#CBC693,stroke-width:1px,stroke-dasharray:4
```

---

## 6. Crash Recovery — Cross-cutting (FEAT-4.4)

Recovery overlay applies to every subsystem's clean state. The WAL discipline guarantees zero record loss; the RECOVERY_AUDIT event encodes six mandatory fields.

```mermaid
graph TD
    START(("●")) --> CLEAN["✅ CLEAN<br/>Normal operation"]
    CLEAN -->|"App crash / force-kill / OS-kill / battery"| UNCLEAN_TERM["💥 UNCLEAN_TERM<br/>Abnormal termination"]
    UNCLEAN_TERM -->|"App restart detected"| RECOVERY_AUDIT["🔍 RECOVERY_AUDIT<br/>Logging audit event"]
    RECOVERY_AUDIT -->|"Resume sequence (no mutation)"| CLEAN_RESUMED["🔄 CLEAN_RESUMED<br/>Recovered, read-only resume"]
    CLEAN_RESUMED -->|"Normal operation resumes"| CLEAN

    N_AUDIT["📝 Audit event schema (6 required fields): 1 Event type RECOVERY_AUDIT ·<br/>2 UTC timestamp · 3 Last clean write timestamp · 4 Session ID ·<br/>5 Last known coordinates · 6 Breadcrumb count · Ref CQR-5026 (CR04 Q9)"]
    N_RESUMED["📝 PROHIBITED during recovery: All 14 breadcrumb mutations<br/>(BC-M01 – BC-M14) · Validation TQP §5.2.1 · Target 0% record loss · Ref BTF-5126 §5.2"]

    RECOVERY_AUDIT -.- N_AUDIT
    CLEAN_RESUMED -.- N_RESUMED

    classDef startEnd fill:#263238,stroke:#263238,stroke-width:2px,color:#fff
    classDef clean fill:#E8F5E9,stroke:#2E7D32,stroke-width:3px,color:#1B5E20
    classDef critical fill:#FFEBEE,stroke:#C62828,stroke-width:3px,color:#B71C1C
    classDef warning fill:#FFF8E1,stroke:#F9A825,stroke-width:2px,color:#F57F17
    classDef ready fill:#E3F2FD,stroke:#1976D2,stroke-width:2px,color:#0D47A1
    classDef note fill:#FFFDE7,stroke:#CBC693,stroke-width:1px,color:#5D4037

    class START startEnd
    class CLEAN clean
    class UNCLEAN_TERM critical
    class RECOVERY_AUDIT warning
    class CLEAN_RESUMED ready
    class N_AUDIT,N_RESUMED note

    linkStyle 0 stroke:#2E7D32,stroke-width:2.5px
    linkStyle 1 stroke:#C62828,stroke-width:3px
    linkStyle 2 stroke:#F9A825,stroke-width:2.5px
    linkStyle 3 stroke:#1976D2,stroke-width:2.5px
    linkStyle 4 stroke:#2E7D32,stroke-width:2.5px
    linkStyle 5,6 stroke:#CBC693,stroke-width:1px,stroke-dasharray:4
```

---

## 7. Inter-Layer Isolation Map (Immutable Separation Boundary)

The isolation half of the matrix — proves that every Experience-Layer event has an enforcement mechanism preventing it from mutating Survival Core state. Dotted arrows represent transitions that are **prohibited** and the label is the **isolation mechanism** that enforces it.

> **Spec terminology:** this enforcement structure realises the **Immutable Separation Boundary** mandated by NAV spec §4 — Experience Layer features are architecturally incapable of blocking, delaying, or mutating core navigation flow. See `../../4-cross-cutting/compliance-matrix.md §5` for the full rule + enforcement-point catalogue.

```mermaid
flowchart LR
    subgraph EXP["Experience &amp; Intelligence Layer (Epic 2 / 3)"]
        E1[TrackIQ recalculation]
        E2[HazTrack feed event]
        E3[PCR submission / resolution]
        E4[CAL transport switch]
        E5[Firebase sync]
        E6[Archetype preset change]
        E7[First Aid screen open]
        E8[Stop-detect prompt]
        E9[satReady flag flip]
    end

    subgraph CORE["Survival Core (Epic 1 / 4)"]
        C1[Breadcrumb sequence]
        C2[BackTrack capture interval]
        C3[SOS access path ≤2 taps]
        C4[SOS log immutability]
        C5[Nav execution path]
        C6[Nav rerouting authority]
        C7[Safe Anchor data]
        C8[TrackIQ difficulty grade]
        C9[HazTrack TTL state]
    end

    E5 -.->|Firebase isolation: no write context to Core| C1
    E2 -.->|14 mutations prohibited &#40;BC-M01–14&#41;| C1
    E6 -.->|Archetype cannot modify Core execution| C2
    E3 -.->|PCR must not interrupt SOS &#40;FQH Q5&#41;| C3
    E7 -.->|FA isolation &#40;TQP §5.7.7&#41;| C3
    E8 -.->|Dismissible; max 3 reprompts| C3
    E5 -.->|Zero outbound packets &#40;ESF-5026 §4.2&#41;| C4
    E9 -.->|Hardcoded FALSE; non-triggerable| C4
    E2 -.->|RT-02: Declarative Consent Model required| C6
    E2 -.->|RT-14: no mutation across layers| C8
    E1 -.->|Read-only display; static analysis| C5
    E5 -.->|Local-Only classification| C7
    E2 -.->|RG-01: deterministic TTL only| C9

    classDef block stroke:#000,fill:#fff,color:#000
    class EXP,CORE block
```

> **Reading the diagram:** each dotted arrow is an invariant. The label tells you *how* it is enforced (static analysis, architectural prohibition, empirical TQP scenario, or audit). A successful Discovery Gate confirms every arrow has a verifiable enforcement mechanism in the build pipeline.

---

## 8. Prohibition Register

Negative-space transitions — things that must provably never happen — and the enforcement mechanism for each. These complement the state diagrams above (which show what *can* happen) by enumerating what *cannot*.

### 8.1 Breadcrumb Mutations (BC-M01 – BC-M14)

All 14 are enforced by static-analysis scans in CI; detection triggers RT-13 automatic release halt.

| ID | Prohibition | Reference |
| --- | --- | --- |
| BC-M01 | Merge of breadcrumb records | BTF-5126 §5.2 |
| BC-M02 | Compaction of breadcrumb data | BTF-5126 §5.2 |
| BC-M03 | Reconstruction of paths from sparse points | BTF-5126 §5.2 |
| BC-M04 | Reordering of records | BTF-5126 §5.2 |
| BC-M05 | Map-matching to roads/trails | BTF-5126 §5.2; VGD-5126 §8.3 |
| BC-M06 | Coordinate interpolation across gaps | BTF-5126 §5.2 |
| BC-M07 | Gap-filling between records | BTF-5126 §5.2 |
| BC-M08 | Deduplication of records | BTF-5126 §5.2 |
| BC-M09 | Lossy compression of records | BTF-5126 §5.2 |
| BC-M10 | Conflict resolution between records | BTF-5126 §5.2 |
| BC-M11 | Reconciliation with cloud state | BTF-5126 §5.2; CDG-5126 §6.1 |
| BC-M12 | Coalescing of nearby records | BTF-5126 §5.2 |
| BC-M13 | Smoothing of coordinates | BTF-5126 §5.2 |
| BC-M14 | Post-capture correction of records | BTF-5126 §5.2 |

### 8.2 Rejection Triggers (determinism-relevant subset)

| ID | Category | Prohibition | Enforcement |
| --- | --- | --- | --- |
| RT-01 | Network | Active or triggerable Satellite SDK / transmission code | Static analysis + SDK audit (V-12) |
| RT-02 | Adaptive | Autonomous rerouting without user confirmation | Static analysis; TQP hazard-intersect scenario |
| RT-03 | Adaptive | AI, probabilistic inference, or adaptive ML in any execution path | Static analysis; Module Isolation Map |
| RT-04 | Adaptive | Telemetry-weighted scoring in TrackIQ | Static analysis |
| RT-05 | Network | Cloud sync of breadcrumb or SOS data | Firebase isolation audit |
| RT-09 | Phase Boundary | Phase 2+ scaffold accessible without "Inactive" label | Discovery review + static analysis |
| RT-13 | Survival Core | Breadcrumb loss/reorder/duplicate on crash | TQP §5.2.1 |
| RT-14 | Survival Core | HazTrack event mutates TrackIQ grade | Static analysis |
| RT-15 | Survival Core | SOS ≤2 tap path not empirically validated | TQP §5.6 |
| RT-19 | PCR | TTL-based PCR expiry (must be supersession-only) | Static analysis |
| RT-20 | PCR | Deletion of PCR records on supersession (must archive) | Static analysis |
| RT-21 | PCR | Automatic PCR submission triggers | Static analysis |

### 8.3 Layer Independence Rules

| ID | Prohibition | Reference |
| --- | --- | --- |
| LIR-01 | Difficulty colour representing freshness or hazard status | OSM-5026 §11 |
| LIR-02 | Verification shields representing terrain difficulty | OSM-5026 §11 |
| LIR-04 | PCR markers using the verification shield icon system | OSM-5026 §11 |
| LIR-05 | Any overlay layer mutating another layer's data or state | OSM-5026 §11 |
| LIR-06 | Visual state distinguishable by colour alone | OSM-5026 §11; RT-11 |

---

## Notes on the matrix as a Discovery Gate artefact

- **Each state diagram** above is the per-subsystem state-transition table required by AOD-5026 §7. Every transition is annotated with its document reference so a reviewer can trace it back to the authoritative source.
- **The isolation map** is the Module Isolation proof required by VGD-5126 §7.1 and FEAT-2.1 / FEAT-4.4 Discovery Gates. It is the artefact that proves the Experience Layer cannot mutate Survival Core behaviour.
- **The prohibition register** is the static-analysis specification — every entry must have a corresponding rule in the CI scanner. This satisfies the FEAT-4.2 static-analysis mandate.
- All three together form the deliverable that clears the Discovery Gate for Survival Core development.
