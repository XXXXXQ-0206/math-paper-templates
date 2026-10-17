# Standard manuscript template

The default template: an `article` class at 11 pt with a modular
preamble, one shared theorem counter, sections split across
`sections/`, and a BibTeX bibliography.

## Layout

```
article/
├── main.tex                 root file: title block, abstract, \input order, bibliography
├── preamble.tex             all packages, theorem environments, macros
├── sections/
│   ├── 00-introduction.tex
│   ├── 01-preliminaries.tex
│   ├── 02-main-result.tex
│   ├── 03-conclusion.tex
│   └── 90-appendix.tex
├── figures/
│   └── example-figure.tex   standalone TikZ figure, \input from a section
├── references.bib           BibTeX database
├── manuscript-README.md     template for the per-manuscript README + citation block
├── latexmkrc                build configuration
└── README.md                this file
```

## Build

```sh
latexmk -pdf main.tex        # full run, resolves cross-references and BibTeX
latexmk -C                   # clean auxiliary files
```

Or manually: `pdflatex main && bibtex main && pdflatex main && pdflatex main`.

## Starting a new paper

1. Copy this whole directory.
2. Rename the sections in `sections/` and update the `\input` list in
   `main.tex`. Keep the zero-padded numeric prefixes so the files sort
   in reading order.
3. Set `\title`, `\author`, `\date`, and the
   `\hypersetup{pdftitle=...,pdfauthor=...}` block in `main.tex`.
4. Replace the abstract and the sample sections.
5. Replace `references.bib` with your own entries.
6. Fill in `manuscript-README.md` and rename it to `README.md` in
   your paper directory.

## Conventions enforced by the template

- **Numbering.** Equations and all theorem-like environments are
  numbered within the section (`\numberwithin{equation}{section}`).
  `theorem` owns the counter; `lemma`, `proposition`,
  `corollary`, `definition`, `remark` and the rest share
  it, so one running sequence per section.
- **Cross-references.** Use `\cref` / `\Cref` from `cleveref`, never
  literal "Theorem 2.1". `cleveref` is configured with `capitalise`,
  `noabbrev`, and `nameinlink`.
- **Labels.** Prefix by kind: `sec:`, `thm:`, `lem:`,
  `prop:`, `cor:`, `def:`, `rem:`, `eq:`,
  `fig:`, `app:`.
- **Proofs.** Use `\begin{proof}` from `amsthm`. For the proof of a
  previously stated result, use
  `\begin{proof}[Proof of \cref{...}]`.
- **Page breaks.** Subsections and theorem-like environments are
  preceded by a `\Needspace`, so a statement never begins on the
  last line of a page.
- **Links.** Hyperlinks use the `linkblue` colour defined in the
  preamble.
- **Metadata.** Set `pdftitle` and `pdfauthor` in `\hypersetup`.

## Adding a theorem-like environment

Add it to `preamble.tex` next to the others, sharing the `theorem`
counter:

```latex
\newtheorem{hypothesis}[theorem]{Hypothesis}
```

Put it after the appropriate `\theoremstyle` line: `definition` for
definition-like environments (upright body), `remark` for
remark-like ones (upright, smaller).

## Adding a figure

Put the TikZ source in its own file under `figures/` and pull it in with
`\input{figures/...}`; see `figures/example-figure.tex`. Reference it as
`\cref{fig:...}` rather than "the figure below".
