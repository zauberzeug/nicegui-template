import subprocess
from pathlib import Path
from subprocess import CompletedProcess
from typing import cast

import pytest
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


def test_basic_template(copie: Copie, answers: dict[str, str | list[str]]):
    # ARRANGE & ACT
    result = copie.copy(extra_answers=answers)
    # ASSERT
    assert result.exit_code == 0
    assert result.exception is None
    assert result.project_dir is not None
    assert result.project_dir.is_dir()
    assert contains_standard_files(result, cast(str, answers['project_name']))


def test_template_with_precommit(copie: Copie, answers: dict[str, str | list[str]]):
    # ARRANGE & ACT
    result = copie.copy(extra_answers={**answers, 'use_precommit': True})
    # ASSERT
    assert result.exit_code == 0
    assert result.exception is None
    assert result.project_dir is not None
    assert result.project_dir.is_dir()
    assert contains_standard_files(result, cast(str, answers['project_name']))
    assert (result.project_dir / '.pre-commit-config.yaml').is_file()


def test_template_with_rosys(copie: Copie, answers: dict[str, str | list[str]]):
    # ARRANGE & ACT
    result = copie.copy(extra_answers={**answers, 'use_rosys': True})
    # ASSERT
    assert result.exit_code == 0
    assert result.exception is None
    assert result.project_dir is not None
    assert result.project_dir.is_dir()
    assert contains_standard_files(result, cast(str, answers['project_name']))
    assert (result.project_dir / cast(str, answers['module_name']) / 'system.py').is_file()


def test_poetry_lock(copie: Copie, answers: dict[str, str | list[str]]):
    # ARRANGE & ACT
    result = copie.copy(extra_answers={**answers, 'use_poetry': True})
    # ASSERT
    assert result.exit_code == 0
    assert result.exception is None
    assert result.project_dir is not None
    assert result.project_dir.is_dir()
    poetry_lock = subprocess.run(['poetry', 'lock'], cwd=result.project_dir, check=False)
    assert poetry_lock.returncode == 0


@pytest.mark.parametrize('use_poetry', ['Poetry', ''])
@pytest.mark.parametrize('use_rosys', ['RoSys', ''])
@pytest.mark.parametrize('use_precommit', ['pre-commit', ''])
@pytest.mark.parametrize('task', ['mypy', 'pylint', 'ruff', 'pytest', 'pre-commit'])
def test_code_checkers(copie: Copie,
                       answers: dict[str, str | list[str]],
                       use_poetry: str,
                       use_rosys: str,
                       use_precommit: str,
                       task: str):
    # ARRANGE
    result = copie.copy(extra_answers={**answers,
                                       'use_poetry': bool(use_poetry),
                                       'use_rosys': bool(use_rosys),
                                       'use_precommit': bool(use_precommit)})
    arguments = [task]
    if task == 'mypy':
        arguments.append('.')
    elif task == 'pylint':
        arguments.append(f'./{result.answers["module_name"]}')
    elif task == 'ruff':
        arguments.extend(['check', '.'])
    elif task == 'pre-commit':
        arguments.extend(['run', '--all-files'])
    # ACT
    test_run: CompletedProcess = subprocess.run(arguments, cwd=result.project_dir, check=False)
    # ASSERT
    assert test_run.returncode == 0
