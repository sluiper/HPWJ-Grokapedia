# Chapter 7: Equipment, Pumps, Tools, Nozzles & Pre-Use Inspection

**Maximum Technical & Operational Depth**

This chapter provides the complete reference for selecting, inspecting, and operating high-pressure water jetting equipment. It combines fundamental engineering principles with practical field requirements from WJTA, WJA, NLB, StoneAge, Hammelmann, WOMA, Peinemann, and other major manufacturers, aligned with KSA/SABIC operational practice.

---

## 7.1 Pump Fundamentals

A high-pressure water jetting pump does **not** create pressure. It displaces a fixed volume of water. Pressure is created only by the restriction at the nozzle (or other orifice) at the end of the system.

### Key Principle
The nozzle operator must always maintain control of the method of pressure relief. This is non-negotiable.

### Pump Types Commonly Used in HPWJ
- **Triplex plunger pumps** (most common in oil & gas HPWJ)
- **Quintuplex plunger pumps** (higher flow, smoother operation, preferred for some automated/large-scale work)

**Triplex vs Quintuplex Comparison**

| Feature                  | Triplex                          | Quintuplex                          | Typical HPWJ Use Case                  |
|--------------------------|----------------------------------|-------------------------------------|----------------------------------------|
| Number of plungers       | 3                                | 5                                   | Triplex dominant in manual work        |
| Flow pulsation           | Higher                           | Lower (smoother)                    | Quintuplex preferred for automated     |
| Footprint & weight       | Smaller / lighter                | Larger / heavier                    | Triplex more common on mobile units    |
| Efficiency at high pressure | Generally good                | Slightly better at very high flow   | Application dependent                  |

---

## 7.2 Flow vs Pressure – How to Select a Pump

### The Fundamental Relationship
- **Flow (litres/min or GPM)** determines cleaning speed and coverage.
- **Pressure (bar or psi)** determines cleaning power / ability to remove hard deposits.

**Practical Selection Rule**
- For surface preparation and coating removal: Higher pressure, moderate flow.
- For tube bundle and vessel cleaning: Higher flow is often more important than ultra-high pressure.
- For line moleing / pipe cleaning: Balance of pressure and flow, with good reaction force management.

### Horsepower Relationship
Approximate relationship:

**Power (kW) ≈ (Pressure × Flow) / Efficiency**

Where efficiency is typically 80–90% for modern triplex pumps.

**Example**
To achieve 20,000 psi (1,379 bar) at 40 L/min requires significantly more power than the same flow at 10,000 psi. Plunger size must be reduced to reach higher pressure on the same power unit.

**Plunger Size Effect**
- Smaller plunger diameter = higher pressure, lower flow (for same RPM and power).
- Larger plunger diameter = higher flow, lower pressure.

### Understanding Pump Performance Curves

Pump manufacturers provide **performance curves** that show the relationship between:
- Pressure vs Flow
- Power consumption
- Efficiency

**How to Read a Typical HPWJ Pump Curve**
- X-axis: Flow (L/min or GPM)
- Y-axis (left): Pressure (psi or bar)
- Y-axis (right): Power (kW or HP) and Efficiency (%)

**Key Insights from Curves**
- At higher pressure, flow decreases (for a fixed power unit).
- There is usually an optimal operating range where efficiency is highest.
- Running at the extreme right or left of the curve can lead to inefficiency, overheating, or cavitation.

**Practical Example**
A 250 kW triplex unit might deliver:
- 15,000 psi at ~80 L/min (high pressure, moderate flow)
- 10,000 psi at ~120 L/min (medium pressure, high flow)

Selecting the correct plunger size and RPM allows the operator to operate near the peak efficiency area of the curve for the required job.

---

## 7.3 Key Selection Factors

### 7.3.1 Application Requirements
- Surface cleaning / coating removal
- Heat exchanger / tube bundle cleaning (internal)
- Vessel / tank cleaning
- Line moleing / pipe descaling
- Concrete cutting / demolition (currently out of primary scope)

