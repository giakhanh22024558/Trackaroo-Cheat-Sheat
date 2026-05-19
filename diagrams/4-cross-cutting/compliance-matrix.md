# Compliance Matrix — All System-Wide Prohibitions, UI Invariants & Enforcement Points

**Status:** 🚧 Stub — checklist populated, content TBD for each row
**Tier:** 3 (Cross-cutting concern)
**Replaces:** All red compliance banners + UI invariants scattered across master + subsystem diagrams

## Why this document exists

The master architecture diagram had **5+ compliance banners** glued to different zones (RT-09, Authority-Origin Mandate, V-12/V-13, Survival Core Compliance, HazTrack Isolation, Tile Cost Governance, NAV Performance). That's visual clutter and forces readers to mentally aggregate.

This file is the **single canonical source** for every architectural prohibition, named rejection trigger, and cross-cutting UI invariant. Subsystem diagrams reference rows here instead of repeating the rule.

## Document structure (when filled)

Each rule will be a row with these columns:

| ID | Rule | Constraint type | Spec authority | Enforcement point | Verification method | Rationale |
|---|---|---|---|---|---|---|

---

## 1. Backend / TrackIQ Pipeline prohibitions

- [ ] **RT-09** — No telemetry feedback into TrackIQ scoring
- [ ] **RT-09** — No ML inference in TrackIQ pipeline
- [ ] **RT-09** — TrackIQ scoring must be idempotent
- [ ] **RT-09** — TrackIQ scores mutate only via OCS-5026 (manual approval gateway)
- [ ] **HazTrack isolation** — Hazards must NOT mutate TrackIQ grade (no `HAZADMIN → SCORE` path)
- [ ] **TrackIQ thresholds** — Must be configurable via OCS · NOT hardcoded

## 2. External data origin mandates

- [ ] **Authority-Origin Mandate** — Hazard data must come from statutory / govt / emergency authorities · aggregators + commercial APIs PROHIBITED
- [ ] **Five-Pillar inclusion filter** — Hazard feeds must pass HFG-5026 eligibility check before integration

## 3. Cloud / Sync (Firebase) isolation

- [ ] **V-12** — Firebase sync threads isolated from Survival Core (no shared lifecycle)
- [ ] **V-13** — Silent failure when offline · no error-state leakage from sync into Core
- [ ] **Zero Reconciliation** — Firestore cloud cannot mutate Survival Core data
- [ ] **Write-Once Security** — PCR collection in Firestore is append-only
- [ ] **TLS 1.3 minimum** for all in-transit traffic to/from Firestore

## 4. Survival Core operational prohibitions

- [ ] **No external search APIs at runtime** — Core paths cannot call any cloud search service
- [ ] **No geocoding services at runtime** — Core paths cannot call Mapbox Geocoding, Google Places, etc.
- [ ] **No cloud rerouting** — Routes recalculated locally only
- [ ] **Zero Auto-Rerouting (RT-02)** — NAV must NOT automatically recalculate or switch routes on hazard intersection, GPS jitter, off-route detection, or any internal trigger. **All reroute decisions require explicit user consent** via the 5-step Declarative Consent Model (HFG-5026 §5.4). Rationale: prevents leading users into unknown hazards without their consent · prevents false confidence in automated decisions during emergencies. Enforced: state-machine transition `NAVIGATING → NOTIFIED` requires user action; no internal trigger emits the transition (see `../3-flows/state/state-trackaroo-transitions.md §1`). Spec authority: **MAS-5126** · **HFG-5026** · RT-02 named rejection trigger
- [ ] **100% local operation** — Pre-downloaded bundles only · no runtime tile fetch
- [ ] **Zero Transmission** — Core functions (SOS, BackTrack) generate zero outbound packets in Phase 1
- [ ] **Deterministic execution** — Identical inputs always produce identical outputs · no AI/ML/adaptive logic

## 5. Core ⇎ App / Core ⇎ Cloud isolation (Immutable Separation Boundary)

> **Spec terminology:** the Experience ⇎ Survival Core wall is the **Immutable Separation Boundary** (per NAV spec §4). Earlier drafts of this matrix called it "Isolation Boundary" — same concept, spec name preferred for traceability.

