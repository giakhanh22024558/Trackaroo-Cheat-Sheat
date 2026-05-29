# MasterMind Integration — Trackaroo® Phase 1 Working Folder

**Mục đích:** Tài liệu này bridge giữa **cấu trúc project hiện có** (`research/`, `diagrams/`, `CLAUDE.md`) và **MasterMind skill library conventions** (Core Rule 3-layer · working folder layout). Đọc file này khi muốn chạy phân tích nghiệp vụ có cấu trúc trên 19 spec docs đã extract.

**Pulled from:** https://github.com/giakhanh22024558/MasterMind (commit hiện tại — update bằng `cd MasterMind && git pull`)

---

## 1. Folder mapping — Trackaroo project ↔ MasterMind convention

```
Trackagroo local management/                       ← working folder (this project)
│
├── MasterMind/                                    ← skill library (read-only · gitignored)
│   ├── core/                                      ← invariant Core Rule + meta + template
│   └── models/model_001/                          ← BA skill cluster (requirements/erd/features/srs/analysis/jira/google_sheets/business_analysis pipeline)
│
├── input/                                         ← raw materials (gitignored · new)
│   └── [empty — symlink or copy from Drive when needed]
│
├── context/                                       ← Layer-1 sidecars (gitignored · new)
│   └── [agent auto-generated · mirrors input/]
│
├── output/                                        ← deliverables (gitignored · new)
│   └── [.docx · .xlsx · .drawio renders go here]
│
├── docs/                                          ← user-edited artifact templates (NEW · committed)
│   ├── requirements.md                            ← REQ-XXXX table
│   ├── planning.md                                ← ★ single source: plan (timeline+sprints) + backlog (Epic/Feat) + Sprint 0 (FND)
│   ├── gap-analysis.md                            ← 17-column CR table
│   └── erd.md                                     ← Mermaid erDiagram
│
├── conventions/                                   ← project overrides for skill defaults (NEW · committed)
│   ├── README.md
│   ├── analysis-conventions.md
│   ├── features-conventions.md
│   └── jira-conventions.md
│
├── research/                                      ← EXISTING — Trackaroo-specific research
│   └── spec-docs/                                 ← ★ 19 spec extracts — already serves as context/ for Trackaroo docs
│       ├── README.md                              ← index
│       ├── READING-GUIDE.md                       ← 6-group clustering + PM/Architect reading paths
│       ├── UXS-5726.md · PRD-5126.md · ... (19 extracts)
│
├── diagrams/                                      ← EXISTING — C4 architecture diagrams
│   ├── 1-overview/                                ← Tier 1 master architecture
│   ├── 2-subsystems/                              ← Tier 2 component deep-dives
│   ├── 3-flows/                                   ← DFD · sequence · state
│   └── 4-cross-cutting/                           ← compliance · perf targets · tile lifecycle
│
├── CLAUDE.md                                      ← project conventions — diagram style guide + working-interaction rules
├── README.md                                      ← project README
└── trackaroo_phase1_epics.xlsx                    ← existing epics xlsx (potential input for features skill)
```

---

## 2. The Trackaroo-specific mapping (where the bridge matters)

| MasterMind expects | Trackaroo project actually has | Status |
|---|---|---|
| `input/` containing raw `.pdf` / `.docx` | The 19 source PDFs in **Google Drive folder** `TRACKAROO 2026 RFT Phase 1/` (mounted at `G:\.shortcut-targets-by-id\1fqaX3DE_KT88tT7ElgewcBM0bKzTvkZp\...`) | ⚠️ External — agent reads directly from Drive path. Optionally: symlink or copy snapshots into `input/` when running specific BA stage |
| `context/` containing `.md` sidecars per input file | `research/spec-docs/` has **19 structured Markdown extracts** of the 19 spec PDFs (UXS, PRD, FSD, TQP, WFD, VGD, OSM, HFG, ESF, CDG, BPS, BTF, TAA, MAS, AOD, PSB, OCS + bonus FQH, SFD) | ✅ Equivalent — treat `research/spec-docs/*.md` as the canonical context layer for the 19 Trackaroo spec docs |
| `output/` for deliverables | `diagrams/*.drawio` (architecture renders) + the new `output/` folder for BA artifacts | ✅ Split: architecture diagrams stay in `diagrams/`, BA pipeline output (REQ xlsx · backlog xlsx · SRS docx · ERD) goes to `output/` |
| `docs/` artifact templates | Newly seeded from MasterMind setup templates | ✅ Empty templates ready |
| `conventions/` project overrides | Newly seeded. **Existing diagram conventions in `CLAUDE.md`** (Mermaid header · zone palette · edge label format · DFD authoring) remain authoritative for diagram skills | ✅ CLAUDE.md > MasterMind defaults for diagrams |

