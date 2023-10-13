"""Example fixture."""

from uuid import uuid4

import pytest

from tests.consts import PROJECT_DIR


@pytest.fixture(scope="session")
def test_session_id() -> str:
    """
    Generate a unique ID for the test session.

    Returns:
        str: The generated test session ID.

    """
    test_session_id: str = str(PROJECT_DIR.name) + str(uuid4())[:6]
    return test_session_id
