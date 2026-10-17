# math-paper-templates

可直接复用的数学论文 LaTeX 模板集，从一批数学研究手稿的结构与格式规范中提炼而来。
每个模板都是完整可编译的，开箱即用，没有需要先填占位符才能构建的空壳。

## 内容

| 模板 | 适用场景 |
|---|---|
| `article/` | 默认选择。完整论文：摘要、目录、多个章节、附录、BibTeX 参考文献 |
| `amsart/` | 需要 AMS 排版规范：`amsart` 文档类、MSC 分类号、关键词、`amsplain` 样式 |
| `family/` | 一篇主论文，外加支撑、扩展或重新证明它的配套论文 |
| `note/` | 单一结果、一气呵成证明的短篇（约十五页以内） |
| `verification/` | 论文附带可机器校验的有限计算证书 |

模板之间相互独立，构建时互不依赖，按需复制一个即可。

```
math-paper-templates/
├── article/          标准全文模板
├── amsart/           AMS 风格模板
├── family/           主论文 + 系列配套论文
├── note/             短篇单文件模板
└── verification/     有限计算验证包
```

每个目录都有自己的 `README.md`，说明其布局、构建命令与约定。

## 快速开始

```sh
cp -r article my-paper
cd my-paper
latexmk -pdf main.tex        # 或：pdflatex、bibtex、pdflatex、pdflatex
```

然后设置 `main.tex` 里的 `\title`、`\author`、`\date` 与
`\hypersetup{pdftitle=...,pdfauthor=...}`，改写 `sections/` 下的章节文件，
替换 `references.bib`。

## 通用格式规范

- **文档类**：`article` 11pt；AMS 变体为 `amsart` 11pt。
- **模块化源码**：根文件负责标题块与 `\input` 顺序；正文在 `sections/`；
  插图在 `figures/`。
- **零填充章节文件名**（`00-introduction.tex`、`01-preliminaries.tex` …），
  使目录列表顺序与阅读顺序一致；附录用 `90-` 起头。
- **统一定理计数器**：`theorem` 持有按节编号的计数器，`lemma`、
  `proposition`、`corollary`、`definition`、`remark` 等共享之，
  每节形成单一连续编号（Theorem 2.1、Lemma 2.2、Proposition 2.3 …）。
- **公式按节编号**：`\numberwithin{equation}{section}`。
- **交叉引用一律走 `cleveref`**：写 `\cref{thm:main}`，不要写死
  "Theorem 2.1"。已配置 `capitalise`、`noabbrev`、`nameinlink`。
- **标签前缀成体系**：`sec:`、`thm:`、`lem:`、`prop:`、
  `cor:`、`def:`、`rem:`、`eq:`、`fig:`、`app:`。
- **证明**使用 `amsthm` 的 `proof` 环境；证明已有结果时写
  `\begin{proof}[Proof of \cref{...}]`。
- **分页控制**：小节与各定理类环境前加 `\Needspace`，避免命题落在页面最后一行。
- **参考文献**用 BibTeX 配合 `references.bib`：一般用 `plain`；需要作者–年份时用
  `plainnat` 搭配 `natbib`；AMS 模板用 `amsplain`。
- **PDF 元数据**显式设置：`\hypersetup{pdftitle=...,pdfauthor=...}`。

## 编译环境

需要 `pdflatex`、`bibtex` 及常用宏包：`amsmath`、
`amssymb`、`amsthm`、`mathtools`、`geometry`、
`microtype`、`enumitem`、`booktabs`、`array`、
`needspace`、`xcolor`、`hyperref`、`cleveref`、
`graphicx`、`tikz`；AMS 模板另需 `amsart` 与 `mathrsfs`。
`verification/` 验证包需要 Python 3.11+ 且断言开启。

已在 MiKTeX 25.12 上验证：六个文档全部零错误、零未定义引用编译通过，两个存储证书
也能逐字节复现。

## 来源

这里编码的约定——定理计数器方案、宏包集合、章节文件布局、`cleveref` 与
`\Needspace` 的用法——来自对 [openai/math](https://github.com/openai/math)
（Apache-2.0）手稿 LaTeX 源码的分析。**未复制任何手稿正文**：模板里的每一句话、
每一个公式都是为模板本身编写的。

## 相关仓库

这些约定背后的写作语料与生成协议：[math-paper-writing](https://github.com/XXXXXXQ-0206/math-paper-writing)。

## 许可

Apache License 2.0 —— 见 [LICENSE](LICENSE)。

## 语言

- 中文：本文件
- English: README.md