### Rule of thumb

- **For the 19 Trackaroo spec docs** — `research/spec-docs/*.md` is the context layer. Don't re-ingest into `context/` unless the agent needs to add new content not yet extracted.
- **For new external input** (e.g. client sends a CR `.docx`, vendor sends a deliverable) — drop into `input/`, let the agent generate `context/<file>.md`, then run downstream skills.
- **For architecture diagrams** — existing `diagrams/` structure + `CLAUDE.md` style guide override MasterMind's `diagram/architecture/` defaults. The MasterMind diagram skill is a fallback / methodology reference only.

---

## 3. When to invoke which MasterMind skill

| Tình huống (Vietnamese) | Skill MasterMind | Đầu ra |
|---|---|---|
| "Consolidate 19 spec docs thành 1 requirements table" | `models/model_001/document/requirements/` | `docs/requirements.md` + `output/requirements.xlsx` |
| "Vẽ ERD cho Trackaroo data model" | `models/model_001/diagram/erd/` | `docs/erd.md` (Mermaid) + optional `output/trackaroo-erd.drawio` |
| "Derive Epic / Feature / User Story từ requirements" | `models/model_001/document/features/` | `docs/planning.md` §B3 + `output/backlog.xlsx` |
| "Build SRS document IEEE-format từ feature list" | `models/model_001/document/srs/` | `output/trackaroo-phase1-SRS.docx` |
| "Client gửi CR mới → impact analysis" | `models/model_001/document/analysis/` | `docs/gap-analysis.md` + `output/impact-analysis.xlsx` |
| "Tạo Jira tasks từ approved CRs" | `models/model_001/integration/jira/` | `output/jira/*.md` (task tree BA/FE/BE) |
| "Edit Google Sheets backlog (cell-level)" | `models/model_001/integration/google_sheets/` | direct cell edits preserving comments/history |
| "Chạy end-to-end BA pipeline (requirements → ERD + features → SRS)" | `models/model_001/business_analysis/` (orchestrator) | tất cả output trên |
| "Vẽ wireframe màn hình (PCR-WF, LoRa onboarding, Snow & Alpine whiteout)" | `models/model_001/diagram/wireframe/` | self-contained annotated `.html` (badge ①②③ + Design Assumptions table) → `output/` |
| "Cập nhật architecture diagram" | **CLAUDE.md style guide** > MasterMind diagram skill | `diagrams/**/*.drawio` |

**Agent invocation:** Khi user mô tả task, agent tự chọn skill phù hợp dựa vào `SKILL.md` của từng skill. Không cần invoke by name.

---

## 4. Standard workflow — from existing spec-docs to deliverable

### Workflow A — Run BA pipeline on existing 19 spec docs (most common)

```
research/spec-docs/*.md  ──read as context──▶  [requirements skill]
                                                       │
                                                       ▼
                                         docs/requirements.md (REQ-0001 → REQ-NNNN)
                                                       │
                                          ┌────────────┴────────────┐
                                          ▼                         ▼
                                   [erd skill]              [features skill]
                                          │                         │
                                          ▼                         ▼
                                    docs/erd.md             docs/planning.md §B3
                                          │                         │
                                          └────────────┬────────────┘
                                                       ▼
                                       Stage 3 — walk ERD for BR + edge cases
                                                       │
                                                       ▼
                                                   [srs skill]
                                                       │
                                                       ▼
                                       output/trackaroo-phase1-SRS.docx
```

Vai trò agent: đọc 19 spec extracts (đặc biệt PRD §4 acceptance criteria, FSD §4 functional spec, UXS §3 5-Q hierarchy), trích thành REQ-XXXX rows. Mỗi REQ Source = `research/spec-docs/<DOC-ID>.md §<section>`.

