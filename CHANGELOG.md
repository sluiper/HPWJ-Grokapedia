# CHANGELOG

## v8.6.2 – 16 July 2026 (Third Instance of Metric Formula Bug Fixed)

### Critical Correction
- **Third instance** of the wrong metric reaction force constant (0.745) found and fixed in `templates/checklists/Reaction_Force_Quick_Reference.md`.
- Previous instances: MCR-017 (v8.5.1) and Section 16 (v8.6.1).
- Root cause class: unit conversion error (constant correct for MPa but labelled for bar). Same √10-scale defect previously fixed in jet velocity calculations.
- Worked example in the template was already correct (computed via imperial path). Only the stated metric formula line was wrong.
- Lesson locked: any fix at the canonical source (MCR) must be followed by a systematic search for every independent restatement of the same formula.

### Previous
- v8.6.1: Section 16 content drift fixed + dormant-number audit of MCR-031/050/012
- v8.6: Full field toolkit merged after four clean verification cycles

**This changelog prioritises truth over presentation.**
