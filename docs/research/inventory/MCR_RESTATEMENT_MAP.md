# MCR Restatement Map (Stub → Phase 3 complete)

**Purpose:** After any formula/control fix at the canonical source, every independent restatement must be found and corrected (standing rule from AUDIT-001–004).  
**Status:** Phase 2 **stub** — high-risk numeric / absolute Anabeeb rules mapped from repo search 28 July 2026. Full wording-diff is Phase 3 Track T3.  
**Canonical control SSOT:** `MASTER_CONTROL_REGISTER.md`

---

## How to use

1. Fix or confirm value in **MCR row** (and Sec 16 for first-principles physics).  
2. Walk every path in the matching table below.  
3. Prefer **cite MCR-ID** over re-typing constants in new training material.  
4. Expand this map when new restatements are added.

---

## High-risk calculated constants

### MCR-017 — Reaction force formulas (imperial 0.052; metric **0.233**)

| Path | Role | Notes |
|------|------|-------|
| `MASTER_CONTROL_REGISTER.md` | Canonical | Corrected 16 Jul 2026 |
| `docs/16_Physics_and_Hydraulics.md` | Derivation home | Full unit conversion shown |
| `docs/appendices/Appendix_C_Reaction_Force_Quick_Calculator.md` | Tables | Tables via imperial path historically |
| `templates/checklists/Reaction_Force_Quick_Reference.md` | Field card | AUDIT-003 site |
| `docs/23_Marine_Offshore_IMCA.md` | Narrative restatement | AUDIT-004 site |
| `docs/audit/TRUTH_AUDIT_v8.6.1.md` | Audit record | Historical 0.745 |
| `CHANGELOG.md` | History | AUDIT-004 note |
| `docs/08_Operational_Control_Team_Composition_Communication_Fatigue.md` | May restate 0.052 | Phase 3 wording check |
| `references/standards/Anabeeb_OPS-P-019_HPWJ_Procedure_Summary.md` | May restate 0.052 | Phase 3 |
| `references/standards/KSA_Anabeeb_ATC_Notes.md` | May restate 0.052 | Phase 3 |

**Search tokens:** `0.233`, `0.052`, `0.745` (legacy — must remain **zero** live operational uses except historical notes)

### MCR-016 — Three additive reaction force controls (≤250 N, ≤1/3 BW, geometry)

| Path | Notes |
|------|-------|
| `MASTER_CONTROL_REGISTER.md` | Canonical |
| `docs/16_Physics_and_Hydraulics.md` | |
| `docs/appendices/Appendix_C_Reaction_Force_Quick_Calculator.md` | |
| `docs/appendices/Appendix_G_Never_Rules_One_Pager.md` | |
| `templates/checklists/Reaction_Force_Quick_Reference.md` | |
| `templates/checklists/Pre_Use_Inspection_Checklist.md` | |
| `templates/checklists/Pre_Use_Inspection_Quick_Card.md` | |
| `docs/07_Equipment_Pumps_Tools_Nozzles.md` | |
| `docs/08_Operational_Control_Team_Composition_Communication_Fatigue.md` | |
| `docs/03_Global_Pressure_Classification_and_Method_Selection.md` | |
| `docs/12_Supervisor_and_Team_Leader_Responsibilities.md` | |
| `docs/13_Competency_Framework_Training_and_Assessment.md` | Training — cite only |
| `docs/23_Marine_Offshore_IMCA.md` | + MCR-054 underwater |
| `docs/20_Failure_Modes_and_Effects_Analysis.md` | RPN link |
| `docs/26_Human_Factors_and_Ergonomics.md` | |
| `docs/25_Incident_Case_Study_Library.md` | |
| `docs/27_Lessons_Learned.md` | |
| `references/standards/21_Regulatory_and_Client_Matrix.md` | |
| `references/standards/KSA_Anabeeb_ATC_Notes.md` | |
| `references/standards/Anabeeb_OPS-P-019_HPWJ_Procedure_Summary.md` | |
| (+ additional MCR-016 citations across Ch2–15 — grep `MCR-016`) | Phase 3 full wording pass |

**Search tokens:** `250 N`, `1/3`, `MCR-016`

---

## Anabeeb absolute procedural rules (OPS-P-019 — freeze candidates for OP-001)

### MCR-046 — Max system pressure 40 000 psi (2 759 bar)

| Path |
|------|
| `MASTER_CONTROL_REGISTER.md` |
| `references/standards/Anabeeb_OPS-P-019_HPWJ_Procedure_Summary.md` |
| `docs/16_Physics_and_Hydraulics.md` |
| `docs/appendices/Appendix_C_Reaction_Force_Quick_Calculator.md` |
| `docs/appendices/Appendix_G_Never_Rules_One_Pager.md` |
| `docs/23_Marine_Offshore_IMCA.md` |
| `references/manufacturers/Safetech/Summary.md` (PPE class context) |

