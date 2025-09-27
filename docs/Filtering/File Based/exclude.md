# --exclude / -e

The `--exclude` flag allows you to **skip specific files or directories** when building the tree.  
You can use glob patterns (wildcards) to match multiple paths.

---

## Usage
```
# Exclude all log files
show-file-tree  --exclude "*.log"
```

```
# Exclude a specific folder
show-file-tree  --exclude "tests/*"
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
show-file-tree  --exclude "*.log" --exclude "tests/*"
```

### Output

```
├── 📁 src
├── README.md
└── config.yaml
```

`debug.log` and `tests/` are excluded from the tree.

---

## Tips

* Multiple `--exclude` flags can be combined for fine-grained filtering.
* Combine with `--include` to **focus on specific file types** while ignoring others:

```
show-file-tree  --include "*.py" --exclude "tests/*"
```

* Works with `--format md` to generate **filtered Markdown documentation**.

