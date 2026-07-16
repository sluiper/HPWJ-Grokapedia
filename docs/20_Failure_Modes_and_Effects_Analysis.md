# Section 20: Failure Modes & Effects Analysis (FMEA-style)

**Version 8.0 – Restored full detail + candidate site-hazard mode**

This section provides a structured Failure Modes and Effects Analysis (FMEA-style) for High Pressure Water Jetting systems. It identifies common failure modes, their causes, potential consequences, and recommended preventive/detective controls. It is designed to support risk assessments, training, and continuous improvement.

Each failure mode includes a simple risk rating and explicit links to relevant items in the **Master Control Register**.

**Risk Rating Legend**:
- **Severity (S)**: 1 (Minor) to 10 (Catastrophic)
- **Likelihood (L)**: 1 (Remote) to 10 (Almost certain)
- **Detection (D)**: 1 (Almost certain to detect) to 10 (Undetectable)
- **Risk Priority Number (RPN)** = S × L × D

**How to Use This FMEA**:
- High RPN items (>150) should be prioritized for additional engineering controls, training emphasis, or procedure improvements.
- After implementing controls, re-estimate the residual RPN to assess effectiveness.
- This document should be reviewed after any significant incident or near miss.

---

## Risk Matrix Interpretation

| Likelihood \ Severity | 1-3 (Low)     | 4-6 (Medium)   | 7-8 (High)     | 9-10 (Very High) |
|------------------------|---------------|----------------|----------------|------------------|
| **1-3 (Low)**          | Low           | Low            | Medium         | High             |
| **4-6 (Medium)**       | Low           | Medium         | High           | Very High        |
| **7-10 (High)**        | Medium        | High           | Very High      | Very High        |

**Interpretation Guidance**:
- **RPN < 100**: Monitor and maintain existing controls.
- **RPN 100–150**: Review and strengthen controls where possible.
- **RPN > 150**: High priority – consider additional engineering or procedural controls.

---

## Top Priority Failure Modes (RPN > 180)

1. **Inadequate Pre-Use Inspection** (RPN 210)
2. **Flex Lance Back-Out / Loss of Control** (RPN 200)
3. **Poor SIMOPS Coordination** (RPN 200)
4. **Quick-Connect Disconnection Under Pressure** (RPN 180)
5. **Loss of Control Due to Excessive Reaction Force** (RPN 180)

These five modes represent the greatest potential for serious injury or fatality based on current assessment.

---

## 20.1 Purpose and Scope

The goal of this FMEA is to:
- Identify credible failure modes in HPWJ equipment and operations
- Understand the potential effects on people, equipment, and operations
- Define practical controls to prevent or mitigate each failure
- Link controls directly to the Master Control Register
- Support the development of robust procedures, training, and maintenance strategies

This analysis draws from industry incident data, manufacturer experience, and operational lessons from major oil & gas contractors.

---

## NEW CANDIDATE MODE (Added 16 July 2026 – v8.0)

### 20.X Adjacent Excavation / Unprotected Opening Hazard (Site Hazard)

**Description**: Worker falls into an uncovered vertical pipe, pit, manhole, or floor opening while performing or supporting HPWJ work.

**Causes**:
- Failure to identify open vertical openings during site preparation
- Failure to cover, guard, or barricade openings inside or immediately adjacent to the exclusion zone
- Poor housekeeping or temporary removal of covers without control
- Inadequate lighting or visual marking of openings

**Consequences**:
- Fall from height / fall into confined space or pipe
- Serious injury or fatality (as documented in NIOSH CA/FACE 16CA001)
- Secondary injury if the person is still connected to or near energized jetting equipment

**Detection**:
- Site walkthrough and pre-start checklist specifically looking for openings
- Visual inspection of covers and barriers before pressurising

**Provisional Risk Rating**: S=9, L=4, D=5 → **RPN = 180** (High – provisional pending full scoring review)

**Recommended Controls**:
- Explicit identification of all open pits, vertical pipes, manholes, and floor openings during site preparation (Chapter 5)
- Physical covering, guarding, or robust barricading of every such opening inside or immediately adjacent to the HPWJ exclusion zone before work starts
- Inclusion of “openings controlled” as a mandatory item on the pre-start site verification checklist
- Clear stop-work if any cover is removed or barrier compromised during the job

