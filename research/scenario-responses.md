# Vendor Scenario Responses — Governance-Traceable Walkthroughs

**Purpose:** Vendor responses to client/evaluator stress-test scenarios. Each step provides (1) system behaviour · (2) governing document + section · (3) implementation evidence. Assertion without governance traceability is assessed negatively per evaluator guidance.

**Scope:** Phase 1 (Discovery / Alpha / Beta / GA gates).

**Cross-reference index** for every claim in this file:

| Topic | Authoritative document |
|---|---|
| All numeric SLAs | `diagrams/4-cross-cutting/performance-targets.md` |
| All prohibitions & RTs | `diagrams/4-cross-cutting/compliance-matrix.md` |
| State machines (NAV · BT · SOS · HAZ · SAP · Crash) | `diagrams/3-flows/state/state-trackaroo-transitions.md` |
| Master architecture (zones · isolation barrier) | `diagrams/1-overview/trackaroo-phase1-architecture.{md,drawio}` |
| Phase 2 scaffold posture (satReady=FALSE invariant) | `diagrams/4-cross-cutting/phase-2-readiness.md` |
| CAL state + UI labels | `diagrams/2-subsystems/mob-cal-architectural-diagram.{md,drawio}` · `diagrams/3-flows/state/state-cal.md` |
| Spec authority stack | `research/spec-authority-stack.md` |
| Design decisions (M0a–M0q) | `research/design-decisions.md` |

---

# SCENARIO 1 — SURVIVAL CORE UNDER STRESS: OFFLINE NAVIGATION, BACKTRACK™, AND SOS

> **Context recap:** 4 travellers · 65 km in outback QLD · no cellular · 31 % battery · 4 hours into loaded bundle · injured passenger · group decides to retrace.

## A · Offline Navigation under no signal

| # | What the system does | Governing doc · § | How the implementation satisfies it |
|---|---|---|---|
| **A.1** | Navigation engine `MOB-2001` continues turn-by-turn from **pre-downloaded vector + raster tile bundle** held in `MOB-3004 Map Bundle Cache`. State stays `NAVIGATING`. No runtime tile fetch is attempted. | **MAS-5126** (offline operation) · **CQR-5026** · **`compliance-matrix.md §4`** — "100% local operation — Pre-downloaded bundles only" | Bundle Download Manager `MOB-2007` enforces an "Offline-ready" gate before navigation can begin (integrity validation + completeness check). At runtime NAV calls only the local tile reader — there is no fallback path to Mapbox runtime API. Static-analysis CI gate fails the build if any Mapbox runtime SDK call lives in a Core code path (`compliance-matrix.md §13`). |
| **A.2** | When cellular drops, **nothing changes in the NAV state machine** — cellular is not an input to it. GNSS sensor `MOB-0001` continues to feed positions; map continues to render; turn-by-turn continues. | **`state-trackaroo-transitions.md §1`** — NAV transitions are triggered only by user action, OS-level GPS boolean, or geometric point-in-polygon test · **ESF-5026** (Survival Core 100 % offline) | Cellular signal is NOT a state transition trigger in `NAV` machine. The only signal-related transitions are `NAVIGATING ⇄ GPS_LOST` (driven by OS GNSS boolean) and `NAVIGATING ⇄ OUT_OF_REGION` (driven by tile-set boundary geometry). Both are local determinations. CAL connectivity status is published to a UI label but **does not feed into NAV control flow** — enforced by the static-analysis rule `CAL → Survival Core imports = 0 matches` (§13). |
| **A.3** | **What the user sees:** ongoing turn-by-turn map · current position dot · breadcrumb trail · vehicle heading · CAL connectivity badge ("Queue pending" / "Offline" using **Visual Calm** copy, not "Reconnecting…"). Max 3 concurrent map layers. Initial map render had completed ≤ 2 s after launch. | **UXS-5726** (Visual Calm doctrine) · **`compliance-matrix.md §8`** — Prohibited copy includes "Reconnecting…", "Searching for signal…" · **PT-NAV-04** ≤ 2 s render · **PT-NAV-05** max 3 layers | The CAL UI Status Publisher (`SPUB`) emits exactly one of 4 mandated labels: "Beacon active" / "Limited Connectivity" / "Queue pending" / "Offline" — anything else is rejected by code review against the CAL state matrix (`state-cal.md §5`). NAV does not subscribe to CAL state for control flow — only the SPUB → UI surface is wired. |
| **A.4** | **Why no degradation:** Survival Core has zero network dependency. The 4 hours of prior navigation persisted breadcrumb-log + bundle cache locally · AES-256 encrypted in `MOB-3002` (SQLite + WAL). | **ESF-5026** §4 (Immutable Separation Boundary) · **BPS-5126** · **`compliance-matrix.md §5`** (MOB_APP ⇎ MOB_CORE) | Architecturally enforced: `CORE_BARRIER` cell in master architecture (red dashed wall, not arrow) between App Layer and Survival Core. Experience Layer can read from Core (limited surfaces) but **never write**. Even if every Experience Layer module crashes, NAV/BackTrack/SOS remain fully operational. |

## B · BackTrack™ retrace path

