# Live Register Schemas (8 sheets)

> **Why:** DCA §7 + CMP §6.10.2 mandate **9 live registers** with continuous PD access.
> **Tool default:** Google Sheets (one sheet per register), shared view-only with `imoore@trackaroosystems.com`.
> **Register #1 (Project plan)** = the Roadmap & Milestones doc — no sheet schema below.
>
> Naming convention: `[CMP-5026] Register — [Name]` (e.g., `[CMP-5026] Register — Risk`).
>
> Each register row is **append-only**; status changes via update column, not by overwriting historical rows.

---

## H2. Risk Register

| Col | Type | Required | Notes |
|---|---|---|---|
| `risk_id` | RISK-NNN | Y | Sequential, never reused |
| `date_raised` | YYYY-MM-DD | Y | |
| `raised_by` | Name | Y | |
| `category` | Delivery / Technical / Security / Legal / Commercial / Resource | Y | |
| `description` | Text | Y | Plain language |
| `likelihood` | L / M / H | Y | |
| `severity` | L / M / H | Y | |
| `priority` | L · M · H computed | Y | =likelihood × severity heuristic |
| `affected_gate` | Discovery / Alpha / Beta-Ready / GA / Warranty | Y | |
| `owner` | Name | Y | Key Personnel role |
| `mitigation` | Text | Y | What we're doing about it |
| `status` | Open / Mitigating / Closed / Watch | Y | |
| `closed_date` | YYYY-MM-DD | When closed | |
| `last_updated` | YYYY-MM-DD | Y | |
| `weekly_status_ref` | Week NN | When raised in status | |

## H3. Decision Register / Technical Decision Record

| Col | Type | Required | Notes |
|---|---|---|---|
| `decision_id` | DEC-NNN | Y | |
| `date` | YYYY-MM-DD | Y | When decision taken |
| `taken_by` | PD / Slitigenz Tech Lead / Joint | Y | |
| `category` | Architecture / SDK / Data model / UX / Process / Other | Y | |
| `decision` | Text | Y | The decision itself |
| `rationale` | Text | Y | Why this was chosen |
| `alternatives_considered` | Text | N | What else was on the table |
| `affected_components` | Text | Y | |
| `authority_doc` | DCA / FSD / OSM / WFD ref | When applicable | |
| `requires_variation` | Y/N | Y | If Y → link to VAR-NNN |
| `recorded_in_status` | Week NN | Y | |
| `superseded_by` | DEC-MMM | When applicable | Never delete original |

## H4. Defect Register

| Col | Type | Required | Notes |
|---|---|---|---|
| `defect_id` | DEF-NNN (or Jira key) | Y | |
| `severity` | SEV-1 / SEV-2 / SEV-3 / SEV-4 | Y | Per DCA §15.1 |
| `module` | Navigation / SOS / BackTrack / HazTrack / First Aid / TrackIQ / PCR / TrackMate / POI / OCS / App / Infrastructure | Y | |
| `summary` | Text | Y | |
| `detected_date` | YYYY-MM-DD | Y | |
| `detected_by` | Name / Auto-test / User report | Y | |
| `detected_environment` | dev / staging / prod | Y | |
| `survival_core_affected` | Y/N | Y | If Y → may trigger SEV-1 + Incident Report |
| `status` | Open / In progress / Fixed / Verified / Closed / Rejected | Y | |
| `assignee` | Name | Y | |
| `notify_within` | Auto from severity | Y | SEV-1 = 2h · SEV-2 = 24h |
| `workaround_in_place` | Y/N + description | When applicable | |
| `permanent_fix_target` | YYYY-MM-DD | Y | SEV-1 = 3 BD |
| `fix_deployed_date` | YYYY-MM-DD | When deployed | |
| `gate_blocker` | None / Discovery / Alpha / Beta-Ready / GA | Y | |
| `related_incident` | INC-NNN | Y if SEV-1 | |

## H5. Dependency Register

| Col | Type | Required | Notes |
|---|---|---|---|
| `dep_id` | DEP-NNN | Y | |
| `name` | Text | Y | Library / SDK / service |
| `type` | OSS library / SDK / Cloud service / Third-party API / Internal | Y | |
| `current_version` | Text | Y | Pinned version |
| `latest_version` | Text | Update monthly | |
| `licence` | Text | Y if OSS | Link to H6 OSS register |
| `source_url` | URL | Y | |
| `app_store_compat` | Y/N | Y | Play + iOS distribution OK? |
| `security_status` | Clean / CVE-open / Patched | Y | From dependency scan |
| `last_scan_date` | YYYY-MM-DD | Y | |
| `used_in` | Module / component | Y | |
| `pd_approved` | Y/N | Y if non-standard | |
| `notes` | Text | N | |

