# Trackaroo® Phase 1 — Spec Authority Stack Reference

**Status:** External governance reference · synthesized from spec
**Purpose:** Single map of all governing documents in the trackaroo Phase 1 authority stack, how they rank against each other, and where each one touches our architecture work.

**Conflict resolution rule:** *"In the event of a conflict, interpretation resolves **strictly upward** through this stack."* — i.e., the higher-ranked document wins, no negotiation.

---

## 1. The 3-tier structure

```
┌───────────────────────────────────────────────────────────────┐
│ TIER 1 — PRIMARY AUTHORITY (6 docs · ranked top → bottom)     │
│                                                               │
│   ↑  UXS-5726 — UX Strategy & Behavioural Authority           │
│   │  PRD-5126 — Product Requirements & Acceptance             │
│   │  FSD-5126 — Functional Specification                      │
│   │  TQP-5026 — Testing & QA Authority                        │
│   │  WFD-5126 — Wireframe & UI State Authority                │
│   ↓  VGD-5126 — Vendor Guidance & Delivery Enforcement        │
│                                                               │
├───────────────────────────────────────────────────────────────┤
│ TIER 2 — SPECIALIST DOMAIN (10 docs · parallel · no ranking)  │
│                                                               │
│   OSM-5026 · CDG-5126 · BTF-5126 · HFG-5026 · MAS-5126        │
│   BPS-5126 · ESF-5026 · TAA-5126 · FRM-5126 · OCS-5026        │
│                                                               │
├───────────────────────────────────────────────────────────────┤
│ TIER 3 — STRATEGIC / OPERATIONAL REFERENCE (5 docs)           │
│                                                               │
│   AOD-5026 · VRB-5126 · PSB-5026 · RFT-5026 · CAR-5026        │
│                                                               │
└───────────────────────────────────────────────────────────────┘

       + 2 Amendments dated 13 April 2026:
         - Process Amendment Notice
         - Commercial Model Amendment Notice
```

**Tier 1 ranking implication:** `UXS > PRD > FSD > TQP > WFD > VGD`. UX behaviour rules override everything else. Vendor obligations are the lowest of Tier 1 (vendor cannot use VGD to override product behaviour).

**Tier 2 has no internal ranking** — each specialist authority owns its own domain. If two specialists conflict, both get overruled by relevant Tier 1.

---

## 2. Full document catalogue

### Tier 1 — Primary Authority (ranked top → bottom)

| Rank | ID | Full title | Authoritative scope |
|---|---|---|---|
| 1 | **UXS-5726** | UX Strategy & Behavioural Authority | All behavioural decisions + human-facing interaction rules |
| 2 | **PRD-5126** | Product Requirements & Acceptance Authority | Acceptance criteria + rejection triggers |
| 3 | **FSD-5126** | Functional Specification | Functional execution baseline for all subsystems |
| 4 | **TQP-5026** | Testing & QA Authority | Validation methodology + gate criteria + testing discipline |
| 5 | **WFD-5126** | Wireframe & UI State Authority | Visual + interaction presentation · build gate for all subsystem development |
| 6 | **VGD-5126** | Vendor Guidance & Delivery Enforcement | Vendor obligations + enforcement controls + rejection triggers |

### Tier 2 — Specialist Domain Authorities (no internal ranking)

| ID | Full title | Sole authority for… |
|---|---|---|
| **OSM-5026** | Overlay Semantics Map | Overlay visual semantics · TTL thresholds · **PCR framework** |
| **CDG-5126** | Cloud & Data Governance Standard | Data classification · persistence models · **Firebase isolation model** |
| **BTF-5126** | BackTrack™ Framework | Breadcrumb architecture · reverse retrace logic · data immutability |
| **HFG-5026** | Hazard Feed Governance | Hazard feed eligibility · ingestion rules · **Five-Pillar inclusion filter** |
| **MAS-5126** | Mapping Architecture & Visual System Standard | Basemap styling · offline tile architecture · cartographic standards |
| **BPS-5126** | Battery Performance Standard | Battery benchmarks · standardised test conditions · **device validation matrix** |
| **ESF-5026** | Emergency Safety Framework | SOS liability boundary · non-dispatch posture · satellite prohibition rules |
| **TAA-5126** | Target Archetypes & Activity Context | **Six canonical archetypes** · activity contexts · subscription tier philosophy |
| **FRM-5126** | First Aid Reference Framework | Content tier model · **clinical review gate** |
| **OCS-5026** | Operations Console Specification | Functional requirements for the web-based internal admin platform |

