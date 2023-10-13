"""Test that the cookiecutter successfully generates a temporary repo."""

from pathlib import Path


def test__can_generate_project(project_dir: Path):
    """
    Test that the cookiecutter successfully generates a temporary repo.

    Args:
        project_dir (Path): Path of the temporary repo.

    """
    assert project_dir.exists()
