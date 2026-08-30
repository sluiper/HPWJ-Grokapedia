# Verification Report — HPWJ 3-Day Training Pack (Claude, Independent Reviewer)

**Date:** 2026-07-21 · **Scope:** claude/ pack (deck + 3 trainer scripts + exam paper + marking key + field verification checklist) vs MASTER_CONTROL_REGISTER.md (65 rows Visible) and docs/13 v8.2
**Role per AGENTS.md:** independent re-derivation + consistency review. No drafting, no push.

## Numeric verification — PASS

| Control | Pack | MCR | Verdict |
|---------|------|-----|---------|
| Reaction force constants | 0.052 imperial (×6), 0.233 metric (×4); zero instances of defective 0.745 | MCR-017 (corrected 16 Jul 2026) | ✓ |
| Worked example Day 1 | 10 GPM @ 15,000 psi → 283 N (fails 250 N) | re-derived: 0.052×10×√15000 = 63.7 lbf = 283.3 N | ✓ |
| Exam Q41 | 0.052×8×110 ≈ 45.8 lbf ≈ 204 N, passes | re-derived 203.5 N | ✓ |
| Exam Q42 | 0.233×40×34.6 ≈ 322 N, fails | re-derived 322.5 N | ✓ |
| Three additive checks | 250 N + ⅓ body weight + geometry | MCR-016 | ✓ |
| System ceiling 40,000 psi | ✓ (×11) | MCR-046 | ✓ |
| Shotgun ≤10,000 psi / ≤1.6 mm | ✓ | MCR-050 | ✓ |
| Rupture disc ≤1.2× lowest MAWP | ✓ | MCR-048 | ✓ |
| Team minimum 3 + dedicated e-stop | ✓ | MCR-047 | ✓ |
| 10 m exclusion | ✓ | MCR-051 | ✓ |
| Tip mark ≥600 mm | ✓ | MCR-052 | ✓ |
| Hose life 2 y / 4 y + annual 3rd-party test | ✓ | MCR-001/002 | ✓ |
| Nozzle wear 20–60 h, pin gauge | ✓ | MCR-018 | ✓ |
| Lance ≥1.2 m | ✓ | MCR-044 | ✓ |
| Exam: 70 marks, pass 56 = 80%; blueprint 40/70 ≈ 57% core rules (≥30% req), 14/70 = 20% injury response (≥20% req) | ✓ arithmetic verified | Ch13 §Theory | ✓ |
| Certificate validity 24 months + VoC refresher | ✓ | Ch13 | ✓ |

Terminology: deck states **NEBOSH Verified** — correct per current ANABEEB programme (human-confirmed 21 Jul; the Endorsed guidance PDF in ~/Desktop/nebosh is the superseded programme).

## Findings

**P1 — Field Verification checklist is 8 items; Ch13 v8.2 mandates 15.**
`field_verification_checklist.docx` covers Ch13 items 1,2,3,4,6,7,8,9. Missing as distinct critical items: tip-mark 600 mm (5), hose handling/bend radius (10), automation/hierarchy awareness (11), team-of-3 verification (12, MCR-047), rupture-disc rating check (13, MCR-048), shotgun limits (14, MCR-050), 10 m exclusion (15, MCR-051). Deck slide 35 and Day-3 script reflect the same 8-item set. **Human decision required:** expand pack to 15 (recommended — matches SSOT and latest commit intent) or document rationale for the 8-item instrument.

**P2 — Alignment ripple:** if P1 resolves to 15 items, deck slide 35 + Day-3 trainer script + exam blueprint note should be updated in the same delivery package (AGENTS.md rule 6).

**P3 (minor) —** Exam paper questions not yet line-checked 1:1 against the marking key beyond spot checks and full numeric grep (clean). Recommend one full pass before print.

## Not in scope / not blocking
Videos are delivery media rendered from this (verified) content; they do not alter the controlled numbers.