**Linked Master Control Register Items (candidate)**: New MCR item recommended for “Openings / Vertical Hazards Control” under Site Preparation. Currently supported by expanded Chapter 5 requirements.

**Source / Trigger for Addition**: NIOSH CA/FACE 16CA001 (hydroblasting laborer fatality – fell into uncovered vertical pipe). This case is outside the previous equipment-centric FMEA scope and has been logged as a gap.

**Status**: Candidate row – full scoring and integration into main body pending next FMEA review cycle.

---

## 20.2 Pump-Related Failure Modes

### 20.2.1 Cavitation Damage

**Description**: Formation and violent collapse of vapour bubbles inside the pump due to low local pressure.

**Causes**:
- Inadequate NPSH (poor inlet conditions, long/restricted suction line, dirty filters)
- High water temperature (reduces NPSHa)
- High pump speed with marginal inlet conditions

**Consequences**:
- Rapid erosion of plungers, valves, and seats
- Loss of pump performance
- Increased vibration and noise
- Potential catastrophic pump failure if ignored

**Detection**:
- Characteristic "gravel" or "marbles" noise
- Increased vibration
- Gradual loss of pressure/flow
- Higher than normal power consumption

**Risk Rating**: S=8, L=6, D=4 → **RPN = 192** (High)

**Recommended Controls**:
- Maintain clean, short suction lines with adequate diameter
- Monitor inlet pressure and filter differential pressure
- Use cooler inlet water where possible in hot climates
- Reduce pump speed if NPSH margin is marginal
- Regular fluid analysis and internal inspection during maintenance

**Mitigation Effectiveness & Residual Risk**:
- Controls are generally effective if consistently applied. Residual risk remains if inlet water temperature is very high or filtration is neglected during peak summer conditions.

**Linked Master Control Register Items**: MCR-012, MCR-013

---

### 20.2.2 Rupture Disc Activation / Failure

**Description**: Rupture disc bursts due to overpressure or material degradation.

**Causes**:
- Blocked nozzle or line restriction
- Pump overspeed or malfunction
- Disc installed with incorrect rating
- Disc already weakened from previous activation or corrosion

**Consequences**:
- Sudden release of high-pressure water
- Potential injury to personnel nearby
- Loss of containment and environmental spill
- Equipment damage

**Detection**:
- Visual inspection of disc condition and tag
- Sudden pressure drop and water discharge
- Activation of secondary relief systems

**Risk Rating**: S=9, L=5, D=3 → **RPN = 135** (High)

**Recommended Controls**:
- Always use correctly rated discs matched to pump and system
- Replace disc after every activation (never reuse)
- Maintain spare discs on the unit
- Tag and record disc installation date and rating
- Inspect disc condition during every pre-use check

**Mitigation Effectiveness & Residual Risk**:
- Highly effective when replacement discipline is followed. Main residual risk comes from using incorrect or previously fired discs.

**Linked Master Control Register Items**: MCR-009

---

### 20.2.3 Overheating / Lubrication Failure (Power End)

**Description**: Failure of bearings, gears, or crossheads due to inadequate lubrication or cooling.

**Causes**:
- Low oil level or wrong oil type
- Blocked oil cooler or filter
- Extended operation at high load without adequate cooling
- Misalignment causing excessive friction

**Consequences**:
- Seizure of power end components
- Catastrophic pump damage
- Fire risk in extreme cases
- Unplanned downtime

**Detection**:
- Rising oil temperature
- Unusual noise or vibration from power end
- Low oil pressure alarm (if fitted)
- Visible oil leaks or discoloration

**Risk Rating**: S=8, L=4, D=5 → **RPN = 160** (High)

**Recommended Controls**:
- Daily oil level and condition checks
- Follow manufacturer oil change intervals strictly
- Monitor oil temperature during operation
- Ensure proper alignment during installation and after transport
- Use correct oil grade for ambient temperature

**Mitigation Effectiveness & Residual Risk**:
- Effective with disciplined maintenance. Residual risk increases during extended high-load operations in high ambient temperatures.

