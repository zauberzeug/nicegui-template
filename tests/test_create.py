import subprocess
from pathlib import Path
from typing import cast

from pytest_copie.plugin import Result


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


def test_basic_template(standard_result: Result, answers: dict[str, str | list[str]]):
    assert standard_result.exit_code == 0
    assert standard_result.exception is None
    assert standard_result.project_dir is not None
    assert standard_result.project_dir.is_dir()
    assert contains_standard_files(standard_result, cast(str, answers['project_name']))


def test_template_with_precommit(use_precommit_result: Result, answers: dict[str, str | list[str]]):
    assert use_precommit_result.exit_code == 0
    assert use_precommit_result.exception is None
    assert use_precommit_result.project_dir is not None
    assert use_precommit_result.project_dir.is_dir()
    assert contains_standard_files(use_precommit_result, cast(str, answers['project_name']))
    assert (use_precommit_result.project_dir / '.pre-commit-config.yaml').is_file()


def test_template_with_rosys(use_rosys_result: Result, answers: dict[str, str | list[str]]):
    assert use_rosys_result.exit_code == 0
    assert use_rosys_result.exception is None
    assert use_rosys_result.project_dir is not None
    assert use_rosys_result.project_dir.is_dir()
    assert contains_standard_files(use_rosys_result, cast(str, answers['project_name']))
    assert (use_rosys_result.project_dir / cast(str, answers['module_name']) / 'system.py').is_file()


def test_poetry_lock(use_poetry_result: Result):
    assert use_poetry_result.exit_code == 0
    assert use_poetry_result.exception is None
    assert use_poetry_result.project_dir is not None
    assert use_poetry_result.project_dir.is_dir()
    poetry_lock = subprocess.run(['poetry', 'lock'], cwd=use_poetry_result.project_dir, check=False)
    assert poetry_lock.returncode == 0
