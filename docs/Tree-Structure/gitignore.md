# --gitignore / --no-gitignore

The `--gitignore` flag makes **show-file-tree** respect `.gitignore` files, excluding ignored files and folders from the tree.  
The `--no-gitignore` flag **ignores `.gitignore`**, showing all files and folders.

---

## Usage

### Respect `.gitignore` (default)
```
show-file-tree  --gitignore
```

Only files **not listed** in `.gitignore` appear.

### Ignore `.gitignore`

```
show-file-tree  --no-gitignore
```

All files are displayed, even if ignored in Git.

---

## Example

#### `.gitignore` contents:

```
__pycache__/
*.log
.env
```

#### With `--gitignore`

```
├── 📁 src
│   └── main.py
└── README.md
```

Ignored: `__pycache__/`, `.env`, `.log` files.

#### With `--no-gitignore`

```
├── 📁 src
│   ├── main.py
│   └── __pycache__/main.cpython-310.pyc
├── .env
├── debug.log
└── README.md
```

---

## Tips

* Useful in **CI pipelines** where you want a complete file tree.
* Combine with `--hidden` to show hidden files that are also ignored by Git.
* Combine with `--format md` for full documentation including ignored files:

```
show-file-tree  --no-gitignore --format md
```
