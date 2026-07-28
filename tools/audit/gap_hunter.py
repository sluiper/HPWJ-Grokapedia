#!/usr/bin/env python3
"""Gap hunter for HPWJ-Grokapedia — finds structural / consistency gaps.

Does not invent content. Reports:
  - Orphan MCR citations (cite without MCR row)
  - docs/*.md missing Verification Log
  - training files missing MCR Controls Referenced line
  - Optional unit-pair issues (delegates to unit_pair_sweep)

Usage (repo root)::

    python3 tools/audit/gap_hunter.py
"""

from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def main() -> int:
    mcr_text = (ROOT / "MASTER_CONTROL_REGISTER.md").read_text(encoding="utf-8")
    mcr_ids = set(re.findall(r"MCR-\d{3}", mcr_text))

    cited: set[str] = set()
    for p in ROOT.rglob("*.md"):
        if ".git" in p.parts:
            continue
        cited |= set(re.findall(r"MCR-\d{3}", p.read_text(encoding="utf-8", errors="replace")))

    orphans = sorted(cited - mcr_ids)
    print(f"MCR rows: {len(mcr_ids)} | unique cites: {len(cited)} | orphan cites: {len(orphans)}")
    for o in orphans:
        print(f"  ORPHAN {o}")

    print("\n# docs/*.md missing 'Verification Log'")
    missing_vl = []
    skip = {"00_Encyclopedia_Structure.md"}
    for p in sorted((ROOT / "docs").glob("*.md")):
        if p.name in skip:
            continue
        t = p.read_text(encoding="utf-8", errors="replace")
        if "Verification Log" not in t:
            missing_vl.append(p.name)
            print(f"  {p.name}")
    print(f"  count={len(missing_vl)}")

    print("\n# training files missing 'MCR Controls Referenced'")
    miss_trn = []
    for p in sorted((ROOT / "training").rglob("*.md")):
        if p.name == "README.md" or "Answer" in p.name or p.name.startswith("04c"):
            continue
        t = p.read_text(encoding="utf-8", errors="replace")
        if "MCR Controls Referenced" not in t:
            miss_trn.append(str(p.relative_to(ROOT)))
            print(f"  {p.relative_to(ROOT)}")
    print(f"  count={len(miss_trn)}")

    print("\n# unit_pair_sweep")
    r = subprocess.run(
        [sys.executable, str(ROOT / "tools/audit/unit_pair_sweep.py")],
        cwd=ROOT,
        capture_output=True,
        text=True,
    )
    print(r.stdout or r.stderr)

    print("\n# Suggested build targets from this hunt")
    if missing_vl:
        print("  - Add lightweight Verification Logs to chapters listed above")
    if orphans:
        print("  - Resolve orphan MCR IDs (typo or missing row)")
    if miss_trn:
        print("  - Add MCR Controls Referenced headers to training files")
    print("  - See docs/audit/campaign/FULL_STACK_AUDIT_2026-07-28.md for human-gated gaps")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
