"""
Package metadata.
"""

AUTHOR = "Rudra Prasad Bhuyan"
EMAIL = "rudra.pbhuyan@example.com" # Placeholder email
PACKAGE_NAME = "show-file-tree"
VERSION = __import__("showfilestree").__version__
DESCRIPTION = "A small, fast CLI tool to display styled file/folder trees with rich options."

def get_about_text():
    """Returns the text for the --about option."""
    return f"""
[bold #5e17eb]{PACKAGE_NAME} v{VERSION}[/bold #5e17eb]
{DESCRIPTION}

[bold]Author[/bold]: {AUTHOR}
[bold]License[/bold]: MIT
"""
