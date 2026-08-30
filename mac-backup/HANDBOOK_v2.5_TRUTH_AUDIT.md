# Truth audit — ATC-HPWJ-OP-001 Learner Handbook v2.5

**Document under test:** `/Users/ab71000372/Downloads/ATC-HPWJ-OP-001_Learner_Handbook_v2.5.docx`  
**Date on cover:** 30 August 2026  
**Audit date:** 30 August 2026  
**Question asked:** treat this handbook as the only truth — find gaps and non-truths.

**Verdict: do not treat v2.5 as the only truth yet.**

The teaching spine (three-layer rules, three reaction-force checks, 1.2× disc, 2/4 year hose + annual proof, three-person team, 10 m unauthorised line, dump-owns-pressure ladder, catcher ≠ stinger) is internally coherent and matches the locked MCR numbers that matter for an operator.

It is **not** clean enough to be the single source of truth. The cover makes a claim that is not evidenced. Appendix A contradicts Chapter 1 on what 10 000 psi is. Level 2 is written as if 40 000 psi work sits inside this certificate, which the competency framework reserved for Level 3. The 15-item Field Verification dropped the tip-mark item. Several MCR hard rules were softened or omitted.

Checked against: Master Control Register v8.5.1; OPS-P-019 summary; Grokapedia Ch3 / Ch8 / Ch11 / Ch13; ATC-HPWJ-OP-001 pack (`00_Course_Specification.md`, `03_Practical_Competency_Checklist.md`); WJTA 2024 videos and FV checklists.

---

## What actually checks out (keep)

Worked reaction-force sums are correct:

| Example | Check |
| --- | --- |
| 10 GPM @ 15 000 psi → 63.7 lbf → 283 N | Fail 250 N. True. |
| 8 GPM @ 10 000 psi → 41.6 lbf → 185 N | Pass 250 N. True. |
| 6 GPM @ 15 000 psi → 38.2 lbf → 170 N | Pass 250 N. True. |
| 40 L/min @ 1 000 bar → 0.233 × 40 × √1000 ≈ 294 N | Fail 250 N. True. Uses the **corrected** 0.233 constant (MCR-017), not the old 0.745 error. |
| 60 kg → 1/3 ≈ 196 N; 90 kg → 1/3 ≈ 294 N | True. |

Locked course numbers that match MCR / OPS-P-019:

| Handbook | MCR / source |
| --- | --- |
| 250 N + 1/3 body weight + geometry | MCR-016 |
| Imperial 0.052 / metric 0.233 | MCR-017 |
| Disc ≤ 1.2 × lowest-rated live part, spare, single-use | MCR-009 / 048 |
| Hose lance/whip 2 y, supply 4 y, pump-mounted 4 y from **fabrication**, + annual proof | MCR-001 / 002 + WJTA 2024 hose video |
| Ceiling 40 000 psi | MCR-046 |
| Shotgun not above 10 000 psi; orifice ≤ 1.6 mm (as two hard limits) | Stricter reading of MCR-050 |
| Team of three, no lone working | MCR-047 |
| 10 m unauthorised persons, dump on breach | MCR-051 |
| Tip mark ≥ 600 mm | MCR-052 (taught; **not** in the 15 items — see below) |
| Catcher pull-test; flex without AWD not permitted | MCR-019 / 020 |
| Whip checks both sides | MCR-006 |
| Shroud 6 ft at gun/lance joint; burst shroud is scrap | MCR-045 + WJTA notes |
| Pressure-up: flush nozzle-off → low → half → full; dump first on the way down | WJTA 2024 shotgun video + FV checklist |
| 80% written + all 15 practical + card | Course spec / Ch13 |

Colour chart is correctly labelled as convention, not a locked number. 40 000 psi → 2 750 bar on that chart is WJTA rounding (exact conversion is ≈ 2 758 bar per MCR-046). Fine if the mark on the part still wins.

---

## Non-truths (false or not evidenced)

### N1. Cover: “NEBOSH Verified Programme”

The masthead is:

> ATC-HPWJ-OP-001 · **NEBOSH Verified Programme** · Chapters 0 to 20

Nothing in Grokapedia, the course spec, or the MCR records a NEBOSH verification, accreditation, or licence for this syllabus. The encyclopedia only says NEBOSH **principles** are embedded. ATC success metrics still list TVTC recognition as a target, not a fact.

**This is the most dangerous sentence in the book.** A learner, a client, or a regulator can treat it as an external stamp. Unless there is a NEBOSH letter on file dated for this syllabus, strike it. Replace with the training-provider name and, if true, “NEBOSH-style risk principles used in teaching.”

### N2. Appendix A: 10 000 psi is “the top of the high-pressure band”

Appendix A:

> 10 000 psi shotgun cap … **Aligns with the top of the high-pressure water-cleaning band** in the same four-band list.

