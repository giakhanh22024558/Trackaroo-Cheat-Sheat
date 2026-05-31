"""Generate Confluence-export skeleton pages for Trackaroo Phase 1.

Section indexes = full-content navigation pages.
Detail pages = draft skeleton (title, purpose, source, outline placeholders).
"""

from pathlib import Path

ROOT = Path(r"C:\Users\Admin\Desktop\Trackagroo local management\confluence-export")

# ---------- Detail page skeleton template ----------

DETAIL_TEMPLATE = """# {title}

> **Status:** Draft skeleton — to be filled.
> **Owner:** {owner}
> **Last updated:** 2026-05-31

## Purpose
{purpose}

## Source artefact(s)
{sources}

## Outline (to fill)

{outline}

---
*Draft created from project repo. Source of truth: see repo files above.*
"""

def write_detail(path, title, owner, purpose, sources, outline_items):
    """sources = list of strings, outline_items = list of (heading, todo)"""
    src_block = "\n".join(f"- `{s}`" for s in sources)
    outline_block = "\n\n".join(
        f"### {h}\n*[TODO: {t}]*" for h, t in outline_items
    )
    content = DETAIL_TEMPLATE.format(
        title=title, owner=owner, purpose=purpose,
        sources=src_block, outline=outline_block
    )
    path.write_text(content, encoding='utf-8')


# ---------- Section indexes (full overview content) ----------

ABOUT_INDEX = """# 📘 1. ABOUT — Project & Team

> **Everything you need to know about *the project itself* — not the product.** Who, what, when, how we work, what to call things.

## Pages in this section

| Page | What's in it | Read if you... |
|---|---|---|
| [Project overview](./01-overview.md) | Mandate, scope, what Phase 1 covers (and doesn't) | …are new or need a refresher on what we're building and why |
| [Roadmap & milestones](./02-roadmap-milestones.md) | The 4 gates (Discovery → Alpha → Beta-Ready → GA) and what's due at each | …need to know "when is X due" |
| [Team & contacts](./03-team-contacts.md) | Who does what, RACI, escalation path | …don't know who to ask about X |
| [Ways of working](./04-ways-of-working.md) | Scrum cadence, DoR/DoD, ceremonies, dual-track | …are joining a sprint or running a refinement |
| [Story / AC conventions](./05-story-ac-conventions.md) | How to write a Story, AC format (Given/When/Then en), ID rules | …are writing or reviewing backlog items |
| [Change Request process](./06-change-request-process.md) | When CR · who approves · impact analysis flow | …have a scope change to raise |
| [Tool stack](./07-tool-stack.md) | Jira · Confluence · Drive · GitHub — what's used for what | …don't know where things live |
| [Onboarding](./08-onboarding.md) | Day-1, Week-1 checklist; environment setup | …are new to the team |
| [Glossary](./09-glossary.md) | Acronyms (SOS, BackTrack™, CAL, PCR, RT/RG…) + domain terms | …saw an acronym you don't know (often!) |

## Core facts (cheat sheet)

| | |
|---|---|
| **Project name** | trackaroo® Phase 1 |
| **Client / IP owner** | Trackaroo Systems Pty Ltd (Australia) |
| **Project Director** | Ian Moore (Founder) |
| **Delivery partner** | Slitigenz Pty Ltd |
| **Contract executed** | 29 May 2026 |
| **Hard launch (GA)** | 13 November 2026 |
| **Operating domain** | Survival-grade outdoor mobile app (4WD / hike / remote pro / fish & hunt) |
| **Primary platforms** | iOS 15+ · Android 13+ (Flutter) |
| **Architecture model** | Dual-layer: Survival Core (offline · deterministic · immutable) ⇎ Experience & Intelligence Layer (online-tolerant) |

## Project mantra

> *"trackaroo® supports safer human decision-making for people travelling and operating in remote or low-signal outdoor environments, when digital information becomes limited or uncertain."*
> — Product Anchor Statement (Ian Moore)

The dual-layer architecture exists to enforce this: **the Experience Layer must NEVER block the Survival Core.** Authority web: AOD §51 · PSB §21 · PRD §182 · UXS §75.
"""

