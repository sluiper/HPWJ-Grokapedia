# Appendix A: Pump Selection Quick Guide

**Version 8.0**  
**Source material only:** Chapter 7, Section 17, Master Control Register. No new sizing formulas or thresholds.

## A.1 Core Decision Flow

1. Define the cleaning task (deposit type + geometry).
2. Choose pressure band (Chapter 3 / MCR-031 exclusion-zone tiers).
3. Decide flow priority (coverage/speed vs point impact).
4. Check reaction force will satisfy MCR-016 for the planned operators/tooling.
5. Confirm hose, fitting, rupture-disc and dump-system ratings after any plunger change (MCR-015, MCR-009, MCR-010).
6. Match competency level (especially MCR-034 for UHP).

## A.2 Plunger Change Relationships (from Chapter 7 / Section 17)

For fixed RPM and power:

- Flow ∝ (Plunger Diameter)²
- New Flow = Old Flow × (New Diameter / Old Diameter)²
- New Pressure ≈ Old Pressure × (Old Flow / New Flow)

**Worked Example 1 – Increase pressure**  
15 mm → 12 mm plungers, was 10 000 psi @ 80 L/min  
→ New Flow ≈ 51.2 L/min, New Pressure ≈ 15 625 psi

**Worked Example 2 – Increase flow**  
12 mm → 14 mm plungers, was 15 000 psi @ 50 L/min  
→ New Flow ≈ 68 L/min, New Pressure ≈ 11 030 psi

Always re-verify component ratings and rupture disc after change.

## A.3 Application Snapshot (from Chapter 7 examples)

| Task | Typical Pressure Band | Flow Priority | Notes |
|------|-----------------------|---------------|-------|
| Surface / coating removal | High (≈15–20k+ psi) | Moderate | Strong reaction-force control |
| Tube bundle (standard) | 10–15k psi | High | AWD mandatory (MCR-019/020) |
| UHP creeping hose / 40k | 30–40k+ psi | Lower flow, high energy | Level 3 only (MCR-034) |
| Multi-gun work | Medium–high | High total flow | Coordination critical (WOMA-style) |
| Automated / robotic | Match tooling design | Match tooling design | Sensor/interlock test (MCR-021) |

## A.4 Post-Selection Checklist (existing MCR only)

- [ ] Reaction force within MCR-016 for named operators
- [ ] Rupture disc correctly rated and spare on unit (MCR-009)
- [ ] Dump system functional and operator-controlled (MCR-010)
- [ ] Hose/fitting MAWP ≥ planned pressure (MCR-001–008)
- [ ] Competency match confirmed (MCR-030 / 034)
- [ ] Exclusion zone sized per MCR-031
- [ ] Pre-use inspection time protected (MCR-023/024)

## A.5 Gaps

Model-specific min/max plunger sizes and exact performance curves → manufacturer data only. Not restated here.

**End of Appendix A**
