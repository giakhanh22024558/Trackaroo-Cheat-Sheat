# Live Register Schemas (8 sheets)

> **Why:** DCA §7 + CMP §6.10.2 mandate **9 live registers** with continuous PD access.
> **Tool default:** Google Sheets (one sheet per register OR 1 sheet with 8 tabs), shared view-only with `imoore@trackaroosystems.com`.
> **Register #1 (Project plan)** = the Roadmap & Milestones doc — no sheet schema below.
>
> Naming convention: `[CMP-5026] Register — [Name]` (e.g., `[CMP-5026] Register — Risk`).
>
> Each register row is **append-only**; status changes via update column, not by overwriting historical rows.

---

## H2. Risk Register → moved

> **Moved to its own template file** with compact 7-column schema + full maintenance/reporting/escalation context: [`registers/risk.md`](./registers/risk.md).
>
> Rationale: client mandate (DCA §7) requires only severity · owner · mitigation status as minimum; previous 15-column schema was over-spec. Sprint-level register in Sprint 0 page uses a 6-col compact mirror.

## H3. Decision Register → moved

> **Moved to its own template file** with compact 9-column schema + full maintenance/reporting/cross-register flow context: [`registers/decision.md`](./registers/decision.md).
>
> Rationale: Decision register has specific CMP §6.10.2 obligations (immediate PD notification for significant categories) that warrant a dedicated page. Compacted from 12 → 9 columns by inlining `alternatives_considered` into `rationale` and tracking supersession via `status=Superseded` instead of a separate column.

## H4. Defect Register

| Col | Type | Required | Sample value | Notes |
|---|---|---|---|---|
| `defect_id` | DEF-NNN (or Jira key) | Y | `DEF-001` | |
| `severity` | SEV-1 / SEV-2 / SEV-3 / SEV-4 | Y | `SEV-2` | Per DCA §15.1 |
| `module` | Navigation / SOS / BackTrack / HazTrack / First Aid / TrackIQ / PCR / TrackMate / POI / OCS / App / Infrastructure | Y | `SOS` | |
| `summary` | Text | Y | `SOS 2-tap activation regression after app backgrounding in offline mode` | |
| `detected_date` | YYYY-MM-DD | Y | `2026-06-25` | |
| `detected_by` | Name / Auto-test / User report | Y | `QA — Nguyen Thi Thom` | |
| `detected_environment` | dev / staging / prod | Y | `staging` | |
| `survival_core_affected` | Y/N | Y | `Y` | If Y → may trigger SEV-1 + Incident Report |
| `status` | Open / In progress / Fixed / Verified / Closed / Rejected | Y | `In progress` | |
| `assignee` | Name | Y | `Nguyen Huy Khoi (Mobile Lead)` | |
| `notify_within` | Auto from severity | Y | `24h` | SEV-1 = 2h · SEV-2 = 24h |
| `workaround_in_place` | Y/N + description | When applicable | `N` | |
| `permanent_fix_target` | YYYY-MM-DD | Y | `2026-06-28` | SEV-1 = 3 BD |
| `fix_deployed_date` | YYYY-MM-DD | When deployed | *(blank)* | |
| `gate_blocker` | None / Discovery / Alpha / Beta-Ready / GA | Y | `Alpha` | |
| `related_incident` | INC-NNN | Y if SEV-1 | *(blank — SEV-2)* | |

## H5. Dependency Register

| Col | Type | Required | Sample value | Notes |
|---|---|---|---|---|
| `dep_id` | DEP-NNN | Y | `DEP-001` | |
| `name` | Text | Y | `mapbox_gl_flutter` | Library / SDK / service |
| `type` | OSS library / SDK / Cloud service / Third-party API / Internal | Y | `SDK` | |
| `current_version` | Text | Y | `2.1.0` | Pinned version |
| `latest_version` | Text | Update monthly | `2.1.0` | |
| `licence` | Text | Y if OSS | `Mapbox TOS (proprietary)` | Link to H6 OSS register |
| `source_url` | URL | Y | `https://github.com/mapbox/mapbox-gl-flutter` | |
| `app_store_compat` | Y/N | Y | `Y` | Play + iOS distribution OK? |
| `security_status` | Clean / CVE-open / Patched | Y | `Clean` | From dependency scan |
| `last_scan_date` | YYYY-MM-DD | Y | `2026-06-01` | |
| `used_in` | Module / component | Y | `EPIC-001 Navigation` | |
| `pd_approved` | Y/N | Y if non-standard | `Y` | |
| `notes` | Text | N | `Pinned per DEC-001 / ADR-002` | |

## H6. OSS Licence Register (also Discovery artefact D9)

| Col | Type | Required | Sample value | Notes |
|---|---|---|---|---|
| `oss_id` | OSS-NNN | Y | `OSS-001` | |
| `dependency_ref` | DEP-NNN | Y | `DEP-007` | Link to H5 |
| `licence_type` | MIT / Apache-2.0 / BSD / GPL / AGPL / SSPL / proprietary / other | Y | `MIT` | |
| `copyleft_obligation` | None / Weak / Strong / Network | Y | `None` | GPL/AGPL/SSPL = needs PD approval |
| `attribution_required` | Y/N | Y | `Y` | |
| `attribution_text` | Text | Y if Y above | `Copyright (c) 2025 Dart contributors — MIT Licence` | |
| `source_disclosure_required` | Y/N | Y | `N` | |
| `pd_approval` | Y/N + date | Y if GPL/AGPL/SSPL or network-copyleft | `N/A` | |
| `app_store_compat` | Y/N | Y | `Y` | |
| `audit_date` | YYYY-MM-DD | Y | `2026-06-10` | Refreshed each Gate |

