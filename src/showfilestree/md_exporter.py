"""
Exports the file tree to a Markdown file.
"""
from pathlib import Path
from typing import Dict, Any, List

from .options import DisplayOptions
from .size_utils import human_readable_size
from .time_filters import format_time
from .sort_utils import sort_nodes
from .theme_styles import get_icon_for_file, ICONS

def export_to_markdown(tree_data: Dict[str, Any], opts: DisplayOptions) -> Path:
    """
    Generates a Markdown file representing the directory tree.
    """
    output_filename = f"{opts.root_path.name}-file-tree.md"
    output_path = Path.cwd() / output_filename
    
    md_lines = []
    
    # Add styled heading hint for rich viewers
    md_lines.append(f'<h1 style="color:#5e17eb;">Hello Data Points</h1>\n')
    
    md_lines.append(f'```text')
    md_lines.append(f'+{"-" * 60}+')
    md_lines.append(f'| {opts.root_path.name.center(58)} |')
    md_lines.append(f'+{"-" * 60}+\n')

    _build_md_lines(md_lines, tree_data, "", True, opts)

    md_lines.append('```')

    with open(output_path, "w", encoding="utf-8") as f:
        f.write("\n".join(md_lines))
        
    return output_path

def _build_md_lines(
    md_lines: List[str],
    node: Dict[str, Any],
    prefix: str,
    is_root: bool,
    opts: DisplayOptions
):
    """Recursively builds the markdown string for the tree."""
    
    if not is_root:
        md_lines.append(_format_md_node(node, prefix, opts))

    children = sort_nodes(node.get("children", []), opts.sort_by, opts.sort_order)
    for i, child in enumerate(children):
        is_last = (i == len(children) - 1)
        new_prefix = prefix + ("    " if is_last else "│   ")
        _build_md_lines(md_lines, child, new_prefix, False, opts)

def _format_md_node(node: Dict[str, Any], prefix: str, opts: DisplayOptions) -> str:
    """Formats a single node for the markdown output."""
    connector = "└── " if prefix.endswith("    ") else "├── "
    
    meta_parts = []
    if opts.show_size:
        size = node.get("total_size", node.get("size", 0))
        meta_parts.append(human_readable_size(size))
    if opts.show_counts and node['type'] == 'dir':
        meta_parts.append(f"{node['file_count']}f, {node['dir_count']}d")
    
    meta_str = f" ({', '.join(meta_parts)})" if meta_parts else ""

    if node["type"] == "dir":
        icon = ICONS["folder_closed"] if not opts.no_icons else "📁"
        name = f"{icon} {node['name']}"
    else:
        icon = get_icon_for_file(node['name']) if not opts.no_icons else "📄"
        name = f"{icon} {node['name']}"

    return f"{prefix.removesuffix('    ').removesuffix('│   ')}{connector}{name}{meta_str}"
