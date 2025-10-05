# AI Agent Guidelines for nicegui-template

> **For**: AI assistants (Cursor, GitHub Copilot, etc.) working on nicegui-template
> **About**: The project purpose and setup is described in [README.md](README.md) > **Standards**: All coding standards are in [CONTRIBUTING.md](CONTRIBUTING.md) – follow those rules
> **Review**: For PR reviews, see [.github/copilot-instructions.md](.github/copilot-instructions.md)

## Core Principles

### Think from First Principles

Don't settle for the first solution.
Question assumptions and think deeply about the true nature of the problem before implementing.

### Discuss Before Implementing

For significant changes:

- Present the problem and possible approaches
- Discuss trade-offs and implications
- Get confirmation before proceeding with large refactorings
- Work iteratively with feedback at each step

### Simplicity First

- Prefer simple, straightforward solutions
- Avoid over-engineering
- Remove obsolete code rather than working around it
- Code should be self-explanatory

## Project-Specific Context

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

## What to Avoid

- **Project-specific details in templates** - Keep templates generic and universal
- **Breaking existing generated projects** - Template changes affect all users
- **Missing tests** - Every template option combination should be tested
- **Undocumented questions** - All copier.yml questions must be in README.md table
- **Complex Jinja2 logic** - Keep template logic simple and readable
- **Duplicate content** - Use Jinja2 includes/variables to avoid repetition in templates

## Template Best Practices

### Jinja2 Templating

- Use `{{ variable }}` for substitution
- Use `{% if condition %}...{% endif %}` for conditional content
- Use `{%- ... -%}` to control whitespace (remove newlines)
- Keep logic simple - complex logic belongs in copier.yml

### File Naming

- Conditional files: `{% if use_feature %}filename{% endif %}.jinja`
- Generated filename: `{{ variable }}.py.jinja`
- Remove `.jinja` extension in generated output

### Testing

- Test with different option combinations
- Verify file existence and content
- Test that generated projects work (can install, run, lint)

## Quick Verification

Before claiming a task complete, verify:

1. Tests written and passing?
2. README.md table updated if copier.yml changed?
3. Template syntax valid (no Jinja2 errors)?
4. Generated projects work correctly?
5. Code follows style guidelines?

## When Uncertain

- **Check copier docs** at https://copier.readthedocs.io/
- **Look at similar templates** for patterns and conventions
- **Test generation** with various option combinations
- **Ask the user** by presenting options and trade-offs if strategy is unclear

---

> This file complements [CONTRIBUTING.md](CONTRIBUTING.md).
> For detailed workflow, testing, and contribution process, see CONTRIBUTING.md.
