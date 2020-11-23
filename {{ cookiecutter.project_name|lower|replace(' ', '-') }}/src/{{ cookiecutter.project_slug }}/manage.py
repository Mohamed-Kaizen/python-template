"""Command-line interface."""
import typer

from . import __version__

app = typer.Typer(help="{{ cookiecutter.project_name }} CLI.")


@app.command()
def version() -> None:
    """Show project Version."""
    project_name = "{{ cookiecutter.project_name }}"
    typer.secho(f"{project_name} Version: {__version__}", fg=typer.colors.BRIGHT_GREEN)


if __name__ == "__main__":
    app()