**Linked Master Control Register Items**: Ch7 pre-use fluids; Ch11 / Ch14 maintenance practices

---

### 20.2.4 Diesel Engine / Drive Failure

**Description**: Failure of the diesel engine or drive system powering the pump.

**Causes**:
- Fuel contamination or exhaustion
- Overheating
- Low oil pressure
- Air intake restriction (dust in KSA environment)
- Electrical or sensor faults

**Consequences**:
- Sudden loss of pumping capability mid-job
- Uncontrolled shutdown
- Potential safety issues if pressure cannot be maintained or relieved properly

**Detection**:
- Engine alarms and gauges
- Unusual engine noise or performance
- Visible smoke or fluid leaks

**Risk Rating**: S=6, L=5, D=3 → **RPN = 90** (Medium-High)

**Recommended Controls**:
- Pre-use engine checks (oil, coolant, fuel, air filter, DEF)
- Regular maintenance per manufacturer schedule
- Protection of air intake from dust in desert environments
- Clear emergency shutdown procedures

**Mitigation Effectiveness & Residual Risk**:
- Generally effective. Main residual risk comes from fuel quality issues or extreme dust conditions during shamal events.

**Linked Master Control Register Items**: Ch7 pre-use engine checks

---

### 20.2.5 Inlet Water Quality / Filtration Failure

**Description**: Inadequate filtration leading to abrasive or contaminated water entering the pump.

**Causes**:
- Dirty or missing inlet filters
- Poor source water quality
- Filter bypass or incorrect filter rating
- Failure to monitor filter differential pressure

**Consequences**:
- Accelerated wear on plungers, valves, and packing
- Increased risk of cavitation and internal damage
- Reduced pump life and performance

**Detection**:
- Rising filter differential pressure
- Visible contamination in inlet water
- Accelerated component wear during maintenance inspections

**Risk Rating**: S=7, L=6, D=4 → **RPN = 168** (High)

**Recommended Controls**:
- Multi-stage filtration with correct micron rating
- Regular monitoring of filter differential pressure
- Use of clean, suitable source water
- Scheduled filter element replacement
- Pre-use visual check of inlet water clarity

**Mitigation Effectiveness & Residual Risk**:
- Highly effective when filtration discipline is maintained. Residual risk increases significantly in dusty environments or when using untreated water sources.

**Linked Master Control Register Items**: MCR-013

---

## 20.3 Hose and Fitting Failure Modes

### 20.3.1 Hose Burst / Rupture

**Description**: Sudden failure of the high-pressure hose under operating pressure.

**Causes**:
- Exceeded service life (age or operating hours)
- Mechanical damage (kinking, crushing, abrasion)
- Incorrect bend radius during use or storage
- Manufacturing defect or previous over-pressurization
- Missed annual pressure testing

**Consequences**:
- High-pressure water release (whip, injection, or struck-by hazard)
- Potential serious injury or fatality
- Environmental contamination

**Detection**:
- Visual inspection (bulging, exposed braid, cuts)
- Weepage from outer cover
- Annual third-party pressure test failure

**Risk Rating**: S=10, L=4, D=4 → **RPN = 160** (High)

**Recommended Controls**:
- Strict hose life management (2 years for flex lances/whip hoses, 4 years for others) – MCR-001
- Mandatory annual third-party pressure testing – MCR-002
- Colour coding and visible expiration marking – MCR-003
- Proper hose handling and storage practices
- Immediate retirement of any hose showing damage or weepage – MCR-004
- Whip checks on both sides of every connection – MCR-006

**Mitigation Effectiveness & Residual Risk**:
- Very effective when hose management program is strictly followed. Main residual risk comes from mechanical damage during use or missed annual testing.

**Linked Master Control Register Items**: MCR-001, MCR-002, MCR-004, MCR-006

---

### 20.3.2 Quick-Connect Disconnection Under Pressure

**Description**: Accidental separation of quick-connect couplings while under pressure.

**Causes**:
- Worn or damaged latch/pin mechanism
- Rotation of hose aligning the safety pin incorrectly
- Incorrect coupling type used in high-movement applications
- Improper connection or incomplete engagement