PRODUCT_INDEX = """# 📗 2. PRODUCT — Product specification

> **What we're building.** All feature-level content lives here. For "why" rules exist → [RULES](../03-rules/_index.md). For architecture → [TECH](../04-tech/_index.md).

## Pages in this section

| Page | What's in it |
|---|---|
| [System overview](./01-system-overview.md) | Dual-layer architecture, the 11 epics, high-level diagrams |
| [User roles](./02-user-roles.md) | 6 user archetypes (TAA-5126) + 3 console roles (OCS-5026) |
| [Modules](./03-modules/_index.md) | The 11 product modules (= Epics) with feature lists |
| [Shared features](./04-shared-features.md) | Cross-module functions (settings, profile, account, attachments, etc.) |

## The 11 product modules (Epics)

| # | Module | Epic | Gate | Spec |
|---|---|---|---|---|
| 1 | [Navigation](./03-modules/01-navigation.md) | EPIC-001 | Alpha | FSD-5126 §4.1 · OSM-5026 §5A · MAS-5126 |
| 2 | [SOS](./03-modules/02-sos.md) | EPIC-002 | Alpha | ESF-5026 · SFD-5026 · FSD-5126 §4.4 |
| 3 | [BackTrack™](./03-modules/03-backtrack.md) | EPIC-003 | Alpha | BTF-5126 · FSD-5126 §4.2 |
| 4 | [HazTrack™](./03-modules/04-haztrack.md) | EPIC-004 | Alpha | HFG-5026 · OSM-5026 §6 |
| 5 | [First Aid Reference](./03-modules/05-first-aid.md) | EPIC-005 | Alpha | FRM-5126 · WFD-5126 §5.9 |
| 6 | [App Experience](./03-modules/06-app-experience.md) | EPIC-006 | Alpha | WFD-5126 §5.16 · FSD-5126 §4.5 |
| 7 | [Operations Console](./03-modules/07-operations-console.md) | EPIC-007 | Alpha+Beta | OCS-5026 |
| 8 | [TrackIQ™](./03-modules/08-trackiq.md) | EPIC-008 | Beta-Ready | OSM-5026 §5 · FSD-5126 · WFD-5126 §5.10 |
| 9 | [PCR (Point Condition Reports)](./03-modules/09-pcr.md) | EPIC-009 | Beta-Ready | OSM-5026 §10 · WFD-5126 §5.17 |
| 10 | [TrackMate™](./03-modules/10-trackmate.md) | EPIC-010 | Beta-Ready | FSD-5126 §6.2 · WFD-5126 §5.7–5.8 |
| 11 | [POI](./03-modules/11-poi.md) | EPIC-011 | Beta-Ready | POI-5026 · WFD-5126 §5.11 |

## Module layer mapping

- **Survival Core (offline, deterministic):** Navigation · SOS · BackTrack™ · HazTrack™ (display only) · First Aid
- **Experience & Intelligence Layer (online-tolerant):** TrackIQ™ · PCR · TrackMate™ · POI · Operations Console
- **App-shell (App Experience):** glue layer, present at both tiers
"""

RULES_INDEX = """# 📕 3. RULES — Business rules & cross-cutting conventions

> **Rules and constraints that apply across the product.** Each Story/Feature references these by ID. If a rule applies to only one feature, it belongs in that feature's page (PRODUCT), not here.

## Pages in this section

| Page | What's in it |
|---|---|
| [Business Rules](./01-business-rules.md) | Catalog of BR-XXXX with rationale + spec authority |
| [Permission Matrix (RBAC)](./02-permission-matrix.md) | 6 user archetypes × app capability · 3 console roles × OCS module |
| [Data Dictionary](./03-data-dictionary.md) | Entity × field × meaning · per CDG-5126 + BTF-5126 |
| [UX Guidelines](./04-ux-guidelines.md) | Date format · error states · validation · 5-Question Hierarchy · accessibility |

## Why these rules exist (top 5)

1. **Non-adaptive · non-inferential** — Survival Core must NEVER use AI/ML/inference. *(UXS-5726, OSM-5026)*
2. **Offline-first · zero-network for Core** — every Survival Core path works in airplane mode. *(FSD-5126, BPS-5126)*
3. **Immutable safety records** — breadcrumbs, SOS logs, anchors cannot be edited/silently overwritten. *(BTF-5126 §5.2, ESF-5026)*
4. **Layer independence** — no overlay system may mutate another (LIR-01..06). *(OSM-5026)*
5. **Phase 1 prohibitions** — no satellite transmission, no AI scoring, no telemetry weighting. *(PSB-5026)*

## Source authority hierarchy

Conflicts resolve upward:

```
UXS-5726 (Highest — behavioural / cognitive authority)
   ↑
PRD-5126 (Acceptance criteria)
   ↑
FSD-5126 (Functional execution)
   ↑
TQP-5026 (Validation)
   ↑
WFD-5126 (UI states · wireframe gate)
   ↑
Specialist docs (OSM · OCS · HFG · BTF · CDG · POI · MAS · ESF · SFD · BPS · TAA · FQH · AOD · PSB · FRM · VGD · CRG · CRQ)
```
"""

TECH_INDEX = """# 📙 4. TECH — Architecture & engineering

> **How the system is built.** Architecture, ERD, APIs, infrastructure, security, decisions, code standards.

## Pages in this section

| Page | What's in it |
|---|---|
| [Architecture overview](./01-architecture-overview.md) | Dual-layer model, 5 subsystems (CBE · MOB · OCS · SYN · CAL), C4 view |
| [ERD](./02-erd.md) | Core entities × relationships across local + cloud |
| [API contract / Integration](./03-api-integration.md) | External integrations (Mapbox, BOM, Firebase) + internal API surface |
| [Infrastructure & environments](./04-infrastructure-environments.md) | Dev / staging / prod · CI/CD pipeline · deployment topology |
| [Security & authentication](./05-security-auth.md) | AES-256 at rest · TLS 1.3 in transit · Firebase Auth scoping · zero outbound from Core |
| [ADR (Architectural Decision Records)](./06-adr-decision-records.md) | Recorded decisions: Flutter, Mapbox SDK choice, Firestore boundary, dual-layer split |
| [Tech standards](./07-tech-standards.md) | Code style · error codes · logging · branching · commit format |

## High-level architecture map

```
┌─────────────────────────────────────────────────────────────┐
│  MOBILE APP — Flutter · iOS 15+ / Android 13+              │
│                                                             │
│  ┌─────────────────────────┐  ┌──────────────────────────┐ │
│  │ MOB-1000 Application    │  │ MOB-2000 Survival Core   │ │
│  │ (Experience & Intel)    │  │ (offline · deterministic)│ │
│  └─────────┬───────────────┘  └──────────────────────────┘ │
│            │                                                │
│  ┌─────────▼───────────────┐                                │
│  │ CAL — Connectivity      │  ← 4 state flags                │
│  │ Abstraction Layer       │                                │
│  └─────────┬───────────────┘                                │
└────────────┼────────────────────────────────────────────────┘
             │
             ▼
┌────────────────────────────┐    ┌─────────────────────────┐
│ SYN-7000 Firebase Firestore│◄───┤ CBE-5000 Cloud Backend │
│ (sync engine · App data)   │    │ (TrackIQ pipeline, etc.) │
└────────────────────────────┘    └────────┬────────────────┘
                                            │
                                  ┌─────────▼─────────┐
                                  │ OCS-5026 Console  │
                                  │ (operator-only)   │
                                  └───────────────────┘
```

Full detail: see [`diagrams/1-overview/trackaroo-phase1-architecture.md`](../../diagrams/1-overview/trackaroo-phase1-architecture.md) and sub-system deep-dives in [`diagrams/2-subsystems/`](../../diagrams/2-subsystems/).

## Top decisions (links to ADR)

- **Flutter** for mobile (cross-platform with iOS/Android parity at low cost)
- **Mapbox SDK + OSM tiles** for offline-first mapping
- **Firebase / Firestore** for sync ONLY (NEVER for Survival Core writes)
- **Dual-layer split** with one-way Experience → Core read-only dependency
"""

