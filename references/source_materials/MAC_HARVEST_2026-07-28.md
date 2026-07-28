# Mac Source Harvest — HPWJ-Grokapedia

**Date:** 28 July 2026  
**Agent:** Grok (local Mac search for all three Grokapedia wikis)  
**Scope:** Desktop, Documents, Downloads, TVTC pack, nebosh tree — not Library / browser caches  
**Purpose:** Map every local file useful for HPWJ encyclopedia + ATC training so multi-AI work can continue offline

---

## 1. What was done (this campaign)

1. Full-disk name search for HPWJ / water jet / WJTA / OPS-P-019 / SABIC / Aramco / CSMS.
2. Opened and summarised primary local sources into this folder.
3. Confirmed **full Saudi Aramco Construction Safety Manual (CSM) / CSMS questionnaire is NOT present as a PDF/DOC on this Mac** — remains GAP-002.
4. Documented what *is* held (Anabeeb OPS, SABIC OMS 8.2, WJTA deck + checklists, ATC decks).
5. Updated inventory + CHANGELOG + campaign log.

---

## 2. Gold-mine paths (HPWJ)

### 2.1 Anabeeb controlled procedure (highest company authority)

| Path | Notes |
|------|-------|
| `/Users/ab71000372/Desktop/nebosh/hpwj/OPS-P-019-High Pressure Water Jetting -Updated.doc` | Canonical binary |
| `/Users/ab71000372/Desktop/TVTC_Site_Visit_Pack/04_Quality_and_Safety/OPS-P-019-High Pressure Water Jetting -Updated.doc` | TVTC pack copy |
| `/Users/ab71000372/Documents/TDS BP/OPS-P-019-High Pressure Water Jetting -Updated.doc` | TDS BP copy |
| **Repo summary** | `references/standards/Anabeeb_OPS-P-019_HPWJ_Procedure_Summary.md` |

### 2.2 SABIC client OMS (mandatory KSA / MEA)

| Path | Notes |
|------|-------|
| `/Users/ab71000372/Documents/WJTANLB/sabic/High Pressure Water Jetting (HPWJ) for MEA Region.docx` | OMS Attachment 8.2 full |
| `/Users/ab71000372/Desktop/nebosh/hpwj/sabic/High Pressure Water Jetting (HPWJ) for MEA Region.docx` | Duplicate |
| `/Users/ab71000372/Desktop/nebosh/hpwj/sabic/HPWJ Awareness.pptx` | Client awareness deck |
| **Repo summary** | `SABIC_OMS_Att_8.2_HPWJ_Summary.md` (this folder) |

### 2.3 WJTA / NLB industry stack

| Path | Notes |
|------|-------|
| `/Users/ab71000372/Documents/WJTANLB/WJTA_FV4.2_UniversalDeck_Updated_04-26-24_FGR.pptx` | ~1.4 GB; 184 slides + video embeds |
| `/Users/ab71000372/Documents/WJTANLB/1WJTA_FV4.2_UniversalDeck_Updated_04-26-24_FGR.pptx` | Smaller/alt copy |
| `/Users/ab71000372/Documents/WJTANLB/WJTA1.pdf` | Supporting PDF |
| Checklists (Man/Auto Shotgun, Tube, Linemole, PPE, Pre Job Pump) | Same folder + `Fillable/` |
| `/Users/ab71000372/Desktop/nebosh/hpwj/claude/GAP_ANALYSIS_WJTA_vs_Anabeeb_HPWJ.md` | Claude gap analysis (already used) |
| `/Users/ab71000372/Desktop/TVTC_Site_Visit_Pack/02_Training_Programs/HPWJ/` | TVTC-facing pack |

### 2.4 Anabeeb ATC / NEBOSH training development

| Path | Notes |
|------|-------|
| `/Users/ab71000372/Desktop/nebosh/hpwj/HPWJ3day.pptx` | 3-day operator deck |
| `/Users/ab71000372/Desktop/nebosh/hpwj/ANABEEB - HPWJ .pptx` | Awareness / Day-1 slice |
| `/Users/ab71000372/Desktop/nebosh/hpwj/Anabeeb_HPWJ_Slides_v1.0.pptx` | Earlier revision |
| `/Users/ab71000372/Desktop/nebosh/hpwj/Course Overview.docx` | 9-day module roadmap draft |
| `/Users/ab71000372/Desktop/nebosh/hpwj/DAY 1 TRAINER SCRIPT.docx` + Day 2 scripts | Trainer scripts |
| `/Users/ab71000372/Desktop/nebosh/hpwj/New Catalogue (EN) Safetech UHP 04-2022 (1).pdf` | PPE OEM catalogue |
| Repo training packs | `training/ATC-HPWJ-*` |

### 2.5 AIMS master list (planned SWP)

| Path | Notes |
|------|-------|
| `…/ANABEEB_HSE_Procedure_Master_List_Rev01.xlsx` | **AIMS-L3-HSE-SWP-005** High Pressure & UHP Water Jetting = **New** (planned; OPS-P-019 is current operational control) |

### 2.6 Aramco / CSMS

| Item | Status |
|------|--------|
| Full CSM / Construction Safety Manual PDF | **NOT FOUND on Mac** |
| Aramco SAES hydrojetting clauses | **NOT FOUND** |
| CSMS contractor questionnaire | **NOT FOUND** (GAP-002 open) |
| Aramco Third Party Approved Safety Training Provider list | Found (WPR context) — TVTC pack correspondence |

See `CROSS_WIKI_ARAMCO_CSM_STATUS.md`.

---

## 3. Cross-domain local material (use carefully)

| Domain | Path | HPWJ use |
|--------|------|----------|
| Confined space (CSE) | `Desktop/nebosh/CS/…` | SIMOPS / vessel entry interface only |
| WPR / LOTO / PTW | `Desktop/nebosh/WPR/…` | Permit interface |
| Working at Height | `Documents/aimshse/AIMS-L3-HSE-P-010-…` | Elevated jetting platforms |
| STORP / SASREF induction | `Documents/Training/…` | Client site culture, not HPWJ controls |

---

## 4. Priority human actions

1. Drop Aramco **CSM** / **SAES** / **CSMS** files into Desktop if Anabeeb holds them → re-run extract.  
2. Confirm whether OPS-P-019 will be renumbered to AIMS-L3-HSE-SWP-005.  
3. Copyright: WJTA deck videos = internal reference only (never republish).  

---

## 5. Multi-AI note

This harvest is shared pattern with Rigging- and Scaffolding-Grokapedia (`references/source_materials/MAC_HARVEST_2026-07-28.md` in each).  
Grok performed the Mac crawl; Claude previously did WJTA gap analysis and numeric verification on HPWJ main branch.
