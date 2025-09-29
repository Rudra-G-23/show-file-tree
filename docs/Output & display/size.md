# --size

!!! info

    - The `--size` flag shows the **size of files and folders** in the tree.  
    - Sizes are displayed in human-readable units (KB, MB, GB) for easy reference.

---

## Usage

!!! success "Usage"

    ```bash
    # Show tree with sizes
    show-file-tree  --size
    ```

---

## Example

!!! example

    === "Without `--size`"
        ```bash
        ├── 📁 docs
        │   └── readme.md
        ├── 📁 src
        │   └── main.py
        └── LICENSE
        ```
    === "With `--size`"
        ```bash
        ├── 📁 docs (12 KB)
        │   └── readme.md (5 KB)
        ├── 📁 src (150 KB)
        │   └── main.py (50 KB)
        └── LICENSE (1 KB)
        ```

### Legend:

!!! tip "Legend"
    - Folder sizes are summed from the files inside.
    - Files show their individual size next to the name.

---

## Tip

!!! tip
    - Combine with `--count` to see both **sizes and file counts**:
      ```bash
      show-file-tree  --size --count
      ```
    - **Combine with `--format md` to export **size-annotated Markdown trees**.

---