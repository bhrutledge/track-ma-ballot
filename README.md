# Track Massachusetts Ballot

TODO: Description

## Installing

TODO

## Usage

TODO

## Developing

Set up your development environment:

- [Fork and clone](https://help.github.com/en/articles/fork-a-repo) this repository

- Create and activate a [virtual environment](https://docs.python.org/3/tutorial/venv.html)

- Install the packages required for development:

    ```
    $ python -m pip install -U setuptools pip wheel

    $ python -m pip install -e .[dev]
    ```

    This will install:

    - [pytest](https://docs.pytest.org/en/latest/) to write and run tests
    - [black](https://black.readthedocs.io/en/stable/) and [isort](https://pycqa.github.io/isort/) to format the code
    - [flake8](http://flake8.pycqa.org/en/latest/) to check code style
    - [mypy](https://mypy.readthedocs.io/en/latest/) to check types
    - [invoke](https://www.pyinvoke.org/) to simplify running these tools

Run the tests:

```
$ pytest
```

Format the code and run the checks:

```
$ invoke format

$ invoke check
```
