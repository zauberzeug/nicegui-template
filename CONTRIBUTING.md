# Contributing to the NiceGUI template

We're thrilled that you're interested in contributing to the NiceGUI template!
Here are some guidelines that will help you get started.

## Reporting issues

If you encounter a bug or other issue with the NiceGUI template, the best way to report it is by opening a new issue on our [GitHub repository](https://github.com/zauberzeug/nicegui-template).
When creating the issue, please provide a clear and concise description of the problem, including any relevant error messages and code snippets.
If possible, include steps to reproduce the issue.

## Code of Conduct

We follow a [Code of Conduct](https://github.com/zauberzeug/nicegui-template/blob/main/CODE_OF_CONDUCT.md) to ensure that everyone who participates in the community feels welcome and safe.
By participating, you agree to abide by its terms.

## Contributing code

We are excited that you want to contribute code to the NiceGUI template.
We're always looking for bug fixes, performance improvements, and new features.

## About This Project

### This is a Copier Template Project

- Main output: Projects generated from `template/` directory
- Users run `copier copy` to generate new projects
- Template files use Jinja2 syntax (`{{variable}}`, `{% if %}`, etc.)
- Configuration in `copier.yml` defines questions and options

### Key Areas

- **`template/`** - Template files that get copied/rendered for new projects
  - Use Jinja2 templating syntax
  - Filenames can be conditional: `{% if condition %}filename{% endif %}.jinja`
  - Keep templates generic and universally applicable
- **`tests/`** - Template generation tests using pytest-copie
  - Test all combinations of options
  - Verify generated files exist and contain expected content
- **`copier.yml`** - Question definitions and template configuration
  - Questions should be clear and have good defaults
  - Use `when` for conditional questions
  - Update README.md table when adding questions

### Template-Specific Guidelines

**What to Avoid:**

- **Project-specific details in templates** - Keep templates generic and universal
- **Breaking existing generated projects** - Template changes affect all users
- **Missing tests** - Every template option combination should be tested
- **Undocumented questions** - All copier.yml questions must be in README.md table
- **Complex Jinja2 logic** - Keep template logic simple and readable
- **Duplicate content** - Use Jinja2 includes/variables to avoid repetition in templates

**Jinja2 Templating:**

- Use `{{ variable }}` for substitution
- Use `{% if condition %}...{% endif %}` for conditional content
- Use `{%- ... -%}` to control whitespace (remove newlines)
- Keep logic simple - complex logic belongs in copier.yml

**File Naming:**

- Conditional files: `{% if use_feature %}filename{% endif %}.jinja`
- Generated filename: `{{ variable }}.py.jinja`
- Remove `.jinja` extension in generated output

**Testing:**

- Test with different option combinations
- Verify file existence and content
- Test that generated projects work (can install, run, lint)

**Before Submitting:**

1. Tests written and passing?
2. README.md table updated if copier.yml changed?
3. Template syntax valid (no Jinja2 errors)?
4. Generated projects work correctly?
5. Code follows style guidelines?

### Review Criteria for Template Changes

When reviewing PRs, pay special attention to:

**BLOCKER Issues (must fix):**

- **Template syntax errors**: Invalid Jinja2 syntax, undefined variables, broken conditionals
- **Breaking changes**: Changes that break existing generated projects without migration path
- **Missing tests**: New template options without corresponding tests; untested file combinations
- **Documentation gaps**: New copier.yml questions not added to README.md table
- **Security**: Exposed secrets/credentials in templates or tests

**MAJOR Issues (should fix):**

- **Template quality**: Complex/hard-to-understand Jinja2 logic; should be simplified
- **Scope creep**: Project-specific details in templates (should stay generic/universal)
- **File placement**: Unexpected template file location without rationale
- **Test coverage**: Edge cases untested (various option combinations, conditional file generation)
- **Unnecessary complexity**: Simpler template design meets requirements
- **Duplicate content**: Repeated Jinja2 blocks that should use variables or includes

**CLEANUP Suggestions:**

- **Readability**: Complex template logic without comments; unclear variable names
- **Whitespace handling**: Missing `{%- -%}` in Jinja2 where whitespace control needed
- **Consistency**: Inconsistent template patterns across similar files

**Template-Specific Checks:**

- Can the generated project be installed and run?
- Is Jinja2 syntax valid with proper variable substitution?
- Do conditional filenames work correctly?
- Are all combinations of copier.yml options tested?
- Is README.md updated with new questions?

## Setup

### Locally

To set up a local development environment for the NiceGUI template, you'll need to have Python 3.11+ and pip installed.

First create a virtual environment with the dependencies to run tests and linting tools inside the project root and activate it:

```bash
virtualenv .venv

source .venv/bin/activate
```

Then install the requirements with `pip install -r requirements-locked.txt` and you're good to go!

If you would like to manually test your changes, use this command to make a copy with copier:

```bash
copier copy {PATH_TO_YOUR_FOLDER}/nicegui-template ./example --vcs-ref=HEAD
```

The same command can be used to update your project while developing.

## Coding Style Guide

### Formatting

We use [autopep8](https://github.com/hhatto/autopep8) with a 120 character line length to format our code.
Before submitting a pull request, please run

```bash
autopep8 --max-line-length=120 --in-place --recursive .
```

on your code to ensure that it meets our formatting guidelines.
Alternatively you can use VSCode, open the nicegui-template.code-workspace and install the recommended extensions.
Then the formatting rules are applied whenever you save a file.

In our point of view, the Black formatter is sometimes a bit too strict.
There are cases where one or the other arrangement of, e.g., function arguments is more readable than the other.
Then we like the flexibility to either put all arguments on separate lines or only put the lengthy event handler
on a second line and leave the other arguments as they are.

### Style Principles

- Always prefer simple solutions
- Avoid having files over 200-300 lines of code. Refactor at that point
- Naming conventions:
  - Python files: lowercase with underscores (e.g., `demo_class.py`)
  - Python classes: CamelCase (e.g., `DemoClass`)
- Use single quotes for strings in Python, double quotes in JavaScript
- Use f-strings wherever possible for better readability (except in performance-critical sections which should be marked with "NOTE:" comments)
- Follow autopep8 formatting with 120 character line length
- Each sentence in documentation should be on a new line
- Use ruff for linting and code checks

### Workflow Guidelines

- Always simplify the implementation as much as possible:
  - Avoid duplication of code whenever possible, which means checking for other areas of the codebase that might already have similar code and functionality
  - Remove obsolete code
  - Ensure the code is not too complicated
  - Strive to have minimal maintenance burden and self explanatory code without the need of additional comments
- Be careful to only make changes that are requested or are well understood and related to the change being requested
- When fixing an issue or bug, do not introduce a new pattern or technology without first exhausting all options for the existing implementation. And if you finally do this, make sure to remove the old implementation afterwards so we don't have duplicate logic
- Keep the codebase very clean and organized
- Write tests for new features
- Run tests before submitting any changes
- Format code using autopep8 before submitting changes
- Use pre-commit hooks to ensure coding style compliance
- When adding new features, include corresponding tests
- For documentation, ensure each sentence is on a new line

## Running tests

Our tests are built with pytest and require python-copie.

Before submitting a pull request, please make sure that all tests are passing.
To run them all, use the following command in the root directory of the NiceGUI template:

```bash
pytest
```

## Documentation

Please add new copier questions to the table in the README.md and explain the available options.

Your contributions are much appreciated.

## Pull requests

To get started, fork the repository on GitHub, clone it somewhere on your filesystem, commit and push your changes,
and then open a pull request (PR) with a detailed description of the changes you've made
(the PR button is shown on the GitHub website of your forked repository).

When submitting a PR, please make sure that the code follows the existing coding style and that all tests are passing.
If you're adding a new feature, please include tests that cover the new functionality.

## AI-Assisted Contributions

We welcome and encourage the use of AI coding assistants (like GitHub Copilot, Cursor, etc.)!

### For Contributors Using AI Tools

This project includes AI instruction files to help assistants understand our template development workflow:

- **[AGENTS.md](AGENTS.md)** - AI-specific guidelines for template development
- **[.github/copilot-instructions.md](.github/copilot-instructions.md)** - Review instructions for GitHub Copilot
- **[.cursor/rules](.cursor/rules)** - Quick reference for Cursor AI
- **[.cursor/commands/\*.md](.cursor/commands/)** - Custom Cursor commands

When using AI assistants:

- See this file for specific guidelines -- the other files mentioned above are just symlinks to the template files
- Always review and understand AI-generated code before committing -- you must take full responsibility for the code you commit
- Ensure the code follows our style guidelines and principles
- Test template generation with various option combinations
- Don't blindly accept suggestions - think critically about the solutions

**Before submitting a PR**, review your changes with an AI assistant:

In **Cursor** or **VS Code with GitHub Copilot Chat**:

Select Agent Mode with claude-sonnet-4 and write:

```
Review my current branch according to @.github/copilot-instructions.md
```

Or in **Cursor**, use these custom commands:

1. Type `/` in Cursor chat
2. Select commands:
   - `/review-uncommitted` - Review your local uncommitted changes
   - `/review-branch` - Review your current branch vs main
   - `/simplify` - Suggest ways to simplify code or templates
   - `/explain` - Explain what code or templates do

### For Projects Created with This Template

Projects created with this template can optionally include similar AI instruction files to help contributors and AI assistants understand the generated project better.

## Thank you!

Thank you for your interest in contributing to the NiceGUI template!
We're looking forward to working with you!