### 7.3.2 Reaction Force Management
Maximum recommended reaction force is generally **250 N** for handheld work.

Additional manufacturer guidance (StoneAge for rotary tools):
- Thrust should not exceed **1/3 of the operator’s body weight**.
- Barrel length must be long enough that the operator cannot pass the jet over their own feet or legs.

**Three Additive Controls** (all three must be satisfied):
1. Absolute limit ≤ 250 N
2. Body weight ratio (≤ 1/3 of operator body weight)
3. Barrel geometry (operator must not be able to pass the jet over their own feet or legs)

### 7.3.3 NPSH and Cavitation Prevention
Adequate Net Positive Suction Head (NPSH) is critical.
- Low NPSH causes cavitation, which damages plungers, valves, and pump components rapidly.
- Always ensure clean, cool inlet water with adequate supply pressure and minimal suction line restrictions.
- Monitor for early signs: unusual noise, vibration, or sudden loss of performance.

### 7.3.4 Pressure Relief & Safety Systems
Every system must have reliable pressure relief that the nozzle operator controls.

Common systems:
- Standard dump valve (most common)
- Nitrogen-assisted dump
- Dry shut / electrical dump systems

**Pressureless-at-Rest Design (WOMA principle)**: The system should be pressureless when the high-pressure gun is not activated. Verify this feature during equipment selection and pre-use inspection.

### 7.3.5 NPSH and Cavitation – Detailed Guidance & Calculations

**NPSH Available (NPSHa) Formula** (simplified for field use):

NPSHa = Atmospheric Pressure + Static Head − Vapour Pressure − Suction Line Losses

**Practical Targets for HPWJ Pumps**
- NPSHa should exceed NPSH Required (NPSHr) by the manufacturer by at least **0.5 – 1.0 bar** margin.
- Cold water (lower vapour pressure) improves NPSHa.
- Dirty or aerated water reduces effective NPSHa.

**NPSH Scenario 1: Sea Level, Flooded Suction, Cool Water**
- Good margin usually exists. Low risk if suction line is short and clean.

**NPSH Scenario 2: Elevated Site (~500 m), Long Suction Line**
- Lower atmospheric pressure reduces NPSHa.
- Long suction line increases losses.
- Mitigation: Use larger diameter suction hose, minimise vertical lift, or use a booster pump if needed.

**NPSH Scenario 3: Hot Water or High Ambient Temperature**
- Higher water temperature increases vapour pressure, reducing NPSHa.
- In KSA summer conditions, this can become critical.
- Mitigation: Use cooler water source if possible, or reduce pump speed slightly to lower NPSHr.

**Cavitation Prevention Measures**
- Use shortest possible suction line with minimal bends
- Ensure flooded suction where possible
- Maintain clean inlet water (good filtration)
- Avoid running the pump at very high speeds with marginal NPSH
- Monitor for characteristic "gravel" or "marbles" noise

---

## 7.4 Worked Pump Selection Examples

### Example 1: Surface Preparation (High Pressure, Moderate Flow)
- Application: Coating removal on vessel external surfaces
- Target: 20,000 psi (1,379 bar) at ~30–40 L/min
- Recommended: Triplex unit with smaller plungers
- Key considerations: High reaction force management, good barricading, experienced operators

### Example 2: Tube Bundle Cleaning (Higher Flow Priority)
- Application: Internal cleaning of heat exchanger tubes during turnaround
- Target: 10,000–15,000 psi at 60–100+ L/min
- Recommended: Larger triplex or quintuplex unit
- Key considerations: Automated or flex lance tooling, higher flow for productivity, good AWD use, vacuum truck integration

### Example 3: Line Moleing / Pipe Descaling
- Application: Descaling long pipe runs
- Target: Balanced pressure and flow (typically 15,000–20,000 psi)
- Recommended: Triplex unit with good reaction force control and appropriate mole/nozzle selection
- Key considerations: Careful monitoring of back pressure, proper mole thrust direction, communication between teams

