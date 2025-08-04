import subprocess
from subprocess import CompletedProcess

import pytest
from pytest_copie.plugin import Result

from helpers import ResultCombinations


def perform_run(result: Result, arguments: list[str]) -> None:
    run_result: CompletedProcess = subprocess.run(arguments, cwd=result.project_dir, check=False)
    assert run_result.returncode == 0


# ---------------------------------------- MYPY ----------------------------------------
@pytest.mark.parametrize('result', [*ResultCombinations.__members__.values()], indirect=True)
def test_mypy_check_runs(result: Result):
    perform_run(result, ['mypy', '.'])


# ---------------------------------------- PYLINT --------------------------------------
@pytest.mark.parametrize('result', [*ResultCombinations.__members__.values()], indirect=True)
def test_pylint_check_runs(result: Result):
    perform_run(result, ['pylint', f'./{result.answers["module_name"]}'])


# ---------------------------------------- RUFF ----------------------------------------
@pytest.mark.parametrize('result', [*ResultCombinations.__members__.values()], indirect=True)
def test_ruff_check_runs(result: Result):
    perform_run(result, ['ruff', 'check', '.'])


# ---------------------------------------- PYTEST --------------------------------------
@pytest.mark.parametrize('result', [*ResultCombinations.__members__.values()], indirect=True)
def test_pytest_check_runs(result: Result):
    perform_run(result, ['pytest'])
