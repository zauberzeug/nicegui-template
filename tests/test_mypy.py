import subprocess
from subprocess import CompletedProcess

from pytest_copie.plugin import Result


def perform_mypy_run(result: Result):
    mypy_result: CompletedProcess = subprocess.run(['mypy', '.', '--non-interactive'],
                                                   cwd=result.project_dir, check=False)
    return mypy_result.returncode == 0


def test_standard_mypy_check_runs(standard_result: Result):
    assert perform_mypy_run(standard_result)


def test_use_poetry_mypy_check_runs(use_poetry_result: Result):
    assert perform_mypy_run(use_poetry_result)


def test_use_rosys_mypy_check_runs(use_rosys_result: Result):
    assert perform_mypy_run(use_rosys_result)


def test_use_precommit_mypy_check_runs(use_precommit_result: Result):
    assert perform_mypy_run(use_precommit_result)


def test_use_all_features_mypy_check_runs(use_all_features_result: Result):
    assert perform_mypy_run(use_all_features_result)
