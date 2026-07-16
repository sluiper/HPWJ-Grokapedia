# Section 27: Lessons Learned

**Status:** Drafted on branch `draft/section-27` – Claude Verification Report complete (zero P0/P1) – awaiting human gate  
**Version:** 8.4-draft  
**Date:** 16 July 2026  
**MCR Controls Referenced:** Existing high-RPN controls + proposed MCR-061 to MCR-065

## MCR Mapping for This Section

| ID | Topic | Status |
|----|-------|--------|
| MCR-023 | Pre-Use Inspection Mandatory | Visible |
| MCR-020 | Flex Lance Back-Out Prevention | Visible |
| MCR-028 | SIMOPS Coordination | Visible |
| MCR-016 | Reaction Force (Three Additive) | Visible |
| MCR-007 | Quick-Connect Couplings | Visible |
| MCR-036 | Supervisor Accountability | Visible |
| MCR-061 | Living Lessons Learned Register | Drafting |
| MCR-062 | 30-Day Incident-to-Lesson Cycle | Drafting |
| MCR-063 | Anonymised Real Incident Capture | Drafting |
| MCR-064 | Training Integration of Lessons | Drafting |
| MCR-065 | Management Review of Lessons | Drafting |

---

## 27.1 Purpose & Scope

This section turns the abstract controls in the Master Control Register and the case studies in Section 25 into a living, continuously improving system of organisational learning.  
It exists so that every real Anabeeb near-miss, incident, or significant observation is converted into a permanent, actionable lesson that strengthens future training, procedures, and the MCR itself. [SYNTHESIS]

It is deliberately designed to grow. The first version seeds the process with the documented public fatality and the highest-RPN composite patterns already in Section 25. Future real Anabeeb events will be added under the rules defined here.

---

## 27.2 Relationship to Other Sections

- **Section 20 (FMEA)** supplies the risk prioritisation (RPN).
- **Section 25 (Incident Case Study Library)** supplies the detailed narrative cases used for training. Note: Section 25 already contained the convention “add a new anonymized entry within 30 days”; MCR-062 formalises that existing convention into a controlled process rule.
- **This Section 27** owns the *process* by which new events become permanent organisational memory and trigger MCR or procedure updates.
- **Chapter 13 (Competency & Training)** and **Chapter 15 (HSE Assurance)** consume the outputs.

---

## 27.3 Core Process Rules (Proposed MCR-061 to MCR-065)

### MCR-061 – Living Lessons Learned Register
A single living register of lessons shall be maintained (this section + linked entries in Section 25). Every entry must map to one or more MCR controls and, where relevant, an FMEA mode. [SYNTHESIS]

### MCR-062 – 30-Day Incident-to-Lesson Cycle
Any Anabeeb HPWJ-related near-miss, incident, or significant observation shall be converted into a structured lesson entry within **30 calendar days** of the event (or of the investigation closing). Delay beyond 30 days requires written justification from the QHSSE Manager. [SYNTHESIS – formalises the 30-day convention already stated in Section 25 “How to Use”]

### MCR-063 – Anonymised Real Incident Capture
Real Anabeeb events shall be recorded in anonymised form that preserves the technical and human-factor learning while protecting individuals and commercial sensitivity. Documented public cases (e.g. the UK HSE flexi-lance fatality) remain fully attributed. [SYNTHESIS + existing Section 25 rule]

### MCR-064 – Training Integration of Lessons
Every new lesson that maps to an RPN > 150 control, or that reveals a previously unrecognised failure mode, shall be incorporated into the next scheduled ATC HPWJ training cycle (or earlier if critical). [SYNTHESIS – links to Chapter 13]

### MCR-065 – Management Review of Lessons
The QHSSE Manager shall review the Lessons Learned register at least quarterly and after any serious event. The review shall decide whether any MCR row needs strengthening, any procedure needs amendment, or any additional training is required. [SYNTHESIS – continuous improvement]

---

## 27.4 Seed Lessons (from existing high-value cases)

These are the initial permanent lessons extracted from Section 25. Future real Anabeeb events will be added in the same format.

### Lesson LL-001 – AWD is Life-Critical (from Documented Case 2)
**Event type:** Real regulatory fatality (UK HSE)  
**What must never be forgotten:** A missing or un-verified anti-withdrawal / anti-ejection device on a flexi-lance, combined with inadequate training and supervision, killed a worker.  
**MCR that would have prevented it:** MCR-019 + MCR-020 + MCR-023 + MCR-030 + MCR-036  
**Permanent rule reinforcement:** Flexible lance without a correctly installed and verified AWD is **Not Permitted**. Pre-use inspection must specifically verify the AWD.  
**Training action:** Case 2 is mandatory on Day 1 and Day 3 of every ATC HPWJ course.  
**Source:** UK HSE investigation (via SAFETY4SEA Dec 2020 + IMCA Safety Flash). [CITATION]

### Lesson LL-002 – Pre-Use Inspection is the Highest RPN for a Reason
**Event type:** Composite pattern (RPN 210)  
**What must never be forgotten:** Starting work without a complete, documented, supervisor-verified pre-use inspection (including spare rupture disc, whip checks, hose condition, dump function) is the single most frequent preventable precursor to serious events.  
**MCR:** MCR-023 + MCR-009 + MCR-024  
**Permanent rule reinforcement:** No permit without completed and verified pre-use inspection checklist.  
**Training action:** Live demonstration of a full pre-use inspection is mandatory in every course.  
**Source basis:** WJTA Best Practices + OEM manuals + FMEA. [SYNTHESIS]

