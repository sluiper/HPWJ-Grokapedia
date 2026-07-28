# Master Source Inventory

**Purpose:** Single inventory of every source used or planned for HPWJ-Grokapedia.  
**SSOT for “where did this claim come from?”** — not a substitute for MCR (controls) or chapters (narrative).  
**Last updated:** 28 July 2026 (Phase 1 baseline from on-disk assets)  
**Access legend:** Public | Public-summary | Member | Internal | Secondary  

---

## A. Company / client procedures (highest operational authority for Anabeeb)

| ID | Title | Type | Owner | Rev / Date | Access | Path in repo | Linked sections | Linked MCR | Last verified |
|----|-------|------|-------|------------|--------|--------------|-----------------|------------|---------------|
| SRC-OPS-001 | Anabeeb OPS-P-019 High Pressure Water Jetting | Company procedure | Anabeeb | Captured 16 Jul 2026 | Internal (summary in repo) | `references/standards/Anabeeb_OPS-P-019_HPWJ_Procedure_Summary.md` | Ch5–13, Sec21 | MCR-046–052, 001–045 (mapped) | 16 Jul 2026 |
| SRC-SAB-001 | SABIC OMS Attachment 8.2 HPWJ | Client OMS | SABIC | Extracted in KSA notes | Internal / client-controlled (extract) | `references/standards/KSA_Anabeeb_ATC_Notes.md` | Ch5–12, Sec21 | MCR-016, 039–045, 027, 040 etc. | 16 Jul 2026 |
| SRC-ARA-001 | Aramco SAES / CSMS HPWJ-related | Client standards | Aramco | — | **Internal – not in repo** | — | Sec21 | TBD | **[INTERNAL GAP]** |
| SRC-ATC-001 | Anabeeb ATC competency notes | Training notes | Anabeeb ATC | v8.1 notes file | Internal / synthesis | `references/standards/KSA_Anabeeb_ATC_Notes.md` | Ch13 | MCR-030, 042, 064 | 16 Jul 2026 |

---

## B. Global industry standards & codes

| ID | Title | Type | Owner | Rev / Date | Access | Path in repo | Linked sections | Linked MCR | Last verified |
|----|-------|------|-------|------------|--------|--------------|-----------------|------------|---------------|
| SRC-WJTA-001 | WJTA Recommended Practices (“Orange Book”) + certification | Industry RP | WJTA | Public summary | Public-summary | `references/standards/WJTA_Summary.md` | Ch13, Sec16 | MCR-001–002, 016, 030 | 16 Jul 2026 |
| SRC-WJA-001 | WJA Codes of Practice + training pathway | Industry CoP | WJA (UK) | Public summary | Public-summary | `references/standards/WJA_Summary.md` | Ch13, Ch10 | MCR-030, 043 | 16 Jul 2026 |
| SRC-ASNZ-001 | AS/NZS 4233.1:2013 + MSMWJ units | National standard | Standards AU/NZ | 2013 + units | Public-summary | `references/standards/ASNZS_4233_Australia_Summary.md` | Ch13 | MCR-030, 042 | 16 Jul 2026 |
| SRC-SIR-001 | SIR industrial cleaning / water jetting | National scheme | SIR (NL) | Overview only | Public-summary | `references/standards/00_Global_Standards_Overview.md` | Ch13 | MCR-030 | 16 Jul 2026 |
| SRC-EWJI-001 | EWJI harmonisation | Industry body | EWJI | Overview only | Public-summary | `references/standards/00_Global_Standards_Overview.md` | Ch13 | — | 16 Jul 2026 |
| SRC-GLO-001 | Global standards overview (composite) | Synthesis | Encyclopedia | 16 Jul 2026 | Synthesis | `references/standards/00_Global_Standards_Overview.md` | Ch13 | MCR-030 | 16 Jul 2026 |
| SRC-REG-021 | Regulatory & Client Matrix (Sec 21) | Matrix | Encyclopedia | Live | Synthesis + sources | `references/standards/21_Regulatory_and_Client_Matrix.md` | Sec21 | Multiple | 16 Jul 2026 |

---

## C. Marine / offshore