### Example 4: Combined Manual + Automated Vessel Cleaning
- Application: Large vessel turnaround requiring both manual lance work on accessible areas and automated 3D heads for internal surfaces
- Target: 15,000 psi at mixed flow rates
- Recommended: Versatile triplex unit capable of supporting both handheld guns and automated tooling interfaces
- Key considerations: Strong SIMOPS controls, clear zoning between manual and automated areas, vacuum truck coordination, and robust barricading

These examples illustrate that **no single pump size fits all applications**. Selection must be driven by the dominant cleaning requirement, reaction force constraints, and whether automated tooling will be used.

---

## 7.5 Global Manufacturer Overview & Variations

### NLB Corp (USA)
- Very strong in diesel triplex units for oil & gas.
- Emphasis on pre-operational fluid checks (engine oil, pump oil, coolant, fuel, DEF), rupture disc inspection, and area/other-end-of-unit checks.
- Clear "do not leave unit running unattended" rule.

### StoneAge Tools (USA / Gardner Denver)
- Leader in rotating nozzles and flex lance systems.
- Specific guidance on wear life (typically 20–60 hours depending on water quality and pressure).
- Corrosion pitting named as a common precursor to cracking and tool failure.
- Reaction force guidance includes body weight ratio and barrel length geometry.

### Hammelmann (Germany)
- Strong in robotic and automated systems (JETMASTER).
- xPRO sensor-based automatic shut-off module for irregular movement detection.
- PIPEMASTER rotary hose reel feeder systems (distinct entanglement and reel-tension hazards).

### WOMA (Germany)
- Pressureless-at-rest / fail-safe circulation design is a core safety principle.
- Twin-Jet / multi-gun simultaneous operation capability (up to 6 guns).
- ATEX-certified options for Zone 2 hazardous areas.

### Peinemann Equipment (Netherlands)
- Specialist in hands-free and semi-automated tube bundle cleaning systems (up to 40,000 psi).
- Different hazard profile from manual lance work – focus on automated feed control, entanglement, and remote operation safety.

### Other Notable Manufacturers
- **Kamat (Germany)**: Ultra-high pressure focus.
- **Uraca (Germany)**: Long-established high-pressure systems.
- **Interpump Group / Hawk (Italy)**: Broad high-pressure pump range.
- **Sugino Machine (Japan)**: Strong in automated tube cleaning systems.
- **Jetstream & Flowplant/Harben**: Relevant in their respective markets.

**Selection Advice**: Match the pump and tooling to the dominant application. For heavy Anabeeb turnaround work involving both manual and automated tube bundle cleaning, a mixed fleet or versatile triplex units with good automated tooling interfaces are common.

---

## 7.6 Manufacturer Comparison Tables

### Pump Capability Comparison (Typical Ranges)

| Manufacturer     | Common Pump Types     | Typical Max Pressure | Typical Flow Range     | Notable Strengths                          | Hazardous Area Options |
|------------------|-----------------------|----------------------|------------------------|--------------------------------------------|------------------------|
| NLB (USA)        | Triplex (diesel)      | 40,000+ psi         | Medium                 | Robust field units, good support in MEA    | Limited                |
| StoneAge         | Triplex + tooling     | 40,000 psi          | Medium                 | Excellent rotating/flex tooling            | Standard               |
| Hammelmann       | Triplex + Robotic     | 40,000+ psi         | Medium-High            | Robotic systems, sensor safety modules     | Good (ATEX options)    |
| WOMA             | Triplex + Multi-gun   | 40,000+ psi         | Medium-High            | Multi-gun capability, pressureless-at-rest | Excellent (ATEX)       |
| Peinemann        | Automated systems     | 40,000 psi          | High                   | Hands-free tube bundle cleaning            | Good                   |
| Kamat            | Ultra-high pressure   | 50,000+ psi         | Lower                  | Very high pressure capability              | Good                   |

