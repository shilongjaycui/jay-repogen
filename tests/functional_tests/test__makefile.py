"""Test that the temporary repo's makefile targets work."""

import subprocess
from pathlib import Path


def test__linting_passes(project_dir: Path):
    """
    Ensure that `make lint-ci` runs successfully.

    Args:
        project_dir (Path): Path of the temporary repo.

    """
    subprocess.run(["make", "lint-ci"], cwd=project_dir, check=True)


def test__tests_pass(project_dir: Path):
    """
    Ensure that `make test-wheel-locally` runs successfully.

    Args:
        project_dir (Path): Path of the temporary repo.

    """
    subprocess.run(["make", "install"], cwd=project_dir, check=True)
    subprocess.run(["make", "test-wheel-locally"], cwd=project_dir, check=True)
