# Package and Run Python Project

![GitHub](https://img.shields.io/github/license/rhbarbhaya/calculator?logo=python)
![GitHub Pipenv locked Python version](https://img.shields.io/github/pipenv/locked/python-version/rhbarbhaya/calculator?logo=python)
![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/rhbarbhaya/calculator?logo=python)
![GitHub repo size](https://img.shields.io/github/repo-size/rhbarbhaya/calculator)
![Lines of code](https://img.shields.io/tokei/lines/github/rhbarbhaya/calculator?logo=python)
![Pylint Test](https://img.shields.io/badge/pylint-10-brightgreen?logo=python)
![pytest](https://img.shields.io/badge/pytest-25%20passed,%201%20expected%20fail-green?logo=python)
![pytest-covereage](https://img.shields.io/badge/coverage-100%25-brightgreen?logo=python)
![tox tested](https://img.shields.io/badge/tox-check-brightgreen?logo=python)
![mypy test](https://img.shields.io/badge/mypy-check-brightgreen?logo=python)
![python version tested](https://img.shields.io/badge/versions-3.8%20%7C%203.9%20%7C%203.10%20%7C%203.11-brightgreen?logo=python)

This is a packing and running training for python package.

1. Store all the python code in a folder.
2. Test scripts should have their own folder. With `tox` setup as its own file
3. Include all the documentation files in their own folder.
4. Sample `pyproject.toml` file used for this project is attached.
5. Using `python -m build`, build the distribution package(s).
6. Running the `unzip.sh` file should run all the scripts as defined in the `deploy` folder.
