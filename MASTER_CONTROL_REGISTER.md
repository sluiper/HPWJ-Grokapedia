# MASTER CONTROL REGISTER (Living Document) — v8.4

**This is the single source of truth for the entire Encyclopedia.**

Every named rule, numeric threshold, procedural requirement, and control from all sources and versions must be recorded here with clear sourcing and linkage to FMEA where applicable.

**Latest Update (16 July 2026):** Section 27 Lessons Learned merged to main after clean Claude verification (zero P0/P1). MCR-061 to MCR-065 added as Drafting (process rules – remain Drafting until first live exercise or explicit human promotion). Total now 65 rules (52 Visible + 13 Drafting). Section 23 Marine rows (053–060) also remain Drafting.

## How to Use
- Add new rows immediately when a gap, new manufacturer requirement, clinical lesson, or incident learning is identified.
- Update Status column as content is drafted or controls are implemented.
- Never remove rows — only mark as superseded if truly replaced by a stronger, documented control.
- Every operational procedure, checklist, and training module must map back to relevant MCR items.

## Status Legend
- **Visible** = Explicitly stated at outline or chapter level
- **Drafting** = Will be expanded at full chapter depth / proposed, awaiting final review & human gate
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
| MCR-001 | Hose Life Management | Flex lances and shotgun whip hoses: maximum 2 years from date of manufacture or receipt. All other high-pressure hoses: maximum 4 years from date of manufacture or receipt. | Sec18; WJTA; SABIC; OPS-P-019 | Visible | Mandatory retirement. |
| MCR-002 | Hose Testing | Annual third-party pressure/proof testing mandatory in addition to visual. | Sec18; WJTA; SABIC; OPS-P-019 | Visible | ~7% fail visual-only. |
| MCR-003 | Hose Colour Coding & Marking | Permanent MAWP marking + colour coding visible from 2 ft matched to system pressure. | Sec18; Ch7 | Visible | |
| MCR-004 | Hose Reject Criteria | Reject on exposed braid, bulging, cuts to reinforcement, kinks, weepage, damaged fittings, exceeded life, missing marking. | Sec18; Ch7; SABIC; OPS-P-019 | Visible | |
| MCR-005 | Hose Bend Radius & Handling | Never exceed min bend radius. Support weight; never drag by coupling. | Sec18; Ch7 | Visible | |
| MCR-006 | Whip Checks | Both sides of every HP connection. Correct WLL. Inspect every use. Prefer HPWJ-rated. | Sec18; Ch7; SABIC; OPS-P-019 | Visible | |
| MCR-007 | Quick-Connect Couplings | Prefer screw/face-seal in high-movement. Inspect latches. Never where rotation likely. No quick-connects on high-pressure hoses. | Sec18; Ch7; SABIC; OPS-P-019 | Visible | RPN 180 |
| MCR-008 | Type M Connections | 3.5–5 full threads. Clean cone/seat, clear weep holes. | Sec18 | Visible | |
| MCR-009 | Rupture Disc | Correct rating. Single-use only. Spare on unit. Tag date/rating. Anabeeb: ≤1.2× MAWP of lowest-rated component. | Ch7; Sec20; SABIC; OPS-P-019 §6.2 | Visible | Never reuse. See MCR-048. |
| MCR-010 | Pressure Relief / Dump | Operator-controlled dump system (failsafe / dead-man). Tested every pre-use. | Ch7; Sec20; SABIC; OPS-P-019 | Visible | Non-negotiable. |
| MCR-011 | Pump Unattended | Never leave pump running unattended. | Ch7; SABIC; OPS-P-019 | Visible | |
| MCR-012 | NPSH Margin | NPSHa ≥ NPSHr + 0.5–1.0 bar. Critical in KSA heat. | Ch7; Sec16 | Visible | |
| MCR-013 | Inlet Filtration | Multi-stage (final 10–50 µm typical). Monitor dP. Clean water source. | Ch7; SABIC; OPS-P-019 | Visible | |
| MCR-014 | Pump Pre-Use Foundation | Level, chocked, grounded, guards, fluids, gauges, extinguisher, rupture disc. | Ch7; OPS-P-019 | Visible | |
| MCR-015 | Plunger Changes | Re-verify all ratings and rupture disc after change. | Ch7 | Visible | |
| MCR-016 | Reaction Force (Three Additive) | ≤250 N AND ≤1/3 body weight AND barrel geometry prevents jet over own feet/legs. All three required. | Ch7; Sec16; SABIC; YANSAB; OPS-P-019 | Visible | RPN 180. Formula: 0.052 × GPM × √psi (lbf). Extended underwater by MCR-054. |
| MCR-017 | Reaction Force Formulas | Imperial ≈ 0.052 × Q(GPM) × √P(psi); Metric ≈ 0.745 × Q(L/min) × √P(bar) | Sec16; SABIC; OPS-P-019 | Visible | |
| MCR-018 | Nozzle Wear | 20–60 h typical. Pin gauge. Reject on pitting. | Ch7; OPS-P-019 | Visible | |
| MCR-019 | Flex Lance AWD | Mandatory correct AWD installation for all flex lance work. | Ch7; Sec20; SABIC; OPS-P-019 | Visible | |
| MCR-020 | Flex Lance Back-Out Prevention | AWD + communication + reaction force. Never bypass. Flexible lance without catcher/AWD = Not Permitted. | Sec20; SABIC Table 4.1; OPS-P-019 | Visible | RPN 200 |
| MCR-021 | Automated Tooling Safety | Pre-use test sensors/auto-shut-off. Clear zoning. Never bypass. Prefer automated methods (2XLTC, 3XLTC, IBC, OBC, Bundle Blaster, 3D). | Ch7; Sec20; SABIC; OPS-P-019 §8 | Visible | |
| MCR-022 | Nozzle Thrust Direction | Correct forward thrust for tube/pipe. Verify before insertion. Stinger length > pipe ID. | Ch7; OPS-P-019 | Visible | |
| MCR-023 | Pre-Use Inspection Mandatory | Full documented inspection (ATT-6 / Anabeeb daily checklist) before every use and each shift. Pre-requisite for permit. | Ch7; Sec20; SABIC; OPS-P-019 | Visible | RPN 210 |
| MCR-024 | Supervisor Pre-Use Verification | Supervisor spot-checks required. Authorising Person / Project in Charge verifies. | Ch7; Sec20; SABIC; OPS-P-019 | Visible | |
| MCR-025 | Communication Protocol | Clear radio/hand signals. Pre-job briefing. Continuous line-of-sight or equivalent. Stop-work on failure. No blind spots. Dedicated emergency-stop person when LOS lost. | Ch6; Ch8; SABIC; OPS-P-019 | Visible | |
| MCR-026 | Pump LOTO & Isolation | Full LOTO + try-out before maintenance or entry into danger zones. | Ch6; SABIC | Visible | |
| MCR-027 | Site Barricading & Exclusion Zones | Physical barricading + pressure-appropriate exclusion zone. SABIC min 6 m; Anabeeb unauthorised persons excluded to 10 m. | Ch5; SABIC; OPS-P-019 | Visible | |
| MCR-028 | SIMOPS Coordination | Daily SIMOPS meeting + clear zoning + hot-work controls when interfaces exist. | Ch6; Ch8 | Visible | RPN 200 |
| MCR-029 | Water Hammer Prevention | Slow valve operation, correct sequence, never slam valves. | Sec16 | Visible | |
| MCR-030 | Training & Competency Link | All personnel trained and assessed against this Register. Method-specific. Anabeeb Training Dept certification verified by Supervisor. | Ch13; OPS-P-019 §7 | Visible | |
| MCR-031 | Exclusion Zone Sizing | 7.5–10 m ≤10k psi; 10–15 m 10–20k; 15–25 m+ UHP/40k. Adjust for jet direction and whip. SABIC baseline 6 m; Anabeeb 10 m for unauthorised. | Ch5; SABIC; OPS-P-019 | Visible | |
| MCR-032 | Lightning Stop-Work | Stop outdoor work if thunder/lightning. 30 min wait after last thunder. | Ch5 | Visible | |
| MCR-033 | Heat Stress Controls | Mandatory work/rest/hydration/shade in high ambient temperatures (KSA). Full PPE + rotation. Consider Safetech Air Comfort (18 °C inside suit). | Ch5; Ch8; Ch10; SABIC; Safetech | Visible | |
| MCR-034 | UHP Creeping Hose Controls | Level 3 operators only. AWD mandatory + verified. Vacuum at outlet. Expanded exclusion. No quick-connects in high-movement run. | Ch7.17 | Visible | Critical for tube bundles. |
| MCR-035 | Post-Job Care & Records | Depressurise fully, inspect, clean, store correctly, complete all records before leaving site. | Ch11 | Visible | |
| MCR-036 | Supervisor Accountability | Supervisor accountable for competency verification, pre-use quality, SIMOPS, and stop-work authority. Project Manager overall responsibility cannot be delegated (OPS-P-019). | Ch12; SABIC; OPS-P-019 §6.1 | Visible | |
| MCR-037 | Controlled Shutdown Sequence | Operator-controlled pressure reduction → confirm zero → secure → decontaminate → post-job inspection → records. | Ch11 | Visible | |
| MCR-038 | Never Rules Enforcement | All Never Rules in Chapter 9 (SABIC Do’s/Don’ts + OPS-P-019) are absolute. Violation requires immediate stop and investigation. No shortcuts, no sub-standard equipment. | Ch9; SABIC; OPS-P-019 | Visible | |
| MCR-039 | Hierarchy of Methods | Automated / mechanized methods with operators outside jetting area shall be selected wherever reasonably practicable. Manual reaction-force work requires elevated approval. Flexible lance without AWD = Not Permitted. | SABIC 2.1; OPS-P-019 §8; Ch8 | Visible | Core selection control. Elevated underwater by MCR-059. |
| MCR-040 | Minimum Team Size (SABIC baseline) | Minimum two competent persons for any pressurised work. Lone working prohibited. Additional members for remote dump, enclosures, UHP, confined space. | SABIC 2.2.4, 2.7.3–4; Ch8 | Visible | See MCR-047 for Anabeeb stricter rule. |
| MCR-041 | HPWJ Authorising Person | End-User Manager appoints trained Authorising Person who reviews Technical Specification, ensures approved contractor, leads JSA, supervises, and verifies controls before permit. | SABIC 2.2.1; Ch8 | Visible | Client-specific gate. |
| MCR-042 | Method-Specific Certification | TQCP (or equivalent) / Anabeeb Training Dept for the specific method/technique and pressure class + experience + refresh. Automatic qualification does not authorise manual. | SABIC 2.3.4; OPS-P-019 §7; Ch8; Ch13 | Visible | |
| MCR-043 | Medical Alert Card | All operators engaged in HPWJ tasks shall carry an immediately accessible waterproof Medical Alert Card (Anabeeb form OPS0080804 or equivalent). | SABIC 2.3.7; OPS-P-019; Ch10 | Visible | Extended underwater by MCR-058. |
| MCR-044 | Lance / Gun Length | Lances minimum 1.2 m (48 in) from trigger/butt to nozzle tip. Shorter only with double trigger + extra hand protection + special RA. Flexible hoses require rigid leader/stinger. | SABIC; OPS-P-019 §9; Ch8 | Visible | |
| MCR-045 | Safety Shroud / Burst Sleeve at Connection | Safety shroud / Burst Protection Sleeve minimum 6 ft at hose-to-gun/lance connection, tested and verified. Required for UHP. | SABIC Checklist; OPS-P-019 §9; Awareness PPT | Visible | |
| MCR-046 | Maximum System Pressure | Maximum allowable pressure for any Anabeeb HPWJ activity = 40 000 psi (2 759 bar). No work above this. | OPS-P-019 §3.8 | Visible | Absolute ceiling. |
| MCR-047 | Anabeeb Minimum Team Size | Anabeeb HPWJ teams shall consist of minimum **three** competent persons. One dedicated to emergency stop/dump when line of sight between lance and pump is lost. | OPS-P-019 §6.4 | Visible | Stricter than SABIC 2-person baseline. Higher manning expected for wet work. |
| MCR-048 | Rupture Disc Rating Factor | Rupture disc shall be rated **no greater than 1.2 times** the MAWP of the lowest-rated component in the system. | OPS-P-019 §6.2 | Visible | |
| MCR-049 | Manual Operator Experience | Manual HPWJ operators shall have minimum **two years continuous** relevant experience, recorded on training card, in addition to method-specific certification. Management approval required before manual lancing/gun work. | OPS-P-019 §9 | Visible | |
| MCR-050 | Shotgun Pressure / Orifice Limit | Hand-held shotgunning shall not be performed above **10 000 psi (680 bar)** with nozzle orifice larger than **1.6 mm**. Reaction force ≤250 N absolute. | OPS-P-019 §9 | Visible | |
| MCR-051 | Unauthorised Person Exclusion | No unauthorised person within **10 metres** of operating Anabeeb HPWJ equipment. System shall be depressurised on breach. | OPS-P-019 §9 | Visible | |
| MCR-052 | Lance Tip Marking | Lance/hose shall be clearly marked with paint or tape **no closer than 600 mm** from the nozzle tip to warn of impending exit. | OPS-P-019 §9 | Visible | |
| MCR-053 | Diver HPWJ Authorisation | Only divers trained and certified for underwater HP/UHP jetting per IMCA D049 (or equivalent company standard) may operate. Surface support must hold concurrent competence. | IMCA D049 Rev 1.2; Anabeeb OPS-P-019 principle; Sec23 | Drafting | Priority for any marine work. |
| MCR-054 | Underwater Reaction Force Control | Reaction force limits remain the three additive controls (≤250 N, ≤1/3 body weight, geometry). In water buoyancy reduces effective weight → tighter practical limit. Dedicated standby diver + surface dump control mandatory. | IMCA D049 principles; MCR-016 extension; Sec23 | Drafting | Higher RPN underwater. |
| MCR-055 | Hose Tethering & Securing (Wet) | All high-pressure hoses must be securely tied off / restrained at multiple points to prevent hose whip or entanglement of diver. Never free-floating. | IMCA D049; IMCA SF 09/17 extract; Sec23 | Drafting | Direct from D049 guidance. |
| MCR-056 | Dump / Dead-Man System (Underwater) | Fail-safe dump system must be operable by both the diver (if equipped) and surface tender. Continuous communication + pre-agreed emergency dump signal. | IMCA D049; general diving safety; Sec23 | Drafting | Non-negotiable. |
| MCR-057 | Exclusion of Non-Essential Personnel | No non-essential personnel (including supervisors) inside the immediate work area or line of fire. Barriers + positive communication. Dock-bottom / moon-pool / confined wet areas treated as high-risk. | IMCA SF 18/20; IMCA D049; Sec23 | Drafting | Direct lesson from SF 18/20. |
| MCR-058 | Medical Alert + DMAC | All divers engaged in HPWJ carry Medical Alert Card + awareness of DMAC recommendations for high-pressure water jet injuries. Immediate surface medical support must know the injury mechanism. | IMCA D049 Appendix 1 (DMAC); MCR-043 extension; Sec23 | Drafting | Critical. |
| MCR-059 | Maximum Pressure for Diver-Held / Method Hierarchy Elevation | Follow IMCA D049 / company limit. Typical public practice for diver-held is lower than land UHP (often ≤10–15k psi class unless specially engineered). Anabeeb 40k psi ceiling still applies but method selection hierarchy (prefer automated/ROV) is stricter underwater. | IMCA D049; MCR-046; MCR-039; Sec23 | Drafting | Hierarchy of methods elevated. |
| MCR-060 | Cavitation Blaster / Special Tools | Cavitation tools have additional injury modes (see IMCA SF 06/07). Require specific risk assessment and training beyond standard HPWJ. | IMCA D049 Appendix 5; SF 06/07; Sec23 | Drafting | |
| MCR-061 | Living Lessons Learned Register | A single living register of lessons shall be maintained. Every entry must map to one or more MCR controls and, where relevant, an FMEA mode. | Sec27; continuous improvement principle | Drafting | Process control. Remains Drafting until first live exercise or explicit human promotion. |
| MCR-062 | 30-Day Incident-to-Lesson Cycle | Any Anabeeb HPWJ-related near-miss, incident, or significant observation shall be converted into a structured lesson entry within 30 calendar days of the event (or of the investigation closing). Delay beyond 30 days requires written justification from the QHSSE Manager. | Sec27; formalises existing Section 25 convention | Drafting | Process control. Remains Drafting until first live exercise or explicit human promotion. |
| MCR-063 | Anonymised Real Incident Capture | Real Anabeeb events shall be recorded in anonymised form that preserves the technical and human-factor learning while protecting individuals and commercial sensitivity. Documented public cases remain fully attributed. | Sec27; Sec25 discipline | Drafting | Process control. |
| MCR-064 | Training Integration of Lessons | Every new lesson that maps to an RPN > 150 control, or that reveals a previously unrecognised failure mode, shall be incorporated into the next scheduled ATC HPWJ training cycle (or earlier if critical). | Sec27; Ch13 | Drafting | Process control. |
| MCR-065 | Management Review of Lessons | The QHSSE Manager shall review the Lessons Learned register at least quarterly and after any serious event. The review shall decide whether any MCR row needs strengthening, any procedure needs amendment, or any additional training is required. | Sec27; Ch15 continuous improvement | Drafting | Process control. |

**Maintenance Note:** Living document. Update promptly after any incident, near-miss, equipment change or new guidance. Link to FMEA. All training and procedures must demonstrate compliance. Where Anabeeb OPS-P-019 is stricter than SABIC or international standards, Anabeeb rule governs Anabeeb operations.

**Total Active Controls: 65** (52 Visible + 13 Drafting)
