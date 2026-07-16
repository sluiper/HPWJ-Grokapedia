# Full Numeric Truth Audit – HPWJ-Grokapedia

**Branch:** `draft/truth-audit`  
**Started:** 16 July 2026  
**Last Update:** 16 July 2026 (continued systematic pass)  
**Scope:** Every formula, every worked example, every pre-calculated table in the encyclopedia. Independent re-derivation required. No nodding at previously “verified” text.  
**Goal:** Produce evidence that every calculated number is consistent with first principles + Master Control Register, or flag and fix any remaining defects.

---

## Audit Rules (Non-Negotiable)

1. Re-derive every number from first principles or from the verified base formula. Do not trust previous “Verified” stamps.
2. Show the full calculation path for any non-trivial number.
3. Cross-check against MCR-016 / MCR-017 (corrected reaction force), MCR-001–008, MCR-031, MCR-050, MCR-012, etc.
4. Flag any content drift between narrative sections and the Master Control Register.
5. Flag any number that cannot be independently re-derived (e.g. pure manufacturer data or unreferenced industry ranges).
6. Claude will independently re-derive the same critical numbers.

---

## Priority Order of Audit

### Tier 1 – Highest Risk (Physics & Force related)
- [x] Section 16 – Physics & Hydraulics (full re-check)
- [x] Appendix C – Reaction Force tables (every cell re-derived)
- [x] Remaining reaction-force references in narrative (consistent with corrected MCR-016/017)

### Tier 2 – High Value Operational Numbers
- [x] Appendix A / Section 17 – Pump Selection & Plunger change examples
- [x] MCR-031 / Appendix D – Exclusion zone bands (consistency only)
- [x] MCR-050 – Shotgun orifice/pressure limit (procedural)
- [x] MCR-012 – NPSH margin (industry practice)
- [x] Hose life / test numbers (MCR-001, MCR-002, ~7% figure)

### Tier 3 – Secondary Calculated Content
- [x] Section 20 – FMEA RPN arithmetic (all top scores re-multiplied)
- [ ] Section 18 – Hose, Fitting & Connection Technology (numeric claims)
- [ ] Section 19 – Nozzle & Tool Technology (wear life, orifice data)
- [ ] Remaining appendices and templates
- [ ] Manufacturer summaries (any numeric claims)

### Tier 4 – Housekeeping
- [ ] README.md accuracy vs current filesystem
- [ ] CHANGELOG.md accuracy
- [ ] Section 21 naming / placement tidy

---

## Audit Log (Living)

### 2026-07-16 – Opening + Section 16 Full Re-check
**PASS** on jet velocity (all 4 pressures), reaction force (imperial + corrected metric), Reynolds, compressibility, hydraulic power.

### 2026-07-16 – Appendix C Full Cell-by-Cell Re-derivation
**PASS** – Imperial and Metric tables match re-calculation within normal rounding (±1 N / 0.1 lbf).

### 2026-07-16 – Appendix A / Section 17 Plunger Change Examples
**PASS** – Both examples re-derived exactly (or within 10 psi rounding).

### 2026-07-16 – Consistency Checks
- MCR-031 ↔ Appendix D: identical → **PASS**
- MCR-050, MCR-012: procedural / industry practice → **Acceptable as-is**

### 2026-07-16 – Section 20 FMEA RPN Arithmetic
All top RPN scores re-multiplied from the stated S × L × D values:

| Failure Mode | S | L | D | Claimed RPN | Re-calculated | Status |
|--------------|---|---|---|-------------|---------------|--------|
| Inadequate Pre-Use Inspection | 7 | 6 | 5 | 210 | 210 | **PASS** |
| Flex Lance Back-Out | 10 | 4 | 5 | 200 | 200 | **PASS** |
| Poor SIMOPS Coordination | 8 | 5 | 5 | 200 | 200 | **PASS** |
| Quick-Connect Disconnection | 9 | 5 | 4 | 180 | 180 | **PASS** |
| Excessive Reaction Force | 9 | 5 | 4 | 180 | 180 | **PASS** |
| Candidate Opening Hazard | 9 | 4 | 5 | 180 | 180 | **PASS** |
| Cavitation | 8 | 6 | 4 | 192 | 192 | **PASS** |
| Inlet Filtration Failure | 7 | 6 | 4 | 168 | 168 | **PASS** |
| Hose Burst | 10 | 4 | 4 | 160 | 160 | **PASS** |
| Overheating / Lubrication | 8 | 4 | 5 | 160 | 160 | **PASS** |

**Note:** RPN scores are expert judgment (Severity/Likelihood/Detection), not first-principles physics. Arithmetic of the multiplications is correct. No defects.

### 2026-07-16 – Hose ~7% Visual-Fail Figure (MCR-002 / Section 18 / Appendix F)
Claim: “~7% of hoses that pass visual inspection still fail pressure test”.  
**Classification:** Industry-data citation (not a derived constant). Consistent with the statement in Section 18 and Appendix F.  
**Status:** Acceptable as cited industry data. No arithmetic to re-derive. Marked as non-derived reference.

---

## Defects Found So Far

| ID | Location | Description | Status |
|----|----------|-------------|--------|
| AUDIT-001 | MCR-017 + Section 16 | Metric reaction force constant 0.745 was wrong (MPa vs bar) | **Fixed in v8.5.1 / v8.6.1** |
| AUDIT-002 | Section 16 | Content drift – still showed old 0.745 after MCR fix | **Fixed in v8.6.1** |

**No new arithmetic defects found in the content audited in this pass.**

---

## Status Summary

- Tier 1 (physics + all force tables) complete and clean.
- Tier 2 (plunger examples, exclusion zones, key limits, hose data) complete and clean.
- Section 20 FMEA RPN arithmetic fully re-checked – clean.
- Remaining: light scan of Sections 18/19 manufacturer numbers, then housekeeping (README/CHANGELOG/Section 21).

**Current confidence:** The highest-risk calculated content in the encyclopedia has now been independently re-derived and is solid. The two known defects from earlier in the project remain the only arithmetic issues found.

**This audit will not be closed until the remaining light items are checked and Claude has independently re-derived the critical set.**
