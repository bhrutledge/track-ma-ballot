# Track Massachusetts Ballot

Print ballot details from [Track My Ballot](https://www.sec.state.ma.us/wheredoivotema/track/trackmyballot.aspx).

## Installing

- [Fork and clone](https://help.github.com/en/articles/fork-a-repo) this repository

- Create and activate a [virtual environment](https://docs.python.org/3/tutorial/venv.html)

- Install the package and its dependencies:

    ```
    $ python -m pip install -e .

    $ python -m playwright install
    ```

- Copy `.env.sample` to `.env`, and fill in your name and address

## Usage

```
$ python -m track_ma_ballot
election   11/3/2020 State Election
mailed     First: 10/13/2020
received   Not returned
status     Not returned
```

Run this daily until status changes. 😉

## Developing

Set up your development environment:

- Install the packages required for development:

    ```
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
