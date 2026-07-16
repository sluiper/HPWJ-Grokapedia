# Full Numeric Truth Audit – HPWJ-Grokapedia

**Branch:** `draft/truth-audit`  
**Started:** 16 July 2026  
**Last Update:** 16 July 2026 (Claude independent pass + third instance of the metric bug)  
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
7. **NEW STANDING RULE (from AUDIT-003):** After any formula fix at the canonical source (MCR or Section 16), systematically search for **every independent restatement** of that formula across the entire repository (templates, appendices, chapters, cards). Source fixes do not automatically propagate.

---

## Priority Order of Audit

### Tier 1 – Highest Risk (Physics & Force related)
- [x] Section 16 – Physics & Hydraulics (full re-check by both models)
- [x] Appendix C – Reaction Force tables (every cell re-derived)
- [x] templates/checklists/Reaction_Force_Quick_Reference.md (third instance of the bug – now fixed)
- [x] Remaining reaction-force references in narrative

### Tier 2 – High Value Operational Numbers
- [x] Appendix A / Section 17 – Pump Selection & Plunger change examples
- [x] MCR-031 / Appendix D – Exclusion zone bands
- [x] MCR-050 – Shotgun orifice/pressure limit
- [x] MCR-012 – NPSH margin
- [x] Hose life / test numbers (MCR-001, MCR-002, ~7% figure)

### Tier 3 – Secondary Calculated Content
- [x] Section 20 – FMEA RPN arithmetic (all top scores re-multiplied by both models)
- [x] Section 18 – Hose, Fitting & Connection Technology
- [ ] Section 19 – Nozzle & Tool Technology
- [ ] Remaining appendices and templates
- [ ] Manufacturer summaries (any numeric claims)

### Tier 4 – Housekeeping
- [ ] README.md accuracy vs current filesystem
- [ ] CHANGELOG.md accuracy
- [ ] Section 21 naming / placement tidy

---

## Audit Log (Living)

### 2026-07-16 – Opening + Section 16 Full Re-check (Grok + Claude independent)
**PASS** on jet velocity, reaction force (imperial + corrected metric), Reynolds, compressibility, hydraulic power.

### 2026-07-16 – Appendix C Full Cell-by-Cell Re-derivation
**PASS** – Imperial and Metric tables match re-calculation within normal rounding.

### 2026-07-16 – Appendix A / Section 17 Plunger Change Examples
**PASS** – Both examples re-derived by both models.

### 2026-07-16 – Section 20 FMEA RPN Arithmetic
**PASS** – All top RPN scores re-multiplied and match (Claude confirmed all 17).

### 2026-07-16 – Section 18 Full Scan
**PASS** – No new calculated numbers; all match MCR.

### 2026-07-16 – Claude Independent Discovery of AUDIT-003
**CRITICAL**: `templates/checklists/Reaction_Force_Quick_Reference.md` still contained the old 0.745 metric constant. This is the third independent location of the same bug. Fixed immediately on main as v8.6.2. Worked example in the file was already correct (imperial path). Standing rule #7 added.

---

## Defects Found So Far

| ID | Location | Description | Status |
|----|----------|-------------|--------|
| AUDIT-001 | MCR-017 | Metric reaction force constant 0.745 was wrong (MPa vs bar) | **Fixed in v8.5.1** |
| AUDIT-002 | Section 16 | Content drift – still showed old 0.745 after MCR fix | **Fixed in v8.6.1** |
| AUDIT-003 | templates/checklists/Reaction_Force_Quick_Reference.md | Third independent restatement of the wrong 0.745 constant | **Fixed in v8.6.2** |

**No other arithmetic defects found to date.**

---

## Status Summary

- The full-audit approach has now proven its value three times on the same root defect class.
- Highest-risk calculated content (physics, force tables, plunger examples, FMEA arithmetic) is clean after independent re-derivation by both models.
- Standing rule added to prevent future source-fix-but-copy-remains-wrong failures.
- Remaining light items: Section 19, manufacturer summaries, housekeeping.

**Current confidence:** High and rising. The systematic dual-model re-derivation is working exactly as designed.

**This audit will not be closed until the remaining light items are checked and both models agree the critical set is fully clean.**
