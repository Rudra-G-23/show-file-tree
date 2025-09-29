---
icon: material/import
---

# --include / -i

!!! info

    - The `--include` flag allows you to **show only specific files or directories** when building the tree.  
    - You can use glob patterns (wildcards) to match multiple paths.

---

## :fontawesome-solid-user-check: Usage

!!! success "Usage"

    ```bash title="Only python files"
    # Include only Python files
    show-file-tree  --include "*.py"
    ```

    ```bash title="All markdown files"
    # Include all Markdown files
    show-file-tree  --include "*.md"
    ```

---

## :material-hexagon-multiple: Example

!!! example

    ```bash title="Files in project"
    src/
    tests/
    README.md
    debug.log
    config.yaml
    ```

    ```bash title="Command"
    show-file-tree . --include "*.py" --include "*.md"
    ```

    ```bash title="Output"
    ├── 📁 src
    │   └── main.py
    └── README.md
    ```

    Only `*.py` and `*.md` files are included in the tree.

---

## :material-fountain-pen-tip: Tips

!!! tip

    - Multiple `--include` flags can be combined to include several file types.
    - Combine with `--exclude` to **refine filtering**:
        ```bash title="Filtering"
        show-file-tree  --include "*.py" --exclude "tests/*"
        ```
    - Works with `--format md` to generate **filtered Markdown documentation**.
