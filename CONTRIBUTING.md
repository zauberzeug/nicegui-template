# Contributing to the NiceGUI template

We're thrilled that you're interested in contributing to the NiceGUI template!
Here are some guidelines that will help you get started.

## Reporting issues

If you encounter a bug or other issue with the NiceGUI template, the best way to report it is by opening a new issue on our [GitHub repository](https://github.com/zauberzeug/nicegui-template).
When creating the issue, please provide a clear and concise description of the problem, including any relevant error messages and code snippets.
If possible, include steps to reproduce the issue.

## Code of Conduct

We follow a [Code of Conduct](https://github.com/zauberzeug/nicegui-template/blob/main/CODE_OF_CONDUCT.md) to ensure that everyone who participates in the NiceGUI community feels welcome and safe.
By participating, you agree to abide by its terms.

## Contributing code

We are excited that you want to contribute code to the NiceGUI template.
We're always looking for bug fixes, performance improvements, and new features.

## Setup

### Locally

To set up a local development environment for the NiceGUI template, you'll need to have Python 3.11+ and pip installed.

First create a virtual environment with the dependencies to run tests and linting tools inside the project root and activate it:

```bash
virtualenv .venv

source .venv/bin/activate
```

Then install the requirements with `pip install -r requirements.txt` and you're good to go!

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

## YouTube

We welcome and support video and tutorial contributions to the NiceGUI community!
As recently [highlighted in a conversation on YouTube](https://www.youtube.com/watch?v=HiNNe4Q32U4&lc=UgyRcZCOZ9i5z6GuDcJ4AaABAg),
creating and sharing tutorials or showcasing projects using NiceGUI can be an excellent way to help others learn and grow,
while also spreading the word about our library.

Please note that NiceGUI is pronounced like "nice guy," which might be helpful to know when creating any video content.

If you decide to create YouTube content around NiceGUI,
we kindly ask that you credit our repository, our YouTube channel, and any relevant videos or resources within the description.
By doing so, you'll be contributing to the growth of our community and helping us receive more amazing pull requests and feature suggestions.

We're thrilled to see your creations and look forward to watching your videos. Happy video-making!

## Thank you!

Thank you for your interest in contributing to the NiceGUI template!
We're looking forward to working with you!
