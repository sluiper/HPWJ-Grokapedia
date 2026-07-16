# Section 22: Global Manufacturer Best Practices & Variations

**Version 8.0**

## 22.1 Purpose

This section synthesises the existing manufacturer summary files in `references/manufacturers/`. It does **not** introduce new manufacturer claims, pressure ratings, or safety features that are not already recorded in those summaries. The goal is a comparative view useful for equipment selection, training, and understanding why certain MCR rules exist.

Manufacturers covered (from existing files): NLB, Hammelmann, StoneAge, Peinemann, WOMA, Kamat, Uraca, Interpump, Jetstream, Sugino, DERC Salotech.

## 22.2 Comparative Overview by Category

| Manufacturer | Primary Strength | Pressure / Application Focus | Automation / Safety Differentiation | Key “Never” Emphasis (from existing summary) |
|--------------|------------------|------------------------------|-------------------------------------|-----------------------------------------------|
| **NLB** (USA) | Diesel triplex field pumps | General industrial & oil & gas HP | Traditional robust units; strong MEA support | Never leave unit running unattended; never ignore rupture disc checks |
| **Hammelmann** (Germany) | Premium pumps + advanced tooling | High-end + robotic systems | xPRO sensor auto-shut-off, JETMASTER robotics, PIPEMASTER reels | Never bypass or disable sensor-based safety modules |
| **StoneAge** (USA) | Tooling specialist (not pumps) | Rotating nozzles, flex lances, automation tooling | Wear-life guidance (20–60 h), reaction-force geometry, fatigue reduction | Never use worn or corrosion-pitted nozzles beyond recommended life |
| **Peinemann** (Netherlands) | Automated tube-bundle cleaning | Up to 40k psi hands-free / semi-automated | Removes operators from direct jet exposure; controlled feed | Never operate automated systems without proper training; never bypass entanglement/feed controls |
| **WOMA** (Germany) | Multi-gun + safety design | Multi-operator simultaneous work; ATEX options | Pressureless-at-rest / fail-safe circulation | Never operate without confirming pressureless-at-rest; never start multi-gun without coordination |
| **Kamat** | High-pressure pump systems | Industrial cleaning | (See individual summary) | Follow manufacturer-specific pre-use and maintenance |
| **Uraca** | High-pressure pumps | Industrial | (See individual summary) | Follow manufacturer-specific pre-use and maintenance |
| **Interpump** | Pumps & systems | Broad industrial | (See individual summary) | Follow manufacturer-specific pre-use and maintenance |
| **Jetstream** | Pumps & tooling | Industrial cleaning | (See individual summary) | Follow manufacturer-specific pre-use and maintenance |
| **Sugino** | Ultra-high pressure / specialised | UHP and specialised applications | (See individual summary) | Follow manufacturer-specific pre-use and maintenance |
| **DERC Salotech** | Tooling & systems | Industrial jetting | (See individual summary) | Follow manufacturer-specific pre-use and maintenance |

## 22.3 Pressure Class & Application Specialisation (from existing summaries)

- **Traditional high-volume field work** → NLB-style diesel triplex units are repeatedly noted for robust field performance and regional support.
- **UHP / tube-bundle automation** → Peinemann systems are explicitly described as capable up to 40,000 psi and focused on hands-free tube cleaning; Hammelmann JETMASTER / PIPEMASTER and StoneAge automated tooling also sit in this space.
- **Multi-operator / multi-gun work** → WOMA Twin-Jet / multi-gun capability (up to 6 guns) is the clearest existing example.
- **Hazardous area (ATEX)** → WOMA is the manufacturer whose existing summary explicitly highlights ATEX-certified options for Zone 2.
- **Tooling-only specialists** → StoneAge and Peinemann do not make pumps; they are paired with OEM pumps (NLB, WOMA, etc.).

## 22.4 Automation Capability Spectrum (existing content only)

1. **Manual / conventional** – NLB-style units with standard guns and lances.  
2. **Semi-automated / rotating tooling** – StoneAge rotating nozzles and flex systems that reduce operator fatigue.  
3. **Sensor-based safety** – Hammelmann xPRO (detects irregular movement and shuts off high pressure).  
4. **Hands-free / robotic tube cleaning** – Peinemann automated feed systems and Hammelmann JETMASTER-style robotics.  

These distinctions already appear in the manufacturer summaries and are the reason MCR-021 (automated tooling safety) and MCR-034 (UHP creeping-hose / Level 3) exist.

## 22.5 “Never Rules” Emphasised by Manufacturers (synthesised from existing files)

| Never Rule (already recorded) | Source Manufacturer Summaries |
|-------------------------------|-------------------------------|
| Never leave the pump running unattended | NLB (and echoed as universal practice) |
| Never bypass or ignore rupture disc checks | NLB |
| Never bypass or disable sensor-based safety modules | Hammelmann |
| Never use worn or corrosion-pitted nozzles beyond recommended life | StoneAge |
| Never operate automated systems without proper training / competency | Peinemann |
| Never bypass entanglement prevention or feed-control safety features | Peinemann |
| Never operate without confirming pressureless-at-rest functionality (where fitted) | WOMA |
| Never start multi-gun operations without agreed coordination procedures | WOMA |

These manufacturer-specific “Never” statements map directly onto existing MCR items (MCR-011, MCR-009, MCR-021, MCR-018, MCR-034, MCR-025, etc.).

## 22.6 Regional Support Notes (from existing summaries)

- NLB is explicitly noted for good parts and service support in the Middle East / Africa region — relevant for Anabeeb operations in KSA.
- Other manufacturers’ regional support strength is not detailed in the current summary files and is therefore not asserted here.

## 22.7 Observations (not manufacturer claims)

- **Observation 1:** No single manufacturer summary currently covers the full stack (pump + advanced robotics + ATEX + multi-gun + creeping-hose tooling) in one product line. Hybrid fleets (e.g., NLB or WOMA pump + StoneAge or Peinemann tooling) are the practical norm reflected in the existing files.
- **Observation 2:** The strongest common thread across all summaries is pre-use inspection discipline and “never leave unattended / never bypass safety devices.” These are already elevated to high-RPN MCR controls.
- **Observation 3:** Detailed model-specific RPM ranges, exact free-spin limits, or quantitative reliability data for rotating heads remain outside the current manufacturer summaries and stay flagged as [UNVERIFIED — needs manufacturer data] (see also Section 19).

## 22.8 How to Use This Section

- Equipment selection and tender technical evaluation.
- Training (why different systems have different safety modules and Never Rules).
- Mapping manufacturer guidance back to the Master Control Register.
- Identifying where a hybrid system (pump from one OEM + tooling from another) requires combined controls from both summaries.

Always refer back to the individual files in `references/manufacturers/` for the full text of each summary.

## Verification Log

| Claim | Status |
|-------|--------|
| All manufacturer statements drawn only from existing Summary.md files | Confirmed |
| No new pressure ratings, RPM values, or safety features invented | Confirmed |
| Comparative table and Never Rules synthesised, not fabricated | Confirmed |
| Gaps and hybrid-fleet observations clearly labelled as observations | Confirmed |
| Links to existing MCR items only | Confirmed |

**End of Section 22**
