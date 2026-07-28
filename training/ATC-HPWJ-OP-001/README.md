# ATC-HPWJ-OP-001 — Training Pack

**MCR Controls Referenced:** MCR-005, 006, 009, 010, 016, 017, 019, 020, 021, 023, 025, 027, 028, 030, 031, 033, 038, 039, 043, 046, 047, 048, 050, 051, 052 (+ high-priority RPN set in MCR)

**Course:** Anabeeb HPWJ Operator Competency Course  
**Level:** Level 2 (HPWJ Operator) per Chapter 13  
**Branch / campaign:** `draft/campaign-max-truth-training` (v9)  
**Living rule:** After any MCR change, review this pack within 30 days (MCR-064 / Ch13 §13.6).

---

## Pack contents

| File | Purpose |
|------|---------|
| `00_Course_Specification.md` | Code, gates, pass criteria, outcomes |
| `01_Trainer_Guide.md` | Day-by-day script; **cite MCR only for formulas** |
| `02_Student_Workbook.md` | Exercises + links to encyclopedia SSOT tools |
| `03_Practical_Competency_Checklist.md` | Field Verification instrument (15 critical items) |
| `04_Theory_Exam_Bank.md` | Versioned question bank mapped to MCR / Ch10 |
| `05_Assessment_Record_and_Certificate.md` | Records, photo card, Medical Alert issue log |
| `06_Equipment_and_PPE_List.md` | Delivery equipment minimum list |

---

## Hard build rules (do not break)

1. Every file starts with **MCR Controls Referenced**.  
2. **Never hard-code** reaction-force formula constants — always **MCR-017** (and Sec16 derivation).  
3. Absolute thresholds (team size, exclusion, shotgun limits, rupture factor, tip mark, max pressure) are cited by **MCR-ID**; live wording lives in `MASTER_CONTROL_REGISTER.md`.  
4. Prefer links / references to appendices and templates rather than copy-paste of numbers.  
5. Pass/fail is only via the practical checklist + theory score + behavioural pass.

---

## SSOT references (do not duplicate)

| Need | Path |
|------|------|
| Controls | `/MASTER_CONTROL_REGISTER.md` |
| Framework | `/docs/13_Competency_Framework_Training_and_Assessment.md` |
| Physics / RF derivation | `/docs/16_Physics_and_Hydraulics.md` |
| RF tables | `/docs/appendices/Appendix_C_Reaction_Force_Quick_Calculator.md` |
| Never Rules card | `/docs/appendices/Appendix_G_Never_Rules_One_Pager.md` |
| Exclusion / team | `/docs/appendices/Appendix_D_Exclusion_Zone_and_Team_Quick_Reference.md` |
| Pre-use full checklist | `/templates/checklists/Pre_Use_Inspection_Checklist.md` |
| Medical Alert | `/templates/medical_alert/HPWJ_Medical_Alert_Card.md` |
| Trauma / emergency | `/docs/10_Emergency_Response_Medical_Management_and_Trauma.md` |

---

## Status

| Item | Status |
|------|--------|
| Pack draft on campaign branch | **Yes** |
| Claude verification of pack | Pending |
| Human pilot approval | Pending |
| Merge to main | Only after human gate |
