# Verification bundle template

Some manuscripts in the collection are accompanied by a finite,
machine-checkable certificate: a set of Python programs that replay a
finite computation and compare the result against stored JSON. This
directory is that companion bundle, extracted so it can be attached to
any manuscript.

The certificate covers **finite computations only**. It never certifies
the analytic argument. Say so explicitly in both this README and the
manuscript, so that no reader mistakes a passing replay for a proof.

## Layout

```
verification/
├── README.md                      this file: prerequisites, how to run, what is checked
├── run_all.ps1                    run every check and report pass/fail
├── checks/
│   ├── scalar_checks.py           exact arithmetic certificate
│   └── matrix_checks.py           exact linear-algebra certificate
└── certificates/
    ├── scalar-certificate.json    stored expected output, committed to the repo
    └── matrix-certificate.json    stored expected output, committed to the repo
```

## Conventions

These are the conventions the collection uses for such bundles.

1. **Exact arithmetic, never floating point, for any claim.** Use
   `fractions.Fraction` for rationals. Floating-point values may be
   printed for information but must not be a premise of any assertion.
2. **Assertions must be enabled.** The programs abort if Python is run
   with `-O`, `-OO`, or `PYTHONOPTIMIZE` set, because the checks are
   assertions.
3. **Write outputs to a separate directory.** Never overwrite the
   committed certificates. Take the output directory as an argument and
   default to a temporary path.
4. **Replay must be reproducible.** Strip genuinely variable metadata
   (wall-clock times, the Python build string) before comparing;
   everything else must match exactly.
5. **State the scope.** Every program's docstring says what it checks
   and, explicitly, what it does not check.

## Running

```sh
python checks/scalar_checks.py /tmp/verify-out
python checks/matrix_checks.py /tmp/verify-out
```

Or run everything and compare against the stored certificates:

```powershell
./run_all.ps1
```

Prerequisites: Python 3.11 or later, assertions enabled, standard
library only. Add NumPy or SciPy only if a specific check needs them,
and record that in the table below.

## What is checked

| Program | Output file | What it certifies | What it does not certify |
|---|---|---|---|
| `checks/scalar_checks.py` | `scalar-certificate.json` | exact rational identities listed in the manuscript | any analytic or asymptotic statement |
| `checks/matrix_checks.py` | `matrix-certificate.json` | exact rank and determinant claims | existence of the objects those matrices describe |

Update this table for your manuscript. A certificate whose scope is
vague is worse than no certificate.
