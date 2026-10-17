# Short note template

One self-contained file. Use this when the manuscript states a single
result and proves it in one pass, with no independent parts.

## Layout

```
note/
├── main.tex          everything: preamble, theorem environments, body, bibliography
├── references.bib
└── README.md
```

## When to use this instead of the article template

Use the note when:

- there is one main theorem and one line of argument;
- the paper is under roughly fifteen pages;
- no table of contents is warranted;
- splitting into files would add structure the argument does not have.

Move up to the standard article template as soon as you need standing
conventions that several sections share, or a section that a reader
might reasonably read on its own.

## Build

```sh
pdflatex main && bibtex main && pdflatex main && pdflatex main
```

## Conventions

Identical to the standard article template: 11 pt article class, one
shared theorem counter numbered within the section, cleveref
cross-references, BibTeX. The only difference is that the preamble is
inlined rather than kept in `preamble.tex`.
