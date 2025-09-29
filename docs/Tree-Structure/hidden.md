# --hidden

!!! info 

    - The `--hidden` flag displays **hidden files and directories** in your tree output.  
    - Hidden files typically start with a dot (`.`) on Unix-like systems (e.g., `.git`, `.env`) or are marked as hidden on Windows.

---

## Usage

!!! success "Usage"

    ```bash linenums="1" hl_lines="2"
    # Include hidden files in the tree
    show-file-tree  --hidden
    ```

---

## Example

!!! example

    === "Without `--hidden`"
        ```bash
        ├── 📁 src
        │   └── main.py
        └── README.md
        ```
    === "With `--hidden`"
        ```bash
        ├── 📁 .git
        ├── 📁 src
        │   └── main.py
        ├── .env
        └── README.md
        ```

---

## Tips

!!! tip

    - Combine with `--gitignore` to **respect `.gitignore`** but still show hidden files not ignored by Git.
    - Combine with `--format md` to generate Markdown documentation including hidden files.
    - Useful for **project auditing**, **debugging**, or **full repo visualization**.

---

# Advanced Features

!!! example "Advanced Feature"

    === "Hidden + gitignore"
        ```bash title="Hidden + gitignore"
        show-file-tree  --hidden --gitignore
        ```
    === "Hidden + gitignore + format md"
        ```bash
        show-file-tree  --hidden --gitignore --format md
        ```
---