Chapter 1 table:

> High pressure | **About 10 000 to 20 000 psi**

So 10 000 psi is the **floor** of the HP band in this same book, not the top. There is also no four-band list in Chapter 1 (three rows: HP, higher-pressure/UHP, above course).

The shotgun cap is a **method** cap (MCR-050), not a band-edge. The appendix sentence is false. It will confuse anyone who tries to reconcile Chapter 1 with the shotgun never-rule.

### N3. Level 2 certificate “may assess” 25 000–40 000 psi work

Cover table + word list + Chapter 1:

> 25 000 to 40 000 psi is **inside this certificate** only as a higher-pressure band.  
> This course **may assess work in that band up to 40 000 psi**.

Grokapedia Chapter 13 competency table:

| Level | Title | Unsupervised |
| --- | --- | --- |
| 2 | HPWJ Operator | Yes (**Class B**) |
| 3 | Advanced / **UHP Operator** | Yes (**up to 40k psi**). Pathway: Level 2 + **specialty modules** |

MCR-034 puts UHP creeping-hose / 40k bundle work on Level 3. The handbook correctly keeps creeping-hose, robots, and auto-indexers **out**. It still sells 25–40k as in-certificate for a Level 2 operator.

That is a scope non-truth against the framework this course is supposed to implement. Either:

- lock this certificate at the HP band (≤ 20 000 psi) plus awareness of the higher band, or
- rename the output Level 3 / add the UHP module and change Ch13.

Do not leave “Level 2” on the cover and “may assess up to 40 000 psi” in Chapter 1.

### N4. Short lance: missing the double-trigger lock

Chapter 13.1 / front table:

> Lance not shorter than 1.2 m from trigger to tip **unless a written risk assessment and extra hand protection are in place**.

MCR-044 / KSA ATC notes:

> Shorter only with **double trigger** + extra hand protection + special RA.

OPS-P-019 also flags double-trigger for short/UHP barrels. The handbook dropped the third control. A learner can pass Chapter 13 and still field a short single-trigger gun “with an RA.” That is not the Anabeeb rule.

### N5. Quick-connects “if both authorise in writing”

Chapter 12.4:

> Quick-connect couplings are not used on high-pressure hoses … **unless your company and the client both authorise that fitting type in writing**.

MCR-007:

> **No quick-connects on high-pressure hoses.** Prefer screw/face-seal. RPN 180.

The handbook turns a Never into a waiver. For a multi-employer course you can say “company/client may be stricter.” You cannot say they may be **looser** than the course standard — the front of this same book forbids that. This paragraph breaks the book’s own three-layer rule.

---

## Internal contradictions

### I1. Who holds the dump vs “one person cannot hold two roles”

Chapter 15.1 table: the **nozzle/gun operator holds the dump**.  
Same section: **one person cannot hold two of these roles** on a live line. Do not drop below three.

If the gun operator holds the dump, they already hold two listed roles. The dedicated dump/hole-watch is only required **when the nozzle operator cannot be seen** (which matches MCR-047).

Fix: say the third person is hole-watch / extra dump **always**; the gun operator still holds the tool dump when they can see and reach it. Dedicated dump-only person when LOS is lost. Do not write “cannot hold two roles” unless you mean shotgun always has a separate dump operator (which the table does not).

### I2. Items 5 and 15 of the 15 critical items

Both are the 10 m unauthorised-person line:

- Item 5: show exclusion, signs, tags, **state** the 10 m rule.  
- Item 15: **confirm** 10 m (or larger) and dump if crossed.

The Grokapedia Field Verification instrument uses item 5 for **tip mark (MCR-052)** and item 15 for exclusion. v2.5 dropped the tip-mark as a critical item and duplicated exclusion. A learner can fail to mark 600 mm and still get a certificate.

### I3. “Phase 0 lock” and “four-band list”

Appendix A cites a Phase 0 lock and a four-band list. Neither appears in the learner chapters. Trainers cannot point a learner at them.

### I4. Cover vs Chapter 15 on what v2.5 changed

Cover: “No locked course number changed.” True for the numeric table. Not true for assessment: the 15-item list changed shape (tip mark out, exclusion doubled, named signals in). That is a locked **assessment** change and should be called one.

---

## Gaps (true teaching missing)

These are not false sentences. They are missing controls a Level 2 operator is still assessed against in the MCR / pack.

