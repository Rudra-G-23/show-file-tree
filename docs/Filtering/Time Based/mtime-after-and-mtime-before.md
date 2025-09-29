---
icon: material/timer-cog
---

# Modification Time Filters

!!! info

    **show-file-tree** supports filtering by **file modification time** using the following flags:

    - `--mtime-after <YYYY-MM-DD>` — Include only files modified **after** the specified date.  
    - `--mtime-before <YYYY-MM-DD>` — Include only files modified **before** the specified date.

    These filters are useful for **tracking recent changes** or **documenting updates** within a specific timeframe.

---

## :fontawesome-solid-user-check: Usage

!!! success "Usage"

    === "After"
        ```bash title="Include files modified after a certain date"
        show-file-tree  --mtime-after 2025-01-01
        ```
    === "Before"
        ```bash title="Include files modified before a certain date"
        show-file-tree  --mtime-before 2025-06-01
        ```
    === "Combine"
        ```bash title="Combine both"
        show-file-tree  --mtime-after 2025-01-01 --mtime-before 2025-06-01 # (1)!
        ```

        1. Only files modified **between Jan 1, 2025 and Jun 1, 2025** will appear.

---

## :material-hexagon-multiple: Example

!!! example

    === "Files in project"
        ```bash
        file1.py   (modified 2024-12-10)
        file2.py   (modified 2025-02-15)
        file3.py   (modified 2025-05-20)
        file4.py   (modified 2025-07-01)
        ```
    === "Command"
        ```bash
        show-file-tree  --mtime-after 2025-01-01 --mtime-before 2025-06-01
        ```
    === "Output"
        ```bash 
        ├── file2.py
        └── file3.py # (1)!
        ```

        1. Files outside the date range are excluded.

---

## :material-fountain-pen-tip: Tips

!!! tip

    - Dates must be in `YYYY-MM-DD` format.
    - Combine with other flags like `--max-depth`, `--sort`, or `--count` for more detailed views:
        ```bash title="Advanced Command"
        show-file-tree  --mtime-after 2025-01-01 --max-depth 2 --count
        ```
    - Works with `--format md` to **export modification-time filtered Markdown trees**.
  
---