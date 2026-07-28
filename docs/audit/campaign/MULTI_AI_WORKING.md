# Multi-AI Working Protocol — HPWJ-Grokapedia

**Living document**  
**Last updated:** 28 July 2026  
**Binding schema:** `AGENTS.md` + `WORKFLOW.md` + `PROCESS.md`  
**Family standard (if present):** `~/projects/GROKAPEDIA_STANDARD.md`

---

## 1. Why multi-AI

Safety-critical content fails when one model both authors and “grades” itself. This repo uses **independent roles** so mistakes (especially unit conversion and restatement drift) surface before human gate.

---

## 2. Role matrix

| Agent | Role | May draft? | May push? | May merge main? | Primary outputs |
|-------|------|------------|-----------|-----------------|-----------------|
| **Grok** | Technical Truth Engine + Drafter | Yes | **draft/*** only | Only if human explicitly orders | Research packages, sections, MCR Drafting rows, CHANGELOG, fix commits for P0/P1 |
| **Claude** | Independent Reviewer | **No** | **No** | No | Mandatory Verification Report (P0/P1/P2); re-derives numbers; pack drift checks |
| **Human (Jacques / QHSSE)** | Owner / final gate | Yes | Yes | **Yes** | Direction, internal PDFs (GAP-004 etc.), Drafting→Visible, merge, freeze sentence |
| **Other tools (optional)** | Scripts / CI | n/a | n/a | n/a | `tools/audit/unit_pair_sweep.py`, future CI |

Two models agreeing is **necessary but never sufficient** for operational rules (PROCESS core principle 3).

---

## 3. Delivery loop (repeat forever)

```
Human priority (+ internal docs)
        ↓
Grok: draft/*  full package + self-check
        ↓
Claude: Verification Report (template in PROCESS.md)
        ↓
Grok: P0/P1 only on same draft branch
        ↓
Human: review → promote Drafting→Visible if any → merge main
        ↓
Both: re-read AGENTS + MCR before next package
```

**Parallelism allowed:** Grok may research the *next* package while Claude reviews the *current* draft branch.

---

## 4. What each agent must re-read before major work

1. `AGENTS.md`  
2. `MASTER_CONTROL_REGISTER.md`  
3. `PROCESS.md` / this file  
4. Relevant `docs/audit/campaign/*` (latest Claude report, FULL_STACK_AUDIT, CAMPAIGN_LOG)

---

## 5. Standing technical checks (multi-AI shared)

| Check | Owner | Tool / method |
|-------|-------|----------------|
| T1 arithmetic re-derive | Grok then Claude | Shown work + independent recompute |
| T1 **unit-pair sweep** | Grok (every threshold edit) + Claude | `python3 tools/audit/unit_pair_sweep.py --fail` |
| T2 citation fidelity | Claude primary | Source exists / matches |
| T3 restatement consistency | Both | `MCR_RESTATEMENT_MAP.md` + repo search |
| Pack drift | Claude / Grok | No free-floating RF constants; cite MCR-017 |
| Restatement after formula fix | Grok mandatory | Full-repo search (AUDIT-001–004 lesson) |

**Claude lesson:** T3-only cannot catch a value wrong *everywhere*. Unit-pair sweep is mandatory.

---

## 6. Where multi-AI artifacts live

| Artifact | Path |
|----------|------|
| Campaign log | `docs/audit/campaign/CAMPAIGN_LOG.md` |
| Claude reports | `docs/audit/campaign/CLAUDE_VERIFICATION_REPORT_*.md` |
| Grok responses to Claude | `docs/audit/campaign/GROK_RESPONSE_*.md` |
| Full stack audit | `docs/audit/campaign/FULL_STACK_AUDIT_*.md` |
| Pack drift | `docs/audit/campaign/PACK_DRIFT_CHECK_*.md` |
| Gap register | `docs/research/inventory/INTERNAL_GAP_REGISTER.md` |
| Multi-AI session board | `docs/audit/campaign/MULTI_AI_SESSION_BOARD.md` (this campaign) |

---

## 7. Hand-off phrases (copy-paste)

**Human → Grok:**  
`Grok: start draft/<topic> per AGENTS. Delivery package. Push draft only.`

**Human → Claude:**  
`Claude: review draft/<branch> using PROCESS verification template. No draft, no push.`

**Claude → Grok (via human or shared report file):**  
Report written to `docs/audit/campaign/…` with P0/P1/P2.

**Grok after Claude:**  
`Applied F-xx only. See GROK_RESPONSE_*.md. Ready for human merge.`

**Human freeze:**  
`Numeric + control freeze for ATC-HPWJ-OP-001 authorized as of <commit> on main.`

---

## 8. Non-negotiables

- No self-grading language (AGENTS rule 8).  
- No inventing INTERNAL GAP content.  
- No promoting Drafting → Visible without human.  
- No free-floating reaction-force constants in training (always MCR-017).  
- CDN/cache: allow cache-bust when verifying just-pushed raw GitHub content.

---

## 9. Replication

Copy AGENTS + WORKFLOW + PROCESS + this file into future Anabeeb technical encyclopedias. Start every repo with an MCR.