### Tier 3 — Strategic / Operational Reference

| ID | Full title | Purpose |
|---|---|---|
| **AOD-5026** | Architecture Overview | **Authoritative visual reference** for dual-layer architecture + component annotation |
| **VRB-5126** | Vendor Response Baseline | Mandatory structured response format + non-scope expansion guardrails |
| **PSB-5026** | Phase Scope Boundary | Single source of truth for active Phase 1 scope vs Phase 2 deferrals |
| **RFT-5026** | Request for Tender | Formal engagement document · scope of work + delivery milestones |
| **CAR-5026** | Central Amendment Register | Living document tracking amendment history of every doc in the stack |

### Amendments (13 April 2026)

| Name | Impact |
|---|---|
| **Process Amendment Notice** | Concessions to delivery process · *content TBD pending read* |
| **Commercial Model Amendment Notice** | Revised pricing structure · *content TBD pending read* |

---

## 3. Document ID numbering pattern

| Suffix | Docs | Hypothesis |
|---|---|---|
| `-5026` | TQP, OSM, HFG, ESF, OCS, AOD, RFT, PSB, CAR | Original baseline release (Series 5026) |
| `-5126` | PRD, FSD, WFD, VGD, CDG, BTF, MAS, BPS, TAA, FRM, VRB | Revision wave (Series 5126) — newer or revised versions |
| `-5726` | UXS | Unique series — possibly elevated tier marker for highest authority |

`CAR-5026` (Central Amendment Register) is likely the record of `5026 → 5126` revision transitions.

→ **Action:** Confirm with client whether different suffixes have semantic meaning or are just versioning quirks.

---

## 4. Mapping to our current work

### 🟢 Already referenced / aligned

| Spec doc | Where we touch it | Our artifact |
|---|---|---|
| **AOD-5026** | The whole architecture diagram is implementation of AOD | `diagrams/1-overview/trackaroo-phase1-architecture.{md,drawio}` |
| **OCS-5026** | OCS-5026 component label in master + scope §reference in CAL doc | `diagrams/1-overview/` + `mob-cal-architecture.md` |
| **BTF-5126** | BackTrack architecture · 14 mutation prohibitions (BC-M01–14) · state machine | `state-trackaroo-transitions.md §2 §8` |
| **OSM-5026** | HazTrack TTL semantics · PCR framework · CAL threshold mention | `state-trackaroo-transitions.md §4` + `mob-cal-architecture.md` |
| **CDG-5126** | Firebase Independence · V-12/V-13 invariants · Firestore prohibited edges | Master diagram + `state-trackaroo-transitions.md §7` |
| **ESF-5026** | SOS non-dispatch · `satReady=false` mandate · satellite prohibition | `mob-cal-architecture.md` + master diagram |
| **MAS-5126** | Mapbox SDK · OSM vector tiles · Bundle Manager · MVT/PBF compression | Master + `cbe-trackiq-pipeline.md` + `mapbox-sdk-overview.md` |
| **HFG-5026** | Authority hazard feeds (BOM/AFAC/SES/Geoscience AU) | Master diagram `EXT_HAZARD` |
| **TQP-5026** | First Aid isolation §5.7.7 reference + testing discipline | `state-trackaroo-transitions.md §7` |

### 🟡 Touched but not explicitly cited (add references)

