# --max-depth / -d

!!! info

    - The `--max-depth` flag limits **how deep the tree will traverse** into directories.  
    - This is useful for large projects where you want a **high-level overview** without listing every nested file.

---

## Usage

!!! success Usage

    ```bash linenums="1" hl_lines="2"
    # Show tree with a maximum depth of 2
    show-file-tree  --max-depth 2
    ```

---

## Example

!!! example

    === "Full tree (default)"
        ```bash title="`Default`"
        ├── 📁 src
        │   ├── 📁 module1
        │   │   ├── file1.py
        │   │   └── file2.py
        │   └── 📁 module2
        │       └── file3.py
        ├── 📁 docs
        │   └── readme.md
        └── LICENSE
        ```
    === "With `--max-depth 1`"
        ``` bash title="`-d 1`"
        ├── 📁 src
        ├── 📁 docs
        └── LICENSE
        ```
    === "With `--max-depth 2`"
        ```bash title="`-d 2`"
        ├── 📁 src
        │   ├── module1
        │   └── module2
        ├── 📁 docs
        └── LICENSE
        ```

---

## Tips
!!! tip
    - Combine with `--count` or `--size` for a summarized view of folders at each depth.
    - Combine with `--format md` to generate **Markdown documentation** for only the top levels of a project.
    - Useful for **quick project overviews**, **documentation snapshots**, or **CI-friendly output**.

---