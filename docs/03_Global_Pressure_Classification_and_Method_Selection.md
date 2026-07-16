# Chapter 3: Global Pressure Classification & Method Selection

**Version 8.0**

## 3.1 Purpose

This chapter defines the pressure classification bands used throughout the Anabeeb HPWJ Encyclopedia and links them directly to existing Master Control Register controls (especially exclusion zone sizing, reaction force, AWD, and competency requirements). It does not invent a new scheme; it formalises the bands already used in Chapter 7, MCR-031, and the UHP section (7.17).

## 3.2 Pressure Classification Bands Used in this Encyclopedia

The following bands are the working classification for Anabeeb operations. They align with common industry practice and with the numeric thresholds already present in the repository.

| Band | Approximate Pressure Range | Typical Applications | Key Existing Controls |
|------|----------------------------|----------------------|-----------------------|
| Low / Medium | Up to ~10,000 psi (≈690 bar) | Light cleaning, some surface work | Base exclusion zone (MCR-031) |
| High Pressure (HP) | 10,000 – 20,000 psi | Vessel cleaning, general industrial jetting, many tube applications | Expanded exclusion zone, full pre-use, reaction force controls (MCR-016, MCR-031) |
| High / Approaching UHP | ~15,000 – 25,000 psi | Harder deposits, higher-energy tube work | Same as HP + stricter reaction-force and tooling checks |
| Ultra-High Pressure (UHP) | 30,000 – 40,000+ psi | Tube bundle cleaning with creeping hose / flex systems, specialised cleaning | MCR-034 (Level 3 only, AWD mandatory, vacuum, expanded exclusion), MCR-031 upper tier |

**Notes on the bands:**
- The 10k / 20k / 40k psi points are already used for jet velocity examples (Section 16), exclusion zone guidance (MCR-031), and the UHP Creeping Hose section (7.17).
- 15,000 psi appears repeatedly as a common planning and reaction-force example pressure.
- No new numeric thresholds are introduced here. All figures already exist in the MCR or technical chapters.

## 3.3 Method Selection Principles

Method selection is driven by:
1. **Deposit type and location** (surface, tube ID, vessel internal, line moleing).
2. **Required pressure and flow** (cleaning power vs coverage).
3. **Reaction force and control method** (handheld vs mechanical assistance vs automation) — always apply the three additive controls in MCR-016.
4. **Competency level required** (especially MCR-034 for UHP).
5. **Site constraints** (access, SIMOPS, heat, barricading – Chapters 5 & 6).

### Quick Selection Guidance (linked to existing controls)

- **Handheld surface or light vessel work** ≤ ~15–20k psi: Confirm reaction force ≤ 250 N + ≤1/3 body weight + barrel geometry (MCR-016). Use full Pre-Use Checklist.
- **Flex lance / tube cleaning**: AWD mandatory and verified every insertion (MCR-019 / MCR-020). Never bypass.
- **UHP creeping hose / 40k psi tube bundle work**: Only Level 3 operators (MCR-034). Expanded exclusion zone (MCR-031), vacuum system at outlet, no quick-connects in high-movement run, full AWD verification.
- **Automated / robotic systems**: Pre-use sensor and interlock test (MCR-021), clear zoning, SIMOPS control (MCR-028).

## 3.4 Exclusion Zone Linkage (MCR-031)

Exclusion zone minimums already defined in MCR-031 and Chapter 5:

- Up to 10,000 psi → 7.5–10 m
- 10,000–20,000 psi → 10–15 m
- 20,000–40,000+ psi (UHP) → 15–25 m+ (adjust for jet direction and possible hose whip)

These distances are the current Anabeeb baseline. They must be increased if jet direction, hose whip potential, or site geometry requires it.

## 3.5 Candidate New MCR Items (if further refinement is needed)

No new mandatory thresholds are asserted in this chapter. If future work requires finer banding (e.g., a formal 25k–30k intermediate class or a hard upper limit for handheld work), the following would be candidates for addition to the Master Control Register rather than chapter-only rules:

- Candidate: Formal upper pressure limit for pure handheld work without mechanical assistance.
- Candidate: Specific competency or tooling requirements for the 20–30k psi transition band.

Until added to the MCR, no such limits are enforceable from this chapter alone.

## 3.6 Summary

Pressure classification in this Encyclopedia is deliberately simple and already operationalised through existing MCR items (especially MCR-016, MCR-019/020, MCR-031, MCR-034). Method selection always starts with the deposit and access constraints, then applies the reaction-force, AWD, competency, and exclusion-zone controls that already exist.

## Verification Log

| Claim | Status |
|-------|--------|
| Pressure bands used | Taken directly from existing Ch7, Section 16, MCR-031, and 7.17 UHP content |
| Exclusion zone distances | Exact match to MCR-031 |
| Reaction force controls | Exact match to MCR-016 |
| UHP / creeping hose rules | Exact match to MCR-034 |
| AWD rules | Exact match to MCR-019 / MCR-020 |
| No new numeric thresholds introduced | Confirmed – any future refinement flagged only as MCR candidates |

**End of Chapter 3**
