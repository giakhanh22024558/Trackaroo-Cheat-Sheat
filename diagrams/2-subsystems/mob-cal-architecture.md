# MOB-1101 · Comms Abstraction Layer (CAL) — Subsystem Deep-Dive

**Tier 2 · C4 Component level.** Specifies the Comms Abstraction Layer — a critical sub-component of the TrackMate™ module (`MOB-1001`) inside the Application Layer (`MOB-1000`). CAL isolates all transport-level complexity from the user **and** — most importantly — from Survival Core execution paths.

**Zone in master:** `MOB_APP / MOB_G2` (Mobile · Application Layer · Comms & Transport · blue)
**Parent module:** TrackMate™ (`MOB-1001`)
**Sibling component:** `MOB-1102` Multi-Tier Transport (MTT) — CAL's downstream
**Draw.io twin:** `../1-overview/trackaroo-phase1-architecture.drawio` → page **CAL Architecture**
**Proposal deliverable #4** — Discovery Gate artifact

---

## 1. Core architectural mandates

| Mandate | Requirement | Enforcement |
|---|---|---|
| **Zero Survival Core interference** | No CAL operation may introduce a network dependency into any Survival Core path (NAV · SOS · BackTrack™) | Static analysis · architectural prohibition · no API surface from CAL into `MOB_CORE` |
| **Transport agnosticism** | CAL must abstract all transports (BLE Mesh · Wi-Fi Direct/MPC · LoRa · future Satellite) behind a unified interface | `ITransport` interface · CAL never references concrete transports directly |
| **Deterministic priority logic** | CAL must internally manage transport priority + selection transparently · no manual user intervention | Hardcoded priority matrix · no user-facing transport picker |
| **Phase 2 readiness** | Architecture must accommodate future **Satellite Relay (Tier 3)** without structural rework | `satReady` flag scaffold present · `ITransport` interface accepts new implementation without changes to CAL contract |

---

## 2. Transport priority tiers

CAL selects transport using a deterministic priority order. Higher tier = preferred. Selection happens transparently — no user prompt.

| Tier | Transport | Status (Phase 1) | Range | Use case |
|---|---|---|---|---|
| **Tier 1 (primary)** | **BLE Mesh** | ✅ Active | ~30-100m | Default for nearby peer comms; lowest latency |
| **Tier 1 (fallback)** | **Wi-Fi Direct / MPC** | ✅ Active | ~50-200m | Higher bandwidth fallback when BLE Mesh saturated or unavailable |
| **Tier 2** | **LoRa** | ✅ Active (paired peripherals only) | ~1-15 km | Long-range when peer outside BLE/Wi-Fi range; requires `EXT-9005` LoRa peripheral |
| **Tier 3** 🔵 | **Satellite Relay** | 🔵 **Phase 2 only — inert scaffold** | Global | Future capability; `satReady` flag hardcoded `false` in Phase 1 |

**Selection rule (deterministic):**
```text
For each outbound payload:
   1. If satReady == true  AND  satellite peer in range  →  Tier 3   (PHASE 2 ONLY)
   2. If BLE Mesh peer in range                          →  Tier 1 primary
   3. If Wi-Fi Direct peer in range                      →  Tier 1 fallback
   4. If LoRa peripheral paired AND peer in range        →  Tier 2
   5. Else                                               →  queue (persisted) + offline beacon
```

No probabilistic / adaptive / telemetry-weighted selection. Same inputs always produce the same transport choice.

---

## 3. Mandatory state flags

CAL must implement and test **four boolean state flags**. Each governs system behavior + UI feedback.

| Flag | Phase 1 value | Active condition | Triggers UI state | Notes |
|---|---|---|---|---|
| **`satReady`** | **Hardcoded `false`** 🔵 | (never — Phase 2 only) | (none in Phase 1) | **Inert scaffold.** Schema field exists but must not be reachable / triggerable. No satellite SDK in codebase. Static analysis enforces |
| **`queueEnabled`** | dynamic | TrackMate™ session active AND persistent message queue operational | (no UI change — internal state) | Indicates Firebase-independent queue accepts outbound payloads |
| **`offlineBeacon`** | dynamic | BLE Mesh stack actively broadcasting presence data via available offline transport | "Beacon active" indicator | Confirms peer-discoverability without cellular |
| **`partialSignal`** | dynamic | Discovery OR propagation latency exceeds calibrated thresholds (intermittent connectivity) | "**Limited Connectivity**" UI indicator | Triggered when comms degraded but not zero |

### Flag interactions

