# CHANGELOG

## v8.6.3 – 16 July 2026 (Housekeeping after full truth audit)

### Housekeeping
- README updated to accurately reflect v8.6.2 state, the three-instance formula fix, the living truth audit, and current gaps.
- No changes to calculated content.

## v8.6.2 – 16 July 2026 (Third Instance of Metric Formula Bug Fixed)

### Critical Correction
- **Third instance** of the wrong metric reaction force constant (0.745) found and fixed in `templates/checklists/Reaction_Force_Quick_Reference.md`.
- Previous instances: MCR-017 (v8.5.1) and Section 16 (v8.6.1).
- Root cause class: unit conversion error (constant correct for MPa but labelled for bar). Same √10-scale defect previously fixed in jet velocity calculations.
- Worked example in the template was already correct (computed via imperial path). Only the stated metric formula line was wrong.
- Lesson locked: any fix at the canonical source (MCR) must be followed by a systematic search for every independent restatement of the same formula.

## v8.6.1 – 16 July 2026 (Truth Audit – Content Drift Fixed + Dormant Number Review)

### Critical Content Drift Fixed
- **Section 16** still contained the old incorrect metric reaction force formula (0.745). Fixed to match corrected MCR-017.

### Dormant Number Audit Findings
- MCR-031, MCR-050, MCR-012 classified as industry/procedural ranges – no arithmetic defects.

## v8.6 – 16 July 2026 (Major Field Toolkit Merge)

### Content
- Merged the complete high-value Appendices field toolkit after four consecutive clean Claude Verification Reports (zero P0/P1).
- All content pure synthesis of already-verified MCR rows.

### Process Win
Four consecutive clean verification cycles with zero P0/P1 findings.

**This changelog prioritises truth over presentation.**