# Write section indexes
(ROOT / "01-about" / "_index.md").write_text(ABOUT_INDEX, encoding='utf-8')
(ROOT / "02-product" / "_index.md").write_text(PRODUCT_INDEX, encoding='utf-8')
(ROOT / "03-rules" / "_index.md").write_text(RULES_INDEX, encoding='utf-8')
(ROOT / "04-tech" / "_index.md").write_text(TECH_INDEX, encoding='utf-8')

# ---------- ABOUT detail pages (9) ----------

about_pages = [
    ("01-overview.md", "Project overview",
     "Delivery Lead / Project Director",
     "Mandate, scope, dual-layer architecture rationale, what Phase 1 covers vs defers.",
     ["docs/planning.md §A1", "research/spec-docs/Slitigenz-Proposal-RFT5026.md §1–2",
      "research/spec-docs/PRD-5126.md §1–3", "CLAUDE.md"],
     [("Mandate & anchor statement", "1-paragraph statement of intent + Product Anchor quote"),
      ("Phase 1 scope (in)", "11 epics summary · 4 client gates · 13 Nov 2026 hard launch"),
      ("Phase 1 scope (out — deferred)", "Phase 2 inert scaffolds (3 permitted) + explicitly excluded items"),
      ("Architecture model in one diagram", "Embed `diagrams/1-overview/` master diagram"),
      ("Why this matters (safety position)", "Survival-grade · non-adaptive · offline-first reasoning")]),

    ("02-roadmap-milestones.md", "Roadmap & milestones",
     "Delivery Lead",
     "The 4 client gates with dates, what's due at each, freeze dates, buffer policy.",
     ["docs/planning.md §A1 + §A2", "docs/planning.md §B5"],
     [("Master timeline", "Gantt / table view of 12 sprints + 4 gates"),
      ("Per-gate commitments", "Discovery (D1-D9 + site) · Alpha (Survival Core) · Beta-Ready · GA"),
      ("Feature freeze policy", "Alpha freeze 8 Aug · Beta freeze 17 Oct"),
      ("Buffer policy", "S5/S10/S11 = stabilisation/release buffers · 15-day pre-gate buffers"),
      ("Critical path & risks", "What slips a gate if it slips · escalation triggers")]),

    ("03-team-contacts.md", "Team & contacts",
     "Delivery Lead",
     "Who does what. RACI for key decisions. Who to ask about X.",
     ["docs/planning.md §A2 (parallel tracks)", "research/spec-docs/Slitigenz-Proposal-RFT5026.md §10.3"],
     [("Client side (Trackaroo Systems)", "Ian Moore (PD), legal, clinical reviewer, validation coordinator"),
      ("Delivery side (Slitigenz)", "Delivery Lead · 8 expert tracks · architects · QA · BA"),
      ("Who to ask about X (matrix)", "Question type → role → person · escalation path"),
      ("RACI for key decisions", "Scope variation · gate sign-off · CR approval · prod incident"),
      ("Comms channels", "Slack / email / weekly steerco / daily standups")]),

    ("04-ways-of-working.md", "Ways of working",
     "Delivery Lead",
     "Scrum cadence, dual-track development, Definition of Ready/Done, ceremonies.",
     ["docs/planning.md §A1 risk-buffer policy", "conventions/features-conventions.md"],
     [("Scrum cadence", "2-week sprints · planning · daily · review · retro"),
      ("Dual-track delivery", "Discovery track (BA + design refines next sprint) parallel to Delivery track (current sprint)"),
      ("Definition of Ready (DoR)", "Story criteria before pulling into sprint"),
      ("Definition of Done (DoD)", "Acceptance criteria · tests · WCAG checks · prohibition scan pass · PD review where applicable"),
      ("Ceremonies", "Planning · Refinement · Daily · Review/demo · Retro · Steerco · Gate review"),
      ("Sprint 0 special case", "Foundation sprint — Topic/Concern/AC model, not feature stories")]),

    ("05-story-ac-conventions.md", "Story / AC conventions",
     "BA Lead",
     "How to write Stories and Acceptance Criteria the way this project requires.",
     ["conventions/features-conventions.md", "MasterMind/models/model_001/document/features/conventions-defaults/ac-writing.md"],
     [("Backlog hierarchy", "Epic (EPIC-NNN) → Feature (FEAT-NNN) → Story (STORY-NNN) → AC (AC-{story}-{nn})"),
      ("Priority-ordered IDs (PROJECT RULE)", "Lower ID = higher delivery priority"),
      ("Story format", "`[User archetype] can [action]` · single behaviour, demonstrable in 1 sprint"),
      ("AC format — Given / When / Then (en)", "Example: `Given a missing required field, when clicking Save, then the Save button is disabled`"),
      ("Foundation hierarchy (Sprint 0 only)", "Topic → Concern → Task (S0-) → AC (AC-C{n}-{nn})"),
      ("References to spec", "Inline reference to spec doc + section, not free prose")]),

    ("06-change-request-process.md", "Change Request process",
     "Delivery Lead + PD",
     "When something needs CR, who approves, impact analysis flow, recorded where.",
     ["research/spec-docs/Slitigenz-Proposal-RFT5026.md §11 CLR-SLZ pattern", "docs/gap-clarifications.md (CLR-TRK)"],
     [("What needs a CR (vs internal clarification)", "Scope change · gate timing · external dependency · prohibition exception"),
      ("CR vs CLR distinction", "CLR (clarification register, internal) = spec ambiguity · CR (Change Request, contractual) = scope variation"),
      ("Impact analysis (17-col gap analysis template)", "Topic · As-Is · To-Be · Impl per role · Est per role · Decision · CAR-5026 record"),
      ("Approval flow", "PM raises → BA impact analysis → Delivery Lead review → PD approval → CAR-5026 record"),
      ("Where they live", "Active CRs in Jira · log in CAR-5026 · CLRs in `docs/gap-clarifications.md`")]),

    ("07-tool-stack.md", "Tool stack",
     "Delivery Lead",
     "What tool is used for what. The single rule: each piece of info lives in exactly one tool.",
     ["CLAUDE.md", "MASTERMIND-INTEGRATION.md"],
     [("Source-of-truth matrix", "Repo (docs/specs/diagrams) · Jira (sprint execution) · Confluence (read view) · Drive (raw inputs + PDFs) · GitHub (code + CI)"),
      ("Project repo layout", "`docs/` · `research/spec-docs/` · `diagrams/` · `conventions/` · `MasterMind/` (read-only)"),
      ("Jira usage", "Epic/Feature/Story/Bug · sprint board · gate evidence linkage"),
      ("Confluence usage", "This space = read view of the repo · re-export to sync"),
      ("Drive usage", "Raw PDFs + Q&A folder + client-shared documents (one-way: download, no edits)"),
      ("GitHub usage", "Code + CI + ADR-as-code + this repo (`Trackaroo-Cheat-Sheat`)")]),

    ("08-onboarding.md", "Onboarding",
     "Delivery Lead",
     "Day-1, Week-1 checklist. Local environment setup. Required reading.",
     ["CLAUDE.md", "docs/planning.md"],
     [("Day 1 — orientation", "Accounts (Jira/Confluence/Drive/GitHub) · workspace tour · meet the team · read this Home + ABOUT"),
      ("Day 1 — read these 6 pages", "[Project overview · Roadmap · Tool stack · Glossary · System overview · UX guidelines]"),
      ("Week 1 — environment setup", "Repo clone · Flutter setup · Firebase emulator · pre-commit hooks · local CI run"),
      ("Week 1 — observe", "Attend 1 sprint planning · 1 refinement · 1 demo · shadow your role lead"),
      ("Role-specific deep dive", "Pointer to BA / Dev / QA / Designer specific path"),
      ("Definition of 'ramped'", "When you can pick up a Story unassisted")]),

    ("09-glossary.md", "Glossary",
     "BA Lead",
     "Acronyms and domain terms — the project uses many. Look here before asking.",
     ["research/spec-docs/READING-GUIDE.md", "research/spec-docs/ (all extracts)"],
     [("Trademark / product terms", "trackaroo® · BackTrack™ · TrackMate™ · TrackIQ™ · HazTrack™"),
      ("Architecture terms", "CAL (Connectivity Abstraction Layer) · Survival Core · Experience & Intelligence Layer · SOS · POI · PCR (Point Condition Report) · CDS · WAL · ADR"),
      ("Document IDs (the 20 spec docs)", "UXS · PRD · FSD · TQP · WFD · OSM · OCS · ESF · SFD · BTF · CDG · MAS · HFG · BPS · TAA · FQH · AOD · PSB · FRM · VGD · POI"),
      ("Compliance shorthand", "RT-NN (Rejection Trigger) · RG-NN (Rollback Governance) · LIR-NN (Layer Independence Rule) · WCAG 2.1 AA"),
      ("Gate / process shorthand", "Discovery · Alpha · Beta-Ready · GA · DoR · DoD · CLR · CR · CAR"),
      ("Archetypes (6)", "4WD · Bushwalker (Hike) · Mountain Bike / e-MTB / Dirt Bike · Remote Professionals · Fish & Hunt · Nomad · Snow & Alpine (Phase 2.5)")])
]