| # | What the system does | Governing doc · § | How the implementation satisfies it |
|---|---|---|---|
| **B.1** | User opens BackTrack from any NAV state in **≤ 3 taps**. State transitions `INACTIVE → RETRACE`. View renders the captured breadcrumb trail. | **BTF-5126 §6.1.3** · **`state-trackaroo-transitions.md §2`** | The breadcrumb capture has been running continuously since session start at **Standard Dual-Trigger** rate (15 m distance OR 20 s time, whichever fires first). Records are WAL-committed **before** the UI is acknowledged — so even on power-off there is no loss of acknowledged records (TQP §5.2.1 zero-loss target). |
| **B.2** | **What the retrace is derived from:** the verbatim breadcrumb_log captured during the outbound 4 hours · stored in `MOB-3002` SQL · AES-256 encrypted · WAL-committed · no cloud copy. | **BTF-5126 §6.1.2** (Dual-Trigger capture) · **`compliance-matrix.md §10`** (AES-256 + WAL + Firebase Independence) · **RT-05** (no cloud sync of breadcrumb) | The retrace renderer reads ordered records from breadcrumb_log and draws them in reverse using a **yellow-dashed animated polyline**. The forward route is cleared from the canvas to remove cognitive load. The polyline is rendered ≤ 3 s for ≤ 10 h trips, ≤ 6 s for longer, interactive ≤ 1.5 s — measurements verified per BTF-5126 §6.1.3. |
| **B.3** | **Why the retrace cannot be modified or smoothed:** the rendered path is the captured points themselves. None of the 14 named mutations is permitted. | **BTF-5126 §5.2** — 14 forensic-integrity mutations BC-M01…BC-M14 prohibited · **`state-trackaroo-transitions.md §8.1`** (full table) · **RT-13** automatic release halt on detection | Each of BC-M01–14 maps to a static-analysis rule in CI · attempted code that invokes road-snapping, path-smoothing, coordinate interpolation, deduplication, lossy compression, reconciliation with cloud state, etc. fails the build. The retrace renderer is a pure read-only pipeline — `SELECT * FROM breadcrumb_log WHERE session_id = ? ORDER BY captured_at` → polyline geometry. No transform function exists between query and renderer. |
| **B.4** | **One-way DISTRESS lock:** the moment SOS Tap 2 confirms, BackTrack capture rate flips to **5 m OR 5 s** for the rest of the session and cannot revert — even if SOS is later deactivated. | **BTF-5126 §6.1.4–5** | The state machine transition `INACTIVE → DISTRESS` (and `RETRACE → DISTRESS`) is irreversible within a session. Session boundary is the only path back to `INACTIVE`. Enforced by the runtime guard inside `MOB-2002` BackTrack module and verified by TQP §5.6. |

## C · SOS activation when the injury deteriorates

### Exact tap count from `NAVIGATING` state

| Tap | What user sees | What system does (Stage) | Doc · § |
|---|---|---|---|
| **(starting)** | Active turn-by-turn map · SOS button persistent on screen (≤ 2-tap reachable from **any** Core state) | NAV in `NAVIGATING`; SOS module `MOB-2004` in `INACTIVE` | `compliance-matrix.md §9` ≤2-tap SOS · **RT-15** empirically validated (TQP §5.6) |
| **Tap 1** | SOS pre-confirm screen · large CONFIRM + CANCEL · countdown is **NOT** auto-dispatching | SOS state `INACTIVE → TRIGGER_PENDING` · UI transition ≤ 0.5 s | **SFD-5026 §3.2** · **BPS-5126 §6.1** |
| **Tap 2** | "Distress logged · awaiting GPS coordinates" *or* "Distress logged" (if GPS already warm) · clear textual confirmation that this is a **local record**, not an outbound call | `TRIGGER_PENDING → STAGE1` · WAL commit of `{timestamp_utc, device_id}` · BackTrack flips ONE-WAY to `DISTRESS` (5 m OR 5 s) · full SOS record completes ≤ 3 s if GPS warm | **SFD-5026 §3.2** · **BTF-5126 §6.1.4–5** · **`state-trackaroo-transitions.md §3`** |

**Total taps: 2.** This satisfies the `≤2-tap SOS` invariant in `compliance-matrix.md §9` and the **RT-15** empirical validation requirement.

### Feedback after activation — and why it does **not** imply dispatch

| What is displayed | Why it does NOT imply dispatch | Doc · § |
|---|---|---|
| "Distress record committed locally · timestamp + device ID stored · awaiting GPS fix" (or "GPS attached · record finalised" once Stage 3 completes) | The copy is intentionally **Visual Calm** — factual, no action verbs like "Dispatched", "Sent", "Help is on the way". Phase 1 Survival Core has **zero outbound packets** in any SOS state — satellite SDKs are PROHIBITED and the static-analysis CI gate enforces 0 matches for iridium/inmarsat/globalstar/orbcomm imports. | **UXS-5726** (Visual Calm) · **ESF-5026 §4.2** (Zero Outbound) · **`compliance-matrix.md §4, §12`** · **RT-01** Satellite SDK Present |
| BackTrack indicator silently flips to denser capture (5 m / 5 s) | No alarming animation; the user-facing change is a small density-change marker | **BTF-5126 §6.1.4–5** |
| CAL UI label may show "Queue pending" — that is the local queue, not a transmission | "Queue pending" is one of 4 mandated CAL labels and explicitly means "stored locally awaiting future transport" — Phase 2 satellite scaffold (`satReady=FALSE`) ensures no transport is actually triggerable | **CAL state matrix** · **`phase-2-readiness.md §1`** scaffold #2 + §4 CI gate (`satReady=true` literal → 0 matches) |

