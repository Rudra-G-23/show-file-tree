# --theme

The `--theme` flag controls the **color theme** for the tree output in the terminal.  
It affects folder/file colors and makes the output easier to read.

---

## Usage
```
# Apply a theme
show-file-tree  --theme monokai
```

---

## Available Themes

| Theme      | Description                                                             |
| ---------- | ----------------------------------------------------------------------- |
| `colorful` | Default. Bright, colorful icons and folders.                            |
| `monokai`  | Dark theme inspired by Monokai editor colors.                           |
| `light`    | Light theme suitable for light terminal backgrounds.                    |
| `nocolor`  | Plain ASCII output without colors (useful for CI or minimal terminals). |

---

## Example

### Default (colorful)

```
├── 📁 docs
│   └── 📝 readme.md
├── 📁 src
│   └── 🐍 main.py
└── 📖 LICENSE
```

### Monokai theme

```
# Same tree, but colored for Monokai theme
```

### No color

```
├── docs
│   └── readme.md
├── src
│   └── main.py
└── LICENSE
```

---

## Tips

* Combine `--theme` with `--size` or `--count` for **a full-featured, colorful tree**.
* Use `nocolor` for **plain outputs** suitable for Markdown export or CI pipelines:

```
show-file-tree  --theme nocolor --size --count
```

