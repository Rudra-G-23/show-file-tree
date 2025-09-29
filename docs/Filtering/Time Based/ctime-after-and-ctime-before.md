---
icon: material/timer-check
---

# Creation Time Filters

!!! info 

    **show-file-tree** supports filtering by **file creation time** using the following flags:

    - `--ctime-after <YYYY-MM-DD>` — Include only files created **after** the specified date.  
    - `--ctime-before <YYYY-MM-DD>` — Include only files created **before** the specified date.

    These filters are useful for **auditing recent changes** or **generating snapshots** of files created within a specific period.

---

## :fontawesome-solid-user-check: Usage

!!! success "Usage"

    === "After"
        ```bash title="Include files created after a certain date"
        show-file-tree  --ctime-after 2025-01-01
        ```
    === "Before"
        ```bash title="Include files created before a certain date"
        show-file-tree  --ctime-before 2025-06-01
        ```

    === "Combine both"
        ```bash title="Combine"
        show-file-tree  --ctime-after 2025-01-01 --ctime-before 2025-06-01 # (1)!
        ```

        1.  Only files created **between Jan 1, 2025 and Jun 1, 2025** will appear.

---

## :material-hexagon-multiple: Example

!!! example

    === "Files in project"
        ```bash
        file1.py   (created 2024-12-10)
        file2.py   (created 2025-02-15)
        file3.py   (created 2025-05-20)
        file4.py   (created 2025-07-01)
        ```
    === "Command"
        ```bash
        show-file-tree  --ctime-after 2025-01-01 --ctime-before 2025-06-01
        ```
    === "Output"
        ```bash
        ├── file2.py
        └── file3. # (1)!
        ```

        1. Files outside the date range are excluded.

---

## :material-fountain-pen-tip: Tips

!!! tip

    - Dates must be in `YYYY-MM-DD` format.
    - Combine with other flags like `--max-depth` or `--sort` for precise views:
        ```bash title="Advanced Features"
        show-file-tree  --ctime-after 2025-01-01 --max-depth 2 --sort name
        ```
    - Works with `--format md` to **export time-filtered Markdown trees**.

---