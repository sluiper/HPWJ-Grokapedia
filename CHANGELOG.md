# CHANGELOG

## v8.6.1 – 16 July 2026 (Truth Audit – Content Drift Fixed + Dormant Number Review)

### Critical Content Drift Fixed
- **Section 16** still contained the old incorrect metric reaction force formula (0.745). This was content drift after MCR-017 was corrected in v8.5.1. Section 16 now matches the corrected constant (0.233) with full derivation shown.

### Dormant Number Audit Findings
- **MCR-031** (Exclusion zone bands 7.5–10 m / 10–15 m / 15–25 m+ / 10 m absolute): Industry-practice ranges, not first-principles constants. Consistent across MCR and Appendix D. No arithmetic defect. Acceptable as guidance ranges.
- **MCR-050** (Shotgun ≤10 000 psi with ≤1.6 mm orifice + ≤250 N): Procedural limit from OPS-P-019. Not a derived constant. Leave as-is.
- **MCR-012** (NPSH margin 0.5–1.0 bar): Standard pump engineering practice. Acceptable industry guidance.
- No additional arithmetic defects found in the remaining numeric MCR rows examined.

### Previous (v8.6)
- Complete high-value field toolkit (Appendices C–J + cards) merged after four consecutive clean Claude Verification Reports.

**This changelog prioritises truth over presentation.**
