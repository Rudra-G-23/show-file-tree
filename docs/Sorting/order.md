---
icon: material/order-alphabetical-ascending
---

# --order

!!! info 

    The `--order` flag controls the **sorting order** of files and directories in the tree.

    - `asc` — Sort in **ascending order** (default).  
    - `desc` — Sort in **descending order**.

---

## :fontawesome-solid-user-check: Usage

!!! success "Usage"

    ```bash title="Sort by Name"
    # Sort by name in descending order
    show-file-tree  --sort name --order desc
    ```

    ```bash title="Sort by Size"
    # Sort by size in ascending order
    show-file-tree  --sort size --order asc
    ```

---

## :material-hexagon-multiple: Example

!!! example "Order Command"

    === "Ascending order (default)"
        ```bash
        ├── README.md
        ├── docs
        └── src
        ```
    === "Descending order"
        ```bash
        ├── src
        ├── docs
        └── README.md
        ```

---

## :material-fountain-pen-tip: Tips

!!! tips

    - Always combine `--order` with `--sort` to define **both sort criteria and direction**.
    - Works with `--format md`, `--size`, or `--count` for **customized tree outputs**.

---