## D · 6-hour battery projection · BPS-5126 endurance survival

### Numbers
| Metric | Spec target (PT) | Current state |
|---|---|---|
| Sustained NAV draw | **≤ 8 %/hr** (PT-NAV-08) | 8 %/hr × 6 h = 48 % required |
| Endurance threshold | **≥ 10 h** total from 100 % (PT-NAV-09) | n/a — group already 4 h in, at 31 % |
| Sustained SOS draw | **≤ 20 %/hr** (`compliance-matrix.md §9`) | depends on SOS activation duration |

**Bare-arithmetic projection** at PT-NAV-08 budget (8 %/hr) + BLE Mesh TrackMate active (negligible delta — built-in radio):
- Remaining at start of retrace: **31 %**
- After 6 hours at 8 %/hr: **31 − 48 = −17 %** → device shuts off at hour ~3.9.

**Device does NOT survive to the 10-hour BPS-5126 threshold** under sustained continuous NAV at PT-NAV-08 limit and zero starting headroom.

### Vendor-proposed mitigations · all within governance

| Mitigation | What it does | Why it stays within governance |
|---|---|---|
| **Deterministic power-save mode (user-toggled)** — reduces frame-rate floor toward PT-NAV-07 minimum 45 fps, dims screen, defers Experience-Layer redraws | Extends runway by reducing the **non-Core** draw budget. NAV core path (GNSS read · breadcrumb commit · map render at minimum 45 fps) remains operational. | User-initiated (no autonomous adaptation → does **not** trigger **RT-02**, **RT-03**) · Deterministic (same input → same behaviour, no ML-driven dimming → respects **`compliance-matrix.md §4`** deterministic execution) |
| **Map-layer reduction to 1 (basemap only)** — drop overlays (HazTrack · TrackIQ grading display) | Reduces per-frame draw cost · stays at PT-NAV-05 (max 3) limit, just exercises it downward | Layer count is user-configurable; reduction is a user action, not autonomous (RT-02 compliant). HazTrack feed continues to be cached server-side via SYN→HAZ_CACHE exception (`compliance-matrix.md §7`) — only the **render** is suppressed. |
| **Stop-detect prompt → Safe Anchor Point** — if vehicle stationary 10 min + < 15 m movement, prompt offers to drop a Safe Anchor and pause active NAV | Frees the GNSS poll cadence + render loop; breadcrumb capture continues in background at standard rate | Prompt is dismissible · max 3 reprompts (`state-trackaroo-transitions.md §7` E8 → C3 isolation rule). Safe Anchor data is AES-256 local · Firebase-INDEPENDENT (FEAT-1.5). |
| **Pre-emptive SOS pre-stage** — if user anticipates injury escalation, Tap 1 the SOS pre-confirm to let CAL stop discovery scans and reduce radio cycling | TRIGGER_PENDING state itself does not transmit (zero outbound is **invariant for all SOS states**) but it lets CAL drop into a quieter scan profile | ESF-5026 §4.2 zero-outbound holds across all SOS states · BTF-5126 §6.1.4 one-way DISTRESS lock is only entered on Tap 2 confirm, so Tap 1 alone is non-destructive of capture cadence |

**Out-of-scope (would violate governance):**
- ❌ Auto-trigger satellite uplink — RT-01 release halt; satReady=FALSE Phase 1 invariant
- ❌ Autonomous re-route to closer Safe Anchor — RT-02 release halt; reroute requires 5-step Declarative Consent (HFG-5026 §5.4)
- ❌ ML-driven adaptive sampling rates — RT-03 release halt; deterministic execution mandate
- ❌ Cloud assist for compute — `MOB_CORE → SYN` PROHIBITED (red dashed edge in master)

## Evaluator probes — Scenario 1

### E.1 · Breadcrumb log interrupted by device power-off — how does BackTrack handle the gap?

| Step | Behaviour | Doc · § |
|---|---|---|
| 1 | Power-off → state transition `CLEAN → UNCLEAN_TERM` (crash-recovery overlay) | **`state-trackaroo-transitions.md §6`** (Crash Recovery / FEAT-4.4) |
| 2 | On restart, app detects unclean shutdown → state `UNCLEAN_TERM → RECOVERY_AUDIT`. A `RECOVERY_AUDIT` event is appended to the event log with **6 mandatory fields**: event type · UTC timestamp · last clean write timestamp · session ID · last known coordinates · breadcrumb count | **CQR-5026 (CR04 Q9)** · `state-trackaroo-transitions.md §6` |
| 3 | The gap **remains a void** in the breadcrumb_log. **No interpolation.** | **BTF-5126 §5.2** · BC-M06 (coordinate interpolation across gaps) · BC-M07 (gap-filling between records) PROHIBITED · enforced by static-analysis CI |
| 4 | On the BackTrack retrace view, the gap appears as a **visible discontinuity** in the yellow-dashed polyline (no line drawn across it) — the user sees the gap honestly, with no synthesized data | `state-trackaroo-transitions.md §1` GPS_LOST note: "gap = void (no interpolation)" |
| 5 | Resume state `RECOVERY_AUDIT → CLEAN_RESUMED` is **read-only resume** — all 14 mutation behaviours BC-M01–14 prohibited during recovery; target 0 % record loss for pre-crash records | **TQP §5.2.1** · **RT-13** automatic release halt on detected loss/reorder/duplicate |

