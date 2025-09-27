# Changelog

All notable changes to this project will be documented in this file.  
The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [0.0.1] - 2025-09-25

### Added
- Initial release of **show-file-tree**.
- Core functionality: build and display styled file/folder trees directly in the terminal.
- CLI flags:
  - `-d, --max-depth` → Limit recursion depth.
  - `--gitignore / --no-gitignore` → Respect or ignore `.gitignore` files.
  - `--hidden` → Show hidden files and directories.
  - `--sort {name,size}` → Sort tree output by name or size.
  - `--order {asc,desc}` → Control sorting order.
  - `--size` → Display file/folder sizes.
  - `--count` → Show file/directory counts inside folders.
  - `--format {tree,md}` → Output format (tree in terminal or export to Markdown).
  - `--theme {colorful, monokai, light, nocolor}` → Apply custom color themes.
  - `--no-icons` → Render plain ASCII trees without icons.
  - `--mtime-after`, `--mtime-before` → Filter files/folders by modification time.
  - `--ctime-after`, `--ctime-before` → Filter files/folders by creation time.
  - `--include`, `--exclude` → Filter paths by glob patterns.
- General commands:
  - `--version` → Show package version.
  - `--about` → Show package information.



