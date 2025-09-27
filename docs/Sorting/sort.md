# --sort

The `--sort` flag controls how files and directories are sorted before displaying the tree.

## Usage
```
show-file-tree  --sort name
show-file-tree  --sort size
```

## Options

* `name` — Sort alphabetically (default).
* `size` — Sort by file or folder size (smallest → largest).

## Examples

### Sort by name (default)

```
show-file-tree .
```

Output (simplified):

```
├── 📁 docs
├── 📁 src
└── 📄 README.md
```

### Sort by size

```
show-file-tree . --sort size
```

Output (simplified):

```
└── 📄 README.md (25 KB)
├── 📁 src (100 KB)
└── 📁 docs (200 KB)
```

---

## Tip

You can combine `--sort` with [`--order`](order.md) to control ascending/descending order.