## H7. SDK Register

| Col | Type | Required | Sample value | Notes |
|---|---|---|---|---|
| `sdk_id` | SDK-NNN | Y | `SDK-001` | |
| `name` | Text | Y | `Mapbox GL Flutter` | e.g. Mapbox SDK / Firebase / Flutter |
| `vendor` | Text | Y | `Mapbox Inc.` | |
| `version_pinned` | Text | Y | `2.1.0` | |
| `licence` | Text | Y | `Mapbox TOS` | |
| `category` | Mapping / Auth / Persistence / Comms / Analytics / Other | Y | `Mapping` | |
| `prohibited_capability_check` | Pass / Fail | Y | `Pass` | Per OSM/PSB/CDG/BTF — no AI/satellite/telemetry weighting/etc. |
| `survival_core_eligible` | Y/N | Y | `Y` | Only deterministic SDKs |
| `pd_approved` | Y/N + date | Y | `Y — 2026-05-30` | Stack departures require PD approval |
| `last_audit_date` | YYYY-MM-DD | Y | `2026-06-10` | Each Gate |

## H8. AI-Tool Register *(DCA §10.6 mandatory — often overlooked)*

| Col | Type | Required | Sample value | Notes |
|---|---|---|---|---|
| `tool_id` | AI-NNN | Y | `AI-001` | |
| `tool_name` | Text | Y | `GitHub Copilot` | e.g. Copilot, ChatGPT, Claude, Cursor |
| `vendor` | Text | Y | `GitHub / Microsoft` | |
| `purpose` | Text | Y | `IDE inline autocomplete for Flutter / Dart developer productivity` | What it's used for |
| `data_handling_model` | No-retention / Vendor-retained / On-prem / Self-hosted | Y | `Vendor-retained (org policy: training opt-out enabled)` | |
| `uploads_client_confidential` | Y/N | Y | `N` (snippet upload disabled in org settings) | If Y → PD prior written approval required |
| `uploads_source_code` | Y/N | Y | `Y` (context window only, no full-file telemetry) | Same |
| `uploads_credentials` | Y/N | Y | `N` (`.gitignore` + secret-scan enforced) | NEVER allowed |
| `uploads_pii` | Y/N | Y | `N` | NEVER allowed |
| `pd_approval` | Y/N + date | Y if Y on any above | `Y — 2026-05-30` | |
| `used_in_production_code` | Y/N | Y | `Y` | If Y → human review + security review + licence-clean confirmation required |
| `human_review_completed` | Y/N | Y if production | `Y (PR review mandatory)` | |
| `security_review_completed` | Y/N | Y if production | `Y` | |
| `licence_clean_confirmed` | Y/N | Y if production | `Y` | |
| `personnel_using` | Names | Y | `Nguyen Huy Khoi · Nguyen Tien Dat` | |
| `last_audit_date` | YYYY-MM-DD | Y | `2026-06-01` | Each Gate |

## H9. Change Register

| Col | Type | Required | Sample value | Notes |
|---|---|---|---|---|
| `change_id` | CHG-NNN | Y | `CHG-001` | |
| `raised_date` | YYYY-MM-DD | Y | `2026-05-31` | |
| `raised_by` | Name | Y | `Luong Gia Khanh (Slitigenz PM)` | |
| `type` | Variation (VAR) / Clarification (CLR) / Spec amendment / Other | Y | `Clarification` | |
| `linked_var_id` | VAR-NNN | Y if Variation | *(blank — clarification)* | |
| `linked_clr_id` | CLR-TRK-NNN / CLR-SLZ-NNN | Y if Clarification | `CLR-TRK-001` | |
| `summary` | Text | Y | `Safe Anchor Point cap appropriateness — Free=3 vs TAA §8.2 "not crippled preview"` | |
| `affected_documents` | Text | Y | `FSD-5126 §5.2.1 · TAA-5126 §8.2 · TQP-5026 §5.5.2` | Spec docs touched |
| `affected_gate` | Discovery / Alpha / Beta-Ready / GA | Y | `Discovery` | |
| `cost_impact_aud` | Numeric | Y | `0` | 0 if none |
| `schedule_impact_days` | Numeric | Y | `0` | 0 if none |
| `status` | Proposed / Under review / Approved / Rejected / Superseded | Y | `Proposed` | |
| `pd_decision_date` | YYYY-MM-DD | When decided | *(blank)* | |
| `car_5026_record_id` | Text | Y if approved | *(blank)* | CAR record reference |
| `notes` | Text | N | `Working assumption: build to spec (3/20/50); surface as UX/commercial risk` | |

---

## Access + sharing convention (applies to all 8 above)

- Each register = **1 Google Sheet tab** under shared Drive folder *(or 1 file with 8 tabs — Slitigenz choice)*.
- Folder URL shared with PD on **Week 1**.
- **View-only** PD access enforced server-side; edit only by Slitigenz Key Personnel + PM.
- Append-only discipline — never overwrite historical rows; use `superseded_by` / `status=Closed` instead.
- **Snapshot at each Gate** — export PDF/CSV into Gate evidence package per `[GATE]-Evidence-[Date]/`.

---
*Source: CMP-5026 §6.10.2 + DCA-5026 §7.*
