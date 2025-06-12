import subprocess
from pathlib import Path
from subprocess import CompletedProcess
from typing import cast

from pytest_copie.plugin import Copie, Result


def contains_standard_files(result: Result, project_name: str):
    files = [
        '.copier-answers.yml',
        '.gitignore',
        'main.py',
        'README.md',
        'pyproject.toml',
        project_name + '.code-workspace',
    ]
    all_found = True
    for file in files:
        if not ((result.project_dir or Path('')) / file).is_file():
            all_found = False
            print('Standard file was not found in generated project:', file)
    return all_found


def perform_ruff_run(result: Result):
    ruff_result: CompletedProcess = subprocess.run(['ruff', 'check', '.'], cwd=result.project_dir, check=False)
    return ruff_result.returncode == 0


def perform_mypy_run(result: Result):
    mypy_result: CompletedProcess = subprocess.run(['mypy', '.', '--non-interactive'],
                                                   cwd=result.project_dir, check=False)
    return mypy_result.returncode == 0


def perform_pylint_run(result: Result):
    pylint_result: CompletedProcess = subprocess.run(['pylint', f'./{result.answers["module_name"]}'],
                                                     cwd=result.project_dir, check=False)
    return pylint_result.returncode == 0


def perform_pytest_run(result: Result):
    pytest_result: CompletedProcess = subprocess.run(['pytest'], cwd=result.project_dir, check=False)
    return pytest_result.returncode == 0


def test_basic_template(standard_result: Result, answers: dict[str, str | list[str]]):
    assert standard_result.exit_code == 0
    assert standard_result.exception is None
    assert standard_result.project_dir is not None
    assert standard_result.project_dir.is_dir()
    assert contains_standard_files(standard_result, cast(str, answers['project_name']))


def test_template_with_precommit(copie: Copie, answers: dict[str, str | list[str]]):
    result = copie.copy(extra_answers={**answers, 'use_precommit': True})
    assert result.exit_code == 0
    assert result.exception is None
    assert result.project_dir is not None
    assert result.project_dir.is_dir()
    assert contains_standard_files(result, cast(str, answers['project_name']))
    assert (result.project_dir / '.pre-commit-config.yaml').is_file()


def test_standard_ruff_check_runs(standard_result: Result):
    assert perform_ruff_run(standard_result)


def test_standard_mypy_check_runs(standard_result: Result):
    assert perform_mypy_run(standard_result)


def test_standard_pylint_check_runs(standard_result: Result):
    assert perform_pylint_run(standard_result)


def test_standard_pytest_check_runs(standard_result: Result):
    assert perform_pytest_run(standard_result)


def test_poetry_lock(copie: Copie, answers: dict[str, str | list[str]]):
    result = copie.copy(extra_answers={**answers, 'use_poetry': True})
    assert result.exit_code == 0
    assert result.exception is None
    assert result.project_dir is not None
    assert result.project_dir.is_dir()
    poetry_lock = subprocess.run(['poetry', 'lock'], cwd=result.project_dir, check=False)
    assert poetry_lock.returncode == 0
