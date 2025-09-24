"""
Miscellaneous utility functions.
"""
import os
import sys
from pathlib import Path
from contextlib import contextmanager

def safe_path_join(*args):
    """Safely join path components."""
    return os.path.join(*args)

def is_windows() -> bool:
    """Check if the current OS is Windows."""
    return sys.platform == "win32"

@contextmanager
def change_dir(destination: Path):
    """Context manager to temporarily change the current working directory."""
    current_dir = Path.cwd()
    try:
        os.chdir(destination)
        yield
    finally:
        os.chdir(current_dir)
