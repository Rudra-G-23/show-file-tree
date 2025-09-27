# --hidden

The `--hidden` flag displays **hidden files and directories** in your tree output.  
Hidden files typically start with a dot (`.`) on Unix-like systems (e.g., `.git`, `.env`) or are marked as hidden on Windows.

---

## Usage
```
# Include hidden files in the tree
show-file-tree  --hidden
```

---

## Example

### Without `--hidden`

```
├── 📁 src
│   └── main.py
└── README.md
```

### With `--hidden`

```
├── 📁 .git
├── 📁 src
│   └── main.py
├── .env
└── README.md
```

---

## Tips

* Combine with `--gitignore` to **respect `.gitignore`** but still show hidden files not ignored by Git:

```
show-file-tree  --hidden --gitignore
```

* Combine with `--format md` to generate Markdown documentation including hidden files.
* Useful for **project auditing**, **debugging**, or **full repo visualization**.