for fname, title, owner, purpose, sources, outline in about_pages:
    write_detail(ROOT / "01-about" / fname, title, owner, purpose, sources, outline)


# ---------- PRODUCT umbrella pages ----------

write_detail(ROOT / "02-product" / "01-system-overview.md", "System overview",
    "Architecture Lead",
    "The dual-layer architecture, 5 subsystems, how the 11 epics map to layers.",
    ["research/spec-docs/AOD-5026.md", "research/spec-docs/PRD-5126.md §1–3",
     "diagrams/1-overview/trackaroo-phase1-architecture.md"],
    [("Dual-layer model", "Survival Core (offline · deterministic · immutable) vs Experience & Intelligence Layer (online-tolerant)"),
     ("5 subsystem zones", "CBE-5000 (Cloud Backend) · MOB-1000/2000 (App layers) · OCS-5026 (Console) · SYN-7000 (Firestore sync) · CAL (Connectivity layer)"),
     ("Authority web", "AOD §51 / PSB §21 / PRD §182 / UXS §75 — 'E&I Layer must NEVER block Survival Core'"),
     ("Epic-to-layer mapping", "Which epics belong to Core vs Experience"),
     ("Phase 2 inert scaffolds (3 permitted)", "BackTrack Emergency Escrow schema · CAL `satReady` flag · CAL satellite pathway")])

