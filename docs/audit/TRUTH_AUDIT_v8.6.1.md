# Full Numeric Truth Audit – HPWJ-Grokapedia

**Branch:** `draft/truth-audit`  
**Started:** 16 July 2026  
**Last Update:** 16 July 2026  
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
- [ ] Any remaining reaction-force examples in Chapters 7, 8, 12, 20

### Tier 2 – High Value Operational Numbers
- [x] Appendix A / Section 17 – Pump Selection & Plunger change examples
- [x] MCR-031 / Appendix D – Exclusion zone bands (consistency only)
- [x] MCR-050 – Shotgun orifice/pressure limit (procedural – no derivation required)
- [x] MCR-012 – NPSH margin (industry practice – no derivation required)
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

### 2026-07-16 – Opening + Section 16 Full Re-check

**Section 16 – Jet Velocity (Bernoulli)**
- Formula: $ v = \sqrt{2 \Delta P / \rho} $
- 10 000 psi = 68.9476 MPa → 371.3 m/s → **PASS** (matches published 44.721√P(MPa))
- 15 000 / 20 000 / 40 000 psi → 455 / 525 / 743 m/s → **PASS**

**Section 16 – Reaction Force**
- Imperial 0.052 × GPM × √psi → **PASS** (WJTA-IMCA)
- Metric 0.233 × L/min × √bar → full unit conversion re-derived → **PASS**
- Worked example 0.040" @ 15k psi ≈ 5–6 GPM → ~38 lbf / 170 N → **PASS**

**Section 16 – Reynolds Number**
- 1" ID, 80 L/min, 20 °C → Re ≈ 66 800 → **PASS**

**Section 16 – Compressibility @ 40k psi**
- ~12.5 % using K ≈ 2.2 GPa → **PASS** (order of magnitude)

**Section 16 – Hydraulic Power**
- P(psi)×Q(GPM)/1714 → standard → **PASS**

### 2026-07-16 – Appendix C Full Cell-by-Cell Re-derivation

**Imperial table (0.052 × Q × √P)**  
All cells re-calculated. Match existing table within 0.1 lbf / 1 N rounding. **PASS**

**Metric table (0.233 × Q × √P)**  
All cells re-calculated. Match existing table within ±1 N rounding (expected). **PASS**

### 2026-07-16 – Appendix A / Section 17 Plunger Change Examples

**Example 1:** 15 mm → 12 mm, 10 000 psi @ 80 L/min  
- Flow ratio = (12/15)² = 0.6400 → New Flow = 51.2 L/min  
- New Pressure = 10 000 × (80/51.2) = 15 625 psi  
- Claimed values match exactly → **PASS**

**Example 2:** 12 mm → 14 mm, 15 000 psi @ 50 L/min  
- Flow ratio = (14/12)² = 1.3611 → New Flow = 68.1 L/min  
- New Pressure = 15 000 × (50/68.1) ≈ 11 020 psi  
- Claimed 68 L/min / 11 030 psi → within normal rounding → **PASS**

### Consistency Checks (No Derivation Required)
- MCR-031 exclusion bands ↔ Appendix D: identical → **PASS**
- MCR-050 shotgun limit: procedural (OPS-P-019) → **Acceptable as-is**
- MCR-012 NPSH margin: standard pump practice → **Acceptable as-is**

---

## Defects Found So Far

| ID | Location | Description | Status |
|----|----------|-------------|--------|
| AUDIT-001 | MCR-017 + Section 16 | Metric reaction force constant 0.745 was wrong (MPa vs bar) | **Fixed in v8.5.1 / v8.6.1** |
| AUDIT-002 | Section 16 | Content drift – still showed old 0.745 after MCR fix | **Fixed in v8.6.1** |

**No new arithmetic defects found in the content audited today.**

---

## Status Summary

- Tier 1 (physics + force tables) essentially complete and clean.
- Tier 2 plunger examples and key operational limits clean.
- Next: Scan remaining narrative sections (7, 8, 12, 18, 19, 20) for any un-audited calculated numbers, then housekeeping.

**This audit will not be closed until every calculated number has an independent re-derivation record.**
