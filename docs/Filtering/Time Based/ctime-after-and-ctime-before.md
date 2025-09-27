# Creation Time Filters

**show-file-tree** supports filtering by **file creation time** using the following flags:

- `--ctime-after <YYYY-MM-DD>` — Include only files created **after** the specified date.  
- `--ctime-before <YYYY-MM-DD>` — Include only files created **before** the specified date.

These filters are useful for **auditing recent changes** or **generating snapshots** of files created within a specific period.

---

## Usage

### Include files created after a certain date
```
show-file-tree  --ctime-after 2025-01-01
```

### Include files created before a certain date

```
show-file-tree  --ctime-before 2025-06-01
```

### Combine both

```
show-file-tree  --ctime-after 2025-01-01 --ctime-before 2025-06-01
```

Only files created **between Jan 1, 2025 and Jun 1, 2025** will appear.

---

## Example

### Files in project

```
file1.py   (created 2024-12-10)
file2.py   (created 2025-02-15)
file3.py   (created 2025-05-20)
file4.py   (created 2025-07-01)
```

### Command

```
show-file-tree  --ctime-after 2025-01-01 --ctime-before 2025-06-01
```

### Output

```
├── file2.py
└── file3.py
```

Files outside the date range are excluded.

---

## Tips

* Dates must be in `YYYY-MM-DD` format.
* Combine with other flags like `--max-depth` or `--sort` for precise views:

```
show-file-tree  --ctime-after 2025-01-01 --max-depth 2 --sort name
```

* Works with `--format md` to **export time-filtered Markdown trees**.