write_detail(ROOT / "02-product" / "02-user-roles.md", "User roles & archetypes",
    "BA Lead",
    "End-user archetypes (TAA-5126) + console operator roles (OCS-5026) + RBAC summary.",
    ["research/spec-docs/TAA-5126.md", "research/spec-docs/OCS-5026.md §5.2"],
    [("6 end-user archetypes", "4WD · Bushwalker · Mountain Bike / e-MTB / Dirt Bike · Remote Professionals · Fish & Hunt · Nomad · (Snow & Alpine deferred to Phase 2.5)"),
     ("Per-archetype default behaviours", "Archetype presets — POI group defaults, UI tone, etc."),
     ("3 console roles (OCS-5026)", "Project Director · Operations · Authorised Contributor"),
     ("Subscription tiers (commercial)", "Free · Plus · Pro — see RULES → Permission Matrix"),
     ("Per-role capability summary", "Pointer to RULES → Permission Matrix for detail")])

write_detail(ROOT / "02-product" / "04-shared-features.md", "Shared features",
    "BA Lead",
    "Cross-module functions: settings, profile, account management, notifications, offline state surfacing, etc.",
    ["research/spec-docs/PRD-5126.md", "research/spec-docs/WFD-5126.md §5.16"],
    [("Account & profile", "Account creation · profile · archetype switching · subscription state surface"),
     ("Settings", "Privacy · permissions · cache management · offline bundle management"),
     ("CAL status surface", "Connectivity indicator (4 states) — shared component, consumed app-wide"),
     ("Notifications (NO push for Core)", "What's allowed vs prohibited (no SOS push, no alert escalation)"),
     ("In-app messaging", "Empty states · error states · 'Inactive in Phase 1' placeholders"),
     ("Audit & event log surfacing", "Local event-log viewer (FEAT-026)")])


# ---------- PRODUCT modules _index ----------

(ROOT / "02-product" / "03-modules" / "_index.md").write_text("""# 2.3 Modules

The 11 product modules of Trackaroo Phase 1. Each = one Epic. Click through for module-level feature lists.

| Module | Epic | Gate | Page |
|---|---|---|---|
| Navigation | EPIC-001 | Alpha | [01-navigation.md](./01-navigation.md) |
| SOS | EPIC-002 | Alpha | [02-sos.md](./02-sos.md) |
| BackTrack™ | EPIC-003 | Alpha | [03-backtrack.md](./03-backtrack.md) |
| HazTrack™ | EPIC-004 | Alpha | [04-haztrack.md](./04-haztrack.md) |
| First Aid Reference | EPIC-005 | Alpha | [05-first-aid.md](./05-first-aid.md) |
| App Experience | EPIC-006 | Alpha | [06-app-experience.md](./06-app-experience.md) |
| Operations Console | EPIC-007 | Alpha + Beta | [07-operations-console.md](./07-operations-console.md) |
| TrackIQ™ | EPIC-008 | Beta-Ready | [08-trackiq.md](./08-trackiq.md) |
| PCR (Point Condition Reports) | EPIC-009 | Beta-Ready | [09-pcr.md](./09-pcr.md) |
| TrackMate™ | EPIC-010 | Beta-Ready | [10-trackmate.md](./10-trackmate.md) |
| POI | EPIC-011 | Beta-Ready | [11-poi.md](./11-poi.md) |

Each module page contains:
- Purpose + spec authority
- Feature list (FEAT-NNN) with 1-line description
- Phase 1 prohibitions (what's explicitly OUT for this module)
- Cross-references to RULES (Business Rules) and TECH (architecture)
- Open clarifications (CLR-TRK) affecting the module
""", encoding='utf-8')

# ---------- PRODUCT module pages (11) ----------