### E.2 · SOS log content if GPS fix not yet acquired at Tap 2

At Tap 2 confirm, the state machine enters `STAGE1` and commits **immediately** without waiting for GPS, satisfying the `≤ 0.5 s UI transition` constraint.

| Field committed at Stage 1 (GPS-cold path) | Source | Doc · § |
|---|---|---|
| `event_type = SOS_DISTRESS` | constant | SFD-5026 §3.2 |
| `timestamp_utc` | OS monotonic clock | SFD-5026 §3.2 |
| `device_id` | provisioned at install | SFD-5026 §3.2 |
| `gps_status = COLD` | flag indicating Stage 3 pending | `state-trackaroo-transitions.md §3` (GPS_PENDING) |
| `last_known_coordinates` (if any cached from prior fix) | breadcrumb_log latest | BTF-5126 §6.1.2 (Standard Dual-Trigger capture means a recent breadcrumb usually exists; if device just powered up: field is NULL with `gps_status = COLD`) |
| `session_id` | current navigation session | crash-recovery alignment §6 |

The record is **AES-256 encrypted · WAL-committed · immutable from this moment**. State machine sits in `GPS_PENDING` waiting on the GNSS subsystem. **When GPS acquires fix → Stage 3** appends the live coordinates → record transitions to `LOG_COMPLETE`. The coordinate append is the only mutation permitted post-Stage 1 (and it is append-only — does not overwrite Stage 1 fields).

- **Why this is forensically defensible:** Stage 1 commit timestamp + device ID is the legal "moment of distress" — independent of GPS availability. Forensic immutability per **BTF-5126** + **`compliance-matrix.md §10`** SOS log immutability · append-only · forever retention.

### E.3 · Group Health Envelope visual indicator change (TrackMate group view) — without triggering automated distress

| Aspect | Behaviour | Doc · § |
|---|---|---|
| **Surface** | TrackMate `MOB-1001` (Application Layer) group view; **not Survival Core** | `compliance-matrix.md §5` (Experience ⇎ Core boundary) |
| **Transport** | BLE Mesh peer messaging via `MOB-1102` MTT through CAL `MOB-1101` — peers exchange compact health-state vectors | **M5 transport priority** (Locked-in · ESF-5026 · FSD-5126) |
| **What the indicator shows** | A small per-peer status pill on the group map — e.g. "in motion · 4 h · battery 41 %" or "stationary 12 min · battery 28 %". When the injured passenger's device shows a stationary-with-low-battery profile, the visual pill silently shifts colour/icon. | **UXS-5726** (Visual Calm) |
| **What the indicator does NOT do** | Does NOT auto-trigger SOS on any peer device · does NOT auto-message authorities · does NOT escalate beyond a visual change | **RT-02** (no autonomous action) · **RT-01** (no triggerable transmission) · `compliance-matrix.md §8` (no UI copy implying autonomous recovery) |
| **How peers can act** | Any group member sees the changed pill and decides — explicit user action (e.g. tap → "open SOS on my device", "send check-in ping via BLE Mesh") | **HFG-5026 §5.4** Declarative Consent Model (5-step) |
| **Why this respects determinism** | The indicator colour/icon mapping is a fixed lookup: `(battery_pct_bucket × motion_state × signal_quality) → icon`. Pure integer/bucket arithmetic; no ML inference, no probabilistic weighting | **RT-03** (no AI/probabilistic/adaptive) · `compliance-matrix.md §4` (Deterministic execution) |
| **CAL state during this surface** | CAL in S3 BeaconingFull or S4 BeaconingPartial — both publish "Beacon active" / "Limited Connectivity" labels respectively · no language implying recovery in progress | **`state-cal.md §5`** state matrix · UXS-5726 |

**Bottom line:** the GHE indicator is an **information surface**, not an actor. The architecture has no path from a GHE state change to any Core mutation — that prohibition is realised by the inter-layer isolation map (`state-trackaroo-transitions.md §7`) and enforced by static analysis on App → Core writes.

---

# SCENARIO 2 — TRACKMATE™ GROUP INTEGRITY AND PHASE BOUNDARY ENFORCEMENT

> **Context recap:** 6 mining-survey professionals · remote site · no cellular · TrackMate active · 2 members separate beyond BLE Mesh range · **no LoRa peripheral connected** · 1 separated device drops below GHE visual threshold.

## A · Main-group transport tier (within BLE Mesh range) and what the user sees

