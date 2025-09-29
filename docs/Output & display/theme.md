---
icon: material/theme-light-dark
---

# --theme

!!! info

    - The `--theme` flag controls the **color theme** for the tree output in the terminal.  
    - It affects folder/file colors and makes the output easier to read.

---

## :fontawesome-solid-user-check: Usage

!!! success "Usage"

    ```bash title="Apply a theme"
    # Apply a theme
    show-file-tree  --theme monokai
    ```

---

## material-heart-multiple-outline: Available Themes

!!! info "Available Themes"

    | Theme      | Description                                                             |
    | ---------- | ----------------------------------------------------------------------- |
    | `colorful` | Default. Bright, colorful icons and folders.                            |
    | `monokai`  | Dark theme inspired by Monokai editor colors.                           |
    | `light`    | Light theme suitable for light terminal backgrounds.                    |
    | `nocolor`  | Plain ASCII output without colors (useful for CI or minimal terminals). |

---

## material-hexagon-multiple: Example

!!! example

    === "Default (colorful)"
        ```bash 
        ├── 📁 docs
        │   └── 📝 readme.md
        ├── 📁 src
        │   └── 🐍 main.py
        └── 📖 LICENSE
        ```
    === "Monokai theme"
        ``` bash
        # Same tree, but colored for Monokai theme
        ```
    === "No color"
        ```bash
        ├── docs
        │   └── readme.md
        ├── src
        │   └── main.py
        └── LICENSE
            ```

---

## :material-fountain-pen-tip: Tips

!!! tip

    - Combine `--theme` with `--size` or `--count` for **a full-featured, colorful tree**.
        ```bash
        show-file-tree  --theme nocolor --size --count
        ```
    - Use `nocolor` for **plain outputs** suitable for Markdown export or CI pipelines:

---