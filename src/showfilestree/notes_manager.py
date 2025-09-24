"""
Manages adding, retrieving, and storing notes for files/directories.
"""
import json
import datetime
from pathlib import Path
from typing import Dict, Any, List

def get_notes_db_path(project_root: Path) -> Path:
    """Determines the path for the notes database."""
    local_db_path = project_root / ".show-file-tree"
    if local_db_path.is_dir() or local_db_path.mkdir(exist_ok=True):
         return local_db_path / "notes.json"

    home_db_dir = Path.home() / ".local" / "share" / "show-file-tree"
    home_db_dir.mkdir(parents=True, exist_ok=True)
    return home_db_dir / f"{project_root.name}_notes.json"

def read_notes(db_path: Path) -> Dict[str, Any]:
    """Reads the notes from the JSON database."""
    if not db_path.exists():
        return {"notes": {}}
    try:
        with open(db_path, "r") as f:
            data = json.load(f)
            return data if "notes" in data else {"notes": {}}
    except (json.JSONDecodeError, IOError):
        return {"notes": {}}

def write_notes(db_path: Path, data: Dict[str, Any]):
    """Writes notes to the JSON database."""
    try:
        with open(db_path, "w") as f:
            json.dump(data, f, indent=2)
    except IOError:
        pass

def add_note(project_root: Path, path_str: str, note_text: str):
    """Adds a note for a specific path, including file metadata."""
    db_path = get_notes_db_path(project_root)
    data = read_notes(db_path)
    
    target_path = project_root / path_str
    size, mtime = None, None
    if target_path.exists():
        stat = target_path.stat()
        size = stat.st_size
        mtime = stat.st_mtime

    note_entry = {
        "text": note_text,
        "timestamp": datetime.datetime.now().isoformat(),
        "project_folder": project_root.name,
        "size_bytes": size,
        "mtime": mtime,
    }
    
    if "notes" not in data:
        data["notes"] = {}
        
    data["notes"][path_str] = note_entry
    write_notes(db_path, data)

def get_all_notes(project_root: Path) -> List[Dict[str, Any]]:
    """Retrieves all notes, sorted by most recent."""
    db_path = get_notes_db_path(project_root)
    data = read_notes(db_path)
    notes_list = []
    
    notes_data = data.get("notes", {})
    if not isinstance(notes_data, dict):
        return []

    for path, details in notes_data.items():
        notes_list.append({
            "file_name": path,
            "note": details["text"],
            "time": details.get("timestamp", "N/A"),
            "size_bytes": details.get("size_bytes"),
            "mtime": details.get("mtime"),
            "main_folder": details.get("project_folder", project_root.name)
        })
    notes_list.sort(key=lambda x: x["time"], reverse=True)
    return notes_list

def delete_note(project_root: Path, path_str: str) -> bool:
    """Deletes a note for a specific path. Returns True if successful."""
    db_path = get_notes_db_path(project_root)
    data = read_notes(db_path)
    if "notes" in data and path_str in data["notes"]:
        del data["notes"][path_str]
        write_notes(db_path, data)
        return True
    return False

def clear_all_notes(project_root: Path):
    """Deletes all notes for the project."""
    db_path = get_notes_db_path(project_root)
    write_notes(db_path, {"notes": {}})