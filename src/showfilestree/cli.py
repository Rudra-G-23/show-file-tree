# src/showfilestree/cli.py

from typing import Optional, List
from pathlib import Path
import typer
from rich.console import Console
from rich.table import Table

from . import __version__
from .options import DisplayOptions
from .tree_builder import build_tree
from .tree_renderer import render_tree
from .md_exporter import export_to_markdown
from .notes_manager import add_note, get_all_notes
from .metadata import get_about_text

from .size_utils import human_readable_size # Add this import
from .notes_manager import add_note, get_all_notes, delete_note, clear_all_notes # Update this import
import datetime
# --- Main App and Callbacks ---
app = typer.Typer(
    name="show-file-tree",
    help="A small, fast CLI tool to display styled file/folder trees.",
    add_completion=False,
    rich_markup_mode="markdown"
)
console = Console()

def version_callback(value: bool):
    if value:
        console.print(f"show-file-tree version: {__version__}")
        raise typer.Exit()

def about_callback(value: bool):
    if value:
        console.print(get_about_text())
        raise typer.Exit()

# --- Notes Sub-App ---
notes_app = typer.Typer(name="note", help="Manage notes for files and directories.")
app.add_typer(notes_app)

@notes_app.command("add")
def add_note_command(
    path: str = typer.Argument(..., help="Path of the file/dir to add a note to."),
    text: str = typer.Argument(..., help="The text of the note to add."),
):
    """Adds a persistent note to a file or directory."""
    project_root = Path.cwd().resolve()
    add_note(project_root, path, text)
    console.print(f"[green]Note added to '{path}'.[/green]")

@notes_app.command("show")
def show_notes_command():
    """Displays all notes for the current project."""
    project_root = Path.cwd().resolve()
    notes = get_all_notes(project_root)
    if not notes:
        console.print("[yellow]No notes found for this project.[/yellow]")
        raise typer.Exit()

    table = Table(title="Project Notes")
    table.add_column("File Path", style="cyan", no_wrap=True)
    table.add_column("Note", style="default")
    table.add_column("Size", style="magenta", justify="right")
    table.add_column("Modified", style="green", justify="right")

    for note in notes:
        size_str = human_readable_size(note['size_bytes']) if note['size_bytes'] is not None else "N/A"
        
        mtime_str = "N/A"
        if note['mtime']:
            mtime_dt = datetime.datetime.fromtimestamp(note['mtime'])
            mtime_str = mtime_dt.strftime("%Y-%m-%d %H:%M")

        table.add_row(note['file_name'], note['note'], size_str, mtime_str)

    console.print(table)

@notes_app.command("delete")
def delete_note_command(
    path: str = typer.Argument(..., help="The path of the note to delete.")
):
    """Deletes a note for a specific file or directory."""
    project_root = Path.cwd().resolve()
    if delete_note(project_root, path):
        console.print(f"[green]Note for '{path}' deleted.[/green]")
    else:
        console.print(f"[yellow]No note found for '{path}'.[/yellow]")

@notes_app.command("clear")
def clear_notes_command(
    force: bool = typer.Option(False, "--force", help="Required to confirm deletion of all notes.")
):
    """Deletes ALL notes for the current project."""
    if not force:
        console.print("[yellow]Aborted. Use the --force flag to delete all notes.[/yellow]")
        raise typer.Exit()
    
    project_root = Path.cwd().resolve()
    clear_all_notes(project_root)
    console.print("[green]All notes for this project have been cleared.[/green]")


