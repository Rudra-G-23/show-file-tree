# Hello Data Points 👋

> A small, fast CLI to display styled file/folder trees — perfect for documenting project structure, exporting to Markdown, or quickly inspecting repos.

---
[![Show File Tree](https://img.shields.io/badge/show--file--tree-5317eb?logo=github&logoColor=black)](https://github.com/Rudra-G-23/show-file-tree) 
[![Downloads](https://img.shields.io/pypi/dm/show-file-tree.svg)](https://pypi.org/project/show-file-tree/)
[![PyPI](https://img.shields.io/pypi/v/show-file-tree.svg)](https://pypi.org/project/show-file-tree)
[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE.md)
[![Python versions](https://img.shields.io/pypi/pyversions/show-file-tree.svg)](https://pypi.org/project/show-file-tree/)
[![GitHub Issues](https://img.shields.io/github/issues/Rudra-G-23/show-file-tree)](https://github.com/Rudra-G-23/show-file-tree/issues)
[![GitHub pull requests](https://img.shields.io/github/issues-pr/Rudra-G-23/show-file-tree)](https://github.com/Rudra-G-23/show-file-tree/pulls)
[![Repo Size](https://img.shields.io/github/repo-size/Rudra-G-23/show-file-tree)](https://github.com/Rudra-G-23/show-file-tree)
[![Fast & Lightweight](https://img.shields.io/badge/fast%20%26%20lightweight-✅-brightgreen)](https://github.com/Rudra-G-23/show-file-tree)
[![Made with 💜 Python](https://img.shields.io/badge/Made%20with%20❤️-Python-brightgreen)](https://github.com/Rudra-G-23/show-file-tree)
[![Contributions Welcome](https://img.shields.io/badge/contributions-welcome-blue)](https://github.com/Rudra-G-23/show-file-tree/issues)

---

## Quick links
- **Getting started** — Installation & Quickstart.
- **CLI reference** — Complete flag list and examples.
- **Features** — What the tool can do.
- **Examples** — Real-world usage and exported Markdown.
- **Contributing** — How to contribute, tests, and release notes.
- **Changelog** — Release history.

---

## Quick start

### Install
```
# From PyPI
pip install show-file-tree
```

```
# From source (dev)
git clone https://github.com/Rudra-G-23/show-file-tree.git
cd show-file-tree
python -m venv .venv
```

```
# Windows (PowerShell)
.venv\Scripts\Activate.ps1
pip install -e ".[all]"
```
### Basic usage

```
# Print a tree of the current directory:
show-file-tree .
```

Limit depth and show sizes & counts:

```
show-file-tree  -d 2 --size --count
```

Export the tree to Markdown (creates `<root>-file-tree.md`):

```
show-file-tree /path/to/project --format md --size
```

---

## Why use `show-file-tree`?

* **Fast, memory-safe traversal** — suitable for large directories.
* **Pretty terminal output** — icons, counts, human-readable sizes.
* **Powerful filtering** — globs, mtime/ctime windows.
* **Markdown export** — create readable project documentation automatically.
* **Themes & ASCII fallback** — works in CI or minimal terminals.

---

## Short CLI reference

```
# structure-related
--max-depth, -d       Maximum recursion depth
--gitignore / --no-gitignore  Respect .gitignore (default: on)
--hidden              Show hidden files
```

```
# sorting
--sort {name,size}
--order {asc,desc}
```

```
# output & display
--format {tree,md}
--size
--count
--no-icons
--theme {colorful,monokai,light,nocolor}
```

```
# filtering
--include, -i <PATTERN>
--exclude, -e <PATTERN>
--mtime-after <YYYY-MM-DD>
--mtime-before <YYYY-MM-DD>
--ctime-after <YYYY-MM-DD>
--ctime-before <YYYY-MM-DD>
```

```
# general
--version
--about
```

For the full reference, see the **CLI reference** page.

---

## Example: generate project documentation

```
# Create a Markdown file documenting your repo root
show-file-tree /home/user/my-project --format md --size --count
# -> my-project-file-tree.md
```

---

## Ready-made next steps

* 🔎 **Read the Getting Started** — installation + first run
* 📚 **Explore Examples** — real outputs and exported Markdown
* 🛠️ **Contribute** — tests, style, feature requests (see CONTRIBUTING.md)

---

## Footer / Contact

- Author: **Rudra Prasad Bhuyan** — [GitHub](https://github.com/Rudra-G-23) 
- License: MIT — see `LICENSE.md` 
- Changelog: `CHANGELOG.md`