**Consequences**:
- Sudden high-pressure water release
- Hose whip injury
- Potential injection or struck-by trauma

**Detection**:
- Visual inspection of latch/pin condition before every use
- Audible click or feel during connection
- Regular function testing of couplings

**Risk Rating**: S=9, L=5, D=4 → **RPN = 180** (High)

**Recommended Controls**:
- Prefer screw-type or face-seal couplings in high-movement applications
- Inspect quick-connect latches and pins before every connection
- Never use quick-connects where rotation under pressure is likely
- Train operators on correct connection technique

**Mitigation Effectiveness & Residual Risk**:
- Effective when inspection discipline is high. Residual risk remains if operators use damaged couplings or incorrect coupling types under dynamic conditions.

**Linked Master Control Register Items**: MCR-007

---

## 20.4 Nozzle and Tooling Failure Modes

### 20.4.1 Nozzle Wear / Orifice Enlargement

**Description**: Gradual enlargement or damage to the nozzle orifice due to erosion and corrosion.

**Causes**:
- Abrasive particles in water
- Extended use beyond recommended wear life
- Corrosion (especially in saline or chemically treated water)
- Poor water quality / inadequate filtration

**Consequences**:
- Reduced cleaning effectiveness
- Increased flow and reduced pressure
- Higher reaction force than expected
- Potential jet instability

**Detection**:
- Visual inspection of orifice condition
- Pin gauge testing
- Change in pump pressure and flow readings
- Reduced cleaning performance

**Risk Rating**: S=6, L=7, D=3 → **RPN = 126** (Medium-High)

**Recommended Controls**:
- Scheduled nozzle replacement based on wear life (typically 20–60 hours) – MCR-018
- Regular pin gauge inspection
- Use of corrosion-resistant nozzles where appropriate
- Good inlet filtration
- Monitor pump performance trends

**Mitigation Effectiveness & Residual Risk**:
- Effective when replacement intervals are respected. Residual risk increases with poor water quality or when operators run nozzles to failure.

**Linked Master Control Register Items**: MCR-018

---

### 20.4.2 Flex Lance Back-Out / Loss of Control

**Description**: Uncontrolled withdrawal of a flex lance from a tube during cleaning.

**Causes**:
- Failure or incorrect use of Anti-Withdrawal Device (AWD)
- Operator error or inadequate training
- Excessive reaction force overpowering the operator
- Blockage or sudden pressure change

**Consequences**:
- High-pressure jet directed toward operator or bystanders
- Serious injury or fatality (documented UK HSE case – Incident Library Case 2)
- Equipment damage

**Detection**:
- Sudden change in lance position or tension
- Loss of cleaning progress
- Operator reports of unusual resistance or movement

**Risk Rating**: S=10, L=4, D=5 → **RPN = 200** (Very High)

**Recommended Controls**:
- Mandatory use and correct installation of Anti-Withdrawal Devices – MCR-019 / MCR-020
- Proper training on flex lance operations
- Good communication between nozzle operator and pump operator
- Use of appropriate reaction force controls – MCR-016

**Mitigation Effectiveness & Residual Risk**:
- Highly effective when AWD discipline and training are strong. Residual risk remains if operators bypass AWD or work with excessive reaction force.

**Linked Master Control Register Items**: MCR-019, MCR-020

**Note**: Now backed by documented UK HSE fatality (Case 2 in Incident Library).

---

### 20.4.3 Automated / Robotic System Failure (e.g., Peinemann, Hammelmann JETMASTER)

**Description**: Failure or loss of control of automated or robotic tube cleaning or jetting systems.

**Causes**:
- Sensor or control system fault
- Mechanical jam or entanglement
- Loss of communication or power
- Operator error in programming or supervision

**Consequences**:
- Uncontrolled high-pressure jet movement
- Damage to tubes or equipment
- Injury to personnel in the area
- Major production delay

**Detection**:
- System alarms and fault codes
- Unusual behaviour or position of tooling
- Loss of expected cleaning progress

**Risk Rating**: S=8, L=4, D=4 → **RPN = 128** (High)