### Tooling & Automation Comparison

| Manufacturer     | Rotating Nozzles | Flex Lance Systems | Automated Bundle Cleaning | Robotic Systems | Sensor Auto-Shut-off | Notable Safety Feature          |
|------------------|------------------|--------------------|---------------------------|-----------------|----------------------|---------------------------------|
| StoneAge         | Excellent        | Excellent          | Good                      | Limited         | Limited              | Wear life guidance + geometry   |
| Hammelmann       | Good             | Good               | Good                      | Excellent       | Excellent (xPRO)     | Irregular movement detection    |
| WOMA             | Good             | Good               | Good                      | Limited         | Good                 | Pressureless-at-rest design     |
| Peinemann        | Good             | Good               | Excellent                 | Limited         | Good                 | Hands-free focus                |
| NLB              | Good             | Good               | Limited                   | Limited         | Limited              | Strong pre-use checklist        |

These tables help when selecting equipment for specific Anabeeb jobs. For heavy tube bundle work, Peinemann or similar automated systems combined with a good triplex pump unit often provide the best productivity and safety balance.

---

## 7.7 Hoses, Fittings & Connections

### Hose Life & Inspection
- **Expiration**: 2 years for flex lances and shotgun whip hoses; 4 years for all other high-pressure hoses (from date of manufacture or receipt).
- **Annual third-party pressure/proof testing** by a competent authority is required **in addition to** visual inspection (WJTA-referenced hose life-cycle data shows approximately 7% of hoses that pass visual inspection can still fail pressure testing).
- Permanent colour coding visible from 2 ft, matched to the maximum working pressure of the pump.

### Fittings & Adapters
- All couplings and fittings must be permanently marked with their Maximum Allowable Working Pressure (MAWP) and matched to the pump capability.
- Proper thread engagement (typically 3.5–5 threads).
- Type M connections (common at higher pressures) require correct cone/seat mating and weep hole inspection.
- **Quick-connect couplings**: Carry a specific risk of accidental disconnection under pressure due to wear or rotation aligning the safety pin/latch. Prefer screw-type or face-seal couplings for high-pressure connections where hose movement occurs.

---

## 7.8 Nozzles & Tooling

### Nozzle Types & Selection
- **Straight jet**: Highest impact, lowest coverage.
- **Fan tips**: Lower impact, wider coverage.
- **Rotating nozzles**: Good balance of impact and coverage; reduce operator fatigue.
- **3D / self-propelled tank cleaning heads**: For vessel and tank work.
- **Automated / hands-free systems** (Peinemann-style): For high-volume tube bundle work.

### Nozzle Inspection & Wear Life
- Inspect threads, sealing surfaces, and orifices before every use.
- Orifices must be clean and produce forward thrust for tube/pipe cleaning applications.
- Use pin gauges (approximately 0.2 mm undersize) to check and clear small orifices.
- Scheduled replacement: typically 20–60 hours depending on water quality and operating pressure.
- **Corrosion pitting** is a named rejection criterion.

### Tool-Specific Hazard Profiles
- Handheld long barrel guns: Reaction force and stance critical.
- Flex lance + Anti-Withdrawal Device (AWD): Back-out prevention inside tubes.
- Foot valves / deadman controls: Operator control of pressure relief.
- Rotating/self-propelled heads: Different thrust and entanglement profile vs handheld lances.
- Rotary hose reel feeder systems (Hammelmann PIPEMASTER-style): Distinct reel-tension and entanglement hazards.
- Sensor-based auto-shut-off modules (Hammelmann xPRO): Irregular movement detection and automatic pressure cut-off.

---

## 7.9 Pre-Use Inspection Checklist (Comprehensive)

The high-pressure pump and all associated equipment must be inspected **prior to each use**.

