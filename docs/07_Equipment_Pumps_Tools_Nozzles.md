# Chapter 7: Equipment, Pumps, Tools, Nozzles & Pre-Use Inspection

**Version 8.0**

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

### Power End vs Fluid End

A high-pressure pump consists of two main sections:

- **Power End**: The mechanical section (crankshaft, connecting rods, crossheads, bearings). It converts rotary motion into reciprocating motion. This section requires regular lubrication and is sensitive to vibration and misalignment.
- **Fluid End**: The hydraulic section (cylinders, plungers, valves, packing, manifold). This is where water is pressurised. It is exposed to high pressure, abrasion, and corrosion.

Understanding the difference helps with troubleshooting and maintenance planning. Most failures in the fluid end are related to water quality and pressure, while power end issues are usually lubrication or alignment related.

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

### Pump Conversions and Plunger Changes – Flow and Pressure Calculations

Changing plunger diameter is one of the most common ways to reconfigure a pump for different pressure/flow requirements.

**Basic Relationship**
For a given pump (fixed RPM and power), flow is proportional to the cross-sectional area of the plunger.

**Flow ∝ (Plunger Diameter)²**

Pressure capability increases as flow decreases (because the same power is applied to a smaller volume of water).

**Practical Calculation Method**
When changing plungers, use the following approximate relationships (assuming constant power and RPM):

- New Flow = Old Flow × (New Diameter / Old Diameter)²
- New Pressure ≈ Old Pressure × (Old Flow / New Flow)

**Important Notes**
- Always verify that the new pressure does not exceed the rated pressure of hoses, fittings, and other components.
- Some pumps have limits on minimum and maximum plunger sizes.
- After changing plungers, re-verify the rupture disc rating and relief settings.

**Worked Example 1: Increasing Pressure**
Current setup: 15 mm plungers delivering 10,000 psi at 80 L/min.
Change to 12 mm plungers.

New Flow ≈ 80 × (12/15)² = 80 × 0.64 = **51.2 L/min**
New Pressure ≈ 10,000 × (80 / 51.2) ≈ **15,625 psi**

**Worked Example 2: Increasing Flow**
Current setup: 12 mm plungers delivering 15,000 psi at 50 L/min.
Change to 14 mm plungers.

New Flow ≈ 50 × (14/12)² = 50 × 1.36 ≈ **68 L/min**
New Pressure ≈ 15,000 × (50 / 68) ≈ **11,030 psi**

These calculations are approximate. Always cross-check with the pump manufacturer’s performance data or software for the specific model.

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

### Variable Speed / RPM Effects

Changing engine or motor speed (RPM) has a significant effect on pump performance:

- Flow is roughly proportional to RPM.
- Pressure capability is less directly affected but can change with flow.
- Lower RPM generally reduces wear and can help with marginal NPSH situations.
- Higher RPM increases flow but also increases power demand and can raise cavitation risk.

Many modern units use electronic governors or variable frequency drives (VFDs) on electric motors to fine-tune performance.

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

It is important to distinguish between **pump manufacturers** (companies that design and build the high-pressure pumps) and **tooling & automation specialists** (companies that focus on nozzles, lances, automated systems, and safety accessories).

### Major High-Pressure Pump Manufacturers (OEMs)

- **NLB Corp (USA)**: Leading diesel triplex pump manufacturer. Strong field support in oil & gas and MEA region. Emphasis on robust pre-use checks and clear safety rules.
- **WOMA (Germany)**: Major pump and multi-gun system manufacturer. Known for pressureless-at-rest design and ATEX options.
- **Hammelmann (Germany)**: High-quality triplex pumps with strong focus on robotic and automated integration.
- **Kamat (Germany)**: Specialist in ultra-high pressure pumps.
- **Uraca (Germany)**: Long-established European pump manufacturer.
- **Interpump Group / Hawk (Italy)**: One of the largest global high-pressure pump manufacturers.
- **Cat Pumps (USA)**: Well-known industrial high-pressure pump brand.
- **Flowplant / Harben (UK)**: Established UK pump and system manufacturer.

### Tooling & Automation Specialists (Not Primary Pump Makers)

