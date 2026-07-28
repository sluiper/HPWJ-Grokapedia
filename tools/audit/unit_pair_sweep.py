#!/usr/bin/env python3
"""Standing T1 unit-pair sweep for HPWJ-Grokapedia.

Recomputes every ``N psi (M bar)`` pair using the repo conversion:
  1 psi = 0.0689475729 bar

Restatement-consistency alone cannot catch a value that is wrong everywhere
(Claude process note 28 July 2026).

Usage (from repo root)::

    python3 tools/audit/unit_pair_sweep.py
    python3 tools/audit/unit_pair_sweep.py --fail  # exit 1 if any issue
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

PSI_TO_BAR = 0.0689475729
# Absolute 2 bar or 1.5% relative, whichever larger
ABS_TOL = 2.0
REL_TOL = 0.015

SKIP_PARTS = {
    ".git",
    "CLAUDE_VERIFICATION",
    "TRUTH_AUDIT",
    "CHANGELOG",
    "GROK_RESPONSE",
    "PACK_DRIFT",
    "T1_T3",
    "FULL_STACK_AUDIT",
}

PAIR_RE = re.compile(
    r"([\d\s]+)\s*psi\s*\((?:≈\s*)?([\d\s.,]+)\s*bar\)",
    re.IGNORECASE,
)


def should_skip(path: Path) -> bool:
    s = str(path)
    return any(p in s for p in SKIP_PARTS)


def parse_num(s: str) -> float:
    return float(s.replace(" ", "").replace(",", ""))


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--fail", action="store_true", help="Exit 1 if issues found")
    ap.add_argument("--min-psi", type=float, default=100.0)
    args = ap.parse_args()

    root = Path(__file__).resolve().parents[2]
    issues = []
    for path in root.rglob("*.md"):
        if should_skip(path):
            continue
        try:
            text = path.read_text(encoding="utf-8", errors="replace")
        except OSError:
            continue
        for m in PAIR_RE.finditer(text):
            try:
                psi = parse_num(m.group(1))
                bar = parse_num(m.group(2))
            except ValueError:
                continue
            if psi < args.min_psi:
                continue
            exp = psi * PSI_TO_BAR
            tol = max(ABS_TOL, abs(exp) * REL_TOL)
            if abs(exp - bar) > tol:
                issues.append(
                    {
                        "file": str(path.relative_to(root)),
                        "match": m.group(0)[:80],
                        "psi": psi,
                        "stated_bar": bar,
                        "expected_bar": round(exp, 2),
                        "delta": round(bar - exp, 2),
                    }
                )

    print(f"Unit-pair sweep: {len(issues)} issue(s) (tol=max({ABS_TOL} bar, {REL_TOL*100:.1f}%))")
    for i in issues:
        print(
            f"  {i['file']}: {i['match']!r} "
            f"→ expected {i['expected_bar']} bar (Δ {i['delta']})"
        )
    if args.fail and issues:
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