### Workflow B — Client gửi CR mới (change-request branch)

```
input/cr-batch-01.docx  ──ingest──▶  context/cr-batch-01/context.md
                                              │
                                              ▼
                                   [analysis skill — gap]
                                              │
                                              ▼
                                docs/gap-analysis.md (compare CR vs current SRS)
                                              │
                                              ▼
                                   [analysis skill — impact]
                                              │
                                              ▼
                              docs/gap-analysis.md (17 cols filled — Decision pending)
                                              │
                                              ▼
                                  ★ USER / PM APPROVAL ★
                                              │
                                              ▼
                                       [features skill]
                                              │
                                              ▼
                              new stories appended to docs/planning.md §B3 với tag [CR-XX]
                                              │
                                              ▼
                                       [jira skill]
                                              │
                                              ▼
                              output/jira/CR-XX/{main, ba, fe, be}.md
```

### Workflow C — Update architecture diagram

```
User asks "update CAL state machine diagram"
                       │
                       ▼
Agent reads CLAUDE.md § Diagram Visual Style Guide  (NOT MasterMind diagram defaults)
                       │
                       ▼
Agent edits diagrams/2-subsystems/<file>.drawio
                       │
                       ▼
Auto-syncs to Google Drive via symlink (Tier-1 master architecture only)
```

---

## 5. Core Rule reminders (binding for every skill)

1. **`input/` = user-managed.** Agent never writes here.
2. **`context/` = agent-managed.** `.md` sidecars only. Do not edit by hand — gets overwritten on re-ingest.
3. **`output/` = deliverables.** Agent writes, user reads/exports. Every binary file in `output/` should have a `.md` companion in `context/` for token-cheap reading.
4. **`MasterMind/` = read-only.** Don't edit skill definitions in this project. To improve a skill, do it upstream in the MasterMind repo, then `git pull`.
5. **`research/spec-docs/` = special context.** Already-extracted 19 Trackaroo spec docs. Treat as authoritative context for Trackaroo content — re-ingest only when new docs added.
6. **Source-truth chain:** raw input → context.md → Python format code (agent layer) → output deliverable. Editing `.docx` / `.xlsx` directly without re-reading context = anti-pattern.
7. **Project conventions win over MasterMind defaults** (per Core Rule §Format conventions). For Trackaroo:
   - **Diagrams** — `CLAUDE.md § Diagram Visual Style Guide` is authoritative
   - **Doc supersession** — DDS-1226 versioning convention applies (e.g. PRD-5126 supersedes PRD-5026)
   - **Working-interaction rule** — CLAUDE.md's "DO NOT auto-apply changes when user asks for analysis/check/audit/review" applies on top of any skill

---

## 6. Project-specific conventions (override MasterMind defaults)

### 6.1 ID schemes — Trackaroo style

| Type | Trackaroo convention | MasterMind default | Authoritative |
|---|---|---|---|
| Spec document | `XYZ-NNNN` (e.g. `UXS-5726`, `PRD-5126`) — DDS-1226 versioning | n/a | Trackaroo wins |
| Requirement | `REQ-NNNN` | `REQ-NNNN` | Match ✓ |
| Epic | `EPIC-NN` | `EPIC-XX` | Match — use 2-digit |
| Feature | `FEAT-NNN` | `FEAT-XXX` | Match — use 3-digit |
| User story | `STORY-NNN` | `STORY-XXX` | Match |
| Rejection trigger | `RT-NN` (1-22) — PRD-5126 §14.4 | n/a | Trackaroo-specific |
| Rollback governance | `RG-NN` (1-11) — OSM-5026 §12 | n/a | Trackaroo-specific |
| Layer independence rule | `LIR-NN` (1-6) — OSM-5026 | n/a | Trackaroo-specific |
| QA Acceptance Register | `QAR-NN` (1-23) — UXS-5726 | n/a | Trackaroo-specific |
| PCR category | `PCR-{OBS,CLO,INF,SRF,WTR,HAZ}` — OSM-5026 §10 | n/a | Trackaroo-specific |
| PCR wireframe state | `PCR-WF-NN` (1-6) — WFD-5126 §5.17 | n/a | Trackaroo-specific |
| Change request | `CR-NN` | `CR-NN` | Match ✓ |

### 6.2 Priority levels