- **StoneAge Tools (USA)**: **Does not manufacture high-pressure pumps**. Specialises in high-quality rotating nozzles, flex lances, automated tooling, and safety modules. Often paired with pumps from NLB or other OEMs.
- **Peinemann Equipment (Netherlands)**: Specialist in hands-free and semi-automated tube bundle cleaning systems. Focuses on automation rather than pump manufacturing.
- **Sugino Machine (Japan)**: Strong Asian manufacturer specialising in automated tube cleaning and water jetting systems.

### Regional / Emerging Manufacturers

- **Pinaman**: Appears to be a regional (likely Chinese or Asian) supplier of water jetting equipment and tooling, particularly for tank and vessel cleaning. Less information is available compared to established Western and European brands. Treat as a lower-tier or regional option with appropriate due diligence on quality and support.

**Asia Water Jetting Note**: The strongest established Asian player in high-pressure water jetting tooling and automated systems is **Sugino Machine (Japan)**. There are numerous Chinese manufacturers, but quality and support levels vary significantly. For critical oil & gas work, preference is generally given to established Western/European pump OEMs paired with proven tooling from StoneAge, Peinemann, or Sugino.

**Selection Advice**: For most Anabeeb work, the most reliable and supportable combinations are proven pump OEMs (NLB, WOMA, Hammelmann, etc.) paired with high-quality tooling from StoneAge, Peinemann, or Sugino. Regional options like Pinaman can be considered for lower-criticality or cost-sensitive applications after proper evaluation.

---

## 7.6 Manufacturer Comparison Tables

### Pump Capability Comparison (Typical Ranges)

| Manufacturer     | Common Pump Types     | Typical Max Pressure | Typical Flow Range     | Notable Strengths                          | Hazardous Area Options |
|------------------|-----------------------|----------------------|------------------------|--------------------------------------------|------------------------|
| NLB (USA)        | Triplex (diesel)      | 40,000+ psi         | Medium                 | Robust field units, good support in MEA    | Limited                |
| WOMA (Germany)   | Triplex + Multi-gun   | 40,000+ psi         | Medium-High            | Multi-gun capability, pressureless-at-rest | Excellent (ATEX)       |
| Hammelmann       | Triplex + Robotic     | 40,000+ psi         | Medium-High            | Robotic systems, sensor safety modules     | Good (ATEX options)    |
| Kamat (Germany)  | Ultra-high pressure   | 50,000+ psi         | Lower                  | Very high pressure capability              | Good                   |
| Peinemann        | Automated systems     | 40,000 psi          | High                   | Hands-free tube bundle cleaning            | Good                   |

### Tooling & Automation Comparison

| Manufacturer     | Rotating Nozzles | Flex Lance Systems | Automated Bundle Cleaning | Robotic Systems | Sensor Auto-Shut-off | Notable Safety Feature          |
|------------------|------------------|--------------------|---------------------------|-----------------|----------------------|---------------------------------|
| StoneAge         | Excellent        | Excellent          | Good                      | Limited         | Limited              | Wear life guidance + geometry   |
| Hammelmann       | Good             | Good               | Good                      | Excellent       | Excellent (xPRO)     | Irregular movement detection    |
| WOMA             | Good             | Good               | Good                      | Limited         | Good                 | Pressureless-at-rest design     |
| Peinemann        | Good             | Good               | Excellent                 | Limited         | Good                 | Hands-free focus                |
| Sugino (Japan)   | Good             | Good               | Excellent                 | Limited         | Good                 | Strong automated tube cleaning  |

These tables help when selecting equipment for specific Anabeeb jobs. For heavy tube bundle work, Peinemann or Sugino automated systems combined with a proven pump from NLB, WOMA, or Hammelmann often provide the best balance.

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
- **Automated / hands-free systems** (Peinemann and Sugino style): For high-volume tube bundle work.

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

## 7.9 Inlet Filtration Best Practices

Clean inlet water is critical for pump life and performance.