### Lesson LL-003 – SIMOPS Requires Named Daily Coordination
**Event type:** Composite pattern (RPN 200)  
**What must never be forgotten:** HPWJ mist + hot work or other incompatible activities without physical zoning and a named daily SIMOPS meeting has repeatedly produced ignition or interference events.  
**MCR:** MCR-028  
**Permanent rule reinforcement:** Daily SIMOPS meeting with recorded attendance and zoning plan is mandatory whenever interfaces exist.  
**Training action:** SIMOPS scenario exercise on Day 2.  
**Source basis:** Process safety literature + client PTW/SIMOPS expectations. [SYNTHESIS]

### Lesson LL-004 – Three Additive Reaction-Force Controls Are Non-Negotiable
**Event type:** Composite pattern (RPN 180)  
**What must never be forgotten:** Exceeding any one of the three additive limits (≤250 N absolute, ≤1/3 body weight, geometry that prevents jet over own feet/legs) has repeatedly produced loss-of-control injuries.  
**MCR:** MCR-016 (+ MCR-054 underwater)  
**Permanent rule reinforcement:** All three must be satisfied; calculation and geometry check are part of pre-use.  
**Training action:** Live reaction-force calculation and stance drills.  
**Source basis:** Verified Fr formula (Section 16) + manufacturer guidance. [DERIVED + CITATION]

### Lesson LL-005 – Quick-Connects Are High-Risk in Dynamic Service
**Event type:** Composite pattern (RPN 180)  
**What must never be forgotten:** Quick-connect couplings that can rotate or whose latches are worn have caused violent hose whip under pressure.  
**MCR:** MCR-007  
**Permanent rule reinforcement:** Prefer screw-type or face-seal couplings wherever relative movement or rotation is possible. No quick-connects on high-pressure hoses in high-movement runs.  
**Training action:** Coupling inspection and rejection criteria practical.  
**Source basis:** Manufacturer warnings + industry alerts. [CITATION]

### Lesson LL-006 – Supervisor Accountability Cannot Be Delegated
**Event type:** Composite pattern  
**What must never be forgotten:** When supervisors fail to enforce stop-work authority, competency verification, or pre-use quality, the organisation loses its last line of defence.  
**MCR:** MCR-036 + MCR-030 + MCR-038  
**Permanent rule reinforcement:** Project Manager overall responsibility cannot be delegated (OPS-P-019). Supervisors are personally accountable for the quality of the controls.  
**Training action:** Supervisor-specific module on accountability and stop-work.  
**Source basis:** Chapter 12 + OPS-P-019 §6.1. [CITATION]

---

## 27.5 How New Lessons Are Added (Operating Procedure)

1. Event occurs or investigation closes.
2. Within 30 days (MCR-062) the QHSSE team produces a structured entry using the template below.
3. Entry is added to this section (and a corresponding short case is added to Section 25 if it is training-valuable).
4. Any required strengthening of an existing MCR row, or creation of a new MCR row, is proposed immediately.
5. Training materials are updated per MCR-064.
6. Quarterly management review (MCR-065) confirms the lesson has been absorbed.

### Template for New Lesson Entry

```markdown
### Lesson LL-XXX – [Short Title]
**Event type:** Real Anabeeb (anonymised) / Documented public / Composite pattern  
**Date of event / investigation close:**  
**What must never be forgotten:**  
**MCR that would have prevented it / that is reinforced:**  
**Permanent rule reinforcement:**  
**Training action:**  
**Source / investigation reference:**  
**FMEA link (if new or changed RPN):**  
```

---

## 27.6 Current Status of the Living Register

| Lesson ID | Title | Type | Linked MCR | Status |
|-----------|-------|------|------------|--------|
| LL-001 | AWD is Life-Critical | Documented public fatality | 019, 020, 023, 030, 036 | Active |
| LL-002 | Pre-Use Inspection Highest RPN | Composite | 023, 009, 024 | Active |
| LL-003 | SIMOPS Daily Coordination | Composite | 028 | Active |
| LL-004 | Three Additive Reaction Force | Composite | 016, 054 | Active |
| LL-005 | Quick-Connects High Risk | Composite | 007 | Active |
| LL-006 | Supervisor Accountability | Composite | 036, 030, 038 | Active |

Future real Anabeeb lessons will be appended here.

---

## 27.7 Remaining Gaps (Honest)

- No real Anabeeb incidents or near-misses have been logged yet (by design — this first version is seeded only from the public documented fatality and the existing high-RPN composite cases in Section 25).
- MCR-062 (30-day cycle) and MCR-065 (quarterly management review) cadence are therefore untested in live Anabeeb operations.
- Future value of this section depends entirely on disciplined capture of real events under the rules defined above.

---

## 27.8 Verification Log

| Claim | Method | Source | Status |
|-------|--------|--------|--------|
| Documented fatality details (LL-001) | Cross-checked against public HSE / SAFETY4SEA / IMCA reporting | Section 25 Case 2 + original sources | **Verified** |
| All other seed lessons | Extracted from existing high-RPN FMEA modes and Section 25 composites | Section 20 + Section 25 | **Verified as patterns** |
| 30-day cycle (MCR-062) | Formalises the existing 30-day convention already stated in Section 25 “How to Use” | Section 25 + industry learning-system good practice | **[SYNTHESIS]** |
| Quarterly management review (MCR-065) | Continuous-improvement principle | Chapter 15 + ISO-style management review | **[SYNTHESIS]** |
| Anonymisation rule | Existing Section 25 discipline + data-protection good practice | Section 25 | **Verified** |

**No new hard numeric claims are introduced in this section.**  
All proposed MCR-061–065 remain in Drafting status pending human gate.

---

**End of Section 27 (draft – Claude clean)**

This section is intentionally process-oriented rather than narrative-heavy. Its value will grow as real Anabeeb events are added under the rules defined here.
