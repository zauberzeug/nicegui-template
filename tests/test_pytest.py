import subprocess
from subprocess import CompletedProcess

from pytest_copie.plugin import Result


def perform_pytest_run(result: Result):
    pytest_result: CompletedProcess = subprocess.run(['pytest'], cwd=result.project_dir, check=False)
    return pytest_result.returncode == 0


def test_standard_pytest_check_runs(standard_result: Result):
    assert perform_pytest_run(standard_result)


def test_use_poetry_pytest_check_runs(use_poetry_result: Result):
    assert perform_pytest_run(use_poetry_result)


def test_use_rosys_pytest_check_runs(use_rosys_result: Result):
    assert perform_pytest_run(use_rosys_result)


def test_use_precommit_pytest_check_runs(use_precommit_result: Result):
    assert perform_pytest_run(use_precommit_result)


def test_use_all_features_pytest_check_runs(use_all_features_result: Result):
    assert perform_pytest_run(use_all_features_result)
