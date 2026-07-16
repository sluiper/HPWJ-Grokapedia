# MASTER CONTROL REGISTER (Living Document) — v8.1

**This is the single source of truth for the entire Encyclopedia.**

Every named rule, numeric threshold, procedural requirement, and control from all sources and versions must be recorded here with clear sourcing and linkage to FMEA where applicable.

**Latest Update (16 July 2026):** Expanded with full SABIC OMS Attachment 8.2 controls (mandatory for KSA). New rows MCR-039 to MCR-045. Total now 45 rules covering the full operational lifecycle + client-specific gates.

## How to Use
- Add new rows immediately when a gap, new manufacturer requirement, clinical lesson, or incident learning is identified.
- Update Status column as content is drafted or controls are implemented.
- Never remove rows — only mark as superseded if truly replaced by a stronger, documented control.
- Every operational procedure, checklist, and training module must map back to relevant MCR items.

## Status Legend
- **Visible** = Explicitly stated at outline or chapter level
- **Drafting** = Will be expanded at full chapter depth
- **Added** = New in current version
- **Priority** = High RPN item from FMEA requiring focused attention

## High-Priority Controls (FMEA RPN > 150 — Immediate Focus)
- Inadequate Pre-Use Inspection (RPN 210) — MCR-023
- Flex Lance Back-Out / Loss of Control (RPN 200) — MCR-020
- Poor SIMOPS Coordination (RPN 200) — MCR-028
- Quick-Connect Disconnection Under Pressure (RPN 180) — MCR-007
- Loss of Control Due to Excessive Reaction Force (RPN 180) — MCR-016

## Master Control Register — Detailed Rules & Thresholds