modules = [
    ("01-navigation.md", "Module: Navigation", "EPIC-001", "FSD-5126 §4.1 · OSM-5026 §5A · MAS-5126",
     "Offline-first navigation: map region download, current location, route planning, instrument overlays."),
    ("02-sos.md", "Module: SOS", "EPIC-002", "ESF-5026 · SFD-5026 · FSD-5126 §4.4",
     "Safety-critical emergency logging. Non-dispatch posture. 2-tap activation. 3-stage log sequence."),
    ("03-backtrack.md", "Module: BackTrack™", "EPIC-003", "BTF-5126 · FSD-5126 §4.2",
     "Immutable breadcrumb capture + reverse retrace. Local-only / non-syncable. 14 prohibited mutations."),
    ("04-haztrack.md", "Module: HazTrack™", "EPIC-004", "HFG-5026 · OSM-5026 §6",
     "Hazard feed ingestion + freshness-indicator display. Cached offline. Never pushes alerts."),
    ("05-first-aid.md", "Module: First Aid Reference", "EPIC-005", "FRM-5126 · WFD-5126 §5.9",
     "Pre-loaded offline first-aid content. Clinically reviewed. Mandatory persistent disclaimer."),
    ("06-app-experience.md", "Module: App Experience", "EPIC-006", "WFD-5126 §5.16 · FSD-5126 §4.5 · UXS-5726",
     "App-shell, onboarding, settings, event-log viewer. The glue between Core and Experience layers."),
    ("07-operations-console.md", "Module: Operations Console (OCS)", "EPIC-007", "OCS-5026",
     "Internal operator tool (web). PCR moderation, account admin, feed admin, audit log. 3-role RBAC."),
    ("08-trackiq.md", "Module: TrackIQ™ Track Difficulty", "EPIC-008", "OSM-5026 §5 · FSD-5126 · WFD-5126 §5.10",
     "Deterministic difficulty scoring. Verification Shield (Gold/Grey). Stop-detection prompt."),
    ("09-pcr.md", "Module: PCR (Point Condition Reports)", "EPIC-009", "OSM-5026 §10 · WFD-5126 §5.17 · FSD-5126 §13",
     "User-submitted condition reports (6 categories). Supersession model (no TTL). 2-reporter confirmation."),
    ("10-trackmate.md", "Module: TrackMate™", "EPIC-010", "FSD-5126 §6.2 · WFD-5126 §5.7–5.8",
     "Peer comms via BLE Mesh → Wi-Fi Direct → LoRa. Group Health Envelope (binary). Offline queue."),
    ("11-poi.md", "Module: POI (Points of Interest)", "EPIC-011", "POI-5026 · WFD-5126 §5.11",
     "55 POI categories across 10 display groups. Group-level toggle. Offline-only search, distance-ranked.")
]

for fname, title, epic, spec, summary in modules:
    src_list = [f"research/spec-docs/{s.split()[0]}.md" for s in spec.split('·') if s.strip()]
    src_list = list(dict.fromkeys(src_list))  # dedup, preserve order
    src_list.append("docs/planning.md §B3")
    write_detail(ROOT / "02-product" / "03-modules" / fname, title,
        "BA Lead + Engineering Lead",
        f"**{epic}** — {summary} Spec authority: {spec}.",
        src_list,
        [("Purpose & user value", "1-paragraph what this module does for the user"),
         ("Features (FEAT-NNN)", "Table of features in this module · 1-line each · pull from planning §B3"),
         ("Wireframe states (WFD)", "List of required WFD states for this module"),
         ("Phase 1 prohibitions", "What's explicitly OUT (per spec) · why"),
         ("Cross-module dependencies", "Other modules this depends on / blocks"),
         ("Open clarifications (CLR-TRK)", "Any active CLR affecting this module · link to gap-clarifications.md")])


# ---------- RULES detail pages (4) ----------

rules_pages = [
    ("01-business-rules.md", "Business Rules catalog",
     "BA Lead",
     "Catalog of cross-cutting Business Rules with stable IDs. Stories reference these by BR-ID.",
     ["research/spec-docs/UXS-5726.md", "research/spec-docs/OSM-5026.md",
      "research/spec-docs/BTF-5126.md", "research/spec-docs/CDG-5126.md",
      "research/spec-docs/FSD-5126.md", "research/spec-docs/PSB-5026.md"],
     [("BR ID convention", "`BR-XXXX` — sequential, stable, never renumbered"),
      ("Survival Core mandates", "Non-adaptive · non-inferential · offline-first · immutable safety records"),
      ("Layer Independence Rules (LIR-01..06)", "Pull from OSM §11"),
      ("Rejection Triggers (RT-01..22)", "Pull from VGD-5126 — what fails a gate"),
      ("Rollback Governance (RG-01..11)", "Pull from OSM §12"),
      ("14 prohibited breadcrumb mutations", "Pull from BTF-5126 §5.2"),
      ("Phase 1 prohibitions (PSB-5026)", "No satellite · no AI scoring · no telemetry weighting"),
      ("Subscription / tier rules", "Free=3 / Plus=20 / Pro=50 anchors (CLR-TRK-001 open)")]),

    ("02-permission-matrix.md", "Permission Matrix (RBAC)",
     "BA Lead",
     "Who can do what. Two matrices: end-user archetypes × app capability, and console roles × OCS module.",
     ["research/spec-docs/TAA-5126.md", "research/spec-docs/OCS-5026.md §5.2",
      "research/spec-docs/POI-5026.md §6.3.2"],
     [("End-user archetype × capability matrix", "6 archetypes × {Nav, SOS, BackTrack, HazTrack, PCR, TrackMate, POI groups}"),
      ("POI group defaults by archetype", "10 groups × 6 archetypes — pull from POI-5026 §6.3.2"),
      ("Subscription tier matrix", "Free / Plus / Pro × {anchors cap, history depth, advanced features}"),
      ("OCS console roles × module matrix", "PD / Operations / Authorised Contributor × {PCR · Grade Admin · TrackIQ · Feed · User Admin · First Aid Content · Audit Log}"),
      ("Server-side enforcement", "All RBAC enforced server-side · OCS UI hides but does not gate"),
      ("Audit log scope", "Every console action logged · PD = all actions · others = own actions only")]),

    ("03-data-dictionary.md", "Data Dictionary",
     "Engineering Lead + BA Lead",
     "Entity × field × meaning. The contract between BA semantics and engineering schemas.",
     ["research/spec-docs/CDG-5126.md §5", "research/spec-docs/BTF-5126.md §5",
      "research/spec-docs/OSM-5026.md §10.5"],
     [("Entity inventory", "Anchor · Breadcrumb · PCR · POI · SOS Log · Hazard Feed · TrackIQ Score · TrackMate Session · User Account · Subscription"),
      ("Per-entity field tables", "Field name · type · required · meaning · mutability · authority spec"),
      ("Data classification (CDG-5126)", "Local-Only · Local-cached-syncable · Cloud-permitted"),
      ("Prohibited fields", "satellite-related field names (PSB-5026) · `confirmation_count` (CDG §5.5) · telemetry-derived"),
      ("ID / UUID conventions", "All safety records use UUID at creation · immutable post-write"),
      ("Schema change governance", "Schema changes = CR + CAR-5026 record · never silent migration on production data")]),

    ("04-ux-guidelines.md", "UX Guidelines",
     "Design Lead + BA Lead",
     "Cross-cutting UX standards: date format, error states, validation, accessibility, the 5-Question Hierarchy.",
     ["research/spec-docs/UXS-5726.md", "research/spec-docs/WFD-5126.md",
      "research/spec-docs/FQH-5026.md", "research/spec-docs/MAS-5126.md"],
     [("Five-Question Cognitive Hierarchy", "1. Where am I? · 2. Where am I going? · 3. What's around me? · 4. How do I get back? · 5. How do I call for help? — all answerable in ≤3 taps · validated across 6 archetypes"),
      ("Non-alarming language model", "What words to use / not use · calm posture · no panic colours unless safety-critical"),
      ("Touch target standards", "Min 44×44pt (WCAG) · 60×60pt recommended for Survival Core controls · glove-compatible"),
      ("WCAG 2.1 AA across the board", "Contrast · keyboard nav · screen reader · low-light / one-handed validated"),
      ("Date / time / unit format", "ISO 8601 timestamps internally · localised display · metric/imperial per archetype default"),
      ("Error & validation states", "Plain language · suggest action · never expose stack traces"),
      ("Empty states", "'Inactive in Phase 1' exact wording for placeholder modules"),
      ("Iconography", "Per MAS-5126 Part B · category-distinct · no colour-only signals (LIR-06)")])
]

