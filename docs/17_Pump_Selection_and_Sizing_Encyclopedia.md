# Section 17: Pump Selection & Sizing Encyclopedia

**Version 8.0**

## 17.1 Purpose

This section is a focused reference for pump selection and sizing. It pulls **only** from the plunger-sizing relationships, worked examples, and manufacturer pressure-class notes already present in Chapter 7 and the manufacturer summaries.  
No new sizing formulas or affinity-law extensions beyond those already verified in Chapter 7 are introduced.

## 17.2 Core Principle (from Chapter 7)

A high-pressure water jetting pump displaces a fixed volume of water. Pressure is created by the restriction at the nozzle (or other orifice).  
Selection is therefore a balance of:
- Required cleaning pressure (deposit hardness)
- Required flow (cleaning speed / coverage)
- Available power
- Reaction-force limits (MCR-016)
- Hose, fitting and rupture-disc ratings after any plunger change (MCR-015)

## 17.3 Plunger Diameter Relationships (Existing Chapter 7 Math)

For a given pump (fixed RPM and power):

- **Flow ∝ (Plunger Diameter)²**
- New Flow = Old Flow × (New Diameter / Old Diameter)²
- New Pressure ≈ Old Pressure × (Old Flow / New Flow)

These are the only sizing relationships used in this section. They are the same approximate relationships already shown and worked in Chapter 7.

### Worked Example 1 (from Chapter 7 – Increasing Pressure)
Current: 15 mm plungers delivering 10 000 psi at 80 L/min.  
Change to 12 mm plungers.

- New Flow ≈ 80 × (12/15)² = 80 × 0.64 = **51.2 L/min**
- New Pressure ≈ 10 000 × (80 / 51.2) ≈ **15 625 psi**

### Worked Example 2 (from Chapter 7 – Increasing Flow)
Current: 12 mm plungers delivering 15 000 psi at 50 L/min.  
Change to 14 mm plungers.

- New Flow ≈ 50 × (14/12)² = 50 × 1.36 ≈ **68 L/min**
- New Pressure ≈ 15 000 × (50 / 68) ≈ **11 030 psi**

**Always** re-verify hose, fitting, and rupture-disc ratings after any plunger change (MCR-015). Cross-check final numbers against the specific pump manufacturer’s performance data or software.

## 17.4 Power Relationship (Existing)

Approximate hydraulic power (already used in Chapter 7 and Section 16):

$$ \text{HP} \approx \frac{P\ (\text{psi}) \times Q\ (\text{GPM})}{1714} $$

Or in SI form: Power (kW) ≈ (Pressure × Flow) / Efficiency, with modern triplex efficiencies typically in the 80–90 % range for the hydraulic end. Overall system efficiency is lower (see Section 16.14).

## 17.5 Selection by Application Class (from Chapter 7 examples)

| Application | Typical Pressure Band | Flow Priority | Preferred Configuration Notes (from Ch7) |
|-------------|-----------------------|---------------|------------------------------------------|
| Surface preparation / coating removal | High (≈15–20k+ psi) | Moderate | Smaller plungers, strong reaction-force control (MCR-016) |
| Tube bundle / heat exchanger (manual or flex) | 10–15k psi (higher flow) or UHP for hard deposits | High | Larger plungers or higher-flow unit; AWD mandatory (MCR-019/020) |
| UHP creeping hose / 40k class tube work | 30–40k+ psi | Lower flow, high energy | Level 3 only (MCR-034); mechanical feed preferred |
| Multi-gun / multi-operator | Medium–high | High total flow | WOMA-style multi-gun systems; coordination critical |
| Automated / robotic | Match tooling design pressure | Match tooling design flow | Sensor / interlock testing (MCR-021) |

## 17.6 Manufacturer Pressure-Class Notes (from existing summaries only)

- **NLB**: Diesel triplex units widely used for general industrial and oil & gas work; robust field performance; good MEA support.
- **WOMA**: Multi-gun capability and pressureless-at-rest design; ATEX options.
- **Hammelmann**: Premium pumps + strong robotic / sensor-based systems (xPRO, JETMASTER).
- **Kamat / Uraca / Interpump / Jetstream / Sugino**: Covered in their individual manufacturer summaries for high-pressure or specialised roles.
- **StoneAge / Peinemann / DERC Salotech**: Tooling and automation specialists; not primary pump OEMs — always paired with a suitable pump.

No new maximum-pressure or flow figures are asserted beyond what already appears in Chapter 7 and the manufacturer summary files.

## 17.7 Mandatory Checks After Sizing / Plunger Change

Before the unit is released to the field:
1. Confirm new pressure does not exceed hose, fitting, and tool MAWP.
2. Fit and tag correctly rated rupture disc; spare on unit (MCR-009).
3. Re-verify dump / pressure-relief system function (MCR-010).
4. Confirm reaction force for the planned nozzle will satisfy MCR-016.
5. Update pre-use inspection records and any job technical specification (Chapter 4).

## 17.8 Gaps Explicitly Flagged

- Exact affinity-law corrections for RPM changes on a specific pump model → use manufacturer performance curves or software; not generalised further here.
- Model-specific minimum/maximum plunger diameters → manufacturer data only.
- Any desire for a hard “never exceed” handheld pressure limit must be added as a new MCR candidate rather than asserted only in this section.

## Verification Log

| Claim | Status |
|-------|--------|
| Plunger diameter / flow / pressure relationships | Taken verbatim from existing Chapter 7 worked examples |
| Power formula | Same as already verified in Section 16 / Chapter 7 |
| Application selection table | Synthesis of Chapter 7 examples only |
| Manufacturer notes | Drawn only from existing manufacturer summaries and Ch7 |
| No new sizing formulas or numeric thresholds | Confirmed |
| Post-change mandatory checks | Linked only to existing MCR items |

**End of Section 17**