**Pump**
- Unit is level and wheels chocked
- Grounded to valid earth
- All protective guards in place (plungers, belts, cooling fan)
- Rupture disc tagged, rated, and validated to the pump and system operating pressure; spare disc stock available on unit
- Filter bag installed and clean
- Engine and high-pressure gauges functional and within calibration period
- Fire extinguisher accessible and tagged
- All fluids checked (engine oil, pump oil, coolant, fuel, DEF where fitted)

**Hoses & Connections**
- Visual inspection for exposed wire braids, bubbling outer jacket, damaged crimps/threads, exceeded bend radius
- Colour coding correct and visible from 2 ft
- Within expiration life
- Annual third-party pressure test records current
- Whip checks correctly installed across all connections (exceptions noted for rotating hoses and feed-through applications)
- Quick-connect latches/pins in good condition (or screw-type/face-seal preferred where movement risk exists)

**Nozzles & Tooling**
- Rated for hose size and pump pressure
- Orifices clean and producing correct thrust direction
- Threads and sealing surfaces undamaged
- Wear life within scheduled replacement interval
- Corrosion pitting absent

**Safety & Control Systems**
- Pressure relief / dump system functional and operator-controlled
- Pressureless-at-rest design verified (where applicable)
- Cold weather winterization completed if required (RV/marine antifreeze only)

---

## 7.10 Common Pump & Hose Related Failure Modes (Bridge to FMEA)

- Cavitation damage from inadequate NPSH or dirty/cold inlet water
- Hose failure from exceeded bend radius, age, or missed annual pressure testing
- Rupture disc activation due to overpressure or blocked nozzle (must be replaced before restart)
- Quick-connect disconnection during hose movement
- Nozzle clog leading to sudden pressure spike
- Sensor module or auto-shut-off failure on advanced tooling

These modes are addressed in more detail in the dedicated Failure Modes & Effects section (Part 2).

---

## 7.11 Maintenance & Reliability (Expanded for Maximum Information)

### Preventive vs Predictive Maintenance
- **Preventive**: Time-based (e.g., oil changes every X hours, annual inspections).
- **Predictive**: Condition-based using vibration analysis, temperature monitoring, and performance trending.

### Key Components to Monitor
- **Plungers and packing**: Most common wear items. Look for scoring, leakage, or reduced performance.
- **Valves and seats**: Check for pitting, erosion, or improper seating.
- **Rupture discs**: Must be replaced after activation. Maintain spares on unit.
- **Hoses**: Age, visual condition, and annual pressure test records.
- **Bearings and power end**: Vibration and temperature trends.

### Recommended Practices for Major Turnarounds
- Pre-turnaround pump inspection and fluid analysis.
- Maintain a critical spares kit (plungers, packing, valves, rupture discs, nozzles).
- Assign dedicated pump technicians during high-activity periods.
- Keep detailed maintenance logs linked to specific units.

### Common Signs of Deterioration
- Increased vibration or unusual noise
- Gradual loss of pressure or flow
- Higher than normal power consumption
- Frequent relief valve or rupture disc activation

### Diesel vs Electric Drive Considerations (KSA Context)
- Diesel units: More mobile, require fuel, DEF, and regular engine maintenance. Good for remote or changing locations.
- Electric units: Cleaner, quieter, lower operating cost where power is available. Require proper grounding and cable management.

### Spare Parts Strategy
- Identify high-wear, long-lead-time items in advance.
- For major turnarounds, stage critical spares on-site or at nearby warehouse.
- Consider consignment stock agreements with key suppliers for high-usage items.

---

## 7.12 Summary of Key Never Rules (Equipment-Related)

- Never reuse or bypass a fired rupture disc.
- Never operate without current annual hose pressure test records.
- Never use quick-connect couplings in high-movement applications without verifying latch/pin condition (prefer screw-type/face-seal where appropriate).
- Never leave the pump unit running unattended.
- Never start the system if potentially frozen without proper winterization.

**References for this chapter**: WJTA Orange Book, NLB operation manuals, StoneAge tooling guidance, Hammelmann and WOMA technical documentation, Peinemann automated system information, and relevant hose life-cycle studies.