import subprocess
from subprocess import CompletedProcess

from pytest_copie.plugin import Copie, Result

answers = {
    'project_name': 'helloworld',
    'project_description': '',
    'module_name': 'hello',
    'python_versions': ['3.9', '3.10', '3.11']
}


def contains_standard_files(result: Result):
    files = [
        '.copier-answers.yml',
        '.gitignore',
        'README.md',
        'pyproject.toml',
    ]
    all_found = True
    for file in files:
        if not (result.project_dir / file).is_file():
            all_found = False
            print('Standard file was not found in generated project:', file)
    return all_found


def test_basic_template(copie: Copie):
    result = copie.copy(extra_answers=answers)
    assert result.exit_code == 0
    assert result.exception is None
    assert result.project_dir.is_dir()
    assert contains_standard_files(result)


def perform_ruff_run(result: Result):
    ruff_result: CompletedProcess = subprocess.run(['ruff', 'check', result.project_dir],
                                                   cwd=result.project_dir, check=False)
    return ruff_result.returncode == 0


def test_ruff_runs(copie: Copie):
    result = copie.copy(extra_answers=answers)
    assert result.exit_code == 0
    assert perform_ruff_run(result)
