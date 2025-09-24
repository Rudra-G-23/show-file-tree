"""
Parses .gitignore files and checks if a path should be ignored.
"""
from pathlib import Path
from typing import Optional, List
import pathspec

def find_gitignore(start_path: Path) -> Optional[Path]:
    """Finds the .gitignore file in the current or parent directories."""
    current = start_path.resolve()
    while current != current.parent:
        gitignore_path = current / ".gitignore"
        if gitignore_path.is_file():
            return gitignore_path
        current = current.parent
    return None

def get_gitignore_spec(root_path: Path) -> Optional[pathspec.PathSpec]:
    """Creates a pathspec object from the .gitignore file."""
    gitignore_file = find_gitignore(root_path)
    if gitignore_file:
        with open(gitignore_file, 'r') as f:
            return pathspec.PathSpec.from_lines('gitwildmatch', f)
    return None