- [ ] **MOB_APP ⇎ MOB_CORE — Immutable Separation Boundary** — Experience Layer cannot mutate Survival Core (rendered as `CORE_BARRIER` wall in master diagram, not arrow). Non-safety-critical features (group messaging, archetype presets, TrackIQ scoring display) are architecturally incapable of blocking, delaying, or mutating core navigation flow. Even if Experience Layer fully fails, NAV/BackTrack/SOS remain operational
- [ ] **MOB_CORE → SYN** PROHIBITED — Core never pushes to cloud (red dashed edge in master)
- [ ] **SYN → MOB_CORE** PROHIBITED — Cloud never pushes to Core (Firebase Independence)
- [ ] **Application → Core boundary** — Application Layer can read from Core (limited surfaces) but NEVER write
- [ ] **Forensic Integrity (BTF-5126)** — 14 specific mutation behaviors prohibited (BC-M01–14): map-matching, path smoothing, coordinate interpolation, etc.

## 6. Tile cost governance (offline maps)

- [ ] **Max tile count ceiling per device** — vendor proposes specific number (M4 blocker)
- [ ] **MVT/PBF compression mandatory** — no uncompressed tile paths
- [ ] **Cache reuse across app updates** — no re-download of unchanged tiles on version bump
- [ ] **Re-download minimization** — partial download recovery via resumable bundle manager

## 7. First Aid Reference (FRM-5126) — Universal Baseline & tier governance

- [ ] **RT-12** — Deploying any FA content without written Project Director clearance = automatic release-halt
- [ ] **RT-XX (named)** — Applying paywall or tier restriction to Universal Baseline, OR displaying upgrade prompt on Baseline screens = named rejection trigger
- [ ] **Universal Baseline = free on every tier** — no paywall, no authentication, no upgrade prompts
- [ ] **No diagnostic AI / symptom inference / adaptive reference logic** — FA must be deterministic step-by-step
- [ ] **Persistent disclaimer** — Every FA screen displays fixed non-dismissible disclaimer + Triple Zero direction (or local emergency service)
- [ ] **Clinical Review Gate** — All FA content reviewed by qualified clinical professional (wilderness paramedic or emergency nurse) before exposure
- [ ] **Free tier privacy** — Static read-only · NO PII collection · NO telemetry · NO clinical health info
- [ ] **Plus tier privacy** — Event log allowed (timestamps + user notes) · NO clinical health info
- [ ] **Pro tier APP 3 compliance** — Professional incident log requires:
  - AES-256 at rest
  - Explicit informed consent before activation
  - Strict access controls
  - APP 3 sensitive information classification
- [ ] **PRO_LOG sync model — opt-in only** — Cloud sync of `MOB-3003 Professional Incident Log` is **user-optional** and **prohibited without explicit, separate consent**. Default state: zero-egress (no cloud sync). Activation requires: (a) explicit informed consent dialog, (b) consent record persisted locally, (c) audit log entry for consent action, (d) ability to revoke + wipe cloud copy. Sync edge in diagram: `PRO_LOG ⤴ SYN` rendered amber dashed (CONSENT-GATED, distinct from auto-sync yellow + prohibited red)
- [ ] **HazTrack cache Firebase ingress exception** — `MOB-3005 HazTrack Overlay Cache` is allowed to receive Firebase ingress for cache refill ONLY (authority-origin data sync). Runtime queries MUST hit local cache exclusively · zero runtime Firebase calls during navigation · sync failures → silent freshness indicator update (NO alarming UI)
- [ ] **Connectivity indicator suppression** — When FA Baseline screen active, CAL status indicator must be hidden (no "offline" UI noise during medical emergency)

## 8. Cross-cutting UI invariants ("Visual Calm" doctrine — UXS-5726)

- [ ] **"Visual Calm" copy** — All system copy uses calm, factual, reassuring language. Prohibited: "Reconnecting…", "Searching for signal…", "Recovery in progress…", anything implying autonomous action or alarm
- [ ] **HazTrack silent failure** — Feed failures result in silent freshness indicator update · NO user-facing alarms
- [ ] **CAL language posture** — Indicators must not imply automated recovery or escalation is pending
- [ ] **FA persistent disclaimer** — Always visible during FA module use (see §7)

## 9. Performance + accessibility invariants (cross-component)