## H6. OSS Licence Register (also Discovery artefact D9)

| Col | Type | Required | Notes |
|---|---|---|---|
| `oss_id` | OSS-NNN | Y | |
| `dependency_ref` | DEP-NNN | Y | Link to H5 |
| `licence_type` | MIT / Apache-2.0 / BSD / GPL / AGPL / SSPL / proprietary / other | Y | |
| `copyleft_obligation` | None / Weak / Strong / Network | Y | GPL/AGPL/SSPL = needs PD approval |
| `attribution_required` | Y/N | Y | |
| `attribution_text` | Text | Y if Y above | |
| `source_disclosure_required` | Y/N | Y | |
| `pd_approval` | Y/N + date | Y if GPL/AGPL/SSPL or network-copyleft | |
| `app_store_compat` | Y/N | Y | |
| `audit_date` | YYYY-MM-DD | Y | Refreshed each Gate |

## H7. SDK Register

| Col | Type | Required | Notes |
|---|---|---|---|
| `sdk_id` | SDK-NNN | Y | |
| `name` | Text | Y | e.g. Mapbox SDK / Firebase / Flutter |
| `vendor` | Text | Y | |
| `version_pinned` | Text | Y | |
| `licence` | Text | Y | |
| `category` | Mapping / Auth / Persistence / Comms / Analytics / Other | Y | |
| `prohibited_capability_check` | Pass / Fail | Y | Per OSM/PSB/CDG/BTF — no AI/satellite/telemetry weighting/etc. |
| `survival_core_eligible` | Y/N | Y | Only deterministic SDKs |
| `pd_approved` | Y/N + date | Y | Stack departures require PD approval |
| `last_audit_date` | YYYY-MM-DD | Y | Each Gate |

## H8. AI-Tool Register *(DCA §10.6 mandatory — often overlooked)*

| Col | Type | Required | Notes |
|---|---|---|---|
| `tool_id` | AI-NNN | Y | |
| `tool_name` | Text | Y | e.g. Copilot, ChatGPT, Claude, Cursor |
| `vendor` | Text | Y | |
| `purpose` | Text | Y | What it's used for |
| `data_handling_model` | No-retention / Vendor-retained / On-prem / Self-hosted | Y | |
| `uploads_client_confidential` | Y/N | Y | If Y → PD prior written approval required |
| `uploads_source_code` | Y/N | Y | Same |
| `uploads_credentials` | Y/N | Y | NEVER allowed |
| `uploads_pii` | Y/N | Y | NEVER allowed |
| `pd_approval` | Y/N + date | Y if Y on any above | |
| `used_in_production_code` | Y/N | Y | If Y → human review + security review + licence-clean confirmation required |
| `human_review_completed` | Y/N | Y if production | |
| `security_review_completed` | Y/N | Y if production | |
| `licence_clean_confirmed` | Y/N | Y if production | |
| `personnel_using` | Names | Y | |
| `last_audit_date` | YYYY-MM-DD | Y | Each Gate |

## H9. Change Register

| Col | Type | Required | Notes |
|---|---|---|---|
| `change_id` | CHG-NNN | Y | |
| `raised_date` | YYYY-MM-DD | Y | |
| `raised_by` | Name | Y | |
| `type` | Variation (VAR) / Clarification (CLR) / Spec amendment / Other | Y | |
| `linked_var_id` | VAR-NNN | Y if Variation | |
| `linked_clr_id` | CLR-TRK-NNN / CLR-SLZ-NNN | Y if Clarification | |
| `summary` | Text | Y | |
| `affected_documents` | Text | Y | Spec docs touched |
| `affected_gate` | Discovery / Alpha / Beta-Ready / GA | Y | |
| `cost_impact_aud` | Numeric | Y | 0 if none |
| `schedule_impact_days` | Numeric | Y | 0 if none |
| `status` | Proposed / Under review / Approved / Rejected / Superseded | Y | |
| `pd_decision_date` | YYYY-MM-DD | When decided | |
| `car_5026_record_id` | Text | Y if approved | CAR record reference |
| `notes` | Text | N | |

---

## Access + sharing convention (applies to all 8 above)

- Each register = **1 Google Sheet** under shared Drive folder.
- Folder URL shared with PD on **Week 1**.
- **View-only** PD access enforced server-side; edit only by Slitigenz Key Personnel + PM.
- Append-only discipline — never overwrite historical rows; use `superseded_by` / `status=Closed` instead.
- **Snapshot at each Gate** — export PDF/CSV into Gate evidence package per `[GATE]-Evidence-[Date]/`.

---
*Source: CMP-5026 §6.10.2 + DCA-5026 §7.*
