"""Helper functions for the project_dir fixture."""

import json
import subprocess
from copy import deepcopy
from pathlib import Path
from typing import Dict

from tests.consts import PROJECT_DIR


def initialize_git_repo(repo_dir: Path):
    """
    Turn the cookiecutted temporary repo into a git repo.

    Args:
        repo_dir (Path): Path of the temporary repo.

    """
    subprocess.run(["git", "init"], cwd=repo_dir, check=True)
    subprocess.run(["git", "branch", "-M", "main"], cwd=repo_dir, check=True)
    subprocess.run(["git", "add", "--all"], cwd=repo_dir, check=True)
    subprocess.run(["git", "commit", "-m", "initial commit by pytest"], cwd=repo_dir, check=True)


def generate_project(template_values: Dict[str, str], test_session_id: str) -> Path:
    """
    Generate a temporary repo using the cookiecutter.

    Args:
        template_values (Dict[str, str]): Cookiecutter configuration.
        test_session_id (str): The test session ID.

    Returns:
        Path: Path of the generated temporary repo.

    """
    template_values: Dict[str, str] = deepcopy(template_values)
    cookiecutter_config = {"default_context": template_values}
    cookiecutter_config_fpath = PROJECT_DIR / f"cookiecutter-{test_session_id}.json"
    cookiecutter_config_fpath.write_text(json.dumps(cookiecutter_config))

    command = [
        "cookiecutter",
        str(PROJECT_DIR),
        "--output-dir",
        str(PROJECT_DIR / "sample"),
        "--no-input",
        "--config-file",
        str(cookiecutter_config_fpath),
    ]
    print(f"Command: {' '.join(command)}")

    subprocess.run(args=command, check=True)

    generated_repo_dir = PROJECT_DIR / "sample" / template_values["repo_name"]
    return generated_repo_dir
