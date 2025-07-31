import subprocess
from subprocess import CompletedProcess

from pytest_copie.plugin import Result


def perform_ruff_run(result: Result):
    ruff_result: CompletedProcess = subprocess.run(['ruff', 'check', '.'], cwd=result.project_dir, check=False)
    return ruff_result.returncode == 0


def test_standard_ruff_check_runs(standard_result: Result):
    assert perform_ruff_run(standard_result)


def test_use_poetry_ruff_check_runs(use_poetry_result: Result):
    assert perform_ruff_run(use_poetry_result)


def test_use_rosys_ruff_check_runs(use_rosys_result: Result):
    assert perform_ruff_run(use_rosys_result)


def test_use_precommit_ruff_check_runs(use_precommit_result: Result):
    assert perform_ruff_run(use_precommit_result)


def test_use_all_features_ruff_check_runs(use_all_features_result: Result):
    assert perform_ruff_run(use_all_features_result)
