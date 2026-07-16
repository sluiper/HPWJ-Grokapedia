# Section 26: Human Factors & Ergonomics

**Version 8.0**

## 26.1 Purpose

This section consolidates the human-factor and ergonomic issues already recognised across the Encyclopedia (especially MCR-033, MCR-025, MCR-016, and the FMEA human-factor modes in Section 20.6). It does **not** introduce new numeric ergonomic thresholds (lifting limits, maximum shift lengths, maximum continuous handheld time, etc.) unless they already exist in the Master Control Register. Any such figure that is not already recorded is flagged **[UNVERIFIED]** rather than asserted.

## 26.2 Why Human Factors Matter in HPWJ

High-pressure water jetting combines:
- High reaction forces that must be continuously controlled (MCR-016)
- High ambient temperatures and full PPE (especially critical in Jubail / KSA summers – MCR-033)
- Noise, vibration, and communication challenges (MCR-025)
- Repetitive high-attention tasks under production pressure
- The knowledge that a single moment of lost control or skipped control can produce a life-changing injury (Chapter 10 / Section 24)

These conditions make fatigue, heat stress, communication breakdown, and normalisation of deviance primary risk drivers — not secondary “soft” issues.

## 26.3 Fatigue and Reaction-Force Control

The three additive reaction-force controls (MCR-016) assume the operator can maintain stance, grip, and attention. Fatigue degrades all three:
- Reduced ability to resist force → higher chance of loss of stance
- Slower reaction time to pressure changes or hose movement
- Increased likelihood of shortcutting pre-use or AWD checks under time pressure

**Existing link:** FMEA 20.6.1 (Loss of Control Due to Excessive Reaction Force) already lists fatigue and poor body positioning as causes. No new numeric shift-length or continuous-handheld-time limit is introduced here. Any future hard limit would need to be added as a new MCR candidate after operational and medical review.

## 26.4 Heat Stress Interaction (MCR-033)

MCR-033 already requires mandatory work/rest/hydration/shade controls in high ambient temperatures. Heat stress interacts with HPWJ human factors in several ways already recognised in the repository:
- Full PPE (including waterproof outer layers) increases heat load.
- Dehydration and elevated core temperature reduce fine motor control and decision quality.
- Heat exhaustion or heat stroke can produce sudden loss of control of the lance or gun.
- The Incident Library includes a composite case (Case 12) specifically for heat-related loss of control in KSA conditions.

**Practical implication already in force:** heat-stress controls are primary safety controls for HPWJ in the Eastern Province, not comfort measures. They sit alongside AWD and reaction-force rules, not below them.

## 26.5 Communication Breakdown Under Stress (MCR-025)

MCR-025 requires clear radio / hand-signal protocols and stop-work on communication failure. FMEA 20.6.4 rates inadequate team communication at RPN 175.

Under fatigue, heat, or high production pressure:
- Radio discipline slips
- Hand signals become ambiguous or ignored
- Assumptions replace confirmation (“he knows what I mean”)

The existing rule remains absolute: any breakdown in communication between nozzle operator and pump operator requires immediate dump and stop. No new threshold is added; the existing stop-work authority is simply re-emphasised as a human-factors control.

## 26.6 Complacency and Normalisation of Deviance

Normalisation of deviance is the gradual acceptance of risk that was previously recognised as unacceptable (skipped pre-use items, “just this once” AWD shortcuts, production pressure overriding stop-work, etc.).

It is already implicit in the highest-RPN FMEA mode (Inadequate Pre-Use Inspection, RPN 210) and in the documented UK HSE flexi-lance fatality (Incident Library Case 2), where training/supervision failures and missing safety devices were causal.

**Controls already in place that combat normalisation:**
- Mandatory documented pre-use inspection (MCR-023) + supervisor verification (MCR-024)
- Supervisor accountability (MCR-036)
- Absolute Never Rules (Chapter 9 / MCR-038)
- 30-day incident / near-miss feedback into FMEA and MCR (Chapter 15)
- Competency reassessment and stop-work authority (Chapter 12 & 13)

No new behavioural metric is introduced. The existing system relies on hard procedural gates and supervisor accountability rather than on unmeasured “culture” claims.

## 26.7 Ergonomics of Tooling and Stance

Existing guidance already used in the repository:
- Reaction force ≤ 250 N and ≤ 1/3 body weight (MCR-016)
- Barrel geometry that prevents the jet crossing the operator’s own feet/legs (MCR-016 / StoneAge guidance)
- Preference for mechanical assistance or automation when force or duration makes pure handheld work unsustainable (MCR-021, Peinemann / Hammelmann systems)

**[UNVERIFIED]:** Specific recommended maximum continuous handheld time, maximum number of consecutive tube insertions, or anthropometric lifting / carrying limits for hose and tooling are not present in the current MCR and are therefore not asserted. They would require ergonomic / occupational-health review before becoming enforceable rules.

## 26.8 Practical Human-Factors Checklist (Planning & Execution)

Drawn only from existing controls:
- Is the planned reaction force within MCR-016 for the named operators?
- Are heat-stress controls (MCR-033) defined for the expected ambient conditions and PPE?
- Is communication method and stop-work rule briefed and confirmed (MCR-025)?
- Is pre-use inspection time protected from production pressure (MCR-023 / 024)?
- Are Level / competency matches correct, especially for UHP or automated work (MCR-030 / 034)?
- Is stop-work authority understood and backed by the supervisor (MCR-036 / 038)?

## 26.9 Summary

Human factors in HPWJ are not soft additions; they are the reason the highest-RPN failure modes exist. Fatigue, heat, communication failure, and normalisation of deviance all degrade the same critical controls (reaction force, AWD, pre-use inspection, dump authority). The Master Control Register and FMEA already treat them as such. This section simply makes the connections explicit without inventing new numeric limits.

## Verification Log

| Claim | Status |
|-------|--------|
| Heat stress controls | MCR-033 and Incident Library Case 12 |
| Communication failure | MCR-025 and FMEA 20.6.4 |
| Reaction force + fatigue | MCR-016 and FMEA 20.6.1 |
| Pre-use / complacency | MCR-023/024 and FMEA 20.6.2 (RPN 210) |
| No new ergonomic numeric thresholds | Confirmed – any missing limits flagged [UNVERIFIED] |
| All content traced to existing MCR / FMEA / chapters | Confirmed |

**End of Section 26**
