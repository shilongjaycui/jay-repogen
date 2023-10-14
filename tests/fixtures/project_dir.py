"""Fixture that uses the cookiecutter to generate a temporary repo."""

import shutil
import subprocess
from pathlib import Path
from uuid import uuid4

import pytest

from tests.consts import PROJECT_DIR
from tests.utils.project import (
    generate_project,
    initialize_git_repo,
)


@pytest.fixture(scope="session")
def project_dir() -> Path:
    """
    Fixture that uses the cookiecutter to generate a temporary repo.

    Returns:
        Path: Path of the generated temporary repo.

    Yields:
        Iterator[Path]: Path of the generated temporary repo.

    """
    test_session_id: str = generate_test_session_id()
    template_values = {
        "repo_name": f"test-repo-{test_session_id}",
        "package_name": f"test_package_{test_session_id}",
    }
    generated_repo_dir: Path = generate_project(
        template_values=template_values,
        test_session_id=test_session_id,
    )
    try:
        initialize_git_repo(repo_dir=generated_repo_dir)
        subprocess.run(["make", "lint-ci"], cwd=generated_repo_dir, check=False)
        yield generated_repo_dir
    finally:
        subprocess.run(
            ["rm", f"cookiecutter-{test_session_id}.json"],
            cwd=PROJECT_DIR,
            check=True,
        )
        shutil.rmtree(path=generated_repo_dir)


def generate_test_session_id() -> str:
    """
    Generate a unique ID for the test session.

    Returns:
        str: The unique test session ID.

    """
    test_session_id: str = str(uuid4())[:6]
    return test_session_id
