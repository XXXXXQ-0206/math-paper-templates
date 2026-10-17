# [Manuscript title](paper.pdf)

**Author:** [OI]

**Date:** Month D, YYYY

## Citation

```bibtex
@misc{<stable-slug>,
  author       = {{[OI]}},
  title        = {{Manuscript title}},
  howpublished = {Preprint, <stable-slug>},
  year         = {YYYY}
}
```

## Verification

Delete this section if the manuscript has no finite certificate. If it
does, state the prerequisites, give the exact commands, and say what
the certificate does and does not establish.

Requires Python 3.11 or later with assertions enabled: do not use
`-O`, `-OO`, or `PYTHONOPTIMIZE`. From this directory, write to a fresh
output directory so the shipped certificates are not overwritten:

```sh
out="$(mktemp -d)"
python verification/checks/scalar_checks.py "$out"
python verification/checks/matrix_checks.py "$out"
```

Successful commands exit with status zero. Compare the generated files
against the stored certificates as described in
`verification/README.md`.

These computations do not replace the analytic arguments in the
manuscript.