**Recommended Controls**:
- Specific competency training for automated system operators
- Pre-use functional testing of all sensors and safety interlocks – MCR-021
- Clear zoning and SIMOPS controls when automated systems are in use
- Emergency stop procedures and backup manual controls

**Mitigation Effectiveness & Residual Risk**:
- Effective with proper training and testing. Residual risk increases during complex or changing site conditions.

**Linked Master Control Register Items**: MCR-021

---

## 20.5 Control and Safety System Failures

### 20.5.1 Failure of Pressure Relief / Dump System

**Description**: Inability to relieve pressure when required (e.g., dump valve fails to open).

**Causes**:
- Mechanical failure or blockage of dump valve
- Electrical or control system fault
- Operator error (incorrect valve position)
- Lack of maintenance

**Consequences**:
- Inability to safely shut down the system
- Continued high-pressure flow even when operator releases trigger
- Potential for serious injury during nozzle changes or emergencies

**Detection**:
- Functional test of dump valve during pre-use inspection
- Alarms or indicators (if fitted)
- Operator reports of slow or incomplete pressure relief

**Risk Rating**: S=9, L=4, D=3 → **RPN = 108** (High)

**Recommended Controls**:
- Mandatory functional test of pressure relief system before every job – MCR-010
- Regular maintenance and inspection of dump valves
- Clear operating procedures for emergency shutdown
- Backup relief systems where required

**Mitigation Effectiveness & Residual Risk**:
- Very effective when functional testing discipline is maintained. Main residual risk is from mechanical blockage or electrical faults between tests.

**Linked Master Control Register Items**: MCR-010

---

### 20.5.2 Sensor / Auto-Shut-off Module Failure (e.g., xPRO)

**Description**: Failure of electronic or mechanical safety sensors to detect irregular movement and shut down the system.

**Causes**:
- Sensor damage or misalignment
- Electrical fault or low battery
- Software/firmware issues
- Bypass or disablement by operators

**Consequences**:
- Loss of automated safety protection
- Continued operation despite dangerous conditions (e.g., operator falling or losing control)

**Detection**:
- Pre-use functional test of safety module
- Alarm or fault indication
- Regular calibration and maintenance checks

**Risk Rating**: S=8, L=3, D=5 → **RPN = 120** (High)

**Recommended Controls**:
- Mandatory pre-use functional test of all safety sensors – MCR-021
- Never bypass or disable safety modules
- Regular maintenance and firmware updates per manufacturer
- Clear procedures prohibiting tampering with safety systems

**Mitigation Effectiveness & Residual Risk**:
- Effective when testing and maintenance are consistent. Residual risk increases if operators bypass systems or if sensors are damaged between checks.

**Linked Master Control Register Items**: MCR-021

---

## 20.6 Human Factor and Operational Failure Modes

### 20.6.1 Loss of Control Due to Excessive Reaction Force

**Description**: Operator loses physical control of the lance or gun due to high reaction force.

**Causes**:
- Incorrect nozzle selection (too much thrust for the operator)
- Fatigue or poor body positioning
- Slippery or unstable footing
- Inadequate training or experience

**Consequences**:
- Uncontrolled jet movement
- Injury to operator or nearby personnel
- Equipment damage

**Detection**:
- Operator reports of difficulty controlling the tool
- Visible struggle or loss of stance
- Sudden change in jet direction

**Risk Rating**: S=9, L=5, D=4 → **RPN = 180** (High)

**Recommended Controls**:
- Strict adherence to the three additive reaction force controls – MCR-016
- Proper training and competency assessment
- Use of mechanical assistance or automation where reaction force is high
- Good footing and stance discipline

**Mitigation Effectiveness & Residual Risk**:
- Highly effective when all three controls are applied together. Residual risk remains during fatigue or in difficult access conditions.

**Linked Master Control Register Items**: MCR-016

---

### 20.6.2 Inadequate Pre-Use Inspection

**Description**: Failure to detect existing defects or unsafe conditions before starting work.

**Causes**:
- Rushed or incomplete inspection
- Lack of training on what to look for
- Complacency or production pressure
- Poor lighting or access