```mermaid
---
config:
  theme: base
  themeVariables:
    fontFamily: Arial
    fontSize: 12px
---
stateDiagram-v2
    [*] --> AppLaunch
    AppLaunch --> Idle: TrackMate not started
    Idle --> SessionActive: User starts TrackMate session<br/>queueEnabled = true

    SessionActive --> BeaconingFull: BLE Mesh peer discovered<br/>offlineBeacon = true<br/>partialSignal = false
    SessionActive --> BeaconingPartial: Discovery latency &gt; threshold<br/>offlineBeacon = true<br/>partialSignal = true
    SessionActive --> QueueOnly: No peer in range<br/>offlineBeacon = false<br/>queueEnabled = true

    BeaconingFull --> BeaconingPartial: Propagation latency degrades
    BeaconingPartial --> BeaconingFull: Latency recovers
    BeaconingPartial --> QueueOnly: All peers lost
    QueueOnly --> BeaconingFull: New peer in range

    SessionActive --> Idle: User stops TrackMate<br/>queueEnabled = false<br/>offlineBeacon = false

    note right of BeaconingPartial
        UI shows "Limited Connectivity"
        Calm language only — NO
        "trying to recover" implication
    end note

    note right of Idle
        satReady remains FALSE
        in ALL states (Phase 1)
        Static analysis enforces
    end note
```

---

## 4. UI & interaction requirements

| Requirement | Spec value |
|---|---|
| **Persistence** | CAL status indicator MUST be persistently visible in the primary navigation view (no dismiss / no hide) |
| **Response time** | Any change in connectivity state (e.g. transition into `partialSignal`) MUST update the UI indicator within **≤ 2 seconds** |
| **Language posture** | Calm, non-alarming text. MUST NOT imply that any automated recovery or escalation action is pending |
| **Accepted labels** | "Beacon active" · "Limited Connectivity" · "Queue pending" · "Offline" |
| **PROHIBITED labels** | "Reconnecting…" · "Searching for signal…" · "Trying satellite…" · "Recovery in progress…" · anything implying autonomous action |

**Rationale for language posture:** users facing emergencies are calmer if comms status is presented as **state** ("you are offline") rather than as **action-in-progress** ("trying to reconnect"). The latter creates false expectation of automated rescue.

---

## 5. CAL component architecture

```mermaid
---
config:
  layout: elk
  theme: base
  themeVariables:
    fontFamily: Arial
    fontSize: 13px
---
graph TB

    subgraph PARENT["<b>MOB-1001 · TrackMate™</b> <i>(parent module)</i>"]
        direction TB

        subgraph CAL["<b>MOB-1101 · Comms Abstraction Layer (CAL)</b>"]
            direction TB

            subgraph CAL_API["<b>Public API</b> · <i>What TrackMate calls</i>"]
                direction LR
                SEND["sendPayload(msg)"]
                STATUS["getStatus() → flags"]
                BROADCAST["startBeacon() / stopBeacon()"]
            end

            subgraph CAL_CORE["<b>CAL Core Engine</b>"]
                direction TB
                ROUTER["<b>Transport Router</b><br/>Deterministic priority<br/>tier selection"]
                FLAGS["<b>State Flag Manager</b><br/>satReady · queueEnabled<br/>offlineBeacon · partialSignal"]
                QUEUE["<b>Persistent Message Queue</b><br/>Firebase-independent<br/>WAL-backed · crash-survivable"]
                LATENCY["<b>Latency Monitor</b><br/>Discovery + propagation<br/>thresholds → partialSignal"]
            end

            subgraph CAL_TRANSPORT_IF["<b>Transport Interface (ITransport)</b> · <i>Vendor-agnostic abstraction</i>"]
                direction LR
                T_BLE["BleAdapter"]
                T_WIFI["WiFiDirectAdapter"]
                T_LORA["LoRaAdapter"]
                T_SAT["SatelliteAdapter<br/><i>Phase 2 stub</i>"]
            end
        end
    end

    subgraph DOWNSTREAM["<b>MOB-1102 · Multi-Tier Transport (MTT)</b>"]
        direction LR
        MTT_BLE["BLE Mesh stack"]
        MTT_WIFI["Wi-Fi Direct / MPC"]
        MTT_LORA["LoRa radio<br/>(via EXT-9005)"]
    end

    subgraph CORE_BOUNDARY["<b>MOB-2000 · Survival Core</b> <i>(NO ACCESS FROM CAL)</i>"]
        direction LR
        CORE_X["NAV · SOS · BackTrack™"]
    end

    SEND --> ROUTER
    STATUS --> FLAGS
    BROADCAST --> ROUTER

    ROUTER --> FLAGS
    ROUTER --> QUEUE
    ROUTER --> LATENCY
    LATENCY --> FLAGS

    ROUTER --> T_BLE
    ROUTER --> T_WIFI
    ROUTER --> T_LORA
    ROUTER -.->|"<i>Phase 2 only</i>"| T_SAT

    T_BLE --> MTT_BLE
    T_WIFI --> MTT_WIFI
    T_LORA --> MTT_LORA

    %% PROHIBITED — explicit
    CAL -.->|"<b>[X] PROHIBITED</b><br/>CAL cannot call Survival Core<br/>No imports · static analysis enforced"| CORE_X

    classDef api fill:#ffffff,stroke:#1976d2,stroke-width:1.5px,color:#000
    classDef core fill:#ffffff,stroke:#555,stroke-width:1.2px,color:#000
    classDef transport fill:#ffffff,stroke:#555,stroke-width:1px,color:#000
    classDef sat fill:#fafafa,stroke:#9e9e9e,stroke-width:1px,stroke-dasharray:5 3,color:#616161
    classDef prohibited fill:#fff5f5,stroke:#c62828,stroke-width:1.5px,color:#b71c1c

    class SEND,STATUS,BROADCAST api
    class ROUTER,FLAGS,QUEUE,LATENCY core
    class T_BLE,T_WIFI,T_LORA,MTT_BLE,MTT_WIFI,MTT_LORA transport
    class T_SAT sat
    class CORE_X prohibited

    style PARENT fill:#e3f2fd,stroke:#1976d2,stroke-width:1.5px,color:#000
    style CAL fill:#ffffff,stroke:#555,stroke-width:1.5px,color:#000
    style CAL_API fill:#e3f2fd,stroke:#1976d2,stroke-width:1px,stroke-dasharray:3 2,color:#000
    style CAL_CORE fill:#f5f5f5,stroke:#555,stroke-width:1px,stroke-dasharray:3 2,color:#000
    style CAL_TRANSPORT_IF fill:#f5f5f5,stroke:#555,stroke-width:1px,stroke-dasharray:3 2,color:#000
    style DOWNSTREAM fill:#e3f2fd,stroke:#1976d2,stroke-width:1.5px,color:#000
    style CORE_BOUNDARY fill:#fff5f5,stroke:#c62828,stroke-width:2px,stroke-dasharray:6 4,color:#b71c1c

    linkStyle 11 stroke:#c62828,stroke-width:2px,stroke-dasharray:5 5
```

