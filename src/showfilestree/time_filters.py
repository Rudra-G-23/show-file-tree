"""
Functions for parsing and applying time-based filters.
"""
import datetime
from typing import Optional

def parse_date_str(date_str: str) -> Optional[datetime.datetime]:
    """Parses a date string into a datetime object."""
    try:
        return datetime.datetime.fromisoformat(date_str)
    except ValueError:
        return None # Or raise a specific error for the CLI to catch

def format_time(timestamp: float, format_str: str) -> str:
    """Formats a timestamp according to the specified format."""
    dt_object = datetime.datetime.fromtimestamp(timestamp)
    if format_str == "iso":
        return dt_object.isoformat(sep=' ', timespec='minutes')
    elif format_str == "relative":
        # Basic relative time implementation
        now = datetime.datetime.now()
        delta = now - dt_object
        if delta.days > 0:
            return f"{delta.days}d ago"
        elif delta.seconds > 3600:
            return f"{delta.seconds // 3600}h ago"
        elif delta.seconds > 60:
            return f"{delta.seconds // 60}m ago"
        else:
            return "just now"
    else:
        try:
            return dt_object.strftime(format_str)
        except ValueError:
            return dt_object.isoformat() # Fallback
