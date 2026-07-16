# CHANGELOG

## v8.0 – 16 July 2026 (Truth Protocol + Full Core + Audit Restoration)

### Critical Fixes
- **Section 16.4 Jet Velocity**: Corrected unit-conversion error (values had been understated by ≈√10). Verified theoretical velocities: 371 / 455 / 525 / 743 m/s at 10 / 15 / 20 / 40k psi.
- **Chapter 7.17 residual velocity band**: Audit found the old wrong 160–235 m/s band still present in the UHP comparison table; corrected to match Section 16.4.
- **Silent content regression**: FMEA (Section 20) and Physics (Section 16) had been gutted during earlier “verification” commits; full Description/Causes/Consequences/Detection/Controls and derivations restored.
- Self-grading language (“10/10”, “world best”, “Max Truth Reviewed”) retired from front-matter and remaining residual headers cleaned as found.

### Structural / Metadata
- README and `00_Encyclopedia_Structure.md` synchronised with actual filesystem (no longer claiming empty chapters that exist).
- Master Control Register: 38 rows, zero dangling citations found in audit passes.
- Duplicate structure file removed earlier in cycle.

### Content Delivered in v8.0 Cycle
- Full operational core: Chapters 1–15
- Technical sections: 16 (restored + SVGs), 17, 18, 19, 20 (restored + candidate site-hazard), 22, 24, 25 (15 cases: 1 documented HSE fatality + 14 composites), 26, 28
- Appendices A (Pump Selection Quick Guide) and B (Manufacturer Comparison Matrix)
- Documented Case 2 (UK HSE flexi-lance fatality via SAFETY4SEA / IMCA) replacing composite
- NIOSH CA/FACE 16CA001 site-hazard case added to Chapter 5 + FMEA candidate row
- 11 manufacturer summaries synthesised in Section 22 / Appendix B

### Remaining Honest Gaps
- Aramco SAES / CSMS and SABIC/PETRO RABIGH clause extraction (requires internal documents)
- Sections 23 (marine/offshore – low priority for Anabeeb onshore scope), 27 (Lessons Learned – grows with real incidents), 29 (Future Tech)
- Thin operational chapters 8, 11, 12 still shorter than field-depth peers (functional but not full encyclopedia depth)
- Additional appendices and more diagrams
- Section 21 Regulatory Matrix naming/placement tidy

**This changelog prioritises truth over presentation.**

## Earlier Activity (15–16 July 2026 / v7.x)
- Built operational core foundations (Ch5–7, 9, 10, 13)
- Templates and standards library
- Competency framework hybrid of WJTA / WJA / AS/NZS elements
- Initial MCR expansion and first incident library pass
