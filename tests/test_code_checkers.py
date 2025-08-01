import subprocess
from subprocess import CompletedProcess

import pytest
from pytest_copie.plugin import Result

from helpers import ResultCombinations


# ---------------------------------------- MYPY ----------------------------------------
def perform_mypy_run(result: Result):
    mypy_result: CompletedProcess = subprocess.run(['mypy', '.'], cwd=result.project_dir, check=False)
    return mypy_result.returncode == 0


@pytest.mark.parametrize('result', [
    *ResultCombinations.__members__.values()
], indirect=True)
def test_mypy_check_runs(result: Result):
    assert perform_mypy_run(result)


# ---------------------------------------- PYLINT --------------------------------------
def perform_pylint_run(result: Result):
    pylint_result: CompletedProcess = subprocess.run(['pylint', f'./{result.answers["module_name"]}'],
                                                     cwd=result.project_dir, check=False)
    return pylint_result.returncode == 0


@pytest.mark.parametrize('result', [
    *ResultCombinations.__members__.values()
], indirect=True)
def test_pylint_check_runs(result: Result):
    assert perform_pylint_run(result)


# ---------------------------------------- RUFF ----------------------------------------
def perform_ruff_run(result: Result):
    ruff_result: CompletedProcess = subprocess.run(['ruff', 'check', '.'], cwd=result.project_dir, check=False)
    return ruff_result.returncode == 0


@pytest.mark.parametrize('result', [
    *ResultCombinations.__members__.values()
], indirect=True)
def test_ruff_check_runs(result: Result):
    assert perform_ruff_run(result)


# ---------------------------------------- PYTEST --------------------------------------
def perform_pytest_run(result: Result):
    pytest_result: CompletedProcess = subprocess.run(['pytest'], cwd=result.project_dir, check=False)
    return pytest_result.returncode == 0


@pytest.mark.parametrize('result', [
    *ResultCombinations.__members__.values()
], indirect=True)
def test_pytest_check_runs(result: Result):
    assert perform_pytest_run(result)