- Trackaroo PRD-5126 §14.4 dùng **22 named Rejection Triggers** (RT-01 → RT-22) thay cho priority enum thông thường.
- Khi map sang MasterMind backlog: dùng `Critical / High / Medium / Low` cho story priority, nhưng giữ RT-NN reference trong AC bullet.

### 6.3 Acceptance Criteria language

- Bilingual cho phép: English (Given/When/Then) hoặc Vietnamese (Khi/Nếu… thì…).
- AC liên quan Survival Core invariants — bắt buộc cite spec source (e.g. `Theo UXS-5726 §7.1: SOS ≤2 taps`).

### 6.4 Doc supersession (DDS-1226)

Khi extract requirements, **luôn dùng doc current** (e.g. PRD-**5126**, KHÔNG dùng PRD-5026). Older docs có ghi "supersedes" marker — không trích từ supersedeed docs.

### 6.5 Working interaction (from CLAUDE.md)

Agent KHÔNG tự apply changes khi user nói "phân tích thử", "kiểm tra giúp mình", "xem giúp". Chỉ apply khi user nói "thực hiện", "apply ngay", "execute".

---

## 7. Quick onboarding — đọc theo thứ tự

Nếu bạn (PM / Architect / BA) mới đến dự án và muốn dùng MasterMind cho phân tích:

1. **`research/spec-docs/READING-GUIDE.md`** — 6-group clustering + PM/Architect reading paths cho 19 spec docs
2. **`research/spec-docs/README.md`** — index + cross-cutting concepts
3. **`CLAUDE.md`** — project conventions (diagram style guide · working-interaction rules)
4. **This file (MASTERMIND-INTEGRATION.md)** — folder mapping + when to invoke which skill
5. **`MasterMind/README.md`** — MasterMind structure
6. **`MasterMind/core/core-rule/core-rule.md`** — invariant 3-layer rule
7. **`MasterMind/models/model_001/README.md`** — model_001 skill cluster overview
8. **`MasterMind/models/model_001/business_analysis/SKILL.md`** — the end-to-end BA pipeline definition

Sau bước 8 bạn đã sẵn sàng để chỉ đạo agent chạy stage cụ thể.

---

## 8. Anti-patterns to avoid

- ❌ **Edit files inside `MasterMind/`** — skill library is read-only; changes get lost on `git pull`. Improve upstream.
- ❌ **Re-extract spec docs into `context/`** — `research/spec-docs/` already serves that role for the 19 Trackaroo specs.
- ❌ **Run features stage without requirements first** — Stage 1 always first (per business_analysis pipeline rule).
- ❌ **Apply MasterMind diagram defaults to architecture diagrams** — `CLAUDE.md § Diagram Visual Style Guide` wins.
- ❌ **Reference spec docs by name in artifacts** — always reference by code (e.g. `UXS-5726 §7.1`, not "UX Strategy doc"). Per MasterMind hand-off contract.
- ❌ **Update older superseded docs** — DDS-1226 convention: only current revision (e.g. PRD-5126, not PRD-5026).

---

## 9. Update procedure

To pull latest skill updates from upstream MasterMind:

```bash
cd MasterMind
git pull
# review CHANGELOG or commits
# update this MASTERMIND-INTEGRATION.md if folder mapping or skill set changes
```

If a new model is added (`model_002/`), evaluate whether it applies to Trackaroo; if yes, add a row to Section 3 (skill invocation table).

---

## 10. Cross-references

| File | Purpose |
|---|---|
| `CLAUDE.md` | Project conventions — diagram style guide, working-interaction rules, folder structure |
| `research/spec-docs/README.md` | 19 spec extracts index + quick-reference |
| `research/spec-docs/READING-GUIDE.md` | 6-group clustering + PM/Architect reading paths |
| `MasterMind/README.md` | MasterMind library overview |
| `MasterMind/core/core-rule/core-rule.md` | The invariant 3-layer rule |
| `MasterMind/models/model_001/business_analysis/SKILL.md` | End-to-end BA pipeline orchestrator |
| `MasterMind/models/model_001/setup/templates/CLAUDE.md` | Reference template for `/set-up` workflow (already adapted into this file) |

---

*Last updated: 2026-05-26 · Initial setup after pulling MasterMind into project root*
