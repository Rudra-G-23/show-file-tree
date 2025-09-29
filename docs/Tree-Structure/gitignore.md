---
icon: material/git
---

# :simple-git: --gitignore / --no-gitignore

!!! info 

    - The `--gitignore` flag makes **show-file-tree** respect `.gitignore` files, excluding ignored files and folders from the tree.  
    - The `--no-gitignore` flag **ignores `.gitignore`**, showing all files and folders.

---

## :fontawesome-solid-user-check: Usage

!!! success "Usage"

    === "Respect `.gitignore` (default)"
        ```bash 
        show-file-tree  --gitignore # (1)!
        ```

        1. Only files **not listed** in `.gitignore` appear.

    === "Ignore `.gitignore`"
        ```bash
        show-file-tree  --no-gitignore # (1)!
        ```

        1. All files are displayed, even if ignored in Git.

    === "Output in CLI"
        ```bash title="When file is ready"
        Markdown tree exported to: [ROOT_PATH]\[FILE_NAME]-file-tree.md
        ```
---

## :material-hexagon-multiple: Example

!!! example
    === "`.gitignore` contents:"
        ```bash
        __pycache__/
        *.log
        .env
        ```
    === "With `--gitignore`"
        ```bash
        ├── 📁 src
        │   └── main.py
        └── README.md # (1)!
        ```

        1. Ignored: `__pycache__/`, `.env`, `.log` files.

    === "With `--no-gitignore`"
        ```bash
        ├── 📁 src
        │   ├── main.py
        │   └── __pycache__/main.cpython-310.pyc
        ├── .env
        ├── debug.log
        └── README.md
        ```

---

## :material-fountain-pen-tip: Tips

!!! tip 

    - Useful in **CI pipelines** where you want a complete file tree.
    - Combine with `--hidden` to show hidden files that are also ignored by Git.
    - Combine with `--format md` for full documentation including ignored files:

---

## :material-heart-multiple-outline: Markdown Support

!!! example "Formatted with Markdown file"

    === "Not supported"
        ```bash title="Not supported"
        show-file-tree  --no-gitignore --format md # (1)!
        ```

        1. In version **v0.0.1**, this feature is not supported. It has been updated in newer versions.
   
    === "Supported"
        ```bash title="Not supported"
        show-file-tree  --hidden --gitignore --format md
        ```   
---