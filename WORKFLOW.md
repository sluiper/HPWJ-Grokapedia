# WORKFLOW.md — Dual-Model + Human Operating Rhythm

**Version:** 1.2 (16 July 2026)  
**See also:** PROCESS.md for the full decision log and replication guide.

## Current Role Split
- **Grok** researches, derives, drafts full production sections, creates Drafting MCR rows, updates CHANGELOG, pushes **only to draft/* branches**, and performs a self-check after every push.
- **Claude** independently verifies using the mandatory report template below; produces P0/P1/P2 findings; does not draft or push.
- **Human** sets priorities, supplies internal sources, gives explicit approval for every Drafting → Visible promotion, and authorizes (or performs) the merge from draft branch to main.

## Standard Delivery Loop (v1.2 — Optimized & Safer)

1. **Human** states the goal + any internal material.
2. **Grok** creates a new branch `draft/section-XX` (or `draft/topic`), produces the complete Delivery Package, performs the mandatory self-check (re-pull and confirm files), and declares the package ready for review.
3. **Claude** runs the **mandatory Verification Report** (template below) against the draft branch.
4. **Grok** applies only the P0 and P1 fixes on the same draft branch.
5. **Human** reviews the final state of the draft branch, explicitly approves any Drafting → Visible promotions desired, and merges (or instructs Grok to merge) to main.

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

## Immediate Priority Queue (as of v8.3.1)
- [x] Lock optimized process (this file + AGENTS.md + PROCESS.md)
- [ ] Claude final verification of Section 23 (already on main — future sections use draft branches)
- [ ] Next priority to be set by Human (Section 27 Lessons Learned recommended as high value)

## Safety Gate (Absolute)
No new MCR row is promoted from Drafting to Visible, and no draft branch is merged to main, without:
- Full derivation or primary citation + stated assumptions
- Clean Claude Verification Report (or only P2 remaining)
- Explicit human approval for any operational or Drafting → Visible change

## How to Start Work
- Human: “Grok: start draft/section-27 for Lessons Learned” (or equivalent)
- Claude: “Claude: review draft/section-XX using the verification template”

Both models re-read AGENTS.md, WORKFLOW.md and the current MASTER_CONTROL_REGISTER.md before every major output.

This workflow is now the standard we will copy into every future technical encyclopedia repository.