---

## 6. Validation & evidence obligations (Discovery Gate)

Vendors must provide the following at Discovery Gate. This file IS one of the deliverables; the other two reference it.

| Evidence | Source | Reference |
|---|---|---|
| **CAL Architecture Documentation** | This file | `mob-cal-architecture.md` (you are here) |
| **Module Isolation Mapping** | Low-level dependency graph proving Experience Layer (where CAL resides) cannot mutate / block Survival Core | `../4-cross-cutting/module-isolation-mapping.md` (TBD — to be extracted from `state-trackaroo-transitions.md §7`) |
| **Static analysis evidence** | CI pipeline scan confirming:<br/>1. `satReady` flag remains `false`<br/>2. No prohibited satellite-specific field names exist in codebase<br/>3. No satellite SDKs imported<br/>4. CAL has no import of Survival Core packages | Vendor build pipeline output |

### Static analysis scan checklist

| Check | Match pattern | Expected result |
|---|---|---|
| `satReady` literal `true` | `satReady\s*=\s*true` | **0 matches** |
| Satellite SDK imports | `import.*(iridium\|inmarsat\|globalstar\|orbcomm)` | **0 matches** |
| Satellite-specific field names | `(satelliteHandle\|iridiumSession\|inmarsatPeer)` | **0 matches** |
| CAL → Survival Core imports | `from mob_core.*` (or equivalent) inside any CAL module | **0 matches** |
| Transport-specific calls outside `ITransport` abstraction | Direct `ble.*` / `wifi.*` / `lora.*` outside `T_BLE/T_WIFI/T_LORA` adapters | **0 matches** |

---

## 7. Cross-references

- Master: `../1-overview/trackaroo-phase1-architecture.md` — see `MOB-1101` in `MOB_G2` (Comms & Transport)
- Parent module: TrackMate™ (`MOB-1001`) — see `./mob-application-layer.md`
- Downstream sibling: Multi-Tier Transport (`MOB-1102`) — see `./mob-application-layer.md`
- Survival Core boundary: `./mob-survival-core.md` — explicit non-target of CAL
- **State matrix (runtime view): `../3-flows/state/state-cal.md`** — explicit `(state × flags × transport × UI × transitions)` matrix consolidating §2/§3/§4 of this doc
- System-wide state map: `../3-flows/state/state-trackaroo-transitions.md` — see §7 Inter-Layer Isolation Map
- Compliance: `../4-cross-cutting/compliance-matrix.md` — entries for `satReady` inertness, CAL→Core prohibition
- Navigation: `../README.md`

## 8. Document status

| Field | Value |
|---|---|
| Document purpose | Proposal stage · Discovery Gate Deliverable #4 |
| Spec coverage | Core mandates · 4 flags · UI rules · validation obligations · static analysis checklist |
| Outstanding | Calibrated threshold values for `partialSignal` trigger (latency ms) — vendor to propose |
| Next review trigger | Vendor proposal received → reconcile threshold values + add measurement methodology |