| ID | Gap | Why it matters |
| --- | --- | --- |
| G1 | **Tip mark not in the 15 items** (MCR-052). Taught in Ch14, not pass/fail. | Pack item 5 is the tip mark. Restore it. Merge HB items 5 and 15. |
| G2 | **MCR-049** — two years continuous relevant experience + management approval before live **manual** gun/lance on Anabeeb work. Ch 0.1 only says you do not need unsupervised time to **sit the classroom**. | Certificate holders will think they can shotgun tomorrow on an Anabeeb site. One sentence in 0.3 / 20.4. |
| G3 | **MCR-031** pressure-banded exclusion (7.5–10 m ≤10k; 10–15 m 10–20k; 15–25 m+ UHP). Book only locks 10 m unauthorised. | 10 m unauthorised does not size the **team** exclusion at 40k. Ch 7 should say: 10 m is the stranger line; working exclusion grows with pressure per company/client, never below 10 m for strangers. |
| G4 | **MCR-032** lightning: 30 minutes after last thunder. Ch 19.5 is “dump when lightning is a threat” with no wait. | Operators will restart too soon. |
| G5 | **MCR-008** Type-M: 3.5–5 full threads, clear weep. Ch 12.4 names the parts, not the thread count. | Easy Field Verification miss. |
| G6 | **MCR-003** colour/mark readable from 2 ft. | One line in 12.2. |
| G7 | **MCR-012 / 013** NPSH + filtration (10–50 µm). Ch 11 only “inlet water clean enough.” Trainer guide still has NPSH awareness. | Cavitation is RPN 192. Operator does not need the formula; they need “gravel noise = stop.” |
| G8 | Double-hearing **within ~35 ft of the pump** (WJTA PPE). Ch 16: “some sites require double hearing.” | Fine as a site rule if you do not want it locked. If WJTA FV is the practical model, lock it. |
| G9 | Rigid leader **≥ 300 mm** stainless (KSA ATC notes) vs “as required for that lance.” | Either lock 300 mm as course minimum or say “maker length, never none.” |
| G10 | 20 000–25 000 psi unnamed. Ch 1 jumps 10–20k then 25–40k. | Operators will not know which bucket 22k sits in. |
| G11 | Class size 8–10, 24–28 hours (course spec) not in the handbook. | Provider ops, not learner truth — optional. |
| G12 | Grounding: WJTA video always earth + prove. Handbook “if the unit and the site require it.” | Softened. Keep “if required” only if you also say “when in doubt, bond and prove.” |

---

## 250 N vs WJTA 60 lbf (not a non-truth, but a trap)

250 N = **56.2 lbf**. The book’s “about 56 lbf” is the correct conversion.

WJTA 2024 shotgun video / FV language uses **60 lbf or 250 N or 1/3 body weight**. 60 lbf = 267 N, which **fails** 250 N.

If a WJTA guest assessor uses 60 lbf, they will pass a gun this course must fail. Put one line on the Formula card: “WJTA materials may say 60 lbf. This course uses 250 N (56 lbf). 250 N is the tighter figure. Use 250 N.”

---

## Shotgun 10 000 psi AND 1.6 mm (stricter, own it)

OPS-P-019 / MCR-050 grammar is conjunctive: do not shotgun **above 10 000 psi with** an orifice **larger than 1.6 mm**.

The handbook splits them into two independent never-rules (front table, Ch 13, Never 13). That **forbids** 15 000 psi even with a tiny orifice. Chapter 13 question 1 expects “no.”

That is a valid **stricter course standard** if you keep it. Appendix A must not pretend it is “the top of the HP band.” Write: “This course treats 10 000 psi and 1.6 mm as two separate caps, stricter than a conjunctive reading of OPS-P-019.”

---

## What must change before this book can be the only truth

1. Remove **NEBOSH Verified** unless a dated NEBOSH artefact exists.  
2. Fix Appendix A (10 000 psi is not the top of the HP band; there is no four-band list in Ch 1).  
3. Resolve Level 2 vs 25–40k psi. Either the band is awareness-only, or the certificate is not Level 2.  
4. Put **double trigger** back on the short-lance exception.  
5. Restore **tip mark** as a critical item. Do not double up 10 m.  
6. Align Chapter 15 roles with MCR-047 (dedicated dump **when LOS is lost**).  
7. Re-lock quick-connects as Never on high-pressure hose (MCR-007).  
8. Add MCR-049 as a post-certificate field gate, not a classroom entry gate.  
9. Add lightning 30-minute wait (or explicitly waive it to the site rule and say so).  
10. Sign the approval row. “Course development team / project owner” with no names is not document control.

Until those ten are done, Grokapedia MCR remains the numeric SSOT. This handbook is a strong learner voice, not the register.

---

## What is already good enough to keep teaching

- Three-layer rule (course / company / client — stricter wins; never looser).  
- One home chapter per rule.  
- Catcher vs stinger vs smash plate vs centralizer, taught as different failures.  
- Dry-shut ≠ dumped.  
- Tap-test film is not a control.  
- Chem suit is not jetting PPE.  
- Pressure-up and shutdown ladder (Ch 15) matching the 2024 WJTA videos.  
- Auto-index and line-mole **out** of this certificate.  
- Formula card as the only place the constants live.

Those are the parts you can defend in an audit today.
