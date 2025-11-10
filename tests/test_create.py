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


def test_template_with_contributing_only(copie: Copie, answers: dict[str, str | list[str]]):
    # ARRANGE & ACT
    result = copie.copy(extra_answers={**answers, 'include_ai_instructions': False})
    # ASSERT
    assert result.exit_code == 0
    assert result.exception is None
    assert result.project_dir is not None
    assert result.project_dir.is_dir()
    assert contains_standard_files(result, cast(str, answers['project_name']))
    assert (result.project_dir / 'CONTRIBUTING.md').is_file()
    assert not (result.project_dir / 'AGENTS.md').exists()
    assert not (result.project_dir / '.github' / 'copilot-instructions.md').exists()
    assert not (result.project_dir / '.cursor' / 'rules' / 'general.mdc').exists()
    # Verify that CONTRIBUTING.md does NOT contain AI section when AI instructions are disabled
    contributing_content = (result.project_dir / 'CONTRIBUTING.md').read_text()
    assert 'AI-Assisted Contributions' not in contributing_content


def test_template_with_ai_instructions(copie: Copie, answers: dict[str, str | list[str]]):
    # ARRANGE & ACT
    # When AI instructions are enabled, CONTRIBUTING.md is automatically included
    result = copie.copy(extra_answers={**answers, 'include_ai_instructions': True})
    # ASSERT
    assert result.exit_code == 0
    assert result.exception is None
    assert result.project_dir is not None
    assert result.project_dir.is_dir()
    assert contains_standard_files(result, cast(str, answers['project_name']))
    # CONTRIBUTING.md is mandatory when AI instructions are enabled
    assert (result.project_dir / 'CONTRIBUTING.md').is_file()
    assert (result.project_dir / 'AGENTS.md').is_file()
    assert (result.project_dir / '.github' / 'copilot-instructions.md').is_file()
    assert (result.project_dir / '.cursor' / 'rules' / 'general.mdc').is_file()
    assert (result.project_dir / '.cursor' / 'commands' / 'review-uncommitted.md').is_file()
    assert (result.project_dir / '.cursor' / 'commands' / 'review-branch.md').is_file()
    assert (result.project_dir / '.cursor' / 'commands' / 'simplify.md').is_file()
    assert (result.project_dir / '.cursor' / 'commands' / 'explain.md').is_file()
    assert (result.project_dir / '.cursor' / 'commands' / 'summarize-branch.md').is_file()
    # Verify that CONTRIBUTING.md contains AI section when AI instructions are enabled
    contributing_content = (result.project_dir / 'CONTRIBUTING.md').read_text()
    assert 'AI-Assisted Contributions' in contributing_content
    assert 'AGENTS.md' in contributing_content


def test_template_without_contributing_and_ai(copie: Copie, answers: dict[str, str | list[str]]):
    # ARRANGE & ACT
    result = copie.copy(extra_answers={**answers, 'include_contributing': False, 'include_ai_instructions': False})
    # ASSERT
    assert result.exit_code == 0
    assert result.exception is None
    assert result.project_dir is not None
    assert result.project_dir.is_dir()
    assert contains_standard_files(result, cast(str, answers['project_name']))
    assert not (result.project_dir / 'CONTRIBUTING.md').exists()
    assert not (result.project_dir / 'AGENTS.md').exists()
    assert not (result.project_dir / '.github' / 'copilot-instructions.md').exists()
    assert not (result.project_dir / '.cursor' / 'rules' / 'general.mdc').exists()
    assert not (result.project_dir / '.cursor' / 'commands').exists()


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


@pytest.mark.parametrize('package_management', ['poetry', 'uv', 'pip'])
@pytest.mark.parametrize('use_rosys', ['RoSys', ''])
@pytest.mark.parametrize('use_precommit', ['pre-commit', ''])
@pytest.mark.parametrize('task', ['mypy', 'pylint', 'ruff', 'pytest'])
def test_code_checkers(copie: Copie,
                       answers: dict[str, str | list[str]],
                       package_management: str,
                       use_rosys: str,
                       use_precommit: str,
                       task: str):
    # ARRANGE
    result = copie.copy(extra_answers={**answers,
                                       'package_management': package_management,
                                       'use_rosys': bool(use_rosys),
                                       'use_precommit': bool(use_precommit)})
    arguments = [task] if task == 'pytest' else ['make', task]
    # ACT
    test_run: CompletedProcess = subprocess.run(arguments, cwd=result.project_dir, check=False)
    # ASSERT
    assert test_run.returncode == 0
