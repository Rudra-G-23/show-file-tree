"""
Recursively scans the filesystem and builds an in-memory tree structure.
"""
import os
from pathlib import Path
from typing import Dict, Any, List, Optional

from .options import DisplayOptions
from .gitignore_parser import get_gitignore_spec
from .time_filters import parse_date_str
from .include_exclude import apply_filters

def build_tree(opts: DisplayOptions) -> Dict[str, Any]:
    """
    Builds the file tree dictionary starting from the root path.
    """
    gitignore_spec = get_gitignore_spec(opts.root_path) if opts.use_gitignore else None
    
    mtime_after_dt = parse_date_str(opts.mtime_after) if opts.mtime_after else None
    mtime_before_dt = parse_date_str(opts.mtime_before) if opts.mtime_before else None

    root_node = _walk(opts.root_path, 0, opts, gitignore_spec, mtime_after_dt, mtime_before_dt)
    
    return root_node

def _walk(
    path: Path,
    depth: int,
    opts: DisplayOptions,
    gitignore_spec: Optional[Any],
    mtime_after_dt: Optional[Any],
    mtime_before_dt: Optional[Any]
) -> Dict[str, Any]:
    """
    Recursive worker function for build_tree.
    """
    try:
        stat = path.stat()
        is_dir = path.is_dir()
    except (FileNotFoundError, PermissionError):
        return None # Skip inaccessible files/dirs

    node = {
        "name": path.name,
        "path": str(path),
        "type": "dir" if is_dir else "file",
        "size": stat.st_size,
        "mtime": stat.st_mtime,
        "ctime": stat.st_ctime,
        "children": [],
        "file_count": 0,
        "dir_count": 0,
        "total_size": stat.st_size
    }

    if not is_dir:
        return node

    if opts.max_depth is not None and depth >= opts.max_depth:
        return node

    try:
        # Get list of child paths
        children_paths = list(path.iterdir())
    except PermissionError:
        return node # Can't read directory

    # Apply include/exclude filters on filenames
    child_names = [p.name for p in children_paths]
    filtered_names = set(apply_filters(child_names, opts.include, opts.exclude))
    
    for child_path in children_paths:
        if child_path.name not in filtered_names:
            continue

        if not opts.show_hidden and child_path.name.startswith('.'):
            continue

        if gitignore_spec and gitignore_spec.match_file(child_path):
            continue

        child_node = _walk(child_path, depth + 1, opts, gitignore_spec, mtime_after_dt, mtime_before_dt)

        if child_node:
            node["children"].append(child_node)
            if child_node["type"] == "dir":
                node["dir_count"] += 1
                node["file_count"] += child_node["file_count"]
                node["dir_count"] += child_node["dir_count"]
                node["total_size"] += child_node["total_size"]
            else:
                node["file_count"] += 1
                node["total_size"] += child_node["size"]

    return node
