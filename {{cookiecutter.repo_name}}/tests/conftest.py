"""Path hacking as well as specifying fixture location(s)."""

import sys
from pathlib import Path

# path hacking
TESTS_DIR = Path(__file__).parent
TESTS_DIR_PARENT = (TESTS_DIR / "..").resolve()

sys.path.insert(0, str(TESTS_DIR_PARENT))

pytest_plugins = ["tests.fixtures.example_fixture"]
