import subprocess
from subprocess import CompletedProcess

from pytest_copie.plugin import Result


def perform_pylint_run(result: Result):
    pylint_result: CompletedProcess = subprocess.run(['pylint', f'./{result.answers["module_name"]}'],
                                                     cwd=result.project_dir, check=False)
    return pylint_result.returncode == 0


def test_standard_pylint_check_runs(standard_result: Result):
    assert perform_pylint_run(standard_result)


def test_use_poetry_pylint_check_runs(use_poetry_result: Result):
    assert perform_pylint_run(use_poetry_result)


def test_use_rosys_pylint_check_runs(use_rosys_result: Result):
    assert perform_pylint_run(use_rosys_result)


def test_use_precommit_pylint_check_runs(use_precommit_result: Result):
    assert perform_pylint_run(use_precommit_result)


def test_use_all_features_pylint_check_runs(use_all_features_result: Result):
    assert perform_pylint_run(use_all_features_result)