### MCR-047 — Minimum team of three + dedicated e-stop when LOS lost

| Path |
|------|
| `MASTER_CONTROL_REGISTER.md` |
| `references/standards/Anabeeb_OPS-P-019_HPWJ_Procedure_Summary.md` |
| `docs/13_Competency_Framework_Training_and_Assessment.md` |
| `docs/12_Supervisor_and_Team_Leader_Responsibilities.md` |
| `docs/appendices/Appendix_D_Exclusion_Zone_and_Team_Quick_Reference.md` |
| `docs/appendices/Appendix_G_Never_Rules_One_Pager.md` |
| `docs/23_Marine_Offshore_IMCA.md` |
| `templates/checklists/Pre_Use_Inspection_Quick_Card.md` |

### MCR-048 — Rupture disc ≤1.2× MAWP of lowest-rated component

| Path |
|------|
| `MASTER_CONTROL_REGISTER.md` |
| `references/standards/Anabeeb_OPS-P-019_HPWJ_Procedure_Summary.md` |
| `docs/13_Competency_Framework_Training_and_Assessment.md` |
| `docs/12_Supervisor_and_Team_Leader_Responsibilities.md` |
| `docs/11_Shutdown_Post_Job_Decontamination_Care_Storage_Records.md` |
| `docs/appendices/Appendix_G_Never_Rules_One_Pager.md` |
| `templates/checklists/Rupture_Disc_and_Pressure_Relief_Verification_Card.md` |
| `templates/checklists/Pre_Use_Inspection_Checklist.md` |

### MCR-050 — Shotgun ≤10 000 psi, orifice ≤1.6 mm, RF ≤250 N

| Path |
|------|
| `MASTER_CONTROL_REGISTER.md` |
| `references/standards/Anabeeb_OPS-P-019_HPWJ_Procedure_Summary.md` |
| `docs/13_Competency_Framework_Training_and_Assessment.md` |
| `docs/12_Supervisor_and_Team_Leader_Responsibilities.md` |

### MCR-051 — 10 m unauthorised-person exclusion

| Path |
|------|
| `MASTER_CONTROL_REGISTER.md` |
| `references/standards/Anabeeb_OPS-P-019_HPWJ_Procedure_Summary.md` |
| `docs/05_Site_Preparation_Barricading_Weather_Environmental.md` |
| `docs/appendices/Appendix_D_Exclusion_Zone_and_Team_Quick_Reference.md` |
| `docs/appendices/Appendix_G_Never_Rules_One_Pager.md` |
| `docs/13_Competency_Framework_Training_and_Assessment.md` |
| `docs/12_Supervisor_and_Team_Leader_Responsibilities.md` |
| `docs/03_Global_Pressure_Classification_and_Method_Selection.md` |
| `docs/23_Marine_Offshore_IMCA.md` |

### MCR-052 — Lance tip mark ≥600 mm from nozzle

| Path |
|------|
| `MASTER_CONTROL_REGISTER.md` |
| `references/standards/Anabeeb_OPS-P-019_HPWJ_Procedure_Summary.md` |
| `docs/13_Competency_Framework_Training_and_Assessment.md` |
| `docs/12_Supervisor_and_Team_Leader_Responsibilities.md` |
| `docs/11_Shutdown_Post_Job_Decontamination_Care_Storage_Records.md` |
| `docs/appendices/Appendix_J_UHP_Creeping_Hose_Card.md` |

### MCR-009 / MCR-044 (related)

- MCR-009 rupture disc single-use / spare — templates + Ch7  
- MCR-044 lance min 1.2 m — Ch8, OPS summary, checklists  

---

## Hose life (MCR-001) — restatement risk medium

Canonical: MCR-001 (flex 2 y / other HP 4 y).  
Also: App F, Ch7, Sec18, OPS summary. Phase 3 check wording alignment.

---

## Phase 3 completion checklist (not done in this stub)

- [ ] Every path above: open file, compare claim to MCR row text  
- [ ] Zero live operational `0.745` (historical notes OK)  
- [ ] Grep for hard-coded training-bound numbers outside MCR citation style  
- [ ] Expand map to MCR-001–015, 018–045, 053–065 as T3 progresses  
- [ ] Record defects as AUDIT-005+

---

## Legacy defect class (closed — keep map awareness)

| ID | Constant | Locations fixed |
|----|----------|-----------------|
| AUDIT-001 | 0.745 → 0.233 | MCR-017 |
| AUDIT-002 | same | Sec16 |
| AUDIT-003 | same | Reaction_Force_Quick_Reference template |
| AUDIT-004 | same | Sec23.6 |
