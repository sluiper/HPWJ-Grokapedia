# Section 19: Nozzle & Tool Technology Encyclopedia

**Version 8.0**

## 19.1 Purpose

This section centrally explains the nozzle and tooling types that are already referenced across the Encyclopedia (especially Chapters 3, 7, 8 and the Master Control Register) but have not previously been described in one place.  
It is a technology reference only. **No new wear-life numbers, pressure ratings, orifice sizes, or RPM values are introduced.** All enforceable limits remain those already recorded in the Master Control Register and Chapter 7.

## 19.2 Common Nozzle / Tool Types

### 19.2.1 Straight / Jet Nozzles

**What it is:** A fixed orifice that produces a coherent, high-velocity round jet.  
**Typical application:** Deep cleaning of deposits, cutting soft materials, tube cleaning with rigid lances, situations requiring maximum energy density at a point.  
**Governing existing controls:**
- MCR-018 – Nozzle wear life (typically 20–60 h) and rejection for pitting or orifice enlargement.
- MCR-016 – Reaction force must still satisfy the three additive controls.
- MCR-022 – Correct thrust direction must be verified before insertion into tubes or pipes.

### 19.2.2 Fan / Flat Nozzles

**What it is:** A nozzle that produces a flat, fan-shaped spray pattern of defined angle.  
**Typical application:** Surface cleaning, coating removal, large-area vessel walls, where coverage speed is more important than maximum point impact.  
**Governing existing controls:**
- MCR-018 – Wear life and visual/pitting rejection criteria still apply.
- MCR-016 – Reaction force assessment remains mandatory; fan nozzles can produce significant thrust at higher flows.

### 19.2.3 Rotating Nozzles

**What it is:** A nozzle assembly that spins under the reaction of the exiting jets, producing a rotating multi-jet pattern that covers a larger effective area than a single straight jet.  
**Typical application:** Vessel internals, large-diameter pipes, surface preparation where uniform coverage is required without constant operator movement.  
**Governing existing controls:**
- MCR-018 – Wear of orifices and rotating seals/bearings.
- MCR-016 – Reaction force still applies to the tool and hose/lance assembly.
- MCR-021 – If the rotating head is part of an automated or sensor-equipped system, pre-use sensor/interlock testing is required.

**[UNVERIFIED — needs manufacturer data]:** Specific recommended RPM ranges, maximum free-spin speeds, or exact bearing life figures for particular rotating heads are not present in the current MCR or Chapter 7 and are therefore not asserted here. Use manufacturer data for the specific model.

### 19.2.4 Flex Lance Nozzles / Flex Lance Tooling

**What it is:** A small nozzle (or multi-orifice head) attached to a flexible high-pressure hose (flex lance) that is inserted into heat-exchanger tubes, pipes, or other restricted geometries.  
**Typical application:** Tube-bundle cleaning (shell-and-tube heat exchangers), long pipe runs, U-tubes.  
**Governing existing controls (critical):**
- MCR-019 – Anti-Withdrawal Device (AWD) is mandatory and must be correctly installed.
- MCR-020 – AWD + communication + reaction-force control; never bypass.
- MCR-018 – Nozzle wear life still applies.
- MCR-016 – Reaction force of the lance/nozzle combination must be assessed.
- MCR-034 – When used in UHP / creeping-hose mode, Level 3 operators only and expanded controls.

### 19.2.5 Automated / Robotic Tooling Heads (including Hammelmann xPRO-style and similar)

**What it is:** Mechanically or robotically driven heads (lance manipulators, tube-bundle cleaners, vessel cleaning robots, etc.) that may incorporate position sensors, auto-shut-off, or remote control. Examples referenced elsewhere include systems with sensor-based auto-shut-off modules (MCR-021).  
**Typical application:** High-volume tube-bundle cleaning, confined or high-risk access areas, repetitive work where human exposure should be reduced.  
**Governing existing controls:**
- MCR-021 – Pre-use functional test of sensors and auto-shut-off; never bypass safety modules; clear zoning.
- MCR-016 – Reaction force and thrust direction still relevant for the tooling itself.
- MCR-019 / 020 – If flex or creeping elements are present, AWD rules still apply.
- MCR-028 – SIMOPS and zoning when automated systems share space with other work parties.
- MCR-034 – UHP automated work remains Level 3.

## 19.3 Cross-Cutting Rules That Apply to All Nozzle / Tool Types

These already exist and are repeated here only for convenience:

- Wear life and rejection criteria → MCR-018
- Reaction force (three additive controls) → MCR-016
- Correct thrust direction (especially tubes/pipes) → MCR-022
- Pre-use inspection of the entire assembly → MCR-023
- Automated safety systems → MCR-021
- Flex / creeping hose systems → MCR-019, MCR-020, MCR-034

## 19.4 Selection Guidance (Linked to Existing Chapters)

Method and nozzle selection is driven by deposit type, geometry, required pressure band (Chapter 3), and the ability to satisfy the existing MCR controls listed above. Detailed equipment selection and pre-use requirements remain in Chapter 7.

## 19.5 Gaps Explicitly Flagged

- Specific rotating-nozzle RPM ranges, free-spin limits, and model-specific bearing lives → **[UNVERIFIED — needs manufacturer data]**
- Exact orifice sizes and flow tables for every commercial nozzle → use manufacturer data; not restated here to avoid introducing new numbers.
- Any future desire for a hard upper pressure limit on pure handheld straight jets would require a new MCR candidate row rather than a chapter-only assertion.

## Verification Log

| Claim | Status |
|-------|--------|
| No new wear-life, pressure, orifice, or RPM numbers introduced | Confirmed |
| All governing rules cited by existing MCR IDs only | Confirmed (MCR-016, 018, 019, 020, 021, 022, 023, 028, 034) |
| Rotating-nozzle RPM and similar missing data | Explicitly flagged [UNVERIFIED — needs manufacturer data] |
| Scope limited to types already referenced in the repo | Confirmed |

**End of Section 19**
