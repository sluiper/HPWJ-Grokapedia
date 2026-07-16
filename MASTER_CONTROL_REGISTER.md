# MASTER CONTROL REGISTER (Living Document) — v7.6 Fully Expanded

**This is the single source of truth for the entire Encyclopedia.**

Every named rule, numeric threshold, procedural requirement, and control from all sources and versions must be recorded here with clear sourcing and linkage to FMEA where applicable.

**Latest Update (16 July 2026):** Expanded with new controls from Chapters 5, 6, 9, 11, 12 and the UHP Creeping Hose section (7.17). Now 38 rules covering the full operational lifecycle.

## How to Use
- Add new rows immediately when a gap, new manufacturer requirement, clinical lesson, or incident learning is identified.
- Update Status column as content is drafted or controls are implemented.
- Never remove rows — only mark as superseded if truly replaced by a stronger, documented control.
- Every operational procedure, checklist, and training module must map back to relevant MCR items.

## Status Legend
- **Visible** = Explicitly stated at outline or chapter level
- **Drafting** = Will be expanded at full chapter depth
- **Added** = New in current version (v7.6)
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
| MCR-001 | Hose Life Management | Flex lances and shotgun whip hoses: maximum 2 years from date of manufacture or receipt. All other high-pressure hoses: maximum 4 years from date of manufacture or receipt. | Sec18; WJTA | Visible | Mandatory retirement. |
| MCR-002 | Hose Testing | Annual third-party pressure/proof testing mandatory in addition to visual. | Sec18; WJTA | Visible | ~7% fail visual-only. |
| MCR-003 | Hose Colour Coding & Marking | Permanent MAWP marking + colour coding visible from 2 ft matched to system pressure. | Sec18; Ch7 | Visible | |
| MCR-004 | Hose Reject Criteria | Reject on exposed braid, bulging, cuts to reinforcement, kinks, weepage, damaged fittings, exceeded life, missing marking. | Sec18; Ch7 | Visible | |
| MCR-005 | Hose Bend Radius & Handling | Never exceed min bend radius. Support weight; never drag by coupling. | Sec18; Ch7 | Visible | |
| MCR-006 | Whip Checks | Both sides of every HP connection. Correct WLL. Inspect every use. Prefer HPWJ-rated. | Sec18; Ch7 | Visible | |
| MCR-007 | Quick-Connect Couplings | Prefer screw/face-seal in high-movement. Inspect latches. Never where rotation likely. | Sec18; Ch7 | Visible | RPN 180 |
| MCR-008 | Type M Connections | 3.5–5 full threads. Clean cone/seat, clear weep holes. | Sec18 | Visible | |
| MCR-009 | Rupture Disc | Correct rating. Single-use only. Spare on unit. Tag date/rating. | Ch7; Sec20 | Visible | Never reuse. |
| MCR-010 | Pressure Relief / Dump | Operator-controlled dump system. Tested every pre-use. | Ch7; Sec20 | Visible | Non-negotiable. |
| MCR-011 | Pump Unattended | Never leave pump running unattended. | Ch7 | Visible | |
| MCR-012 | NPSH Margin | NPSHa ≥ NPSHr + 0.5–1.0 bar. Critical in KSA heat. | Ch7; Sec16 | Visible | |
| MCR-013 | Inlet Filtration | Multi-stage (final 10–50 µm typical). Monitor dP. | Ch7 | Visible | |
| MCR-014 | Pump Pre-Use Foundation | Level, chocked, grounded, guards, fluids, gauges, extinguisher, rupture disc. | Ch7 | Visible | |
| MCR-015 | Plunger Changes | Re-verify all ratings and rupture disc after change. | Ch7 | Visible | |
| MCR-016 | Reaction Force (Three Additive) | ≤250 N AND ≤1/3 body weight AND barrel geometry prevents jet over own feet/legs. All three required. | Ch7; Sec16 | Visible | RPN 180 |
| MCR-017 | Reaction Force Formulas | Imperial ≈ 0.052 × Q(GPM) × √P(psi); Metric ≈ 0.745 × Q(L/min) × √P(bar) | Sec16 | Visible | |
| MCR-018 | Nozzle Wear | 20–60 h typical. Pin gauge. Reject on pitting. | Ch7 | Visible | |
| MCR-019 | Flex Lance AWD | Mandatory correct AWD installation for all flex lance work. | Ch7; Sec20 | Visible | |
| MCR-020 | Flex Lance Back-Out Prevention | AWD + communication + reaction force. Never bypass. | Sec20 | Visible | RPN 200 |
| MCR-021 | Automated Tooling Safety | Pre-use test sensors/auto-shut-off. Clear zoning. Never bypass. | Ch7; Sec20 | Visible | |
| MCR-022 | Nozzle Thrust Direction | Correct forward thrust for tube/pipe. Verify before insertion. | Ch7 | Visible | |
| MCR-023 | Pre-Use Inspection Mandatory | Full documented inspection before every use. No excuses. | Ch7; Sec20 | Visible | RPN 210 |
| MCR-024 | Supervisor Pre-Use Verification | Supervisor spot-checks required. | Ch7; Sec20 | Visible | |
| MCR-025 | Communication Protocol | Clear radio/hand signals. Pre-job briefing. Stop-work on failure. | Ch6; Ch8 | Visible | |
| MCR-026 | Pump LOTO & Isolation | Full LOTO + try-out before maintenance or entry into danger zones. | Ch6 | Visible | |
| MCR-027 | Site Barricading & Exclusion Zones | Physical barricading + pressure-appropriate exclusion zone mandatory before pressurising. | Ch5 | Visible | |
| MCR-028 | SIMOPS Coordination | Daily SIMOPS meeting + clear zoning + hot-work controls when interfaces exist. | Ch6; Ch8 | Visible | RPN 200 |
| MCR-029 | Water Hammer Prevention | Slow valve operation, correct sequence, never slam valves. | Sec16 | Visible | |
| MCR-030 | Training & Competency Link | All personnel trained and assessed against this Register. | Ch13 | Visible | |
| MCR-031 | Exclusion Zone Sizing | 7.5–10 m ≤10k psi; 10–15 m 10–20k; 15–25 m+ UHP/40k. Adjust for jet direction and whip. | Ch5 | Added | |
| MCR-032 | Lightning Stop-Work | Stop outdoor work if thunder/lightning. 30 min wait after last thunder. | Ch5 | Added | |
| MCR-033 | Heat Stress Controls | Mandatory work/rest/hydration/shade in high ambient temperatures (KSA). | Ch5; Ch10 | Added | |
| MCR-034 | UHP Creeping Hose Controls | Level 3 operators only. AWD mandatory + verified. Vacuum at outlet. Expanded exclusion. No quick-connects in high-movement run. | Ch7.17 | Added | Critical for tube bundles. |
| MCR-035 | Post-Job Care & Records | Depressurise fully, inspect, clean, store correctly, complete all records before leaving site. | Ch11 | Added | |
| MCR-036 | Supervisor Accountability | Supervisor accountable for competency verification, pre-use quality, SIMOPS, and stop-work authority. | Ch12 | Added | |
| MCR-037 | Controlled Shutdown Sequence | Operator-controlled pressure reduction → confirm zero → secure → decontaminate → post-job inspection → records. | Ch11 | Added | |
| MCR-038 | Never Rules Enforcement | All Never Rules in Chapter 9 are absolute. Violation requires immediate stop and investigation. | Ch9 | Added | |

**Maintenance Note:** Living document. Update promptly after any incident, near-miss, equipment change or new guidance. Link to FMEA. All training and procedures must demonstrate compliance.

**Total Active Controls: 38**