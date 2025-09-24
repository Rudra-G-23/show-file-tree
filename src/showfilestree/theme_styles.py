"""
Defines color themes, icons, and styles for rendering the tree.
"""
from typing import Dict

# Using Nerd Font icons for better visual representation
# Users without Nerd Fonts will see placeholder characters.
# A fallback to ASCII is handled in the renderer.
ICONS = {
    "folder_closed": "📁",
    "folder_open": "📂",
    "file": "📄",
    "python": "🐍",
    "javascript": "📜",
    "typescript": "📜",
    "html": "🌐",
    "css": "🎨",
    "json": "📦",
    "markdown": "📝",
    "git": "🌿",
    "image": "🖼️",
    "archive": "📦",
    "audio": "🎵",
    "video": "🎬",
    "font": "🔤",
    "binary": "⚙️",
    "config": "🔧",
    "lock": "🔒",
    "license": "📜",
    "readme": "📖",
}

# Mapping file extensions to icon names
FILE_ICON_MAP = {
    ".py": "python",
    ".js": "javascript",
    ".ts": "typescript",
    ".jsx": "javascript",
    ".tsx": "typescript",
    ".html": "html",
    ".css": "css",
    ".scss": "css",
    ".json": "json",
    ".md": "markdown",
    ".gitignore": "git",
    ".git": "git",
    ".png": "image",
    ".jpg": "image",
    ".jpeg": "image",
    ".gif": "image",
    ".svg": "image",
    ".zip": "archive",
    ".tar": "archive",
    ".gz": "archive",
    ".rar": "archive",
    ".7z": "archive",
    ".mp3": "audio",
    ".wav": "audio",
    ".mp4": "video",
    ".mov": "video",
    ".avi": "video",
    ".ttf": "font",
    ".otf": "font",
    ".woff": "font",
    ".woff2": "font",
    ".lock": "lock",
    ".yml": "config",
    ".yaml": "config",
    ".toml": "config",
    ".ini": "config",
    "license": "license",
    "readme.md": "readme",
}

class Theme:
    """Holds the styles for a theme."""
    def __init__(self, heading, dir_style, file_style, meta_style, highlight_style):
        self.heading = heading
        self.dir = dir_style
        self.file = file_style
        self.meta = meta_style # For size, counts, time
        self.highlight = highlight_style

THEMES: Dict[str, Theme] = {
    "colorful": Theme(
        heading="bold #5e17eb",
        dir_style="bold cyan",
        file_style="default",
        meta_style="dim green",
        highlight_style="bold white on #5e17eb"
    ),
    "monokai": Theme(
        heading="bold #f92672",
        dir_style="bold #a6e22e",
        file_style="#e6db74",
        meta_style="#75715e",
        highlight_style="bold black on #f92672"
    ),
    "light": Theme(
        heading="bold #d7005f",
        dir_style="bold blue",
        file_style="black",
        meta_style="dim #5f5f00",
        highlight_style="bold white on #d7005f"
    ),
    "nocolor": Theme(
        heading="",
        dir_style="",
        file_style="",
        meta_style="",
        highlight_style=""
    ),
}

def get_icon_for_file(filename: str) -> str:
    """Returns an icon for a given filename based on its extension."""
    filename_lower = filename.lower()
    # Check for full filenames first (e.g., 'LICENSE')
    if filename_lower in FILE_ICON_MAP:
        return ICONS.get(FILE_ICON_MAP[filename_lower], ICONS["file"])

    # Check extensions
    ext = "." + filename_lower.split(".")[-1] if "." in filename_lower else None
    if ext and ext in FILE_ICON_MAP:
        return ICONS.get(FILE_ICON_MAP[ext], ICONS["file"])
    return ICONS["file"]