# --- Main Callback for Tree-Drawing and Global Options ---
@app.callback(invoke_without_command=True)
def main(
    ctx: typer.Context,
    root_path: Path = typer.Argument(
        ".",
        exists=True,
        file_okay=False,
        dir_okay=True,
        readable=True,
        resolve_path=True,
        help="The root directory to start the tree from.",
    ),
    max_depth: Optional[int] = typer.Option(None, "-d", "--max-depth", help="Maximum recursion depth.", rich_help_panel="Tree Structure"),
    gitignore: bool = typer.Option(True, "--gitignore/--no-gitignore", help="Respect .gitignore files.", rich_help_panel="Tree Structure"),
    hidden: bool = typer.Option(False, "--hidden", help="Show hidden files and directories.", rich_help_panel="Tree Structure"),
    
    sort_by: str = typer.Option("name", "--sort", help="Sort by 'name' or 'size'.", rich_help_panel="Sorting"),
    sort_order: str = typer.Option("asc", "--order", help="Sort order: 'asc' or 'desc'.", rich_help_panel="Sorting"),
    
    output_format: str = typer.Option("tree", "--format", help="Output format: 'tree' or 'md'.", rich_help_panel="Output and Display"),
    show_size: bool = typer.Option(False, "--size", help="Show file/directory sizes.", rich_help_panel="Output and Display"),
    show_counts: bool = typer.Option(False, "--count", help="Show file/directory counts in folders.", rich_help_panel="Output and Display"),
    no_icons: bool = typer.Option(False, "--no-icons", help="Disable icons in the output.", rich_help_panel="Output and Display"),
    theme: str = typer.Option("colorful", "--theme", help="Color theme: colorful, monokai, light, nocolor.", rich_help_panel="Output and Display"),

    include: Optional[List[str]] = typer.Option(None, "-i", "--include", help="Include only paths matching this glob pattern.", rich_help_panel="Filtering"),
    exclude: Optional[List[str]] = typer.Option(None, "-e", "--exclude", help="Exclude paths matching this glob pattern.", rich_help_panel="Filtering"),
    mtime_after: Optional[str] = typer.Option(None, "--mtime-after", help="Filter by modification time after this date (YYYY-MM-DD).", rich_help_panel="Filtering"),
    mtime_before: Optional[str] = typer.Option(None, "--mtime-before", help="Filter by modification time before this date (YYYY-MM-DD).", rich_help_panel="Filtering"),
    ctime_after: Optional[str] = typer.Option(None, "--ctime-after", help="Filter by creation time after this date (YYYY-MM-DD).", rich_help_panel="Filtering"),
    ctime_before: Optional[str] = typer.Option(None, "--ctime-before", help="Filter by creation time before this date (YYYY-MM-DD).", rich_help_panel="Filtering"),
    
    version: Optional[bool] = typer.Option(None, "--version", callback=lambda v: version_callback(v), is_eager=True, help="Show version and exit.", rich_help_panel="General"),
    about: Optional[bool] = typer.Option(None, "--about", callback=lambda v: about_callback(v), is_eager=True, help="Show information about the package.", rich_help_panel="General"),
):
    """
    Displays a styled file/folder tree of any directory.
    This command runs by default if no subcommand (like 'note') is provided.
    
    **Examples:**
    - `show-file-tree . --max-depth 2 --size`
    - `show-file-tree . -i "*.py" -e "*_test.py"`
    """
    if ctx.invoked_subcommand is not None:
        return # Do not run this code if a subcommand was called

    opts = DisplayOptions(
        root_path=root_path,
        max_depth=max_depth,
        use_gitignore=gitignore,
        show_hidden=hidden,
        sort_by=sort_by,
        sort_order=sort_order,
        output_format=output_format,
        show_size=show_size,
        show_counts=show_counts,
        no_icons=no_icons,
        theme=theme,
        include=include,
        exclude=exclude,
        mtime_after=mtime_after,
        mtime_before=mtime_before,
        ctime_after=ctime_after,
        ctime_before=ctime_before,
    )

    tree_data = build_tree(opts)

    if not tree_data:
        console.print(f"[red]Could not build tree for '{root_path}'.[/red]")
        raise typer.Exit(code=1)

    if opts.output_format == "md":
        md_path = export_to_markdown(tree_data, opts)
        console.print(f"[green]Markdown tree exported to:[/] [bold]{md_path}[/bold]")
    else:
        render_tree(tree_data, opts)

if __name__ == "__main__":
    app()