#!/bin/bash

set -e

THIS_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"

# install core and development Python dependencies into the currently activated venv
function install {
    python -m pip install --upgrade pip
    python -m pip install --editable "$THIS_DIR/[dev]"
}

# run linting, formatting, and other static code quality tools
function lint {
    pre-commit run --all-files
}

# same as `lint` but with any special considerations for CI
function lint:ci {
    # We skip no-commit-to-branch since that blocks commits to `main`.
    # All merged PRs are commits to `main` so this must be disabled.
    SKIP=no-commit-to-branch pre-commit run --all-files
}

# execute tests against the installed package; assumes the wheel is already installed
function test:ci {
    INSTALLED_PKG_DIR="$(python -c 'import {{cookiecutter.package_name}}; print({{cookiecutter.package_name}}.__path__[0])')"
    # in CI, we must calculate the coverage for the installed package, not the src/ folder
    COVERAGE_DIR="$INSTALLED_PKG_DIR" test
}

# (example) ./run.sh test tests/test_states_info.py::test__slow_add
function test {
    PYTEST_EXIT_STATUS=0
    python -m pytest ${@:-"$THIS_DIR/tests/"} \
        --cov "${COVERAGE_DIR:-$THIS_DIR/src}" \
        --cov-report json \
        --cov-fail-under 60 || ((PYTEST_EXIT_STATUS+=$?))
    return $PYTEST_EXIT_STATUS
}

function test:wheel-locally {
    deactivate || true
    rm -rf test-venv || true
    python -m venv test-venv
    source test-venv/bin/activate
    clean || true
    pip install build
    build
    pip install ./dist/*.whl pytest pytest-cov
    test:ci
    deactivate || true
}

# build a wheel and sdist from the Python source code
function build {
    python -m build --sdist --wheel "$THIS_DIR/"
}

# remove all files generated by tests, builds, or operating this codebase
function clean {
    rm -rf dist build coverage.json
    find . \
      -type d \
      \( \
        -name "*cache*" \
        -o -name "*.dist-info" \
        -o -name "*.egg-info" \
      \) \
      -not -path "*env/*" \
      -exec rm -r {} + || true

    find . \
      -type f \
      -name "*.pyc" \
      -not -path "*env/*" \
      -exec rm {} +
}

TIMEFORMAT="Task completed in %3lR"
time ${@:-help}
