# Phase 2 Readiness · Scaffold Zone Catalog

**Tier:** 3 (Cross-cutting concern)
**Purpose:** Canonical reference for the **3 permitted Phase 2 scaffolds** in the Phase 1 build · the **4 Placeholder Discipline rules** · the **2 named rejection triggers** · the **static analysis verification gates**. Demonstrates to client/vendor/auditor that Phase 1 architecture is **forward-compatible to Phase 2 without structural rework**.

**Status:** ✅ Filled · canonical reference for gate review (Alpha · Beta · GA exit criteria)

---

## 1. The 3 permitted Phase 2 scaffolds

Only these three architectural hooks are authorized for inclusion in Phase 1. Anything else would violate **RT-01 (Satellite SDK Present)** or **RT-09 (Phase 2+ Scaffold Triggerable)** (⚠️ RT-09 ID collision — see `design-decisions.md M0q`).

| # | Scaffold | Location in architecture | Phase 1 state | Phase 2 activation |
|---|---|---|---|---|
| **1** | **BackTrack™ Emergency Escrow Data Schema** | Schema lives in `MOB-3002` SQL (alongside breadcrumb_log) · accessed by `BT (MOB-2002)` | Versioned schema · stubs for sync-consent flags + encryption envelopes · **zero transmission logic** · **zero user-visible artefacts** | Schema-complete · ready for forward migration when satellite escrow goes live |
| **2** | **CAL `satReady` Flag** | Boolean in CAL state schema (`MOB-1101`) | Hardcoded `FALSE` · **not reachable** by any application path · enforced by static analysis | Flipped to runtime-controlled `TRUE/FALSE` when satellite transport activates |
| **3** | **CAL Satellite Transport Architectural Pathway** | Extensible `ITransport` adapter interface in CAL (`MOB-1101` Transport Router) · **no compile-time branches** capable of activation | Documented interface · no implementing class · no SDK linked | Tier-3 transport adapter implementation slots in via `ITransport` |

### Visual indicators on master architecture

| Scaffold | Visual marker on `diagrams/1-overview/trackaroo-phase1-architecture.{md,drawio}` |
|---|---|
| BT Escrow Schema | `BT` cell badge: `P2 ESCROW SCAFFOLD · Inactive in Phase 1.` |
| CAL satReady flag | `CAL` cell badge: `satReady = FALSE · Inactive in Phase 1.` |
| CAL Satellite Pathway | `HW_SAT` cell with `PHASE 2` badge + dashed grey style · "Inactive in Phase 1." · "Future: BackTrack Emergency Escrow" + new edge `HW_SAT -.-> MOB_G2` dashed grey labeled "Phase 2 pathway · Inactive in Phase 1." |

---

## 2. The 4 Placeholder Discipline rules (non-negotiable)

All items in the scaffold zone MUST satisfy:

1. **Visually Surfaced** — each scaffold explicitly identifiable + reviewable during QA validation
   - ✅ Master architecture cells carry visible badges (see table above)
2. **Mandatory Display Text** — any user-visible placeholder MUST display **exactly** the text: **"Inactive in Phase 1."**
   - ✅ All 3 scaffold cells use this exact phrase
3. **Schema-Complete** — data structures ready for Phase 2 activation without structural rework
   - ✅ BT escrow schema versioned per spec · stubs declared · forward-migration tested
4. **Zero Executable Logic** — no runtime pathway · no compile-time branch capable of activation
   - ✅ Enforced by static-analysis CI gate (see §4 below)

---

## 3. Rejection Triggers

| RT ID | Mandate | Enforcement |
|---|---|---|
| **RT-01 · Satellite SDK Present** | Release halts if Phase 1 build contains: satellite SDKs (active or linked) · feature-flagged satellite modules · stubbed transmission classes | Static-analysis CI gate — `compliance-matrix.md §13` |
| **RT-09 · Phase 2+ Scaffold Triggerable** | Release halts immediately if any dormant scaffolding is accessible · visible (outside of QA placeholders) · or executable in Phase 1 build | Static-analysis CI gate — `compliance-matrix.md §13` |

### ⚠️ RT-09 ID collision (deferred)

`RT-09` is used in `compliance-matrix.md §1` for "No telemetry feedback into TrackIQ scoring" mandate. Spec author's Scaffold Zone document also uses `RT-09` for "Phase 2+ Scaffold Triggerable". Same numeric ID, different mandates · **client/spec author must disambiguate before Beta gate**. Tracked in `research/design-decisions.md M0q`.

---

## 4. Verification · static analysis CI gates

The following automated checks run during CI/CD pipeline · 0 matches expected for each (full list in `compliance-matrix.md §13`):

| Check | Pattern | Enforces |
|---|---|---|
| satReady literal `true` | `satReady\s*=\s*true` | Scaffold #2 hardcoded FALSE |
| Satellite SDK imports | `import.*(iridium\|inmarsat\|globalstar\|orbcomm)` | RT-01 |
| Prohibited field names | `(satTransmissionStatus\|satelliteEndpoint\|dispatch_channel)` | Placeholder Discipline #4 |
| Scaffold reachability | Static reachability analysis from Phase 1 execution surfaces | RT-09 (no triggerable path) |
| CAL → Survival Core imports | `from mob_core` inside CAL modules | Architectural isolation (separate concern) |

Vendors (Slitigenz et al.) commit to running these checks before each release gate. **Full verification is a mandatory exit criterion for Alpha · Beta · GA gates.**

---

## 5. Gate exit criteria (per phase)

| Gate | Phase 2 readiness criteria (this doc enforces) |
|---|---|
| **Alpha** | All 3 scaffolds present + 4 disciplines verified + static analysis green for satReady=FALSE + RT-01/RT-09 checks pass |
| **Beta** | Above + RT-09 ID collision resolved (M0q closure required) + scaffold reachability analysis attached to release notes |
| **GA** | Above + 3rd-party security review confirms no dormant code paths reachable + signed-off Phase 2 migration runbook references this doc |

---

## 6. Cross-references

- Master architecture (visual markers): `../1-overview/trackaroo-phase1-architecture.md` · `.drawio` — see badges on BT · CAL · HW_SAT · EXT_GPS + dashed grey edge `HW_SAT → MOB_G2`
- Compliance matrix (full mandate text · static analysis gates): `./compliance-matrix.md` §12 (RT-01 + RT-09) · §13 (static analysis enforcement)
- CAL subsystem deep-dive (satReady detail): `../2-subsystems/mob-cal-architecture.md` §3 "Mandatory state flags"
- CAL architectural diagram (visual flag transitions): `../2-subsystems/mob-cal-architectural-diagram.md` Page 2 (S0–S5 state machine with satReady=F invariant)
- BackTrack subsystem (escrow schema): `../2-subsystems/mob-survival-core.md` BT section (stub currently · spec-confirmed scaffold)
- Design decisions: `../../research/design-decisions.md` — M0p (Phase 2 scaffold visibility policy) · M0q (RT-09 collision deferred)
- Performance targets: `./performance-targets.md` — Alpha/Beta/GA gate dates · scaffold verification exit criteria

---

## 7. Document status

| Field | Value |
|---|---|
| Purpose | Canonical Phase 2 scaffold zone catalog · gate-review reference |
| Scope | 3 scaffolds · 4 disciplines · 2 RT triggers · static-analysis enforcement |
| Outstanding | RT-09 ID collision (M0q deferred · Blocker for Beta) |
| Trigger to update | (a) Phase 2 kickoff · (b) new scaffold proposed (must be added here BEFORE Phase 1 commit) · (c) RT-09 disambiguation closes M0q |
