"""
Sorting policies for directory contents.
"""
from typing import List, Dict, Any

def sort_nodes(nodes: List[Dict[str, Any]], sort_by: str, order: str) -> List[Dict[str, Any]]:
    """Sorts a list of file/directory nodes."""
    if sort_by not in ["name", "size"]:
        sort_by = "name"

    # Separate directories and files to sort them independently and list dirs first
    dirs = sorted([n for n in nodes if n['type'] == 'dir'], key=lambda x: x.get(sort_by, 0))
    files = sorted([n for n in nodes if n['type'] == 'file'], key=lambda x: x.get(sort_by, 0))

    if order == "desc":
        dirs.reverse()
        files.reverse()

    return dirs + files
