---
icon: material/human-greeting-variant
---

# Hello Data Points 👋

!!! quote "Description" 
    :fontawesome-solid-address-card: __A small, fast CLI to display styled file/folder trees — perfect for documenting project structure, exporting to Markdown, or quickly inspecting repos.__

---

[![Show File Tree](https://img.shields.io/badge/show--file--tree-5317eb?logo=github&logoColor=black)](https://github.com/Rudra-G-23/show-file-tree) 
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

## :material-robot-industrial-outline: Install

!!! success "Install" 
    
    === "From PyPI"
        ```py linenums="1" hl_lines="2"
        # From PyPI 
        pip install show-file-tree
        ```

    === "From UV"
        ```py linenums="1" hl_lines="2"
        # From UV
        uv pip install show-file-tree
        ```

    === "From Source"
        ```py linenums="1" title="From Source"
        # From source (dev)
        git clone https://github.com/Rudra-G-23/show-file-tree.git

        cd show-file-tree
        python -m venv .venv
        ```

    === "Windows PowerShell"
        ```ps1 linenums="1" title="Windows PowerShell"
        .venv\Scripts\Activate.ps1
        pip install -e ".[all]"
        ```

---

## :fontawesome-brands-nfc-directional: Basic 

!!! tip "Command Line Interface of show-file-tree"

    === "Usage" 
        ```bash linenums="1" hl_lines="2"
        # This is the first message you’ll see if you encounter any errors.
        show-file-tree [OPTIONS] [ROOT_PATH] COMMAND [ARGS]...
        ```
    === "COMMAND"
        ```text
        [OPTIONS]:  TThe specific command or action to perform, e.g., `--count` or `--size`.
        ```
    === "ROOT_PATH"
        ```text
        [ROOT_PATH]: The root directory to start the file tree from. Default is current directory (.) 
        ```

---

## :material-map-marker-path: File Path 

### :fontawesome-regular-square-minus: Incorrect File Path

!!! danger "File path miss Match"

    === "Incorrect File Path"
        ```bash
        show-file-tree [ROOT_PATH] COMMAND 
        ```
    === "Examples"
        !!! example "Incorrect File Path Examples"

        === "Example 1"
            ```bash
            # Why Incorrect ✖️: Dot is default path,so no need to use
            show-file-tree . --size
            ``` 
        === "Example 2"
            ```bash
            # Why Incorrect ✖️: First Path used 
            show-file-tree "C:\Users\Rudra\Desktop\MLOPs" --count
            ```
        === "Example 3"
            ```bash
            # Why Incorrect ✖️: First Path used 
            show-file-tree "C:\Users\Rudra\Desktop\MLOPs"  --format md 
            ```
### :fontawesome-regular-plus-square: Correct File Path

!!! success "File path  Match"

    === "Correct File Path"
        ```bash
         show-file-tree COMMAND [ROOT_PATH]
        ```
    === "Examples"
        !!! example "Correct File Path Examples"

        === "Example 1"
            ```bash
            # Why Correct ✔️: Directly used the command 
            show-file-tree  --size 
            ``` 
        === "Example 2"
            ```bash
            # Why Correct ✔️: First command -> Path
            show-file-tree --count "C:\Users\Rudra\Desktop\MLOPs" 
            ```
        === "Example 3"
            ```bash
            Why Correct ✔️: First command -> Path 
            show-file-tree  --format md "C:\Users\Rudra\Desktop\MLOPs"  
            ```

---

## :material-hand-heart-outline: Error Handing 

!!! info "When a typo error occurs"

    === "If typo error occurs"
        !!! failure "Error"
        ```bash
        Usage: show-file-tree [OPTIONS] [ROOT_PATH] COMMAND [ARGS]...
        Try 'show-file-tree --help' for help.
        ╭─ Error ──────────────────────────────────────────────────────────────────────────╮
        │ Invalid value for '[ROOT_PATH]': Directory 'count' does not exist.               │
        ╰──────────────────────────────────────────────────────────────────────────────────╯
        ```
    === "Use `Help` command" 
        !!! success "Used `--help` command"
        ```bash
        show-file-tree --help
        ```

---

## :material-hexagon-multiple: Example

!!! example "Examples"
    ``` bash title="1. Exported in Markdown format"
    show-file-tree --format md [ROOT_PATH]
    ```

    ```bash title="2. Limit depth and show sizes & counts"
    show-file-tree  -d 2 --size --count
    ```
---

## 😎 Why use `show-file-tree`?

- [x] **Fast, memory-safe traversal** — suitable for large directories.
- [x] **Pretty terminal output** — icons, counts, human-readable sizes.
- [x]  **Powerful filtering** — globs, mtime/ctime windows.
- [x]  **Markdown export** — create readable project documentation automatically.
- [x]  **Themes & ASCII fallback** — works in CI or minimal terminals.
- [x] and many more .....

---