**Consequences**:
- Use of damaged or unsafe equipment
- Preventable failures during operation
- Increased risk of injury or equipment damage

**Detection**:
- Post-incident investigation often reveals missed defects
- Audit findings on inspection quality

**Risk Rating**: S=7, L=6, D=5 → **RPN = 210** (Very High)

**Recommended Controls**:
- Clear, comprehensive pre-use checklists – MCR-023
- Training on inspection techniques and acceptance criteria
- Supervisor spot checks of inspection quality – MCR-024
- Time allocated for proper inspection before every job

**Mitigation Effectiveness & Residual Risk**:
- Very effective when checklists and training are strong and time is allocated. Main residual risk comes from production pressure and complacency.

**Linked Master Control Register Items**: MCR-023, MCR-024

---

### 20.6.3 Poor SIMOPS Coordination

**Description**: Failure to properly coordinate HPWJ work with other simultaneous operations (e.g., hot work, lifting, scaffolding, vacuum trucks).

**Causes**:
- Inadequate planning or communication
- Unclear responsibilities
- Production pressure overriding safety controls
- Changing work scope without re-assessment

**Consequences**:
- Ignition of flammable materials from jet spray/mist near hot work
- Struck-by incidents from moving equipment
- Conflicts between work parties

**Detection**:
- Near misses or incidents during SIMOPS
- Audit findings on permit and coordination quality

**Risk Rating**: S=8, L=5, D=5 → **RPN = 200** (Very High)

**Recommended Controls**:
- Robust SIMOPS planning and daily coordination meetings – MCR-028
- Clear permit-to-work interfaces
- Specific controls for hot work near jetting operations
- Strong supervision and communication discipline

**Mitigation Effectiveness & Residual Risk**:
- Effective when daily coordination and permit discipline are strong. Residual risk increases during rapidly changing turnaround conditions.

**Linked Master Control Register Items**: MCR-028

---

### 20.6.4 Inadequate Team Communication

**Description**: Poor communication between nozzle operator, pump operator, and support team during operations.

**Causes**:
- No clear communication protocol
- Language barriers
- Noise interference
- Distraction or complacency

**Consequences**:
- Uncoordinated pressure changes
- Delayed response to problems
- Increased risk of incidents during critical phases (nozzle changes, blockages)

**Detection**:
- Near misses involving miscommunication
- Post-job debrief findings

**Risk Rating**: S=7, L=5, D=5 → **RPN = 175** (High)

**Recommended Controls**:
- Clear communication protocols and hand signals – MCR-025
- Radio communication where noise is high
- Pre-job briefing on roles and signals
- Stop-work authority for any communication breakdown

**Mitigation Effectiveness & Residual Risk**:
- Effective when protocols are trained and followed. Residual risk remains in high-noise or multi-language environments.

**Linked Master Control Register Items**: MCR-025

---

## 20.7 Summary and Continuous Improvement

This FMEA is a living document. It should be reviewed and updated after any significant incident, near miss, or major equipment change. Key lessons should be fed back into procedures, training, and the Master Control Register.

**Highest Priority Items (RPN > 180)**:
- Inadequate Pre-Use Inspection
- Flex Lance Back-Out / Loss of Control (now with documented fatality)
- Poor SIMOPS Coordination
- Quick-Connect Disconnection Under Pressure
- Loss of Control Due to Excessive Reaction Force
- **NEW CANDIDATE**: Adjacent Excavation / Unprotected Opening Hazard (provisional RPN 180)

Common themes across many failure modes include:
- Importance of pre-use inspection discipline
- Correct equipment selection and matching
- Adherence to maintenance and life management intervals
- Training and competency
- Clear communication and procedural discipline
- Strong SIMOPS management

Regular review of this section during toolbox talks and safety meetings is recommended. High RPN items should be prioritized for additional controls or engineering solutions.

---

**References**:
- Industry incident databases and lessons learned
- Manufacturer failure mode data
- WJTA and WJA safety guidance
- NIOSH CA/FACE 16CA001
- UK HSE / IMCA / SAFETY4SEA flexi-lance fatality investigation
- Operational experience from major HPWJ contractors
- Master Control Register (linked items)
