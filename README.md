# math-paper-templates

Reusable LaTeX templates for mathematics papers, distilled from the
structural conventions of a large collection of research manuscripts.
Every template is complete and compiles as shipped — no placeholders that
need filling before the first build.

## What is here

| Template | Use it when |
|---|---|
| `article/` | the default. A full paper: abstract, table of contents, several sections, appendices, BibTeX |
| `amsart/` | you need AMS house style: `amsart` class, MSC codes, keywords, `amsplain` bibliography |
| `family/` | one principal manuscript plus companion manuscripts that support, extend or reprove it |
| `note/` | a single result proved in one pass, under roughly fifteen pages |
| `verification/` | the manuscript is accompanied by a finite, machine-checkable certificate |

The templates are independent: copy the one you need, nothing is shared at
build time.

```
math-paper-templates/
├── article/          the default full-paper template
├── amsart/           AMS house-style variant
├── family/           principal manuscript + companions
├── note/             short single-file note
└── verification/     finite-certificate bundle for any manuscript
```

Each directory has its own `README.md` with its layout, build commands and
conventions.

## Quick start

```sh
cp -r article my-paper
cd my-paper
latexmk -pdf main.tex        # or: pdflatex, bibtex, pdflatex, pdflatex
```

Then set `\title`, `\author`, `\date` and the
`\hypersetup{pdftitle=...,pdfauthor=...}` block in `main.tex`, rename the
files under `sections/`, and replace `references.bib`.

## Conventions common to every template

- **Class and size.** `article` at 11 pt, or `amsart` at 11 pt for the AMS
  variant.
- **Modular source.** A root file sets the title block and the `\input`
  order; content lives in `sections/`; figures live in `figures/`.
- **Zero-padded section file names** (`00-introduction.tex`,
  `01-preliminaries.tex`, ...) so the directory listing matches the reading
  order. Appendices use `90-` and up.
- **One shared theorem counter.** `theorem` owns a counter numbered within
  the section; `lemma`, `proposition`, `corollary`, `definition`,
  `remark` and the rest share it, giving one running sequence per section
  (Theorem 2.1, Lemma 2.2, Proposition 2.3, ...).
- **Equations numbered within the section** via
  `\numberwithin{equation}{section}`.
- **Cross-references through `cleveref`**, never literal numbers: write
  `\cref{thm:main}`, not "Theorem 2.1". Configured with `capitalise`,
  `noabbrev` and `nameinlink`.
- **Labels are typed**: `sec:`, `thm:`, `lem:`, `prop:`, `cor:`,
  `def:`, `rem:`, `eq:`, `fig:`, `app:`.
- **Proofs** use `amsthm`'s `proof` environment, with
  `\begin{proof}[Proof of \cref{...}]` for a previously stated result.
- **Page-break hygiene**: a `\Needspace` precedes subsections and each
  theorem-like environment, so a statement never starts on the last line of
  a page.
- **Bibliographies** are BibTeX against `references.bib`: `plain`, or
  `plainnat` with `natbib` for author-year, or `amsplain` for the AMS
  template.
- **PDF metadata** is set explicitly with
  `\hypersetup{pdftitle=...,pdfauthor=...}`.

## Build requirements

A LaTeX distribution with `pdflatex`, `bibtex` and the standard packages:
`amsmath`, `amssymb`, `amsthm`, `mathtools`, `geometry`,
`microtype`, `enumitem`, `booktabs`, `array`,
`needspace`, `xcolor`, `hyperref`, `cleveref`,
`graphicx`, `tikz` — plus `amsart` and `mathrsfs` for the AMS
template. The `verification/` bundle needs Python 3.11 or later with
assertions enabled.

Verified with MiKTeX 25.12: all six documents compile with no errors and no
undefined references, and both stored certificates replay byte-identically.

## Provenance

The conventions encoded here — the theorem-counter scheme, the package set,
the section-file layout, the `cleveref` and `\Needspace` usage — were derived by
analysing the LaTeX sources of the manuscripts in
[openai/math](https://github.com/openai/math) (Apache-2.0). No manuscript text
is reproduced: every word and every formula in these templates is written for
the template itself.

## See also

The writing corpus and protocol behind these conventions: [math-paper-writing](https://github.com/XXXXXQ-0206/math-paper-writing).

## Licence

Apache License 2.0 — see [LICENSE](LICENSE).

## Language

- English: this file
- 中文: README.zh-CN.md