**Recommended Practices**
- Use multi-stage filtration (coarse strainer + fine filter).
- Typical final filtration: 10–50 microns depending on pump manufacturer recommendations.
- Monitor pressure drop across filters and change elements when differential pressure increases.
- In dusty KSA environments, protect inlet from airborne contamination.
- Consider automated back-flush filters for high-duty applications.

Poor filtration is one of the fastest ways to damage plungers, valves, and packing.

---

## 7.10 Pre-Use Inspection Checklist (Comprehensive)

The high-pressure pump and all associated equipment must be inspected **prior to each use**.

**See the controlled field document**: `templates/checklists/Pre_Use_Inspection_Checklist.md` (fully MCR-mapped, signature-ready).

Key summary items remain as previously detailed (pump, hoses, nozzles, safety systems).

---

## 7.11 Common Pump & Hose Related Failure Modes (Bridge to FMEA)

- Cavitation damage from inadequate NPSH or dirty/cold inlet water
- Hose failure from exceeded bend radius, age, or missed annual pressure testing
- Rupture disc activation due to overpressure or blocked nozzle (must be replaced before restart)
- Quick-connect disconnection during hose movement
- Nozzle clog leading to sudden pressure spike
- Sensor module or auto-shut-off failure on advanced tooling

These modes are addressed in more detail in the dedicated Failure Modes & Effects section (Part 2).

---

## 7.12 Maintenance & Reliability

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

## 7.13 Transport, Mounting & Site Setup Considerations

- Units should be mounted on stable skids or trailers with adequate vibration isolation.
- Ensure proper tie-down points for transport.
- On site, the unit must be level and chocked.
- Consider noise and exhaust direction relative to work areas and accommodation.
- Provide spill containment bunding where required.
- Ensure adequate ventilation and access for maintenance.

---

## 7.14 Enhanced Safety Systems Beyond Rupture Disc

In addition to rupture discs, many modern systems include:
- Pressure relief valves (adjustable or fixed)
- High-pressure and low-pressure shutdown interlocks
- Engine overspeed and low oil pressure shutdowns
- Remote emergency stop buttons
- Sensor-based auto-shut-off on advanced tooling (e.g., Hammelmann xPRO)

All safety systems should be tested as part of the pre-use inspection.

---

## 7.15 Common Operator Errors to Avoid

Even with good equipment, many incidents occur due to avoidable operational mistakes:

- Failing to perform full pre-use inspection (especially rupture disc and hose condition).
- Changing plungers without verifying component pressure ratings and relief settings.
- Ignoring early signs of cavitation (unusual noise/vibration).
- Using quick-connect couplings in high-movement applications without proper latch inspection.
- Leaving the pump running unattended.
- Poor inlet water quality / inadequate filtration.
- Incorrect stance or barrel positioning leading to reaction force incidents.

Awareness of these common errors significantly reduces risk.

---

## 7.16 Summary of Key Never Rules (Equipment-Related)

- Never reuse or bypass a fired rupture disc.
- Never operate without current annual hose pressure test records.
- Never use quick-connect couplings in high-movement applications without verifying latch/pin condition (prefer screw-type/face-seal where appropriate).
- Never leave the pump unit running unattended.
- Never start the system if potentially frozen without proper winterization.

---

## 7.17 Ultra-High Pressure (UHP) Creeping Hose, 40k psi Operations & Tube Bundle Cleaning (NLB Focus)

**This section is critical for Anabeeb tube bundle and high-pressure work.**

### 7.17.1 What is a Creeping Hose / UHP Flex Lance System?

A “creeping hose” (also called self-propelled or crawling flex lance) is a specialised high-pressure hose assembly designed to advance itself through heat exchanger tubes under the reaction force of the jet. At 30,000–40,000+ psi it becomes extremely powerful and extremely hazardous if not perfectly controlled.

