"""Command-line interface."""
import typer
from rich.console import Console

from . import __version__

app = typer.Typer(help="{{ cookiecutter.project_name }} CLI.")

console = Console()

@app.command()
def version() -> None:
    """Show project Version."""
    project_name = "{{ cookiecutter.project_name }}"
    console.print(f"{project_name} Version: {__version__}", style="bold green")


if __name__ == "__main__":
    app()
