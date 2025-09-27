# --include / -i

The `--include` flag allows you to **show only specific files or directories** when building the tree.  
You can use glob patterns (wildcards) to match multiple paths.

---

## Usage
```
# Include only Python files
show-file-tree  --include "*.py"
```

```
# Include all Markdown files
show-file-tree  --include "*.md"
```

---

## Example

### Files in project

```
src/
tests/
README.md
debug.log
config.yaml
```

### Command

```
show-file-tree . --include "*.py" --include "*.md"
```

### Output

```
├── 📁 src
│   └── main.py
└── README.md
```

Only `*.py` and `*.md` files are included in the tree.

---

## Tips

* Multiple `--include` flags can be combined to include several file types.
* Combine with `--exclude` to **refine filtering**:

```
show-file-tree  --include "*.py" --exclude "tests/*"
```

* Works with `--format md` to generate **filtered Markdown documentation**.
