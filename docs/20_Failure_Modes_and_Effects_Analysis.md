# Section 20: Failure Modes & Effects Analysis (FMEA-style)

**Version 8.0 – Updated with new candidate site-hazard mode**

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
**Risk Rating**: S=8, L=6, D=4 → **RPN = 192** (High)
**Linked MCR**: MCR-012, MCR-013

### 20.2.2 Rupture Disc Activation / Failure
**Risk Rating**: S=9, L=5, D=3 → **RPN = 135** (High)
**Linked MCR**: MCR-009

### 20.2.3 Overheating / Lubrication Failure (Power End)
**Risk Rating**: S=8, L=4, D=5 → **RPN = 160** (High)

### 20.2.4 Diesel Engine / Drive Failure
**Risk Rating**: S=6, L=5, D=3 → **RPN = 90** (Medium-High)

### 20.2.5 Inlet Water Quality / Filtration Failure
**Risk Rating**: S=7, L=6, D=4 → **RPN = 168** (High)
**Linked MCR**: MCR-013

---

## 20.3 Hose and Fitting Failure Modes

### 20.3.1 Hose Burst / Rupture
**Risk Rating**: S=10, L=4, D=4 → **RPN = 160** (High)
**Linked MCR**: MCR-001, MCR-002, MCR-004, MCR-006

### 20.3.2 Quick-Connect Disconnection Under Pressure
**Risk Rating**: S=9, L=5, D=4 → **RPN = 180** (High)
**Linked MCR**: MCR-007

---

## 20.4 Nozzle and Tooling Failure Modes

### 20.4.1 Nozzle Wear / Orifice Enlargement
**Risk Rating**: S=6, L=7, D=3 → **RPN = 126** (Medium-High)
**Linked MCR**: MCR-018

### 20.4.2 Flex Lance Back-Out / Loss of Control
**Risk Rating**: S=10, L=4, D=5 → **RPN = 200** (Very High)
**Linked MCR**: MCR-019, MCR-020
**Note**: Now backed by documented UK HSE fatality (Case 2 in Incident Library).

### 20.4.3 Automated / Robotic System Failure
**Risk Rating**: S=8, L=4, D=4 → **RPN = 128** (High)

---

## 20.5 Control and Safety System Failures

### 20.5.1 Failure of Pressure Relief / Dump System
**Risk Rating**: S=9, L=4, D=3 → **RPN = 108** (High)
**Linked MCR**: MCR-010

### 20.5.2 Sensor / Auto-Shut-off Module Failure
**Risk Rating**: S=8, L=3, D=5 → **RPN = 120** (High)

---

## 20.6 Human Factor and Operational Failure Modes

### 20.6.1 Loss of Control Due to Excessive Reaction Force
**Risk Rating**: S=9, L=5, D=4 → **RPN = 180** (High)
**Linked MCR**: MCR-016

### 20.6.2 Inadequate Pre-Use Inspection
**Risk Rating**: S=7, L=6, D=5 → **RPN = 210** (Very High)
**Linked MCR**: MCR-023, MCR-024

### 20.6.3 Poor SIMOPS Coordination
**Risk Rating**: S=8, L=5, D=5 → **RPN = 200** (Very High)
**Linked MCR**: MCR-028

### 20.6.4 Inadequate Team Communication
**Risk Rating**: S=7, L=5, D=5 → **RPN = 175** (High)
**Linked MCR**: MCR-025

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

**References**:
- Industry incident databases and lessons learned
- Manufacturer failure mode data
- WJTA and WJA safety guidance
- NIOSH CA/FACE 16CA001
- UK HSE / IMCA / SAFETY4SEA flexi-lance fatality investigation
- Operational experience from major HPWJ contractors
- Master Control Register (linked items)
