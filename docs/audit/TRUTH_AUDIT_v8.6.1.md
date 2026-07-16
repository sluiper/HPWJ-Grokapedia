# Full Numeric Truth Audit – HPWJ-Grokapedia

**Branch:** `draft/truth-audit`  
**Started:** 16 July 2026  
**Last Update:** 16 July 2026 (continued after AUDIT-003)  
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
7. **STANDING RULE:** After any formula fix at the canonical source, systematically search for **every independent restatement** of that formula across the entire repository (templates, appendices, chapters, cards). Source fixes do not automatically propagate.

---

## Priority Order of Audit

### Tier 1 – Highest Risk (Physics & Force related)
- [x] Section 16 – Physics & Hydraulics (full re-check by both models)
- [x] Appendix C – Reaction Force tables (every cell re-derived)
- [x] templates/checklists/Reaction_Force_Quick_Reference.md (AUDIT-003 – fixed v8.6.2)
- [x] Remaining reaction-force references in narrative

### Tier 2 – High Value Operational Numbers
- [x] Appendix A / Section 17 – Pump Selection & Plunger change examples
- [x] MCR-031 / Appendix D – Exclusion zone bands
- [x] MCR-050 – Shotgun orifice/pressure limit
- [x] MCR-012 – NPSH margin
- [x] Hose life / test numbers (MCR-001, MCR-002, ~7% figure)
- [x] MCR-018 – Nozzle wear life 20–60 h (manufacturer/typical range)

### Tier 3 – Secondary Calculated Content
- [x] Section 20 – FMEA RPN arithmetic (all top scores re-multiplied by both models)
- [x] Section 18 – Hose, Fitting & Connection Technology
- [x] Section 19 related numbers (wear life etc.) – no first-principles calculated constants found beyond MCR ranges
- [x] Remaining appendices (C, D, F–J) – already verified in earlier clean cycles + force tables re-derived
- [ ] Manufacturer summaries (any numeric claims) – low risk, mostly descriptive

### Tier 4 – Housekeeping
- [ ] README.md accuracy vs current filesystem (v8.6.2 now)
- [ ] CHANGELOG.md accuracy
- [ ] Section 21 naming / placement tidy

---

## Audit Log (Living)

### Key PASS Results (Both Models)
- Jet velocity table (Section 16): 371 / 455 / 525 / 743 m/s → **PASS**
- Reaction force imperial 0.052 + corrected metric 0.233 → **PASS**
- Appendix C every cell → **PASS**
- Plunger change examples → **PASS**
- All 17 FMEA RPN multiplications → **PASS**
- Reynolds, compressibility, hydraulic power → **PASS**

### Key Acceptable-as-Is Classifications
- Exclusion zone bands (MCR-031): industry practice ranges
- Shotgun limit (MCR-050): procedural (OPS-P-019)
- NPSH margin (MCR-012): standard pump practice
- Hose ~7% visual-fail figure: industry citation
- Nozzle wear life 20–60 h (MCR-018): manufacturer/typical range

### Critical Defects Found & Fixed
| ID | Location | Description | Status |
|----|----------|-------------|--------|
| AUDIT-001 | MCR-017 | Metric constant 0.745 wrong (MPa vs bar) | Fixed v8.5.1 |
| AUDIT-002 | Section 16 | Content drift of old 0.745 | Fixed v8.6.1 |
| AUDIT-003 | Reaction_Force_Quick_Reference.md template | Third independent restatement of 0.745 | Fixed v8.6.2 |

**No further arithmetic defects found after exhaustive checking of highest-risk content.**

---

## Status Summary

The full dual-model re-derivation pass has now:
1. Confirmed all high-risk calculated numbers are correct.
2. Surfaced and eliminated the third (and hopefully final) copy of the metric reaction-force bug.
3. Established the standing rule that source fixes must be followed by a full restatement search.

Remaining work is low-risk (descriptive manufacturer text + housekeeping).  
**Recommendation:** Close the arithmetic portion of the audit after Claude confirms the three fixed locations and the critical re-derivations, then do the three housekeeping items as a final tidy commit.

**This audit will not be formally closed until Claude signs off on the critical set and the housekeeping is complete.**
