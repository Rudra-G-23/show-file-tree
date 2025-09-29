# --exclude / -e
!!! info
    - The `--exclude` flag allows you to **skip specific files or directories** when building the tree.  
    - You can use glob patterns (wildcards) to match multiple paths.

---

## Usage

!!! success "Usage"

    ```bash title="Only *log files"
    # Exclude all log files
    show-file-tree  --exclude "*.log"
    ```

    ```bash title="A specific folder"
    # Exclude a specific folder
    show-file-tree  --exclude "tests/*"
    ```

---

## Example
!!! example "Example how this command works"

    ```bash title="Files in project"
    src/
    tests/
    README.md
    debug.log
    config.yaml
    ```

    ```bash title="Command"
    show-file-tree  --exclude "*.log" --exclude "tests/*"
    ```

    ```bash title="Output"
    ├── 📁 src
    ├── README.md
    └── config.yaml
    ```

    - `debug.log` and `tests/` are excluded from the tree.

---

## Tips
!!! tip 
    - Multiple `--exclude` flags can be combined for fine-grained filtering.
    - Combine with `--include` to **focus on specific file types** while ignoring others:
        ```bash title="Both"
        show-file-tree  --include "*.py" --exclude "tests/*"
        ```
    - Works with `--format md` to generate **filtered Markdown documentation**.

---