"""Test cases for the manage module."""
from typer.testing import CliRunner

from {{ cookiecutter.project_slug }}.manage import app

runner = CliRunner()


def test_help_succeeds() -> None:
    """It exits with a status code of zero."""
    result = runner.invoke(app, ["--help"])
    assert result.exit_code == 0
    assert "version" in result.output


def test_version_succeeds() -> None:
    """It exits with a status code of zero."""
    result = runner.invoke(app)
    assert result.exit_code == 0
    assert "{{ cookiecutter.project_name }}" in result.stdout
