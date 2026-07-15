# Section 20: Failure Modes & Effects Analysis (FMEA-style)

**Maximum Practical Depth**

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

The following modes currently carry the highest risk and should receive focused attention in training, audits, and procedure reviews:

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

**Linked Master Control Register Items**:
- Ch7: Inlet filtration best practices
- Ch5/Ch7: Weather and temperature-related stop-work criteria
- Ch7: Pre-use inspection checklist (pump section)

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

**Linked Master Control Register Items**:
- Ch7: Rupture disc single-use replacement and spare stock
- Ch7: Pre-use inspection checklist (rupture disc section)

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

**Linked Master Control Register Items**:
- Ch7: Pre-use inspection checklist (pump fluids section)
- Ch11: Maintenance and reliability practices

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

**Linked Master Control Register Items**:
- Ch7: Pre-use inspection checklist (engine fluids and filters)

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

**Linked Master Control Register Items**:
- Ch7: Inlet filtration best practices
- Ch7: Pre-use inspection checklist (pump section)

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
- Strict hose life management (2 years for flex lances/whip hoses, 4 years for others)
- Mandatory annual third-party pressure testing
- Colour coding and visible expiration marking
- Proper hose handling and storage practices
- Immediate retirement of any hose showing damage or weepage

**Mitigation Effectiveness & Residual Risk**:
- Very effective when hose management program is strictly followed. Main residual risk comes from mechanical damage during use or missed annual testing.

**Linked Master Control Register Items**:
- Ch7: Annual third-party hose pressure/proof testing
- Ch7: Hose expiration and colour coding rules
- Ch7: Pre-use inspection checklist (hoses section)

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

**Linked Master Control Register Items**:
- Ch7: Quick-connect coupling disconnection risk mitigation
- Ch7: Pre-use inspection checklist (fittings section)

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
- Scheduled nozzle replacement based on wear life (typically 20–60 hours)
- Regular pin gauge inspection
- Use of corrosion-resistant nozzles where appropriate
- Good inlet filtration
- Monitor pump performance trends

**Mitigation Effectiveness & Residual Risk**:
- Effective when replacement intervals are respected. Residual risk increases with poor water quality or when operators run nozzles to failure.

**Linked Master Control Register Items**:
- Ch7: Nozzle wear life and corrosion pitting rejection criteria
- Ch7: Pre-use inspection checklist (nozzles section)

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
- Serious injury or fatality
- Equipment damage

**Detection**:
- Sudden change in lance position or tension
- Loss of cleaning progress
- Operator reports of unusual resistance or movement

**Risk Rating**: S=10, L=4, D=5 → **RPN = 200** (Very High)

**Recommended Controls**:
- Mandatory use and correct installation of Anti-Withdrawal Devices
- Proper training on flex lance operations
- Good communication between nozzle operator and pump operator
- Use of appropriate reaction force controls

**Mitigation Effectiveness & Residual Risk**:
- Highly effective when AWD discipline and training are strong. Residual risk remains if operators bypass AWD or work with excessive reaction force.

**Linked Master Control Register Items**:
- Ch7: Tool-specific hazard profiles (flex lance + AWD)
- Ch8: Team composition and communication rules

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
- Pre-use functional testing of all sensors and safety interlocks
- Clear zoning and SIMOPS controls when automated systems are in use
- Emergency stop procedures and backup manual controls

**Mitigation Effectiveness & Residual Risk**:
- Effective with proper training and testing. Residual risk increases during complex or changing site conditions.

**Linked Master Control Register Items**:
- Ch8: Robotic/remote operation variant controls
- Ch7: Sensor-based auto-shut-off module requirements

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
- Mandatory functional test of pressure relief system before every job
- Regular maintenance and inspection of dump valves
- Clear operating procedures for emergency shutdown
- Backup relief systems where required

**Mitigation Effectiveness & Residual Risk**:
- Very effective when functional testing discipline is maintained. Main residual risk is from mechanical blockage or electrical faults between tests.

**Linked Master Control Register Items**:
- Ch7: Pre-use inspection checklist (safety & control systems)
- Ch6: Pump LOTO and isolation procedures

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
- Mandatory pre-use functional test of all safety sensors
- Never bypass or disable safety modules
- Regular maintenance and firmware updates per manufacturer
- Clear procedures prohibiting tampering with safety systems

**Mitigation Effectiveness & Residual Risk**:
- Effective when testing and maintenance are consistent. Residual risk increases if operators bypass systems or if sensors are damaged between checks.

**Linked Master Control Register Items**:
- Ch7: Sensor-based auto-shut-off module requirements
- Ch8: Robotic/remote operation variant controls

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
- Strict adherence to the three additive reaction force controls
- Proper training and competency assessment
- Use of mechanical assistance or automation where reaction force is high
- Good footing and stance discipline

**Mitigation Effectiveness & Residual Risk**:
- Highly effective when all three controls are applied together. Residual risk remains during fatigue or in difficult access conditions.

**Linked Master Control Register Items**:
- Ch7: Reaction force management (three additive controls)
- Ch8: Quantitative fatigue management

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
- Clear, comprehensive pre-use checklists
- Training on inspection techniques and acceptance criteria
- Supervisor spot checks of inspection quality
- Time allocated for proper inspection before every job

**Mitigation Effectiveness & Residual Risk**:
- Very effective when checklists and training are strong and time is allocated. Main residual risk comes from production pressure and complacency.

**Linked Master Control Register Items**:
- Ch7: Pre-use inspection checklist (comprehensive)
- Ch5: Site preparation and inspection requirements

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
- Robust SIMOPS planning and daily coordination meetings
- Clear permit-to-work interfaces
- Specific controls for hot work near jetting operations
- Strong supervision and communication discipline

**Mitigation Effectiveness & Residual Risk**:
- Effective when daily coordination and permit discipline are strong. Residual risk increases during rapidly changing turnaround conditions.

**Linked Master Control Register Items**:
- Ch8: SIMOPS and hot work interface controls
- Ch5: Site preparation and barricading rules

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
- Clear communication protocols and hand signals
- Radio communication where noise is high
- Pre-job briefing on roles and signals
- Stop-work authority for any communication breakdown

**Mitigation Effectiveness & Residual Risk**:
- Effective when protocols are trained and followed. Residual risk remains in high-noise or multi-language environments.

**Linked Master Control Register Items**:
- Ch8: Team composition and communication rules

---

## 20.7 Summary and Continuous Improvement

This FMEA is a living document. It should be reviewed and updated after any significant incident, near miss, or major equipment change. Key lessons should be fed back into procedures, training, and the Master Control Register.

**Highest Priority Items (RPN > 180)**:
These modes represent the greatest current risk and should receive focused attention:
- Inadequate Pre-Use Inspection
- Flex Lance Back-Out / Loss of Control
- Poor SIMOPS Coordination
- Quick-Connect Disconnection Under Pressure
- Loss of Control Due to Excessive Reaction Force

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
- Operational experience from major HPWJ contractors
- Master Control Register (linked items)