| ID | Topic | Rule / Number / Threshold | Source(s) | Status | Notes / FMEA Link |
|----|-------|---------------------------|-----------|--------|-------------------|
| MCR-001 | Hose Life Management | Flex lances and shotgun whip hoses: maximum 2 years from date of manufacture or receipt. All other high-pressure hoses: maximum 4 years from date of manufacture or receipt. | Sec18; WJTA; SABIC Checklist | Visible | Mandatory retirement. |
| MCR-002 | Hose Testing | Annual third-party pressure/proof testing mandatory in addition to visual. | Sec18; WJTA; SABIC | Visible | ~7% fail visual-only. |
| MCR-003 | Hose Colour Coding & Marking | Permanent MAWP marking + colour coding visible from 2 ft matched to system pressure. | Sec18; Ch7 | Visible | |
| MCR-004 | Hose Reject Criteria | Reject on exposed braid, bulging, cuts to reinforcement, kinks, weepage, damaged fittings, exceeded life, missing marking. | Sec18; Ch7; SABIC Checklist | Visible | |
| MCR-005 | Hose Bend Radius & Handling | Never exceed min bend radius. Support weight; never drag by coupling. | Sec18; Ch7 | Visible | |
| MCR-006 | Whip Checks | Both sides of every HP connection. Correct WLL. Inspect every use. Prefer HPWJ-rated. | Sec18; Ch7; SABIC | Visible | |
| MCR-007 | Quick-Connect Couplings | Prefer screw/face-seal in high-movement. Inspect latches. Never where rotation likely. No quick-connects on high-pressure hoses (SABIC). | Sec18; Ch7; SABIC Checklist 14 | Visible | RPN 180 |
| MCR-008 | Type M Connections | 3.5–5 full threads. Clean cone/seat, clear weep holes. | Sec18 | Visible | |
| MCR-009 | Rupture Disc | Correct rating. Single-use only. Spare on unit. Tag date/rating. | Ch7; Sec20; SABIC | Visible | Never reuse. |
| MCR-010 | Pressure Relief / Dump | Operator-controlled dump system (failsafe / dead-man). Tested every pre-use. | Ch7; Sec20; SABIC | Visible | Non-negotiable. |
| MCR-011 | Pump Unattended | Never leave pump running unattended. | Ch7; SABIC Do’s/Don’ts | Visible | |
| MCR-012 | NPSH Margin | NPSHa ≥ NPSHr + 0.5–1.0 bar. Critical in KSA heat. | Ch7; Sec16 | Visible | |
| MCR-013 | Inlet Filtration | Multi-stage (final 10–50 µm typical). Monitor dP. Clean water source. | Ch7; SABIC | Visible | |
| MCR-014 | Pump Pre-Use Foundation | Level, chocked, grounded, guards, fluids, gauges, extinguisher, rupture disc. | Ch7 | Visible | |
| MCR-015 | Plunger Changes | Re-verify all ratings and rupture disc after change. | Ch7 | Visible | |
| MCR-016 | Reaction Force (Three Additive) | ≤250 N AND ≤1/3 body weight AND barrel geometry prevents jet over own feet/legs. All three required. | Ch7; Sec16; SABIC 2.4.5.2; YANSAB JSA | Visible | RPN 180. Formula: 0.052 × GPM × √psi (lbf) |
| MCR-017 | Reaction Force Formulas | Imperial ≈ 0.052 × Q(GPM) × √P(psi); Metric ≈ 0.745 × Q(L/min) × √P(bar) | Sec16; SABIC | Visible | |
| MCR-018 | Nozzle Wear | 20–60 h typical. Pin gauge. Reject on pitting. | Ch7 | Visible | |
| MCR-019 | Flex Lance AWD | Mandatory correct AWD installation for all flex lance work. | Ch7; Sec20; SABIC | Visible | |
| MCR-020 | Flex Lance Back-Out Prevention | AWD + communication + reaction force. Never bypass. Flexible lance without catcher/AWD = Not Permitted (SABIC). | Sec20; SABIC Table 4.1 | Visible | RPN 200 |
| MCR-021 | Automated Tooling Safety | Pre-use test sensors/auto-shut-off. Clear zoning. Never bypass. Prefer automated methods (SABIC hierarchy). | Ch7; Sec20; SABIC 2.1 | Visible | |
| MCR-022 | Nozzle Thrust Direction | Correct forward thrust for tube/pipe. Verify before insertion. | Ch7 | Visible | |
| MCR-023 | Pre-Use Inspection Mandatory | Full documented inspection (ATT-6) before every use. Pre-requisite for HPWJ Work Permit. No excuses. | Ch7; Sec20; SABIC 2.6.8 | Visible | RPN 210 |
| MCR-024 | Supervisor Pre-Use Verification | Supervisor spot-checks required. Authorising Person verifies. | Ch7; Sec20; SABIC | Visible | |
| MCR-025 | Communication Protocol | Clear radio/hand signals. Pre-job briefing. Continuous line-of-sight or equivalent. Stop-work on failure. No blind spots. | Ch6; Ch8; SABIC 2.7.2 | Visible | |
| MCR-026 | Pump LOTO & Isolation | Full LOTO + try-out before maintenance or entry into danger zones. | Ch6; SABIC | Visible | |
| MCR-027 | Site Barricading & Exclusion Zones | Physical barricading + pressure-appropriate exclusion zone mandatory before pressurising. SABIC minimum 6 m (or robust ≥2 m screen not closer than 3 m if agreed). | Ch5; SABIC 2.6.11 | Visible | |
| MCR-028 | SIMOPS Coordination | Daily SIMOPS meeting + clear zoning + hot-work controls when interfaces exist. | Ch6; Ch8 | Visible | RPN 200 |
| MCR-029 | Water Hammer Prevention | Slow valve operation, correct sequence, never slam valves. | Sec16 | Visible | |
| MCR-030 | Training & Competency Link | All personnel trained and assessed against this Register. Method-specific. | Ch13 | Visible | |
| MCR-031 | Exclusion Zone Sizing | 7.5–10 m ≤10k psi; 10–15 m 10–20k; 15–25 m+ UHP/40k. Adjust for jet direction and whip. SABIC baseline 6 m minimum. | Ch5; SABIC | Visible | |
| MCR-032 | Lightning Stop-Work | Stop outdoor work if thunder/lightning. 30 min wait after last thunder. | Ch5 | Visible | |
| MCR-033 | Heat Stress Controls | Mandatory work/rest/hydration/shade in high ambient temperatures (KSA). Full PPE + rotation. | Ch5; Ch8; Ch10; SABIC 2.4.5.4 | Visible | |
| MCR-034 | UHP Creeping Hose Controls | Level 3 operators only. AWD mandatory + verified. Vacuum at outlet. Expanded exclusion. No quick-connects in high-movement run. | Ch7.17 | Visible | Critical for tube bundles. |
| MCR-035 | Post-Job Care & Records | Depressurise fully, inspect, clean, store correctly, complete all records before leaving site. | Ch11 | Visible | |
| MCR-036 | Supervisor Accountability | Supervisor accountable for competency verification, pre-use quality, SIMOPS, and stop-work authority. HPWJ Supervisor is primary liaison with Permit Issuer. | Ch12; SABIC 2.7 | Visible | |
| MCR-037 | Controlled Shutdown Sequence | Operator-controlled pressure reduction → confirm zero → secure → decontaminate → post-job inspection → records. | Ch11 | Visible | |
| MCR-038 | Never Rules Enforcement | All Never Rules in Chapter 9 (and SABIC Do’s/Don’ts) are absolute. Violation requires immediate stop and investigation. | Ch9; SABIC ATT-5 | Visible | |
| MCR-039 | Hierarchy of Methods | Automated / mechanized methods with operators outside jetting area shall be selected wherever reasonably practicable. Manual reaction-force work requires elevated approval. Flexible lance without AWD = Not Permitted. | SABIC 2.1 Table 4.1; Ch8 | Added | Core selection control. |
| MCR-040 | Minimum Team Size | Minimum two competent persons for any pressurised work. Lone working prohibited. Additional members required for remote dump, enclosures, UHP, confined space. | SABIC 2.2.4, 2.7.3–4; Ch8 | Added | |
| MCR-041 | HPWJ Authorising Person | End-User Manager appoints trained Authorising Person who reviews Technical Specification (ATT-1), ensures approved contractor, leads JSA, supervises, and verifies controls before permit. | SABIC 2.2.1, 2.7.8; Ch8 | Added | Client-specific gate. |
| MCR-042 | Method-Specific Certification | TQCP (or equivalent) for the specific method/technique and pressure class + minimum 1 year similar experience + 2-year refresh. Stamped in passport. Automatic qualification does not authorise manual. | SABIC 2.3.4; Ch8; Ch13 | Added | |
| MCR-043 | Medical Alert Card | All operators engaged in HPWJ tasks shall carry an immediately accessible waterproof Medical Alert Card outlining the nature of high-pressure injection injury. | SABIC 2.3.7; Checklist 31; Ch10 | Added | |
| MCR-044 | Lance / Gun Length | Lances minimum 1.2 m (48 in) from trigger to nozzle tip. Shorter lances only with double trigger + additional hand protection. Flexible hoses require ≥300 mm stainless rigid leader at nozzle end. | SABIC 2.6.5; Checklist 17; Awareness PPT | Added | |
| MCR-045 | Safety Shroud at Connection | Safety shroud minimum 6 ft long at the point where hose connects to gun/lance, tested and verified to protect operator if connection or hose fails. | SABIC Checklist 16; Awareness PPT | Added | |

**Maintenance Note:** Living document. Update promptly after any incident, near-miss, equipment change or new guidance. Link to FMEA. All training and procedures must demonstrate compliance.

**Total Active Controls: 45**