| # | What the system does | Governing doc · § | How the implementation satisfies it |
|---|---|---|---|
| **A.1** | All 4 in-range devices run CAL `MOB-1101` in **state S3 · BeaconingFull** (or S4 BeaconingPartial if some peer latency exceeds M6 threshold). Flag vector `[satReady=F, queueEnabled=T, offlineBeacon=T, partialSignal=F]` (S3) or `[F,T,T,T]` (S4). | **`state-cal.md §5`** (CAL state matrix) · **FSD-5126** (CAL spec) | CAL state is computed deterministically by `SFM` (State Flag Manager) from MTT peer-discovery events + LMON latency readings. Same inputs → same state — no probabilistic transitions (RT-03 compliant). |
| **A.2** | **Active transport tier:** Tier 1 **BLE Mesh** (primary). Wi-Fi Direct is the fallback if BLE saturates. LoRa Tier 2 is **not available** here (no peripheral paired). Satellite Tier 0 is **architecturally inert** in Phase 1 (`satReady=FALSE` invariant). | **M5 Comms transport priority** (Locked-in · ESF-5026 · FSD-5126) · **`state-cal.md §158`** transport tier table | `MOB-1102` MTT Transport Router applies the **5-rule priority algorithm** per outbound packet: `1. Sat (inert) → 2. BLE Mesh → 3. Wi-Fi Direct → 4. LoRa → 5. Queue`. With sat hardcoded inert and LoRa not paired, BLE Mesh wins. Implementation lives behind `ITransport` adapter pattern — no compile-time branch can bypass the priority order. |
| **A.3** | **UI label shown to user:** **"Beacon active"** (S3) or **"Limited Connectivity"** (S4). One of the 4 mandated CAL labels emitted by SPUB. Repaint ≤ 2 s after state change. | **UXS-5726** (Visual Calm) · **`compliance-matrix.md §9`** CAL ≤ 2 s repaint · **`state-cal.md §5`** | SPUB has a fixed lookup table — anything outside the 4 labels is rejected by code review. Repaint timing is asserted in CI perf benchmark. |
| **A.4** | **Group presence shown in TrackMate group view:** a per-peer pill list — for each peer device the user sees: peer name · last-heard timestamp · current motion state · current battery bucket · current CAL state (Beacon active / Limited / Queue pending / Offline). Refreshed via BLE Mesh peer-state broadcasts. | **TrackMate group view (`MOB-1001` Application Layer)** · BLE Mesh transport per **M5** · **UXS-5726** (Visual Calm) | Group presence pills are an **information-rendering** surface in TrackMate — they read peer-state broadcasts that arrived through CAL/MTT and render them via a deterministic icon lookup (RT-03 compliant). |

### What "group presence" means — and what it does NOT imply

| Group presence **DOES** mean | Group presence **DOES NOT** imply |
|---|---|
| "Peer device was reachable over BLE Mesh at last-heard timestamp" | "Peer human is conscious / unharmed / not lost" |
| "Peer's local CAL/MTT can currently exchange frames with my device" | "Peer's authorities have been notified of anything" |
| "Peer's broadcast battery / motion bucket is X" (deterministic bucket lookup) | "Anything is being transmitted to satellite / cloud / SOS dispatch" (RT-01 prohibits transmission) |
| "Inter-device messaging via BLE Mesh is operational" | "An outbound message has reached anywhere outside the local mesh" (BLE Mesh is a peer LAN — no internet gateway in Phase 1) |
| "I, the user, can decide to send a check-in or coordinate a response" | "The system has performed any autonomous action on the user's behalf" (RT-02 prohibits autonomous action) |

**Doc trail:** `compliance-matrix.md §4` (Zero Transmission · Core functions) · §8 ("Visual Calm" — CAL language posture must not imply automated recovery) · **RT-01** (Satellite SDK Present) · **RT-02** (no autonomous action) · UXS-5726.

## B · The 2 separated devices · what they see · what the main group sees

### B.1 — On the separated devices

| Step | Behaviour on the separated device | Doc · § |
|---|---|---|
| 1 | MTT loses BLE Mesh peer-discovery for all 4 main-group peers. Peer-lost events propagate from MTT → CAL.SFM. | **`state-cal.md`** (S3/S4 → S5 transitions) |
| 2 | CAL state transitions `S3 → S5 · QueueOnly` (or `S4 → S5` if previously degraded). Flag vector becomes `[F, T, F, F]`. | **FSD-5126** · `state-cal.md §5` |
| 3 | UI label changes to **"Queue pending"** initially. After the discovery window elapses with no peer found → label may transition to **"Offline"**. Repaint ≤ 2 s. | **UXS-5726** · CAL state matrix S5 label set |
| 4 | Any outgoing user message / heartbeat is **enqueued** to `MOB-3002` SQL via `CAL.QMGR` (comms_queue partition). WAL · AES-256 · Firebase-independent (M0f). The queue is **purely local**. | **`compliance-matrix.md §10`** Mobile data persistence · **M0f** Firebase-independent queue |
| 5 | NAV `MOB-2001` is **unaffected** — it does not depend on CAL state. The user still has full offline navigation + breadcrumb capture + BackTrack + SOS available. | **ESF-5026** §4 (Immutable Separation Boundary) · **`state-trackaroo-transitions.md §7`** (Inter-layer isolation map) |
| 6 | What the user sees overall: a calm "Queue pending" / "Offline" CAL badge · normal NAV map · normal SOS button. **No alarm. No "Searching for signal…" copy.** | **UXS-5726** · `compliance-matrix.md §8` |

### B.2 — On the main-group devices (what the GHE pills show)