| Spec doc | Where it implicitly applies | Action |
|---|---|---|
| **FRM-5126** | `MOB-2008 First Aid (Baseline)` + `MOB-1002 First Aid` tier split (decision M0a) | Add FRM-5126 ref to design-decisions.md M0a + future `mob-survival-core.md` |
| **BPS-5126** | All battery + device validation perf targets (≤8%/hr nav, ≥10hr endurance, etc.) | Populate `4-cross-cutting/performance-targets.md` with BPS-5126 column |
| **TAA-5126** | `MOB-1003 Six Archetype Presets` component | Verify our 6 archetypes match TAA's canonical list when filling `mob-application-layer.md` |
| **PSB-5026** | `EXT_GPS` Phase 2 inert · `satReady=false` Phase 2 stub · all "Phase 2" labels | Reference PSB-5026 wherever Phase 2 inertness is shown |

### 🔴 Not yet referenced — gaps to close

| Spec doc | Why we need it | Status |
|---|---|---|
| **UXS-5726** ⚠️ | **Highest authority.** CAL "calm language" rules + UI response time + interaction posture likely derive from here | NOT READ |
| **PRD-5126** | Acceptance criteria for every component · drives our component definitions | NOT READ |
| **FSD-5126** | Functional execution baseline · **bedrock for all MOB-xxxx and CBE-xxxx components** | NOT READ |
| **WFD-5126** | UI wireframes · out of architecture scope but relevant if vendor needs UI deliverables | NOT READ |
| **VGD-5126** | **Vendor obligations + rejection triggers** — critical for our proposal not getting rejected | NOT READ |
| **VRB-5126** | **Structured response format** — our proposal must follow this format | NOT READ |
| **CAR-5026** | Amendment history — need to confirm we're working with latest versions | NOT READ |
| **2 Amendments 13 Apr 2026** | Process + Commercial concessions — may change scope/pricing assumptions | NOT READ |

---

## 5. Implications for our proposal

### Critical actions before submission

1. **Get + read VRB-5126** — non-compliant response format = automatic rejection
2. **Get + read VGD-5126** — vendor rejection triggers; avoid these landmines
3. **Get + read 2 Amendments (13 Apr 2026)** — could materially change cost estimates
4. **Cross-check AOD-5026** vs our master diagram — our master is *derivative* of AOD; if AOD has authoritative component IDs differing from ours, AOD wins
5. **Get + skim FSD-5126** — verify our component inventory (MOB-1xxx, MOB-2xxx, CBE-xxxx) matches FSD's functional baseline

### Documentation hygiene going forward

When filling Tier 2 subsystem deep-dives (`diagrams/2-subsystems/*.md`), each component description should include:

```markdown
**Spec authority:** <Primary doc> (primary) · <Specialist docs> (supporting)
```

Example:
```markdown
### MOB-2002 BackTrack™
**Spec authority:** BTF-5126 (primary) · FSD-5126 (functional baseline) · TQP-5026 §X (test discipline)
```

This makes Discovery Gate review faster — auditor can verify trace chain in one pass.

### How to use this stack when client raises objections

If client says *"your diagram contradicts spec"*, the resolution path is:

1. Identify which spec doc raises the issue
2. Identify which tier it's in
3. If our work derives from a **lower-tier** doc → we must update to match
4. If our work derives from a **higher-tier** doc → we have ammunition to push back
5. If unclear → escalate to UXS-5726 (highest) for behavioural questions, PRD-5126 for acceptance questions

---

## 5b. Discovery Gate deliverables required

Specific named artifacts vendor must produce at the Discovery Gate, per spec:

