---
icon: material/sort
---

# --sort

!!! info

    The `--sort` flag controls how files and directories are sorted before displaying the tree.

## :fontawesome-solid-user-check: Usage

!!! success "Usage"

    ```bash title="Sort By Name"
    show-file-tree  --sort name
    ```

    ```bash title="Sort By Size"
    show-file-tree  --sort size
    ```
    
!!! abstract
    - `name` — Sort alphabetically (default).
    - `size` — Sort by file or folder size (smallest → largest).

## :material-hexagon-multiple: Examples

!!! example  "Sort by {name, order}"

    === "Sort by name (default)"

        ```bash title="Command"
        show-file-tree .
        ```
        ```bash title="Output (simplified)"
        ├── 📁 docs
        ├── 📁 src
        └── 📄 README.md
        ```
    === "Sort by size"

        ```bash title="Command"
        show-file-tree . --sort size
        ```

        ```bash title="Output (simplified)"
        └── 📄 README.md (25 KB)
        ├── 📁 src (100 KB)
        └── 📁 docs (200 KB)
        ```

---

## :material-fountain-pen-tip: Tip

!!! tip

    You can combine `--sort` with [`--order`](order.md) to control ascending/descending order.

---