| Step | Behaviour on the main-group devices | Doc · § |
|---|---|---|
| 1 | Main-group peers' MTTs no longer hear broadcasts from the 2 separated devices. After the heartbeat-miss threshold (per peer-state TTL), the pill for each missing peer enters a **stale** visual state — last-heard timestamp ages, status bucket greys out. | TrackMate group view spec · UXS-5726 |
| 2 | When the separated peer crosses the **Group Health Envelope visual threshold** (e.g. last-heard older than threshold, OR broadcast battery bucket fell below threshold before they went out of range), the pill silently changes colour/icon — **no animation, no audio alert**, per Visual Calm doctrine. | **UXS-5726** · `compliance-matrix.md §8` |
| 3 | The pill change is **deterministic** — `(last_heard_age_bucket × last_battery_bucket × last_motion_bucket) → icon`. No ML, no inference, no probabilistic weighting. | **RT-03** (no AI/probabilistic/adaptive) · `compliance-matrix.md §4` |
| 4 | **No automated message is generated. No SOS is triggered on any device. No authorities are notified.** | **RT-01** · **RT-02** · `compliance-matrix.md §4` Zero Transmission |
| 5 | A main-group user who notices the indicator change can **manually decide** to send a BLE Mesh check-in ping (which won't reach the out-of-range peers — message queues locally) or to coordinate a recovery action via voice/visual signal among in-range members, or to manually open SOS on their own device. | **HFG-5026 §5.4** Declarative Consent Model (explicit user action only) |

## C · GHE-vs-SOS boundary · what the system does and does NOT do

| Question | Answer | Doc · § |
|---|---|---|
| **Does GHE indicator dropping below threshold trigger SOS on the affected peer's device?** | **No.** SOS state machine only transitions out of `INACTIVE` via Tap 1 → Tap 2 by the user holding the device. No remote trigger exists. | **`state-trackaroo-transitions.md §3`** (SOS state machine — `INACTIVE → TRIGGER_PENDING` only via "Tap 1") · **RT-15** (SOS ≤ 2-tap path empirically validated; no other entry path exists) |
| **Does GHE indicator dropping below threshold trigger SOS on a main-group peer's device?** | **No.** Same reason — SOS is a strictly human-initiated state transition on the device that activates it. No mesh-message can flip another device's SOS state. | Same as above · enforced by code review against the SOS state machine — no MTT incoming-message handler is wired to the SOS module |
| **Does GHE indicator dropping below threshold transmit anything off-device?** | **No.** No outbound packets, no cloud call, no satellite trigger. The GHE indicator change is a **rendering** event in TrackMate using already-received peer-state broadcasts. | **RT-01** Satellite SDK Present · **ESF-5026 §4.2** Zero outbound · `compliance-matrix.md §4` Zero Transmission |
| **Does GHE indicator change escalate UI on the main group's devices (alarm tone, full-screen banner, modal)?** | **No.** Visual Calm doctrine prohibits alarming copy and forbids "Recovery in progress" / "Searching for signal…" language. The pill changes colour/icon and **that is the entire system response.** | **UXS-5726** (Visual Calm) · `compliance-matrix.md §8` |
| **What CAN happen autonomously?** | Exactly one thing: the local CAL state machine flips between S3/S4/S5 according to its **deterministic** flag vector (peer-presence + latency). UI label changes per state. **That's it.** | `state-cal.md §5` |

### Why no automated distress response is triggered — architectural proof

1. **Inter-Layer Isolation Map** (`state-trackaroo-transitions.md §7`) enumerates every Experience-Layer event and the prohibition that prevents it from mutating Survival Core. The relevant row: `E2 HazTrack feed event → C3 SOS access path` is prohibited; the principle generalises — **no Experience-Layer event can flip SOS state**.
2. **App → Core write barrier** — Application Layer (where TrackMate + GHE live) may only **read** from Core. SOS module `MOB-2004` does not expose a write API to App Layer.
3. **Static-analysis CI gate** — checks that no Experience-Layer module imports the SOS state-transition function (compliance-matrix.md §13).
4. **Architectural barrier visualised** — `CORE_BARRIER` red dashed wall in master architecture (`trackaroo-phase1-architecture.drawio`) physically separates App Layer from Survival Core.

> **Bottom line for the evaluator:** GHE is a **visual indicator only**. No code path exists that turns a GHE state change into an automated SOS trigger. This is enforced by 4 independent mechanisms (state-machine entry points, write-barrier, static-analysis, architectural separation).

## D · Phase 2 boundary confirmation — satellite scaffold is inert

### The 3 permitted Phase 2 scaffolds in the Phase 1 build

| # | Scaffold | Location in architecture | Phase 1 state |
|---|---|---|---|
| **1** | **BackTrack™ Emergency Escrow Data Schema** | Schema lives in `MOB-3002` SQL alongside breadcrumb_log; accessed by BT `MOB-2002` | Versioned schema · stubs for sync-consent flags + encryption envelopes · **zero transmission logic** · **zero user-visible artefacts** |
| **2** | **CAL `satReady` Flag** | Boolean in CAL state schema (`MOB-1101.SFM`) | Hardcoded `FALSE` · **not reachable** by any application path · enforced by static analysis |
| **3** | **CAL Satellite Transport Architectural Pathway** | Extensible `ITransport` adapter interface in CAL Transport Router (`MOB-1101.TR`) · **no compile-time branches** capable of activation | Documented interface · no implementing class · no SDK linked |

**Doc trail:** `diagrams/4-cross-cutting/phase-2-readiness.md §1`.

### The 4 Placeholder Discipline rules — every scaffold must satisfy ALL four

1. **Visually Surfaced** — each scaffold has a visible cell/badge in the master architecture diagram (BT escrow badge · CAL satReady badge · HW_SAT cell with PHASE 2 badge) so QA + evaluators can locate them on inspection.
2. **Mandatory Display Text** — any user-visible placeholder MUST display **exactly** "Inactive in Phase 1." HW_SAT cell text + EXT_GPS cell text both contain this string verbatim.
3. **Schema-Complete** — data structures are ready for Phase 2 activation without structural rework (BT escrow schema versioned, CAL flag schema accommodates runtime control).
4. **Zero Executable Logic** — no runtime pathway, no compile-time branch capable of activation. Enforced by static-analysis CI gate.

**Doc trail:** `phase-2-readiness.md §2`.

### How the vendor ensures scaffolds cannot be triggered — **Mode C: static reachability confirmation**

Per evaluator note ("Mode B or Mode C accepted for phase boundary confirmation") the vendor delivers **Mode C — static reachability analysis with CI gate enforcement**:

| Check | Pattern | What it enforces |
|---|---|---|
| `satReady` literal `true` | Regex `satReady\s*=\s*true` → **0 matches required** | Scaffold #2 hardcoded FALSE invariant |
| Satellite SDK imports | Regex `import.*(iridium\|inmarsat\|globalstar\|orbcomm)` → **0 matches required** | RT-01 Satellite SDK Present prohibition |
| Prohibited field names | Regex `(satTransmissionStatus\|satelliteEndpoint\|dispatch_channel)` → **0 matches required** | Placeholder Discipline #4 (Zero Executable Logic) |
| **Scaffold reachability** | **Static reachability analysis from every Phase 1 execution surface** → **0 paths** to any of the 3 permitted scaffolds | **RT-09 · Phase 2+ Scaffold Triggerable** (release halts if any dormant scaffold is reachable) |
| CAL → Survival Core imports | Regex `from mob_core` inside CAL modules → **0 matches required** | Architectural isolation (separate concern but enforced in same CI pass) |

**Doc trail:** `phase-2-readiness.md §4` · `compliance-matrix.md §13`.

**Vendors (Slitigenz et al.) commit to running these checks before each release gate. Full verification is a mandatory exit criterion for Alpha · Beta · GA gates.**

### Why no edge-case operating state can trigger the scaffolds

| Edge case | Why scaffolds remain inert |
|---|---|
| Cellular drops, battery low, BLE peers lost, queue full, SOS active, breadcrumb gap, all at once | CAL state machine has exactly 5 reachable states (S0–S5) and **`satReady=F` invariant in every one of them** (see `mob-cal-architectural-diagram.drawio` Page 2 + `state-cal.md §3`). No flag combination flips satReady. |
| User taps a Phase 2 UI cell repeatedly | The cells are visually inert — no event handler is wired. Static reachability analysis confirms no execution path emerges from clicking them. |
| OTA / config push attempts to flip satReady | satReady is `final true → false` hardcoded constant in build · not a config-table key · not a runtime-mutable state. Static analysis catches any attempted re-binding. |
| BT escrow schema gets data written by mistake | The escrow tables are **schema-defined but no producer code exists** — static reachability shows 0 writer paths. Even if hand-edited bytes appeared, no consumer code reads them either. |
| Satellite SDK arrives via transitive dependency | CI gate `import.*(iridium\|inmarsat\|globalstar\|orbcomm)` matches transitive imports too (compiled module manifests are scanned, not just source). |

## Evaluator probes — Scenario 2

### E.1 · UI element referencing satellite relay — hidden, greyed out, or absent?

| Aspect | Answer | Doc · § |
|---|---|---|
| **Present** in master architecture diagram? | **Yes** — visually surfaced per Placeholder Discipline #1 (M0p Maximal scope decision). HW_SAT cell visible with PHASE 2 amber badge + grey-dashed border + exact text "Inactive in Phase 1." · EXT_GPS the same · BT cell has "P2 ESCROW SCAFFOLD · Inactive in Phase 1." badge · CAL has "satReady = FALSE · Inactive in Phase 1." badge. | **`phase-2-readiness.md §1`** Visual indicators table · **M0p** in `design-decisions.md` |
| **Present in the running app UI** (what the end-user actually sees)? | **No.** The Phase 1 app UI surfaces the 4 CAL labels only ("Beacon active" / "Limited Connectivity" / "Queue pending" / "Offline"). There is no UI affordance referencing satellite — no greyed-out button, no "Phase 2" tab, no settings toggle. | **UXS-5726** (Visual Calm — language posture) · CAL state matrix `state-cal.md §5` |
| **Why this asymmetry?** | The architecture diagram is for vendors/evaluators/auditors — Placeholder Discipline mandates visual surfacing so QA can locate the scaffold. The end-user app is for end-users — exposing inert UI would confuse them and would risk RT-09 (scaffold triggerable / accessible outside QA placeholders). The diagram is the "QA placeholder" exception. | **`phase-2-readiness.md §2`** Discipline #1 + #4 · **RT-09** ("…accessible · visible (outside of QA placeholders)") |
| **What if a user uses a developer build / debug mode?** | Even debug builds must pass the static-reachability CI gate. The 3 scaffolds remain unreachable from any Phase 1 execution surface in any build flavour. | **`phase-2-readiness.md §4`** static-analysis CI gate |

**Summary:** the Phase 2 satellite functionality is **absent from end-user UI**, **present in the architecture diagram with mandated "Inactive in Phase 1." text**, and **unreachable at runtime in every build flavour**.

### E.2 · LoRa peripheral connected mid-session — what does the user see? Are the 4 WFD-5126 onboarding states triggered?

| Step | Behaviour | Doc · § |
|---|---|---|
| 1 | User pairs a LoRa peripheral (GoTenna Mesh or Meshtastic) over BLE during an active TrackMate session. | **M8 LoRa peripheral vendor** (FSD-5126 · PSB-5026) · GoTenna SDK / Meshtastic open integration |
| 2 | OS BLE-pairing flow completes → app receives a paired-device event for `EXT-9007` LoRa peripheral. | OS-level BLE pairing (out of scope for governance — Phase 1 spec respects native OS pairing UX) |
| 3 | App enters the **4-state WFD-5126 LoRa peripheral onboarding flow** — vendor proposes the implementation reflects the 4 states verbatim from WFD-5126 (Wireframe & UI State Authority): **(a) Detection** — peripheral detected, awaiting user acknowledgement · **(b) Pairing/Provisioning** — peripheral firmware/config exchange in progress · **(c) Active/Paired** — peripheral healthy and registered with MTT as a Tier-2 transport adapter · **(d) Error/Disconnect** — peripheral unreachable, error displayed, retry path offered. | **WFD-5126** (Wireframe & UI State Authority) — full state copy + visual treatment derives from this doc · vendor implements all 4 states |
| 4 | When state (c) reaches **Active/Paired**, MTT registers the LoRa `ITransport` adapter. CAL's 5-rule priority algorithm now sees Tier 2 as available (provided a peer is in LoRa range). | **M5 transport priority** · `state-cal.md §158` Tier 2 LoRa "✅ Active (paired peripherals only)" |
| 5 | The user does **not** see "LoRa active" copy in the main UI — they see the same 4 CAL labels (Beacon active / Limited / Queue pending / Offline). The transport tier is intentionally **transparent** to the user. (See E.3 below.) | **UXS-5726** · `state-cal.md §5` |
| 6 | If the 2 separated devices come into LoRa range of any device with a paired LoRa peripheral, the system can opportunistically exchange peer-state broadcasts via Tier 2 — **deterministically** per the 5-rule priority. | **M5 priority** · `mob-cal-architectural-diagram.md` Tier 2 row |

**Yes — all 4 WFD-5126 onboarding states are triggered. Vendor will deliver UI for each state matching the WFD-5126 wireframes verbatim.**

### E.3 · "Transport-transparent to the user" — what it means in practice

| Aspect | Answer | Doc · § |
|---|---|---|
| **What "transport-transparent" means** | The user is shown only the **outcome** of CAL's transport decisions (one of 4 calm labels — Beacon active / Limited Connectivity / Queue pending / Offline) — **never** the underlying tier (BLE Mesh / Wi-Fi Direct / LoRa / Sat). | **UXS-5726** (Visual Calm) — calm-language enforcement · **`state-cal.md §5`** mandated label set |
| **Can the user determine which transport is currently active from the UI?** | **No** — and **deliberately so**. The 4 CAL labels are intentionally tier-agnostic. There is no "BLE active" / "LoRa active" / "Wi-Fi active" indicator in the user-facing UI. | UXS-5726 · CAL state matrix |
| **Should the user be able to determine it?** | **No.** Surfacing transport mechanism would (a) violate Visual Calm doctrine (creates anxiety when tiers switch), (b) tempt the user to make decisions based on tier knowledge that the system already handles deterministically via the 5-rule priority, (c) leak architectural detail that is meant to be abstracted. | **UXS-5726** · **M5** transport priority (system, not user, owns tier selection) · **RT-02** (no autonomous user-driven reroute on tier change) |
| **Where IS transport tier observable?** | (a) Engineering diagnostics / dev-tools view (not in end-user app) · (b) Audit log + event log (`MOB-2005` Local Event Log, 30-day retention) · (c) `mob-cal-architectural-diagram.drawio` for vendors/evaluators. | **`compliance-matrix.md §11`** event log retention · `mob-cal-architectural-diagram.drawio` |
| **What if the user really wants to know?** | An advanced "Diagnostics" screen (Pro tier · settings-deep) MAY surface tier in a future iteration — but only as **read-only display** never as control. Even then, the main NAV / TrackMate UI remains tier-agnostic. | UXS-5726 — read-only display permitted; control prohibited (RT-02 spirit) |

**Practical implication for this scenario:** the user with the freshly paired LoRa peripheral does not see "LoRa now active." They see the same CAL label they always see. If LoRa enables a peer-state broadcast to reach the separated members, the GHE pills for those members will refresh — and the user infers from the pill change, not from a transport label, that the connection improved.

---

# Document status

| Field | Value |
|---|---|
| Purpose | Canonical vendor responses to client scenario walkthroughs · governance traceability for Discovery / Alpha / Beta / GA gate review |
| Scope | Scenario 1 (Survival Core) · Scenario 2 (TrackMate group + Phase 2 boundary) |
| Mode used for Phase 2 boundary confirmation | **Mode C — static reachability analysis with CI gate enforcement** (per evaluator preparation note: Mode B or Mode C accepted) |
| Outstanding governance items | **RT-09 ID collision** — deferred per M0q · client/spec author to disambiguate before Beta gate · see `design-decisions.md M0q` and `phase-2-readiness.md §3` |
| Trigger to update | (a) New scenario added by client · (b) governing-document version bump (BTF-5126, SFD-5026, UXS-5726, ESF-5026, BPS-5126, WFD-5126, FSD-5126, HFG-5026, MAS-5126, CQR-5026) · (c) RT-09 disambiguation closes M0q · (d) M6 calibration finalises (CAL latency threshold) |
