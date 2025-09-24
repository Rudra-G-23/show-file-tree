"""
Central dataclass for holding parsed CLI options.
"""
from dataclasses import dataclass, field
from typing import Optional, List
from pathlib import Path

@dataclass
class DisplayOptions:
    """A structured class to hold all CLI options."""
    root_path: Path
    max_depth: Optional[int] = None
    use_gitignore: bool = True
    show_hidden: bool = False
    sort_by: str = "name"
    sort_order: str = "asc"
    output_format: str = "tree"
    show_size: bool = False
    show_counts: bool = False
    mtime_after: Optional[str] = None
    mtime_before: Optional[str] = None
    ctime_after: Optional[str] = None
    ctime_before: Optional[str] = None
    time_format: str = "iso"
    include: Optional[List[str]] = field(default_factory=list)
    exclude: Optional[List[str]] = field(default_factory=list)
    no_icons: bool = False
    folder_mode: str = "fd" # fd: folders + files, f: folders only
    theme: str = "colorful"
    note_path: Optional[str] = None
    note_text: Optional[str] = None
    show_notes: bool = False
    top_n: Optional[int] = None
    top_by: str = "size"