| ID | Title | Type | Owner | Rev / Date | Access | Path in repo | Linked sections | Linked MCR | Last verified |
|----|-------|------|-------|------------|--------|--------------|-----------------|------------|---------------|
| SRC-IMCA-D049 | IMCA D049 HP jetting by divers | Recommended practice | IMCA | Rev 1.2 Nov 2023 | **Member** | Research package notes only | Sec23 | MCR-053–060 | Partial public |
| SRC-IMCA-SF1820 | SF 18/20 Serious injury HP washer | Safety flash | IMCA | 12 Jun 2020 | Public | Cited in Sec23 + research | Sec23, Sec25 | MCR-057 | 16 Jul 2026 |
| SRC-IMCA-SF0917 | SF 09/17 Leg injury HP water jetting | Safety flash | IMCA | 2017 | Public | Cited in Sec23 | Sec23 | MCR-055 | 16 Jul 2026 |
| SRC-IMCA-SF0315 | SF 03/15 Diver water jetting injury | Safety flash | IMCA | 2015 | Public | Cited in Sec23 | Sec23 | MCR-053 | 16 Jul 2026 |
| SRC-IMCA-SF0607 | SF 06/07 Cavitation blaster injury | Safety flash | IMCA | 2007 | Public / D049 extract | Cited in Sec23 | Sec23 | MCR-060 | 16 Jul 2026 |
| SRC-IMCA-SF1518 | SF 15/18 LTI diver water jetting | Safety flash | IMCA | 2018 | Public | Cited in Sec23 research | Sec23 | — | 16 Jul 2026 |
| SRC-DMAC-HPWJ | DMAC HP water jet accident guidance | Medical | DMAC | Via D049 App 1 | Public via refs | Cited in Sec23 | Sec23, Ch10 | MCR-058 | Partial |

---

## D. Physics / engineering (derived + industry formula lineage)

| ID | Title | Type | Owner | Rev / Date | Access | Path in repo | Linked sections | Linked MCR | Last verified |
|----|-------|------|-------|------------|--------|--------------|-----------------|------------|---------------|
| SRC-PHYS-RF | Reaction force industry formula (imperial 0.052) | Formula lineage | WJTA-IMCA conference paper lineage (cited Sec16) | — | Secondary + derivation | `docs/16_Physics_and_Hydraulics.md` | Sec16, App C | MCR-016, 017 | 16 Jul 2026 (audit) |
| SRC-PHYS-RF-M | Metric constant 0.233 from imperial | First-principles conversion | Encyclopedia dual-model | 16 Jul 2026 | Derived | Sec16, MCR-017, App C, templates | Sec16, Sec23 | MCR-017 | Closed audit + AUDIT-004 |
| SRC-PHYS-V | Jet velocity / Bernoulli √(2P/ρ) | First principles | Textbook fluid mechanics | — | Derived | Sec16 | Sec16 | — | 16 Jul 2026 audit |
| SRC-AUDIT-861 | Full numeric truth audit | Audit record | Grok+Claude | Closed 16 Jul 2026 | Internal process | `docs/audit/TRUTH_AUDIT_v8.6.1.md` | All numeric | MCR-017 etc. | 16 Jul 2026 |

---

## E. Clinical / injury

| ID | Title | Type | Owner | Access | Path | Linked | MCR | Notes |
|----|-------|------|-------|--------|------|--------|-----|-------|
| SRC-CLIN-CH10 | Ch10 Emergency / medical (synthesis) | Chapter | Encyclopedia | Synthesis + citations in chapter | `docs/10_Emergency_Response_Medical_Management_and_Trauma.md` | Ch10 | MCR-043, 058 | Expand in RP-INJ |
| SRC-CLIN-CH24 | Ch24 Clinical & forensic encyclopedia | Chapter | Encyclopedia | Synthesis | `docs/24_Clinical_and_Forensic_Injury_Encyclopedia.md` | Ch24 | — | Expand in RP-INJ |
| SRC-MED-CARD | HPWJ Medical Alert Card template | Template | Anabeeb / encyclopedia | Controlled form | `templates/medical_alert/HPWJ_Medical_Alert_Card.md` | Ch10, Ch13 | MCR-043 | |

---

## F. Incidents & lessons

| ID | Title | Type | Access | Path | Linked | MCR |
|----|-------|------|--------|------|--------|-----|
| SRC-INC-SEC25 | Incident case study library (15 cases) | Library | Mixed public + composite | `docs/25_Incident_Case_Study_Library.md` | Sec25 | — |
| SRC-INC-SEC27 | Lessons Learned process | Process section | Process | `docs/27_Lessons_Learned.md` | Sec27 | MCR-061–065 |
| SRC-INC-ANB | Real Anabeeb incidents | Events | **Internal** | — | Sec27 | MCR-062–063 | **[INTERNAL GAP]** |

---

## G. Manufacturers (descriptive summaries — no first-principles constants)

| ID | Manufacturer | Path | Access |
|----|--------------|------|--------|
| SRC-MFG-HAM | Hammelmann | `references/manufacturers/Hammelmann/Summary.md` | Public-summary |
| SRC-MFG-NLB | NLB | `references/manufacturers/NLB/Summary.md` | Public-summary |
| SRC-MFG-SA | StoneAge | `references/manufacturers/StoneAge/Summary.md` | Public-summary |
| SRC-MFG-WOM | WOMA | `references/manufacturers/WOMA/Summary.md` | Public-summary |
| SRC-MFG-URA | Uraca | `references/manufacturers/Uraca/Summary.md` | Public-summary |
| SRC-MFG-KAM | Kamat | `references/manufacturers/Kamat/Summary.md` | Public-summary |
| SRC-MFG-JET | Jetstream | `references/manufacturers/Jetstream/Summary.md` | Public-summary |
| SRC-MFG-PEI | Peinemann | `references/manufacturers/Peinemann/Summary.md` | Public-summary |
| SRC-MFG-DER | DERC Salotech | `references/manufacturers/DERC_Salotech/Summary.md` | Public-summary |
| SRC-MFG-SAF | Safetech | `references/manufacturers/Safetech/Summary.md` | Public-summary |
| SRC-MFG-SUG | Sugino | `references/manufacturers/Sugino/Summary.md` | Public-summary |
| SRC-MFG-INT | Interpump | `references/manufacturers/Interpump/Summary.md` | Public-summary |
| SRC-MFG-MAT | Appendix B comparison matrix | `docs/appendices/Appendix_B_Global_Manufacturer_Comparison_Matrix.md` | Synthesis — expansion P2 |

