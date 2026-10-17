# Manuscript family template

A *family* is the unit the collection is actually organised around: one
principal manuscript plus the companion manuscripts that support,
extend, or reprove parts of it. Every manuscript in a family is a
complete, independently buildable paper with its own root file,
sections, and bibliography.

## Layout

```
family/
├── README.md                  family index: what the family claims, who cites whom
├── build-all.ps1              build every manuscript in the family
├── principal/                 the principal manuscript
│   ├── main.tex
│   ├── preamble.tex
│   ├── sections/
│   ├── references.bib
│   └── latexmkrc
└── companions/
    ├── companion-a/           complete manuscript, same internal shape
    │   ├── main.tex
    │   ├── preamble.tex
    │   ├── sections/
    │   └── references.bib
    └── companion-b/
        ├── main.tex
        ├── preamble.tex
        ├── sections/
        └── references.bib
```

## When to use a family instead of a single paper

Use a family when:

- a principal result needs a long technical companion that would
  unbalance the main paper;
- two or more results share a common technical core and are best read
  together;
- an alternative proof of the same statement is worth publishing
  alongside the original.

If none of these apply, use the article template instead.

## Cross-referencing between manuscripts

Companions are separate documents with separate bibliographies, so a
citation from the principal manuscript to a companion is an ordinary
bibliography entry. Give each companion a stable key in the principal
manuscript's references.bib:

```bibtex
@misc{companion-a,
  author       = {{[OI]}},
  title        = {Companion A: a supporting estimate},
  howpublished = {Companion manuscript, this family},
  year         = {2026}
}
```

and cite it with the ordinary cite command. Do not use a label
reference across manuscripts: LaTeX cannot resolve a label that lives
in a different document. If you need a precise pointer, cite the
companion and name the result in words, for example "see Companion A,
Theorem 3.2".

## Building

Build one manuscript:

```sh
cd principal && latexmk -pdf main.tex
```

Build the whole family (PowerShell):

```powershell
./build-all.ps1
```

Each manuscript is independent, so a failure in one does not block the
others.

## Conventions

Every manuscript in the family uses the same house conventions as the
standard article template: article class at 11 pt, one shared theorem
counter numbered within the section, cleveref cross-references, and
BibTeX. Keep them consistent across the family so that result numbering
and terminology do not drift between the principal manuscript and its
companions.
