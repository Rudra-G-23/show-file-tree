# --no-icons

The `--no-icons` flag disables file/folder icons in the output.  
This is useful if:
- You’re working in a terminal that doesn’t support Unicode emojis.
- You prefer a plain ASCII output.
- You want minimal, icon-free Markdown exports.

---

## Usage
```
show-file-tree  --no-icons
```

---

## Example

### Default (with icons)

```
├── 📁 docs
│   └── 📝 readme.md
├── 📁 src
│   └── 🐍 main.py
└── 📖 LICENSE
```

### With `--no-icons`

```
├── docs
│   └── readme.md
├── src
│   └── main.py
└── LICENSE
```

---

## Behind the scenes 

By default, **show-file-tree** uses a rich icon mapping for file types:


| File Type / Extension         |   Icon  | Meaning / Notes         |
| ----------------------------- | :-----: | ----------------------- |
| Folders                       | 📁 / 📂 | Closed / Open folder    |
| Generic file                  |    📄   | Default file            |
| `.py`                         |    🐍   | Python script           |
| `.js`, `.jsx`                 |    📜   | JavaScript file         |
| `.ts`, `.tsx`                 |    📜   | TypeScript file         |
| `.html`                       |    🌐   | HTML file               |
| `.css`, `.scss`               |    🎨   | Stylesheet              |
| `.json`                       |    📦   | JSON data               |
| `.md`                         |    📝   | Markdown file           |
| `readme.md` (exact match)     |    📖   | README file             |
| `.git`, `.gitignore`          |    🌿   | Git-related file        |
| `.png`, `.jpg`, `.jpeg`, etc. |   🖼️   | Image files             |
| `.zip`, `.tar`, `.gz`, etc.   |    📦   | Archive/compressed file |
| `.mp3`, `.wav`                |    🎵   | Audio file              |
| `.mp4`, `.mov`, `.avi`        |    🎬   | Video file              |
| `.ttf`, `.otf`, `.woff`, etc. |    🔤   | Font files              |
| `.exe`, `.bin` (generic bin)  |    ⚙️   | Binary file             |
| `.yml`, `.yaml`, `.ini`, etc. |    🔧   | Config file             |
| `.lock`                       |    🔒   | Lock file               |
| `license`                     |    📜   | License file            |


If any file type is missing then you can create an [Github Issues](https://github.com/Rudra-G-23/show-file-tree/issues_)

---

## Tip

You can combine `--no-icons` with other options such as `--size`, `--count`, or `--theme` for a clean but informative tree.


