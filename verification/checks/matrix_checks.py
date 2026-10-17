#!/usr/bin/env python3
"""Exact matrix certificate.

Verifies determinant and rank claims over the rationals using exact
fraction arithmetic (Gaussian elimination with Fraction entries). No
floating-point value is ever a premise of an assertion.

This program does NOT certify that the matrices describe any particular
mathematical object; it certifies only the stated linear-algebra facts.

Usage:
    python matrix_checks.py [OUTPUT_DIRECTORY]
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


def determinant(matrix) -> Q:
    """Exact determinant by fraction-free Gaussian elimination."""
    n = len(matrix)
    assert all(len(row) == n for row in matrix), "matrix must be square"
    a = [row[:] for row in matrix]
    det = Q(1)
    for col in range(n):
        pivot = next((r for r in range(col, n) if a[r][col] != 0), None)
        if pivot is None:
            return Q(0)
        if pivot != col:
            a[col], a[pivot] = a[pivot], a[col]
            det = -det
        det *= a[col][col]
        inv = Q(1) / a[col][col]
        for r in range(col + 1, n):
            factor = a[r][col] * inv
            if factor:
                for c in range(col, n):
                    a[r][c] -= factor * a[col][c]
    return det


def rank(matrix) -> int:
    """Exact rank over the rationals."""
    if not matrix:
        return 0
    a = [row[:] for row in matrix]
    rows, cols = len(a), len(a[0])
    r = 0
    for c in range(cols):
        pivot = next((i for i in range(r, rows) if a[i][c] != 0), None)
        if pivot is None:
            continue
        a[r], a[pivot] = a[pivot], a[r]
        inv = Q(1) / a[r][c]
        a[r] = [x * inv for x in a[r]]
        for i in range(rows):
            if i != r and a[i][c] != 0:
                factor = a[i][c]
                a[i] = [x - factor * y for x, y in zip(a[i], a[r])]
        r += 1
        if r == rows:
            break
    return r


def main() -> int:
    outdir = Path(sys.argv[1]) if len(sys.argv) > 1 else Path.cwd() / "_verification-output"
    outdir.mkdir(parents=True, exist_ok=True)

    started = time.time()

    # A matrix with a known exact determinant and rank.
    m = [
        [Q(2), Q(1), Q(0)],
        [Q(1), Q(3), Q(1)],
        [Q(0), Q(1), Q(2)],
    ]
    det = determinant(m)
    assert det == Q(8), "determinant: %s != 8" % det
    assert rank(m) == 3, "expected full rank"

    # A rank-deficient matrix.
    singular = [
        [Q(1), Q(2), Q(3)],
        [Q(2), Q(4), Q(6)],
        [Q(1), Q(0), Q(1)],
    ]
    assert determinant(singular) == Q(0), "expected zero determinant"
    assert rank(singular) == 2, "expected rank 2"

    payload = {
        "determinant": {
            "label": "sample-3x3",
            "value": str(det),
            "expected": "8",
            "exact": True,
        },
        "rank": {
            "label": "singular-3x3",
            "value": rank(singular),
            "expected": 2,
            "exact": True,
        },
        "wall_seconds": round(time.time() - started, 6),  # metadata: stripped on comparison
    }

    target = outdir / "matrix-certificate.json"
    target.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print("PASS: 1 exact determinant and 1 exact rank; no floating-point premise")
    print("wrote %s" % target)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
