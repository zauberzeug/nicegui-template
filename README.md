# NiceGUI Project Template

## Prerequisites

`pipx` is used to install `copier` independent of your new project's dependencies:

1. install `pipx` according to the documentation [here](https://pipx.pypa.io/stable/).
2. install [`copier`](https://copier.readthedocs.io/en/stable/) with pipx: `pipx install copier`.


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