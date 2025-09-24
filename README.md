# show-file-tree

A small, fast CLI tool to display styled file/folder trees with rich options, colors, icons, and metadata.

## Installation

You can install `show-file-tree` using `pip`:

```bash
pip install show-file-tree
````

## Quick Start

Navigate to any directory and run the command.

### Default Output:

    ```bash
    show-file-tree .
    ```




### Display with more details like size, counts, and limited depth:

    ```bash
    show-file-tree . -d 2 --size --count
    ```

### Export the tree to a Markdown file:

    ```bash
    show-file-tree /path/to/your/project --format md
    ```

This will create a `project-file-tree.md` file in your current directory.

## Features & Flags

`show-file-tree` offers a rich set of flags to customize the output.

* `-d, --max-depth`: Limit the recursion depth.
* `--gitignore / --no-gitignore`: Respect or ignore `.gitignore` files (default: respect).
* `--hidden`: Show hidden files and folders.
* `--sort {name,size}`: Sort the output by name or size.
* `--order {asc,desc}`: Set the sort order.
* `--format {tree,md}`: Output format (default: tree). Automatically falls back to `md` for very large trees.
* `--size`: Display file/folder sizes.
* `--count`: Display file/directory counts within folders.
* `--mtime-after, --mtime-before`: Filter by modification time.
* `--include, --exclude`: Filter by glob patterns.
* `--no-icons`: Render a plain ASCII tree.
* `--theme`: Apply a color theme (`colorful`, `monokai`, `light`, `nocolor`).
* `--top N`: List the top N files by size or modification time.
* `--about, --version`: Show package information.

## Contributing

Contributions are welcome! Please see CONTRIBUTING.md for details on how to set up your development environment and submit pull requests.

## Author / Maintainer

Rudra Prasad Bhuyan

## License

This project is licensed under the MIT License - see the LICENSE file for details.


