"""
Applies include/exclude filters to file paths.
"""
import fnmatch
from typing import List

def apply_filters(paths: List[str], include: List[str], exclude: List[str]) -> List[str]:
    """Applies include and exclude glob patterns to a list of paths."""
    # Start with all paths if no include patterns, otherwise start with an empty set
    if include:
        included_paths = set()
        for pattern in include:
            included_paths.update(fnmatch.filter(paths, pattern))
    else:
        included_paths = set(paths)

    # If there are no exclude patterns, we are done
    if not exclude:
        return list(included_paths)

    # Filter out excluded paths
    excluded_paths = set()
    for pattern in exclude:
        excluded_paths.update(fnmatch.filter(included_paths, pattern))

    return list(included_paths - excluded_paths)
