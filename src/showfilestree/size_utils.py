"""
Helper functions for formatting file sizes.
"""

def human_readable_size(size_bytes: int) -> str:
    """Converts bytes to a human-readable format (KB, MB, GB, TB)."""
    if size_bytes == 0:
        return "0 B"
    size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
    i = 0
    while size_bytes >= 1024 and i < len(size_name) - 1:
        size_bytes /= 1024.0
        i += 1
    # Format to one decimal place if not a whole number, otherwise show as integer
    if size_bytes == int(size_bytes):
        return f"{int(size_bytes)} {size_name[i]}"
    return f"{size_bytes:.1f} {size_name[i]}"