for fname, title, owner, purpose, sources, outline in rules_pages:
    write_detail(ROOT / "03-rules" / fname, title, owner, purpose, sources, outline)


# ---------- TECH detail pages (7) ----------

tech_pages = [
    ("01-architecture-overview.md", "Architecture overview",
     "Architecture Lead",
     "C4-style architecture: master view (Tier 1) + subsystem deep-dives (Tier 2) + behavioural flows (Tier 3) + cross-cutting concerns.",
     ["diagrams/1-overview/trackaroo-phase1-architecture.md", "diagrams/2-subsystems/",
      "research/spec-docs/AOD-5026.md", "diagrams/README.md"],
     [("Tier 1 — Master architecture", "Embed master diagram · 5 zones · 1-line component names"),
      ("Tier 2 — Subsystem deep-dives", "CBE-5000 TrackIQ pipeline · MOB-2000 Survival Core · MOB-1000 App layer · OCS-5026 Console · SYN-7000 Firestore"),
      ("Tier 3 — Flows", "DFDs · sequence diagrams · state transitions"),
      ("Cross-cutting concerns", "Compliance matrix · performance targets · tile lifecycle"),
      ("Authority web", "AOD §51 / PSB §21 / PRD §182 / UXS §75 — codified in architecture")]),

    ("02-erd.md", "ERD — Entity Relationship",
     "Engineering Lead",
     "Entities × relationships across local Core store, cached Experience data, and Firestore-permitted entities.",
     ["research/spec-docs/CDG-5126.md §5", "research/spec-docs/BTF-5126.md §5"],
     [("ERD scope split", "Core (local-only · SQLite+WAL) vs Experience (Firestore-permitted)"),
      ("Core entities", "Breadcrumb · SOS Log · Anchor · CAL state"),
      ("Experience entities", "User profile · subscription · PCR cache · HazTrack overlay cache · TrackIQ scoring cache · POI bundle"),
      ("Sync boundaries", "What syncs vs what is local-only-non-syncable"),
      ("Mermaid erDiagram block", "Render via Mermaid for vendor reference")]),

    ("03-api-integration.md", "API contract & integrations",
     "Engineering Lead",
     "External integrations (Mapbox, Firebase, BOM hazard feeds, IAP) + internal API surface (CAL).",
     ["research/spec-docs/HFG-5026.md", "research/spec-docs/MAS-5126.md",
      "research/spec-docs/CDG-5126.md"],
     [("External integrations", "Mapbox SDK (offline tiles) · Firebase Auth + Firestore (sync only) · BOM hazard feeds (HFG) · Apple/Google IAP (subscription)"),
      ("Internal API — CAL", "4 state flags · contract surface · 1-way Experience → Core read-only"),
      ("Auth flow", "Firebase Auth scoped to non-Core profile only · Core paths require no auth"),
      ("Offline contract", "Every external integration MUST degrade gracefully to cached state · no auto-retry storms")]),

    ("04-infrastructure-environments.md", "Infrastructure & environments",
     "DevOps Lead",
     "Dev / staging / prod environments. CI/CD pipeline. Deployment topology.",
     ["research/spec-docs/VGD-5126.md", "research/spec-docs/CDG-5126.md",
      "research/spec-docs/TQP-5026.md"],
     [("Environment matrix", "Dev (local emulator) · Staging (Firebase staging project) · Prod (Firebase prod project + AWS/GCP backend)"),
      ("CI/CD pipeline", "GitHub Actions · iOS 15+ / Android 13+ build matrix · signed artefacts · prohibited-capability scan · static analysis"),
      ("Per-gate evidence bundle", "Discovery / Alpha / Beta / GA — what evidence is collected automatically"),
      ("Mobile distribution", "TestFlight (iOS) · Internal track (Android) for Alpha/Beta · App Store + Play for GA"),
      ("OCS deployment", "Web app (React) · cloud-hosted (AWS/GCP) · internal-only access (no public DNS)"),
      ("Validation lab (Phase 1)", "GPS-spoofing + Faraday simulating Australian envelope (per CLR-SLZ-001)")]),

    ("05-security-auth.md", "Security & authentication",
     "Security Lead",
     "Encryption at rest / in transit, auth scoping, zero-outbound-from-Core posture, RBAC enforcement.",
     ["research/spec-docs/CDG-5126.md", "research/spec-docs/ESF-5026.md",
      "research/spec-docs/SFD-5026.md", "research/spec-docs/OCS-5026.md"],
     [("Encryption", "AES-256 at rest · TLS 1.3 in transit · key management policy"),
      ("Authentication", "Firebase Auth (non-Core only) · OCS Firebase Auth + session mgmt"),
      ("Zero outbound from Core", "Verified by airplane-mode packet capture (AC-C8-04) · non-dispatch posture"),
      ("RBAC server-side enforcement", "OCS 3-role RBAC enforced server-side · audit log"),
      ("PII handling", "PCR strictly anonymised (`reporter_archetype` only) · no PII in PCR data path"),
      ("Phase 2 security scaffolds (inert)", "BackTrack Emergency Escrow schema (no transmission code)"),
      ("Compliance scope", "Australia APPs · NZPA · GDPR / CCPA addressed via product design before respective release")]),

    ("06-adr-decision-records.md", "ADR — Architectural Decision Records",
     "Architecture Lead",
     "Key decisions in 'why we picked X' format. Append-only. New decisions get new ADRs.",
     ["docs/planning.md", "research/spec-docs/AOD-5026.md", "diagrams/"],
     [("ADR-001 — Flutter for mobile", "Context · Decision · Consequences · Status"),
      ("ADR-002 — Mapbox SDK + OSM tiles", "Offline-first requirement → Mapbox SDK bundle download"),
      ("ADR-003 — Firestore for sync ONLY, never Core", "Survival Core local-only mandate"),
      ("ADR-004 — Dual-layer split (Survival Core vs E&I)", "Authority web rationale"),
      ("ADR-005 — SQLite + WAL for Core store", "Crash-survivability · airplane-mode operation"),
      ("ADR-006 — Group-level POI toggle (vs binary/individual)", "Cognitive granularity rationale (POI-5026 §6.3.1)"),
      ("ADR-007 — PCR supersession (not TTL)", "Per OSM-5026 §10 — binary conditions don't decay"),
      ("ADR-008 — Append-only breadcrumb (14 prohibited mutations)", "BTF-5126 §5.2 forensic integrity"),
      ("ADR template", "Use this template for new ADRs · status = Proposed / Accepted / Superseded")]),

    ("07-tech-standards.md", "Tech standards",
     "Engineering Lead",
     "Code style, error codes, logging, branching, commit format, review process.",
     ["research/spec-docs/VGD-5126.md", "research/spec-docs/TQP-5026.md", "CLAUDE.md"],
     [("Code style", "Flutter / Dart conventions · ESLint+Prettier for OCS web · enforced via pre-commit"),
      ("Error code taxonomy", "ERR-{module}-{nn} format · catalog in repo · user-facing copy via UX guidelines"),
      ("Logging", "Local event log (FEAT-026) · structured · privacy-aware · no PII"),
      ("Branching", "main + feature branches · short-lived · PR-based merge · gates evidence linked"),
      ("Commit format", "Conventional commits (`type(scope): subject`) · references issue/Jira"),
      ("Code review", "2-reviewer minimum for Survival Core · 1-reviewer for Experience · all gates require sign-off"),
      ("Prohibited patterns", "No AI inference in Core · no telemetry weighting · no auto-trigger on PCR/verification · no satellite field names")])
]

for fname, title, owner, purpose, sources, outline in tech_pages:
    write_detail(ROOT / "04-tech" / fname, title, owner, purpose, sources, outline)


# ---------- Summary ----------

import os
counts = {"_index": 0, "detail": 0}
for root, dirs, files in os.walk(ROOT):
    for f in files:
        if f.startswith("_index"):
            counts["_index"] += 1
        elif f.endswith(".md") and f not in ("README.md",):
            counts["detail"] += 1

print(f"Generated:")
print(f"  - Home + README: 2")
print(f"  - Section indexes: {counts['_index']}")
print(f"  - Detail pages: {counts['detail'] - 1}  (minus 00-home.md already counted)")
print(f"  - Total .md files: {counts['_index'] + counts['detail'] + 1}")  # +1 for README
print()
print("Folder tree:")
for root, dirs, files in os.walk(ROOT):
    level = root.replace(str(ROOT), '').count(os.sep)
    indent = '  ' * level
    print(f"{indent}{os.path.basename(root)}/")
    for f in sorted(files):
        print(f"{indent}  {f}")
