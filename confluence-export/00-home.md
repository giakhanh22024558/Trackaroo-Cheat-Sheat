# Trackaroo® Phase 1 — Workspace Home

> **trackaroo® supports safer human decision-making for people travelling and operating in remote or low-signal outdoor environments, when digital information becomes limited or uncertain.**
> — Product Anchor Statement (Ian Moore, Founder & Project Director)

## Status (as of 31 May 2026)

| Item | Value |
|---|---|
| **Phase** | Phase 1 — first commercial release |
| **Contract Execution** | 29 May 2026 ✅ |
| **Next gate** | **Discovery — 15 June 2026** (16 days) |
| **Hard launch** | 13 November 2026 |
| **Delivery partner** | Slitigenz Pty Ltd |
| **Current sprint** | Sprint 0 — Foundation |

## Quick links

| If you want… | Go to |
|---|---|
| Project overview, scope, mandate | [About → Project overview](#) |
| Sprint timeline, gate dates, what's due when | [About → Roadmap & milestones](#) |
| Who does what, who to ask about X | [About → Team & contacts](#) |
| How we work (Scrum, DoR, DoD) | [About → Ways of working](#) |
| Write a Story or AC the right way | [About → Story / AC conventions](#) |
| Raise a Change Request | [About → Change Request process](#) |
| Where things live (Jira / Confluence / Drive) | [About → Tool stack](#) |
| First-day / first-week setup | [About → Onboarding](#) |
| What does this acronym mean? | [About → Glossary](#) |
| System architecture, modules | [Product → System overview](#) |
| Spec for a specific feature | [Product → Modules](#) |
| Business rule reference (by ID) | [Rules → Business rules](#) |
| Who can do what (RBAC) | [Rules → Permission matrix](#) |
| Entity / field definitions | [Rules → Data dictionary](#) |
| Date format, error states, validation | [Rules → UX guidelines](#) |
| Architecture diagrams, ERD, security | [Tech section](#) |
| Why we picked X (decisions) | [Tech → ADR](#) |

## How to find what you need

1. **Looking for a feature spec?** → PRODUCT → Modules → pick the module. Each module page links to its source spec (in `research/spec-docs/`).
2. **Looking for "how do we…?"** → ABOUT (process) or RULES (business rules) or TECH (architecture).
3. **Looking for "why does it work this way?"** → TECH → ADR (architectural decisions) or RULES (business constraints).
4. **Stuck?** → ABOUT → Team & contacts → ask the right person.

## Workspace structure at a glance

```
🏠 Home (this page)
│
├── 📘 1. ABOUT          The project, the team, how we work
├── 📗 2. PRODUCT        What we're building — modules + features
├── 📕 3. RULES          Business rules, permissions, data, UX cross-cutting
└── 📙 4. TECH           Architecture, ERD, APIs, infra, security, decisions
```

## Critical reading for new joiners

- [ ] [About → Project overview](#) (15 min)
- [ ] [About → Ways of working](#) (10 min)
- [ ] [About → Tool stack](#) (5 min)
- [ ] [About → Glossary](#) (skim — acronym-heavy domain)
- [ ] [Product → System overview](#) (15 min — dual-layer architecture is key)
- [ ] [Rules → UX guidelines](#) (10 min — the *"5-question hierarchy"* anchor)
- [ ] [About → Onboarding](#) (your Day-1 / Week-1 checklist)

## Source of truth note

This Confluence space is **the read view**. The **source of truth lives in the project repository** under:
- `docs/planning.md` — delivery plan, sprints, gates, deliverable checklist
- `docs/sprint-0-foundation-criteria.md` — 45 Foundation ACs
- `docs/gap-clarifications.md` — open clarification register (CLR-TRK)
- `research/spec-docs/*.md` — 20 spec doc extracts (PRD, FSD, OSM, etc.)
- `diagrams/` — architecture diagrams (4-tier C4 layout)
- `conventions/` — backlog ID conventions, AC writing rules

If a Confluence page conflicts with the repo file, **the repo wins**. Re-export to refresh.
