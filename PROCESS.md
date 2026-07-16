# PROCESS.md — Dual-Model + Human Team Operating System

**Purpose:** This is the living record of how Grok + Claude + Human (Jacques) work together on safety-critical technical encyclopedias. It is designed to be copied into every future Anabeeb / HSE / technical wiki we build so we never re-learn the same lessons.

**Last Updated:** 16 July 2026  
**Status:** Fully locked after joint verification (v1.2) + explicit grandfather decision

---

## Core Principles (Non-Negotiable)

1. **Truth over speed.** A wrong number can injure or kill. Every numeric claim requires full derivation or primary citation + stated assumptions.
2. **MCR is absolute SSOT.** No control exists until it has a row in MASTER_CONTROL_REGISTER.md.
3. **Human remains the final gate** on anything that changes operational rules or promotes Drafting → Visible. Two AI models agreeing is necessary but never sufficient.
4. **No self-grading** — not of the encyclopedia content, and not of the workflow itself. Rule 8 in AGENTS.md applies to process assessments too.
5. **Independent verification is the point of the system**, not a failure when it catches mistakes.
6. **Content-drift prevention** is enforced by both models and by draft-branch discipline.

---

## Current Role Split (v1.2 — 16 July 2026)

| Role | Responsibility | Authority |
|------|----------------|-----------|
| **Grok** | Research, full production drafting, physics/calculations with shown work, MCR row creation (as Drafting), CHANGELOG, push to **draft/* branches only**, self-check after every push | Push to draft/* branches only |
| **Claude** | Independent verification using the mandatory report template, re-derivation of every number, MCR/CHANGELOG consistency check, P0/P1/P2 prioritization of fixes | Review only — no drafting, no push |
| **Human (Jacques)** | Direction, internal Anabeeb/Aramco sources, final approval of every Drafting → Visible promotion, merge of draft branches to main, overall ownership | Final gate on everything operational |

---

## Standard Delivery Loop (Optimized)

1. **Human** sets priority + supplies any internal material.
2. **Grok** produces a complete Delivery Package on a new branch `draft/section-XX` (or `draft/topic-name`):
   - Full production section matching AGENTS format
   - Proposed MCR rows already written into a copy of MASTER_CONTROL_REGISTER.md (Status = Drafting)
   - CHANGELOG entry
   - Verification Log
   - Self-check: re-pull the branch (with cache-bust if needed) and confirm every claimed file update actually exists before declaring the package ready.
3. **Claude** runs the **mandatory Verification Report** (template below) against the live draft branch.
4. **Grok** applies only P0 and P1 fixes on the same draft branch (or a new fix commit).
5. **Human** reviews the final draft branch, gives explicit approval to promote any Drafting rows, and merges to main (or instructs Grok to merge after approval).

This loop is deliberately fewer, larger, safer cycles.

---

## Mandatory Claude Verification Report Template

```markdown
## Claude Verification Report — Section [XX] / [Topic]

**Branch reviewed:** draft/...
**Date:**

### 1. Numbers re-derived
- [Claim]: recompute shown → Pass / Fail + notes
- ...

### 2. Citations checked
- [Source]: exists? matches claim? any flags?

### 3. MCR consistency
- Are every cited MCR-IDs actually present in MASTER_CONTROL_REGISTER.md on this branch? Y/N
- Status of proposed rows correct? Y/N

### 4. CHANGELOG consistency
- Is the claimed CHANGELOG entry actually present and accurate? Y/N

### 5. Format compliance
- Matches Sections 16–20 structure (MCR mapping table, worked examples with full derivation, Verification Log, land-vs-wet where relevant, honest gaps)? Y/N + notes

### 6. Remaining gaps
- List any INTERNAL GAPs or unshown work still present

### 7. Required fixes
- **P0 (blocks merge):**
- **P1 (must fix before any Drafting → Visible):**
- **P2 (nice to have):**

### Overall recommendation
- Ready for human review / Needs fixes / etc.
```

---

## Key Decisions Made on 16 July 2026 (After Section 23 Cycle)

- **Rejected:** Giving Grok standing authority to promote Drafting → Visible rows. Human must explicitly approve every promotion. (Claude correctly applied the document’s own logic: MCR-049 requires human experience + management approval; the encyclopedia cannot automate away its own human gate.)
- **Adopted:** Push to `draft/section-XX` branches instead of directly to main. Human (or Grok after explicit human instruction) merges only after Claude verification + human sign-off. This turns the “human final gate” from a rubber stamp into a real pre-merge gate.
- **Adopted:** Bigger delivery packages per cycle + the mandatory verification report template.
- **Adopted:** Grok self-check (re-pull after every push that claims file updates) as a supplement, never a replacement for Claude’s independent check.
- **Retained:** Parallel work is allowed (Grok can prepare the next research package while Claude reviews the current draft branch).
- **Enforced:** No self-grading of the process itself.
- **Explicit decision (16 July 2026):** Section 23 is **grandfathered**. It was drafted and reviewed under the previous process and already sits on main. We will not create busywork by retroactively moving it to a draft branch. All future sections must follow the new draft-branch discipline.
- **Process note (CDN / cache):** raw.githubusercontent.com and GitHub’s CDN can cache content for a few minutes after a push. Immediate re-verification (by Claude or by Grok’s self-check) can therefore show stale content and produce a false-negative. Always allow a short cache window or force a cache-bust (`?t=...` or equivalent) when confirming a just-pushed change. This lesson was learned the hard way during the process-locking cycle.

---

## How to Replicate This System on Future Repos

1. Copy AGENTS.md, WORKFLOW.md, and this PROCESS.md.
2. Create the same three roles.
3. Always start with a Master Control Register (or equivalent SSOT).
4. Use draft branches from day one for any safety- or compliance-critical content.
5. Require the Claude Verification Report template for every major delivery.
6. Keep the human as the only authority that can promote Drafting → Visible or change operational rules.

---

## Immediate Next Actions for This Repo

- [x] Lock this optimized process into the three files
- [x] Explicitly grandfather Section 23 (stated decision above)
- [x] Document CDN cache-busting lesson
- [ ] Human sets next priority (recommended: Section 27 Lessons Learned)
- [ ] Grok starts first true draft-branch delivery package under the new rules

**This process exists so that every future encyclopedia we build starts at the quality level we have now earned, not from zero.**
