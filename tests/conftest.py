import pytest
from pytest_copie.plugin import Copie, Result

from helpers import ResultCombinations


@pytest.fixture(name='answers')
def fixture_answers() -> dict[str, str | list[str]]:
    return {
        'project_name': 'helloworld',
        'project_description': '',
        'module_name': 'hello',
        'python_versions': ['3.9', '3.10', '3.11']
    }


@pytest.fixture
def standard_result(copie: Copie, answers: dict[str, str | list[str]]) -> Result:
    return copie.copy(extra_answers=answers)


@pytest.fixture
def use_poetry_result(copie: Copie, answers: dict[str, str | list[str]]) -> Result:
    return copie.copy(extra_answers={**answers, 'use_poetry': True})


@pytest.fixture
def use_rosys_result(copie: Copie, answers: dict[str, str | list[str]]) -> Result:
    return copie.copy(extra_answers={**answers, 'use_rosys': True})


@pytest.fixture
def use_precommit_result(copie: Copie, answers: dict[str, str | list[str]]) -> Result:
    return copie.copy(extra_answers={**answers, 'use_precommit': True})


@pytest.fixture
def use_poetry_and_rosys_result(copie: Copie, answers: dict[str, str | list[str]]) -> Result:
    return copie.copy(extra_answers={**answers, 'use_poetry': True, 'use_rosys': True})


@pytest.fixture
def use_poetry_and_precommit_result(copie: Copie, answers: dict[str, str | list[str]]) -> Result:
    return copie.copy(extra_answers={**answers, 'use_poetry': True, 'use_precommit': True})


@pytest.fixture
def use_rosys_and_precommit_result(copie: Copie, answers: dict[str, str | list[str]]) -> Result:
    return copie.copy(extra_answers={**answers, 'use_rosys': True, 'use_precommit': True})


@pytest.fixture
def use_all_features_result(copie: Copie, answers: dict[str, str | list[str]]) -> Result:
    return copie.copy(extra_answers={**answers, 'use_rosys': True, 'use_precommit': True})


@pytest.fixture
def result(request) -> Result:
    """Parametrized fixture that returns the named result variation."""
    variation: ResultCombinations = request.param
    return request.getfixturevalue(variation.value)
