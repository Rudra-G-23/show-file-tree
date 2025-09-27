# --order

The `--order` flag controls the **sorting order** of files and directories in the tree.

- `asc` — Sort in **ascending order** (default).  
- `desc` — Sort in **descending order**.

---

## Usage
```
# Sort by name in descending order
show-file-tree  --sort name --order desc
```

```
# Sort by size in ascending order
show-file-tree  --sort size --order asc
```

---

## Example

### Ascending order (default)

```
├── README.md
├── docs
└── src
```

### Descending order

```
├── src
├── docs
└── README.md
```

---

## Tips

* Always combine `--order` with `--sort` to define **both sort criteria and direction**.
* Works with `--format md`, `--size`, or `--count` for **customized tree outputs**.

```
