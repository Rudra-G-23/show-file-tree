# show-file-tree

A small, fast CLI tool to display **styled file/folder trees** with rich options — colors, icons, sizes, counts, sorting, filtering and Markdown export.

Perfect for quickly visualizing and documenting project structure.

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

* **PyPI:** `pip install show-file-tree`
* **Author / Maintainer:** Rudra Prasad Bhuyan
* **License:** MIT
* **Changelog:** see `CHANGELOG.md` (v0.0.1 — Released: 2025-09-25)

---

## Install

Install from PyPI:

```bash
pip install show-file-tree
```

Install from source (development):

```bash
git clone https://github.com/YOUR_USERNAME/show-file-tree.git

cd show-file-tree

python -m venv .venv
```

```bash
# Linux / macOS
source .venv/bin/activate

# Windows (PowerShell)
.venv\Scripts\Activate.ps1

pip install -e ".[all]"
pip install pytest
```

---

## Quick start

Print a tree of the current directory:

```bash
show-file-tree .
```

Limit depth and show sizes & counts:

```bash
show-file-tree  -d 2 --size --count
```

Export the tree to Markdown:

```bash
# creates: project-file-tree.md
show-file-tree --format md /path/to/your/project 
```

---

## What it does (core features)

* Build a hierarchical tree of files and folders (fast, memory-safe traversal).
* Render a pleasant, readable terminal tree with icons and counts.
* Display file/folder sizes in human-readable units (KB/MB/GB).
* Filter by glob patterns and by modification/creation time.
* Sort by name or size (ascending/descending).
* Export the tree to Markdown (`--format md`) when desired or auto-fallback for long trees.
* Multiple visual themes and a plain ASCII mode for compatibility.



---

## Example output (terminal)

```
Hello Data Points

+ ------------------------------------------------------------------------ +
                                My Project
+ ------------------------------------------------------------------------ +

├── 📁 src (3f, 2d)
│   ├── 📁 showfilestree (2f)
│   └── 📁 showfilestree.egg-info (0f)
├── 📁 tests (2f)
└── 📄 README.md (25 KB)
```


---

## CLI reference (main flags)

### Tree structure

* `--max-depth, -d <INT>` — Maximum recursion depth. Default: unlimited.
* `--gitignore / --no-gitignore` — Respect `.gitignore` files by default.
* `--hidden` — Show hidden files and directories.

### Sorting

* `--sort {name,size}` — Sort by `name` or `size`. Default: `name`.
* `--order {asc,desc}` — Sorting order. Default: `asc`.

### Output & display

* `--format {tree,md}` — `tree` (terminal) or `md` (Markdown file). Default: `tree`.
* `--size` — Show file/folder sizes.
* `--count` — Show counts inside folders (e.g. `src (2f, 4d)`).
* `--no-icons` — Disable icons / emojis for plain ASCII output.
* `--theme {colorful,monokai,light,nocolor}` — Choose a color theme.

### Filtering

* `--include, -i <PATTERN>` — Include only paths matching glob pattern (repeatable).
* `--exclude, -e <PATTERN>` — Exclude paths matching glob pattern (repeatable).
* `--mtime-after <YYYY-MM-DD>` / `--mtime-before <YYYY-MM-DD>` — Filter by modification time.
* `--ctime-after <YYYY-MM-DD>` / `--ctime-before <YYYY-MM-DD>` — Filter by creation time.

### General

* `--version` — Show package version.
* `--about` — Show package information.

---

## Markdown export behavior

When `--format md` is used (or when the CLI auto-falls back due to long output), a Markdown file named `<rootname>-file-tree.md` is created in your current working directory. The MD file includes:

* A top heading (`Hello Data Points`) and a visual tree block.
* Sizes, counts, and timestamps (if requested).
* A short summary (top files) when `--top` is used.

---

## Usage examples

Default (current dir):

```bash
show-file-tree .
```

Depth + metadata:

```bash
show-file-tree  -d 3 --size --count --theme monokai
```

Export to markdown (project):

```bash
# -> my-project-file-tree.md
show-file-tree --format md --size /home/user/my-project 
```

Filtering and sorting:

```bash
show-file-tree  --include "*.py" --exclude "tests/*" --sort size --order desc
```

---

## Development & contributing

Contributions are welcome — bug reports, feature requests, documentation updates, tests, and code. See `CONTRIBUTING.md` for full guidelines. Short summary:

* Fork the repo and branch from `main`.
* Branch prefixes:

  * `feature/` — new features
  * `fix/` — bug fixes
  * `docs/` — documentation
  * `wip/` — work-in-progress
  * `chore/` — tooling / config
  * `refactor/` — code cleanup
* Run tests: `pytest`
* Format code with `black`/`ruff`.
* Open PR with clear description and tests.

(Full contributing guidelines are available in `CONTRIBUTING.md`.)

---

## Testing

* Tests live in `tests/` and use `pytest`.
* Use lightweight fixtures and temporary directories for fast tests.
* Recommended to run: `pytest -q` in your virtual environment.

---

## CHANGELOG & Releases

* v0.0.1 — **Initial release** — *Released: 2025-09-25*

  * Core features: tree building, terminal rendering, `-d/--max-depth`, `--gitignore`, `--hidden`, `--size`, `--count`, Markdown export `--format md`, filters, sorting, theming.
  
* See `CHANGELOG.md` for full history and future releases.

---

## License

`show-file-tree` is released under the **MIT License**. See `LICENSE` for details.

---

## Contact / support

Author: **Rudra Prasad Bhuyan**
GitHub: `https://github.com/Rudra-G-23/show-file-tree`

---
