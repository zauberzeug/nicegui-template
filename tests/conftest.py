import pytest


@pytest.fixture(name='answers')
def fixture_answers() -> dict[str, str | list[str]]:
    return {
        'project_name': 'helloworld',
        'project_description': '',
        'module_name': 'hello',
        'python_versions': ['3.9', '3.10', '3.11']
    }
