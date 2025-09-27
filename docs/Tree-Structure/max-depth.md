# --max-depth / -d

The `--max-depth` flag limits **how deep the tree will traverse** into directories.  
This is useful for large projects where you want a **high-level overview** without listing every nested file.

---

## Usage
```
# Show tree with a maximum depth of 2
show-file-tree  --max-depth 2
```

---

## Example

### Full tree (default)

```
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

### With `--max-depth 1`

```
├── 📁 src
├── 📁 docs
└── LICENSE
```

### With `--max-depth 2`

```
├── 📁 src
│   ├── module1
│   └── module2
├── 📁 docs
└── LICENSE
```

---

## Tips

* Combine with `--count` or `--size` for a summarized view of folders at each depth.
* Combine with `--format md` to generate **Markdown documentation** for only the top levels of a project.
* Useful for **quick project overviews**, **documentation snapshots**, or **CI-friendly output**.

