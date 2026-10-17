# AMS-style template

The AMS flavour of the collection: the `amsart` class, an abstract placed
before `\maketitle`, AMS subject classification and keywords, and the
`amsplain` bibliography style.

## Layout

```
amsart/
├── main.tex                 root file (abstract before \maketitle; MSC/keywords before it too)
├── preamble.tex             packages, theorem environments, macros
├── sections/
│   ├── introduction.tex
│   ├── geometry.tex
│   ├── conclusion.tex
│   └── appendix.tex
├── references.bib
└── README.md
```

## What differs from the standard article template

| | article | amsart |
|---|---|---|
| Class | `article[11pt]` | `amsart[11pt,reqno]` |
| Abstract | after `\maketitle`, in the body | before `\maketitle` |
| Subject class | none | `\subjclass[2020]{...}` |
| Keywords | none | `\keywords{...}` |
| Theorem numbering | within section (2.1, 2.2) | continuous (1, 2, 3) by default |
| Bibliography | `plain` | `amsplain` |
| Title head | none | short title in `\title[short]{long}` |
| Author | plain | `\NoCaseChange{...}` to protect the running head |

## Placement rules (important)

`amsart` differs from `article` in two ways that silently produce
wrong output if you get them wrong:

1. The abstract is typeset **before** `\maketitle`, so it must appear
   before that command in the source.
2. `\subjclass` and `\keywords` must be set **before**
   `\maketitle`. `\maketitle` emits them as the page-1 administrative
   footnotes; setting them afterwards leaves them as loose, unlabelled
   body text at the top of the paper. Put them in the preamble, next to
   `\title` and `\author`.

## Build

```sh
pdflatex main && bibtex main && pdflatex main && pdflatex main
```

## Notes

- `amsart` already defines `thm`, `lem`, `prop`, `cor`,
  `defn`, `rem` and others. The preamble additionally defines
  article-style aliases (`theorem`, `lemma`, ...) sharing one counter, so
  section sources can be moved between this template and the article
  template without rewriting every environment name.
- To number results within the section, as the article template does,
  uncomment `\numberwithin{thm}{section}` in the preamble.
- `mathrsfs` is loaded for `\mathscr`. If you do not use it, drop it.
