# Trackaroo® Phase 1 — Architecture Cheat Sheet

Reference repo for **trackaroo® Phase 1 RFT** architecture work. Curated set of C4-style diagrams · cross-cutting governance matrices · vendor scenario responses · spec-authority traceability.

## Quick start — pick your tier

| Want to understand… | Open this |
|---|---|
| The whole system at one glance | [`diagrams/1-overview/trackaroo-phase1-architecture.md`](diagrams/1-overview/trackaroo-phase1-architecture.md) |
| How one zone works internally | [`diagrams/2-subsystems/`](diagrams/2-subsystems/) — pick a `*.md` file |
| How data moves at runtime | [`diagrams/3-flows/data-flow/`](diagrams/3-flows/data-flow/) |
| How state changes over time | [`diagrams/3-flows/state/`](diagrams/3-flows/state/) |
| What is prohibited (and why) | [`diagrams/4-cross-cutting/compliance-matrix.md`](diagrams/4-cross-cutting/compliance-matrix.md) |
| Performance numbers I must hit | [`diagrams/4-cross-cutting/performance-targets.md`](diagrams/4-cross-cutting/performance-targets.md) |
| Phase 2 scaffold rules | [`diagrams/4-cross-cutting/phase-2-readiness.md`](diagrams/4-cross-cutting/phase-2-readiness.md) |
| Vendor scenario walkthroughs | [`research/scenario-responses.md`](research/scenario-responses.md) |
| Spec authority hierarchy | [`research/spec-authority-stack.md`](research/spec-authority-stack.md) |
| Design decisions log (M0a–M0q) | [`research/design-decisions.md`](research/design-decisions.md) |

## Repo layout

```
.
├── README.md                                   ← you are here
├── CLAUDE.md                                   ← visual style guide + working conventions
│
├── diagrams/                                   ← C4-style 4-tier architecture
│   ├── README.md                               ← navigation map (read first)
│   ├── 1-overview/                             ← Tier 1 — Master architecture
│   ├── 2-subsystems/                           ← Tier 2 — Per-zone deep-dives
│   ├── 3-flows/                                ← Tier 3 — Behavioral views (DFD · state)
│   └── 4-cross-cutting/                        ← Tier 3 — System-wide concerns
│
├── research/                                   ← External knowledge + synthesis
│   ├── design-decisions.md                     ← Decision log (M0a … M0q)
│   ├── scenario-responses.md                   ← Vendor walkthroughs (governance-traced)
│   ├── spec-authority-stack.md                 ← Spec hierarchy (UXS · BPS · BTF · ESF · …)
│   ├── tech-stack-inventory.md                 ← Every tech mapped to zone + component
│   └── mapbox-sdk-overview.md
│
├── .scripts/                                   ← Atomic Python/PowerShell edit scripts for the drawio twin
├── .claude/                                    ← Claude Code project config (skills + hooks)
└── .vscode/                                    ← Editor settings
```

## Conventions

- **C4 tier prefix** — numbered folders (`1-`, `2-`, `3-`, `4-`) force reading order.
- **Drawio twin** — `diagrams/1-overview/trackaroo-phase1-architecture.drawio` is a multi-page draw.io file (Architecture · Legend · CAL Architecture · per-subsystem tabs). Open with [draw.io desktop](https://github.com/jgraph/drawio-desktop) or [app.diagrams.net](https://app.diagrams.net).
- **Visual style** — see [`CLAUDE.md`](CLAUDE.md) for the canonical visual style guide (Mermaid header · zone color palette · edge semantics · same-level consistency rules).
- **Governance traceability** — every diagram cell or claim cross-references its governing spec doc (`BPS-5126`, `BTF-5126`, `ESF-5026`, `UXS-5726`, etc.) and named rejection trigger where applicable (`RT-01`, `RT-02`, `RT-09`, `RT-13`, `RT-15`).

## Status legend used across docs

- ✅ Complete
- 🟡 Work in progress
- 🚧 Stub / skeleton — scope declared, content TBD
- 🔵 Phase 2 placeholder (architecturally surfaced · inert in Phase 1)

## Phase 2 readiness — the 3 permitted scaffolds

Phase 1 build contains exactly 3 architectural hooks for Phase 2, each subject to the 4 Placeholder Disciplines:

1. **BackTrack™ Emergency Escrow Schema** (in `MOB-3002` SQL)
2. **CAL `satReady` flag** — hardcoded `FALSE` · CI-enforced (in `MOB-1101.SFM`)
3. **CAL Satellite Transport Pathway** — `ITransport` adapter slot · no implementing class

See [`diagrams/4-cross-cutting/phase-2-readiness.md`](diagrams/4-cross-cutting/phase-2-readiness.md) for the full catalog + static-analysis CI gates.

## Cross-reference to related repos

- **MasterMind skills** — diagram authoring skills extracted from this work: <https://github.com/giakhanh22024558/MasterMind>
