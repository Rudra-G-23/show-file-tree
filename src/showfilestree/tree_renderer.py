"""
Renders the in-memory tree to the terminal using Rich.
"""
from rich.console import Console
from rich.tree import Tree
from typing import Dict, Any

from .options import DisplayOptions
from .theme_styles import THEMES, get_icon_for_file, ICONS
from .size_utils import human_readable_size
from .time_filters import format_time
from .sort_utils import sort_nodes

def render_tree(tree_data: Dict[str, Any], opts: DisplayOptions):
    """
    Renders the file tree to the console.
    """
    console = Console()
    theme = THEMES.get(opts.theme, THEMES["colorful"])

    console.print() # Spacer
    console.print(f"[{theme.heading}]Hello Data Points[/{theme.heading}]")
    console.print(f"[{theme.heading}]+{' ' * 20}---[/]")
    console.print(f"[{theme.highlight}] {opts.root_path.name} [/{theme.highlight}]")
    console.print(f"[{theme.heading}]+{' ' * 20}---[/]")
    
    rich_tree = Tree(
        f"[{theme.dir}]{get_icon_for_file(tree_data['name']) if not opts.no_icons else ''} {tree_data['name']}[/{theme.dir}]"
    )

    _add_nodes(rich_tree, tree_data["children"], opts, theme)
    
    console.print(rich_tree)

def _add_nodes(parent_tree: Tree, children: list, opts: DisplayOptions, theme: Any):
    """Recursively adds nodes to the Rich tree."""
    
    sorted_children = sort_nodes(children, opts.sort_by, opts.sort_order)

    for i, child in enumerate(sorted_children):
        is_last = (i == len(sorted_children) - 1)
        
        meta_parts = []
        if opts.show_size:
            size = child.get("total_size", child.get("size", 0))
            meta_parts.append(human_readable_size(size))
        if opts.show_counts and child['type'] == 'dir':
            meta_parts.append(f"{child['file_count']}f, {child['dir_count']}d")
        
        meta_str = f" ([{theme.meta}]{', '.join(meta_parts)}[/{theme.meta}])" if meta_parts else ""

        if child["type"] == "dir":
            icon = ICONS["folder_closed"] if not opts.no_icons else "D:"
            label = f"[{theme.dir}]{icon} {child['name']}[/{theme.dir}]{meta_str}"
            child_tree = parent_tree.add(label, guide_style="bold" if not is_last else "dim")
            _add_nodes(child_tree, child["children"], opts, theme)
        else: # It's a file
            icon = get_icon_for_file(child["name"]) if not opts.no_icons else "F:"
            label = f"[{theme.file}]{icon} {child['name']}[/{theme.file}]{meta_str}"
            parent_tree.add(label)