| # | Deliverable | Spec source | Our artifact | Status |
|---|---|---|---|---|
| 1 | **High-Level Architecture Diagram** annotated with Survival Core isolation boundaries | (general spec) | `diagrams/1-overview/trackaroo-phase1-architecture.{md,drawio}` — Architecture page with `CORE_BARRIER` wall + 2 prohibited edges | 🟢 Done |
| 2 | **Deterministic State Transition Matrix** for Survival Core | TQP-5026 + spec on determinism | `diagrams/3-flows/state/state-trackaroo-transitions.md` — 6 state machines + §7 isolation map + §8 prohibition register | 🟢 Done (existing) |
| 3 | **Module Isolation Mapping** — low-level dependency graph proving Experience cannot mutate Core | CDG-5126 + FSD-5126 | Partial: `state-transitions.md §7` + master diagram `CORE_BARRIER`. Standalone `4-cross-cutting/module-isolation-mapping.md` pending | 🟡 Partial |
| 4 | **CAL Architecture Documentation** — transport priority + 4 state flags + static analysis | FSD-5126 + ESF-5026 + UXS-5726 | `diagrams/2-subsystems/mob-cal-architecture.md` (filled) + drawio CAL Architecture page | 🟢 Done |
| 5 | **PCR Architecture Documentation** — supersession-based resolution model | OSM-5026 (PCR framework authority) | Not started — stub planned at `diagrams/2-subsystems/mob-pcr-framework.md` | 🔴 TODO |
| 6 | **Offline-First Execution Explanation** — proof of 100% functionality without network | (general spec) + TQP-5026 (Offline Resilience Testing) | Not started — needs dedicated doc explaining: (a) zero-network paths in Survival Core, (b) Faraday + GPS spoofing test methodology, (c) "visual calm" UX evidence | 🔴 TODO |

### Validation methods bound to deliverables

| Method | Spec source | Applies to |
|---|---|---|
| **Offline Resilience Testing** — Faraday shielding + GPS spoofing (beyond airplane mode) | TQP-5026 | Deliverable #6 (Offline-First Execution Explanation) |
| **Static Analysis** — confirm `satReady=false`, no satellite SDKs, no Core imports from CAL | TQP-5026 + VGD-5126 | Deliverable #4 (CAL) |
| **"Visual Calm" criteria** — UI must remain calm during signal denial (no alarming language / animations / escalation messaging) | UXS-5726 | Deliverables #1, #4, #6 |
| **Forensic Immutability check** — confirm Core data cannot be modified/reordered/uploaded post-write | BTF-5126 + CDG-5126 | Deliverables #2, #3 |

---

## 6. Open questions for client (Discovery Gate ammo)

Bring these to next client meeting to unblock dependencies:

| # | Question | Why it matters |
|---|---|---|
| Q1 | Do we have access to **UXS-5726**? | Highest authority — drives all UX/behavioural decisions including CAL UI language posture |
| Q2 | Is **VRB-5126 (Vendor Response Baseline)** available? | Our proposal format must comply — risk of rejection |
| Q3 | Are **VGD-5126 (Vendor Guidance)** rejection triggers documented? | Need to avoid them in proposal |
| Q4 | What's in the **2 Amendments dated 13 April 2026**? | Could change pricing model or process timelines |
| Q5 | Does **AOD-5026** (Architecture Overview) exist as a visual artifact? | We could align our diagrams more tightly · risk of inventing components not in AOD |
| Q6 | Is **CAR-5026 (Central Amendment Register)** kept current? Can we get latest version of every doc? | Avoid working with stale specs |
| Q7 | Is **FRM-5126** specific about FA Baseline vs Plus/Pro tier split? | Confirms our M0a decision (MOB-2008 in Core vs MOB-1002 in App) |
| Q8 | Does **TAA-5126** list the canonical six archetypes? | Verify MOB-1003 component matches |
| Q9 | Does **BPS-5126** define device validation matrix beyond "iPhone 15/16/17 + Samsung/Pixel flagships"? | Need full list for test plan |
| Q10 | What's HFG-5026's **"Five-Pillar inclusion filter"** for hazard feeds? | New concept · may affect EXT_HAZARD scope |

---

## 7. Maintenance

Update this file when:
- A new spec doc is added to the stack → add to relevant tier table
- A spec is read for the first time → flip its row from 🔴/🟡 to 🟢 + cite where it's now referenced
- An amendment changes ranking or scope → note the amendment ID and date
- Client confirms answer to one of Q1–Q10 → remove from §6 and add insight to §4 mapping

---

## Cross-references

- Design decisions: `./design-decisions.md` — each row should cite Spec Authority column
- Master architecture: `../diagrams/1-overview/trackaroo-phase1-architecture.md`
- Tech stack inventory: `./tech-stack-inventory.md`
- Mapbox notes: `./mapbox-sdk-overview.md`
- Subsystem docs (when filled): `../diagrams/2-subsystems/`
