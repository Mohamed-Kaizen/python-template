"""Command-line interface."""
import typer

from . import __version__

app = typer.Typer(help="{{ cookiecutter.project_name }} CLI.")


@app.command()
def version() -> None:
    """Show project Version."""
    typer.echo(f"Novizi Version: {__version__}")


if __name__ == "__main__":
    app()
