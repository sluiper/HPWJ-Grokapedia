# CHANGELOG

## v8.5.1 – 16 July 2026 (CRITICAL: MCR-017 Metric Formula Corrected)

### Critical Correction
- **MCR-017 metric reaction force constant** corrected from **0.745** to **≈0.233** × Q(L/min) × √P(bar).
- Root cause: unit conversion error. The constant 0.745 is correct when pressure is expressed in **MPa**, but it was incorrectly paired with **bar**. This is the same class of √10-scale unit conversion error previously fixed in Section 16 jet velocity.
- Full first-principles conversion from the verified imperial formula (0.052 × GPM × √psi) yields ≈0.2327. Rounded operational constant: **0.233**.
- Direction of error was conservative (over-estimated force by ~3.2×). No known unsafe operations resulted, but the defect violated the “every number derived” standard.
- Appendix C tables on the draft branch were already correct because they were computed via the imperial path + conversion rather than the buggy metric formula.

### Previous (v8.5)
- All 13 Drafting MCR rows promoted to Visible (human “lfg all”).
- MCR fully clean at 65 Visible.

**This changelog prioritises truth over presentation.**