---

## H. Field toolkit & templates (controlled operational tools)

| ID | Title | Path | Linked MCR (typical) |
|----|-------|------|----------------------|
| SRC-APP-A | Pump selection quick guide | `docs/appendices/Appendix_A_Pump_Selection_Quick_Guide.md` | Sec17 |
| SRC-APP-C | Reaction force calculator | `docs/appendices/Appendix_C_Reaction_Force_Quick_Calculator.md` | MCR-016, 017 |
| SRC-APP-D | Exclusion zone & team | `docs/appendices/Appendix_D_Exclusion_Zone_and_Team_Quick_Reference.md` | MCR-027, 031, 047, 051 |
| SRC-APP-F | Hose life / reject matrix | `docs/appendices/Appendix_F_Hose_Life_Inspection_Rejection_Matrix.md` | MCR-001–004 |
| SRC-APP-G | Never Rules one-pager | `docs/appendices/Appendix_G_Never_Rules_One_Pager.md` | MCR-038 |
| SRC-APP-H | Emergency medical pocket card | `docs/appendices/Appendix_H_Emergency_Medical_Pocket_Card.md` | MCR-043, Ch10 |
| SRC-APP-I | SIMOPS / permit card | `docs/appendices/Appendix_I_SIMOPS_Permit_Interface_Card.md` | MCR-028 |
| SRC-APP-J | UHP creeping hose card | `docs/appendices/Appendix_J_UHP_Creeping_Hose_Card.md` | MCR-034 |
| SRC-TPL-PRE | Pre-use inspection checklist | `templates/checklists/Pre_Use_Inspection_Checklist.md` | MCR-023 |
| SRC-TPL-RF | Reaction force quick reference | `templates/checklists/Reaction_Force_Quick_Reference.md` | MCR-017 |
| SRC-TPL-RD | Rupture disc verification card | `templates/checklists/Rupture_Disc_and_Pressure_Relief_Verification_Card.md` | MCR-009, 048 |
| SRC-TPL-WH | Whip check / hose card | `templates/checklists/Whip_Check_and_Hose_Inspection_Card.md` | MCR-006 |

**Note:** Appendix **E** letter is currently unused (A–D then F–J). Reserved in structure docs during Phase 2.

---

## I. Process & SSOT meta-sources

| ID | Title | Path | Role |
|----|-------|------|------|
| SRC-MCR | Master Control Register | `MASTER_CONTROL_REGISTER.md` | Absolute SSOT for controls (65 Visible) |
| SRC-AGENTS | AGENTS.md | `AGENTS.md` | Dual-model schema |
| SRC-WF | WORKFLOW.md | `WORKFLOW.md` | Delivery loop |
| SRC-PROC | PROCESS.md | `PROCESS.md` | Decision log |
| SRC-RES-23 | Sec 23 research package (audit trail) | `docs/research/23_Marine_Offshore_IMCA_Research_Package.md` | Pattern for RP-* packages |

---

## Collection queue (Phase 1 expansion — public first)

Priority order for *new* public harvest beyond on-disk assets:

1. **RP-PHYS** — strengthen primary citations for RF formula lineage + velocity (no constant change without dual re-derive)
2. **RP-STD** — deeper public extracts for WJTA/WJA/ASNZS/SIR into package files (not only short summaries)
3. **RP-INJ** — peer-reviewed injection-injury literature list
4. **RP-INC** — complete public IMCA SF inventory + any WJTA safety alerts publicly available
5. **RP-MFG** — primary URL + datasheet links per OEM (ranges only)
6. **RP-IMCA** — public-only consolidation; full D049 remains INTERNAL GAP
7. **RP-OPS** — no new Anabeeb rules without human; organize existing OPS/SABIC extract traceability
8. **RP-TRN** — competency pathway comparison table for training design (feeds Phase 4 after freeze)
9. **RP-ENV** — Sec 28 public environmental sources

---

## Maintenance rules

1. Add a row here **before or with** any new research package claim that introduces a new external source.  
2. Never invent Internal/Member clause numbers — use INTERNAL_GAP_REGISTER.md.  
3. After Phase 3 truth campaign, set **Last verified** on high-risk sources.  
4. Training packs (Phase 4) must reference SRC-MCR / MCR-IDs, not restate numbers from secondary copies.
