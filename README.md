# NiceGUI Project Template

## Prerequisites

`pipx` is used to install `copier` independent of your new project's dependencies:

1. install `pipx` according to the documentation [here](https://pipx.pypa.io/stable/).
2. install [`copier`](https://copier.readthedocs.io/en/stable/) with pipx: `pipx install copier` (tested with `copier==9.7.1`).

## Quickstart

1. generate your project:

```bash
copier copy git@github.com:zauberzeug/nicegui-template.git path/to/project
```

2. explore your new project:

```bash
cd path/to/project
```

3. initialize a git repo:

```bash
git init
```

4. create a virtual environment:

```bash
virtualenv .venv # or without virtualenv:
python -m venv .venv

source .venv/bin/activate # to activate your virtual environment
```

5. install standard dependencies to start working:

```bash
poetry install --with dev # with poetry
pip install -r requirements-dev.txt # without poetry
```

6. start your project:

```bash
./main.py
```

## Available Questions / Options

| name                    | type    | options      | default                 | explanation                                                                                            |
| ----------------------- | ------- | ------------ | ----------------------- | ------------------------------------------------------------------------------------------------------ |
| project name            | str     |              | -                       | the project's name as stated in the pyproject.toml                                                     |
| module name             | str     |              | same as project name    | the name of the main module in the root directory of the project                                       |
| project description     | str     |              | -                       | used in the pyproject.toml                                                                             |
| use poetry              | boolean | true / false | false                   | use [Poetry](https://python-poetry.org/) to manage the project's dependencies and virtual environment  |
| python versions         | str     | 3.8 to 3.13  | [3.9, 3.10, 3.11, 3.12] | defines the required and supported python versions                                                     |
| use precommit           | boolean | true / false | false                   | use [pre-commit](https://pre-commit.com/) to check your changes before committing                      |
| use rosys               | boolean | true / false | false                   | add [RoSys](https://github.com/zauberzeug/rosys) framework to dependencies                             |
| include contributing    | boolean | true / false | true                    | include CONTRIBUTING.md with development guidelines (only asked if AI instructions disabled)           |
| include ai instructions | boolean | true / false | true                    | include AI agent instructions (AGENT.md, .github/copilot-instructions.md, .cursor/\*, CONTRIBUTING.md) |

## Contributing Guidelines

When `include_contributing` is enabled (default when AI instructions are disabled), a **`CONTRIBUTING.md`** file is generated with:

- Development setup instructions
- Coding style guidelines
- Workflow and testing guidelines
- Pull request checklist

## AI Instructions

When `include_ai_instructions` is enabled (default), the template generates files to help AI coding assistants (GitHub Copilot, Cursor, etc.) understand your project better:

- **`CONTRIBUTING.md`** - Development guidelines and coding standards (mandatory, serves as the detailed reference)
- **`AGENT.md`** - Focused AI agent guidelines with principles and AI-specific patterns
- **`.github/copilot-instructions.md`** - Brief GitHub Copilot instructions that reference the main files
- **`.cursor/rules`** - Brief Cursor AI quick reference
- **`.cursor/commands/*.md`** - Custom Cursor commands (review-code, check-style, suggest-tests, explain-code, simplify)

**Structure Philosophy**: Following the [NiceGUI approach](https://github.com/zauberzeug/nicegui/blob/main/AGENT.md), CONTRIBUTING.md contains the comprehensive coding standards and workflow, while AGENT.md focuses on AI-specific principles. Tool-specific files (.cursor/rules, .github/copilot-instructions.md) are kept brief and reference the main files.