- [ ] **≤2-tap SOS** — Reachable from any screen state in ≤2 taps
- [ ] **≤2-tap FA Reference** — Reachable from any screen state in ≤2 taps (including active navigation + SOS confirmation screen)
- [ ] **NAV initial render ≤2 seconds** on validated device matrix
- [ ] **NAV max 3 concurrent map layers** active
- [ ] **Cold start ≤6s (bundles ≤500MB) / ≤8s (>500MB)**
- [ ] **Frame rate** — 60fps idle · ≥45fps floor during interaction
- [ ] **Battery** — ≤8%/hr nav · ≥10hr endurance · ≤20%/hr sustained SOS

## 10. Mobile data persistence requirements

- [ ] **AES-256 encryption at rest** — All Survival Core data (MOB-3002) + Professional Incident Log (MOB-3003)
- [ ] **Write-Ahead Logging (WAL)** — Crash survivability for safety-critical stores
- [ ] **Firebase Independence** — Survival Core data classified Local-Only & Non-Syncable
- [ ] **Forensic Immutability** — Once written locally, Survival Core data cannot be modified, reordered, or uploaded to cloud in Phase 1
- [ ] **SOS log immutability** — SOS distress records are append-only · forever retention
- [ ] **Pro Incident Log (MOB-3003)** — APP 3 sensitive · explicit consent before activation · access controls beyond just encryption

## 11. Audit + governance

- [ ] **System Audit Log retention** — 7-year minimum (OCS-5026)
- [ ] **Pipeline Run History retention** — 90-day minimum (OCS-5026)
- [ ] **Event Log retention** — 30-day minimum on device (MOB-2005)
- [ ] **All OCS metrics module actions logged immutably** to system audit log

## 12. Regulatory / external compliance

- [ ] **TGA Software as a Medical Device (SaMD)** classification — FA module requires legal opinion (FRM-5126)
- [ ] **Australian Privacy Principles (APPs)** — particularly APP 3 (sensitive info) for Pro tier
- [ ] **Phase 2 prohibition: Satellite SDKs** — no `satReady=true` in Phase 1 · static analysis enforced (ESF-5026 · CAL doc)
- [ ] **RT-01 · Satellite SDK Present** — Release halt if Phase 1 build contains: satellite SDKs (active or linked) · feature-flagged satellite modules · stubbed transmission classes. Enforced by static-analysis CI gate (§13)
- [ ] **RT-09 · Phase 2+ Scaffold Triggerable** — Release halt if any dormant scaffolding is accessible · visible (outside QA placeholders) · or executable in Phase 1 build. **⚠️ ID COLLISION with §1 RT-09 (TrackIQ feedback prohibition) — see `design-decisions.md M0q` · client/spec author to disambiguate before Beta gate**

## 13. Static analysis enforcement (CI gate)

- [ ] `satReady` literal `true` → 0 matches expected
- [ ] Satellite SDK imports (iridium/inmarsat/globalstar/orbcomm) → 0 matches expected
- [ ] CAL → Survival Core imports → 0 matches expected (architectural isolation)
- [ ] Direct transport calls outside `ITransport` abstraction → 0 matches expected
- [ ] AI/ML inference framework imports (tensorflow, pytorch, onnxruntime, coreml) in Core modules → 0 matches expected
- [ ] **Phase 2 Scaffold prohibited field names** → 0 matches expected for: `satTransmissionStatus` · `satelliteEndpoint` · `dispatch_channel` (enforces Placeholder Discipline #4 "Zero Executable Logic")
- [ ] **Phase 2 Scaffold reachability** → static reachability analysis MUST show 0 paths from any Phase 1 execution surface to the 3 permitted scaffolds (BT escrow schema · CAL satReady flag · CAL satellite transport pathway)

---

## Additional sections (to fill)

- [ ] **Master Visualization** — render all PROHIBITED edges + barriers as a single Mermaid diagram with system zones as light backdrops, only red elements shown
- [ ] **Verification mapping table** — each rule → test/audit that verifies it
- [ ] **Spec source quotes** — direct quotes from spec documents per rule (traceability)
- [ ] **RT-trigger summary** — all named Rejection Triggers (RT-09, RT-12, RT-XX paywall) in one table with halt conditions
- [ ] **Enforcement mechanisms** — static analysis · runtime checks · architectural barriers · process gates · code review

---

## Cross-references

- Master: `../1-overview/trackaroo-phase1-architecture.md`
- Performance siblings: `./performance-targets.md`
- Tile lifecycle: `./tile-lifecycle.md`
- All subsystems link back to specific rows in this file
- Spec authority stack: `../../research/spec-authority-stack.md`
- Design decisions: `../../research/design-decisions.md`
- Navigation: `../README.md`
