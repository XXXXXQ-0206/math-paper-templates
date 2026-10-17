#!/usr/bin/env python3
"""Exact scalar certificate.

Verifies finite rational identities of the form a/b + c/d == e/f and
integer power comparisons, using fractions.Fraction throughout. No
floating-point value is ever a premise of an assertion; the decimal
display values are informational only.

This program does NOT certify any analytic, asymptotic, or limiting
statement. It checks finitely many exact arithmetic identities.

Usage:
    python scalar_checks.py [OUTPUT_DIRECTORY]

Run with assertions enabled: the checks abort under -O, -OO, or a
non-empty PYTHONOPTIMIZE.
"""
from __future__ import annotations

from fractions import Fraction as Q
from pathlib import Path
import json
import os
import sys
import time

if not __debug__ or sys.flags.optimize or os.environ.get("PYTHONOPTIMIZE", "0") not in ("", "0"):
    raise SystemExit("Exact certificate requires assertions enabled (do not use -O/-OO/PYTHONOPTIMIZE).")


def check_identities() -> list:
    """Return the list of exact identities that were verified."""
    cases = [
        # (label, left-hand side, right-hand side)
        ("sample-sum", Q(1, 3) + Q(1, 6), Q(1, 2)),
        ("sample-product", Q(3, 4) * Q(8, 9), Q(2, 3)),
        ("sample-power", Q(2, 3) ** 4, Q(16, 81)),
    ]
    results = []
    for label, lhs, rhs in cases:
        assert lhs == rhs, "%s: %s != %s" % (label, lhs, rhs)
        results.append({
            "label": label,
            "lhs": str(lhs),
            "rhs": str(rhs),
            "lhs_decimal": float(lhs),  # informational only
            "exact": True,
        })
    return results


def check_power_comparison() -> dict:
    """Compare two exact integer powers without floating point."""
    base, exp = 3, 40
    lhs = base ** exp
    rhs = 2 ** 64
    # 3**40 = 12157665459056928801 and 2**64 = 18446744073709551616,
    # so the strict inequality goes the other way. Checking it exactly
    # (rather than in floating point, where both round to 1.2e19 and
    # 1.8e19) is the point of this case.
    assert lhs < rhs, "expected 3**40 < 2**64"
    return {
        "label": "3**40-vs-2**64",
        "lhs_digits": len(str(lhs)),
        "rhs_digits": len(str(rhs)),
        "relation": "<",
        "exact": True,
    }


def main() -> int:
    outdir = Path(sys.argv[1]) if len(sys.argv) > 1 else Path.cwd() / "_verification-output"
    outdir.mkdir(parents=True, exist_ok=True)

    started = time.time()
    payload = {
        "identities": check_identities(),
        "power_comparison": check_power_comparison(),
        "wall_seconds": round(time.time() - started, 6),  # metadata: stripped on comparison
    }

    target = outdir / "scalar-certificate.json"
    target.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print("PASS: %d exact identities and 1 power comparison; no floating-point premise"
          % len(payload["identities"]))
    print("wrote %s" % target)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