**Typical Anabeeb / NLB Configuration**:
- NLB diesel triplex pump configured for 40,000 psi class
- Small diameter multi-wire braided or spiral UHP hose (often 3/8" or smaller ID for high pressure)
- Specialised rotating or multi-orifice nozzle at the tip
- Anti-Withdrawal Device (AWD) / safety clamp system mandatory
- Vacuum recovery or catch system at the far end of the tube bundle

### 7.17.2 Key Technical Differences at 40k psi vs Standard HP

| Parameter | Standard HP (10–20k psi) | UHP Creeping Hose (30–40k+ psi) |
|-----------|---------------------------|---------------------------------|
| Jet velocity (theoretical, Cd=1) | ~371–525 m/s (see Section 16.4) | ~640–743+ m/s at 30–40k psi |
| Reaction force | Manageable with controls | Extremely high – mechanical assistance or automation preferred |
| Hose stiffness | More flexible | Much stiffer, higher bend radius critical |
| Failure consequences | Severe | Catastrophic (whip energy much higher) |
| AWD importance | High | Absolute (non-negotiable) |
| Water quality | Important | Critical (orifice erosion accelerated) |
| Operator skill | High | Expert / Level 3 Advanced only |

**Note:** Earlier versions of this table incorrectly listed ~160–235 m/s for standard HP. Those values were residual from the Section 16 unit-conversion error and have been corrected to match the verified Bernoulli-derived velocities in Section 16.4.

### 7.17.3 Mandatory Controls for Creeping Hose / 40k psi Tube Bundle Work

1. **Only Level 3 Advanced / UHP Operators** (Chapter 13) may perform this work.
2. **Anti-Withdrawal Device (AWD)** must be correctly installed and verified before every insertion (MCR-019 / MCR-020). Never bypass.
3. Full pre-use inspection with extra focus on hose condition, fittings, and AWD (use the controlled checklist).
4. Reaction force assessment – often exceeds safe handheld limits → use mechanical feeders, reels, or automated systems wherever possible.
5. Vacuum truck or catch system at the outlet end of the tubes to control water, debris, and prevent back-spray.
6. Clear communication protocol between lance operator, pump operator, and vacuum operator.
7. Exclusion zone expanded due to higher energy.
8. Immediate dump capability under operator control at all times.
9. No quick-connects in the high-movement creeping hose run – prefer permanent or screw-type connections.
10. Continuous visual monitoring of the hose as it advances; stop immediately on any abnormal resistance or whip.

### 7.17.4 NLB-Specific Guidance (Practical)

- Follow NLB operation manuals for the specific pump model and pressure configuration.
- Pre-use checks emphasised by NLB: rupture disc, fluid levels, area clear, never leave unattended.
- Plunger size and RPM must be correctly matched for the target 40k psi performance curve.
- Use only hoses and fittings rated and certified for the full operating pressure with appropriate safety factor.
- After any rupture disc activation or unusual event, full system inspection before restart.

### 7.17.5 Common Failure Modes Specific to Creeping Hose / UHP Tube Bundle

- Hose burst or fitting blow-out under high energy
- AWD failure or incorrect installation leading to uncontrolled back-out (highest RPN risk)
- Nozzle blockage causing sudden pressure spike and whip
- Excessive reaction force causing loss of control
- Inadequate vacuum → water/debris blow-back toward operator
- Orifice erosion leading to loss of self-propulsion or incorrect thrust

All of these map directly into the FMEA (Section 20) and must be briefed before every UHP job.

### 7.17.6 Best Practice Sequence for Tube Bundle Cleaning with Creeping Hose

1. Bundle prepared, ends accessible, vacuum system ready.
2. Full pre-use inspection completed and signed.
3. AWD installed and function-tested.
4. Communication check with all parties.
5. Controlled pressure build-up.
6. Controlled insertion and advancement under continuous observation.
7. Monitoring of progress, pressure, and vacuum performance.
8. Controlled withdrawal and pressure dump.
9. Post-job inspection of hose, nozzle, and AWD.

### 7.17.7 Training & Competency Link

This work requires the **ATC-HPWJ-UHP specialty module** (Chapter 13). Operators must hold current Level 3 competency and have demonstrated AWD proficiency and emergency response for injection injuries.

---

**References for this chapter**: WJTA Orange Book, NLB operation manuals, StoneAge tooling guidance, Hammelmann and WOMA technical documentation, Peinemann automated system information, Sugino technical data, relevant hose life-cycle studies, Master Control Register, Chapter 10, Chapter 13, Section 16, Section 20 FMEA.
