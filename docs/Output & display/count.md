# --count

!!! info 

    - The `--count` flag displays **the number of files and directories** inside each folder in the tree.  
    - This makes it easy to see folder contents at a glance without expanding everything.

---

## Usage

!!! success "Usage"

    ```bash
    show-file-tree  --count
    ```

---

## Example

=== "Without `--count`"
    ```bash 
    ├── 📁 docs
    │   └── readme.md
    ├── 📁 src
    │   └── main.py
    └── LICENSE
    ```
=== "With `--count`"
    ```bash
    ├── 📁 docs (3f, 2d)
    │   └── readme.md
    ├── 📁 src (5f, 1d)
    └── LICENSE
    ```

!!! tips "Legend"
    - `3f` = 3 files
    - `2d` = 2 subdirectories

---

## Tip
!!! tip
    - Combine `--count` with other display flags:
    ```bash 
    show-file-tree  --count --size --theme monokai
    ```
    - This shows folder counts, file sizes, and a colored theme in one view.

---

## Why it’s useful

!!! abstract

    - Quickly assess folder contents without opening directories.
    - Helpful in **documentation**, **code reviews**, or **project analysis**.
    - Works well with `--max-depth` for summarized folder overviews.

---