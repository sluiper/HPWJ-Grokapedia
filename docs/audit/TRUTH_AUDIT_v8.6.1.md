# Full Numeric Truth Audit – HPWJ-Grokapedia

**Branch:** `draft/truth-audit`  
**Started:** 16 July 2026  
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
- [x] Section 16 – Physics & Hydraulics (partially done; full re-check of remaining numbers)
- [ ] Appendix C – Reaction Force tables (already corrected, re-confirm every cell)
- [ ] Any remaining reaction-force examples in Chapters 7, 8, 12, 20

### Tier 2 – High Value Operational Numbers
- [ ] Section 17 – Pump Selection & Sizing (plunger change examples, flow/pressure relationships)
- [ ] MCR-031 / Appendix D – Exclusion zone bands (confirm consistency only)
- [ ] MCR-050 – Shotgun orifice/pressure limit
- [ ] MCR-012 – NPSH margin
- [ ] Hose life / test numbers (MCR-001, MCR-002, ~7% figure)

### Tier 3 – Secondary Calculated Content
- [ ] Section 18 – Hose, Fitting & Connection Technology
- [ ] Section 19 – Nozzle & Tool Technology
- [ ] Section 20 – FMEA RPN numbers (are the RPN scores themselves consistent?)
- [ ] Remaining appendices and templates
- [ ] Manufacturer summaries (any numeric claims)

### Tier 4 – Housekeeping
- [ ] README.md accuracy vs current filesystem
- [ ] CHANGELOG.md accuracy
- [ ] Section 21 naming / placement tidy

---

## Audit Log (Living)

### 2026-07-16 – Opening + Section 16 Re-check

**Section 16 – Jet Velocity (Bernoulli)**
- Formula: $ v = \sqrt{2 \Delta P / \rho} $
- 10 000 psi = 68.9476 MPa → $ v = \sqrt{2 \times 6.89476 \times 10^7 / 1000} = 371.3 $ m/s → **Pass** (matches published 44.721√P(MPa) check)
- 15 000 psi → 455 m/s → **Pass**
- 20 000 psi → 525 m/s → **Pass**
- 40 000 psi → 743 m/s → **Pass**

**Section 16 – Reaction Force**
- Imperial: 0.052 × GPM × √psi → previously verified against WJTA-IMCA → **Pass**
- Metric: now correctly 0.233 × L/min × √bar (full unit conversion shown in MCR-017 and Section 16) → **Pass**
- Worked example 0.040" @ 15 000 psi ≈ 5–6 GPM → ~38 lbf / 170 N → **Pass**

**Section 16 – Reynolds Number worked example**
- 1" ID hose, 80 L/min, 20 °C → v ≈ 2.63 m/s → Re ≈ 66 800 → **Pass** (re-derived)

**Section 16 – Compressibility at 40k psi**
- Bulk modulus ~2.2 GPa, ΔP ≈ 276 MPa → ~12.5 % → **Pass** (order-of-magnitude correct)

**Section 16 – Hydraulic Power**
- HP ≈ P(psi) × Q(GPM) / 1714 → standard formula → **Pass**

### Next Immediate Actions
1. Full cell-by-cell re-derivation of Appendix C reaction force tables (both Imperial and Metric).
2. Re-derive all plunger-change worked examples in Section 17 / Appendix A.
3. Scan Chapters 7, 8, 12, 20 for any remaining reaction-force or pressure/flow numbers that were never exercised.

---

## Defects Found So Far

| ID | Location | Description | Status |
|----|----------|-------------|--------|
| AUDIT-001 | MCR-017 + Section 16 | Metric reaction force constant 0.745 was wrong (MPa vs bar) | **Fixed in v8.5.1 / v8.6.1** |
| AUDIT-002 | Section 16 | Content drift – still showed old 0.745 after MCR fix | **Fixed in v8.6.1** |

---

## Status Summary

- Audit opened and structure locked.
- Highest-risk physics section re-checked and clean.
- Ready for systematic expansion to all remaining calculated content.

**This audit will not be closed until every calculated number has an independent re-derivation record.**
