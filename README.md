# Track Massachusetts Ballot

Print ballot details from [Track My Ballot](https://www.sec.state.ma.us/wheredoivotema/track/trackmyballot.aspx).

I wrote this partially as an excuse to play with web automation using [playwright-python](https://github.com/microsoft/playwright-python).

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

Run this daily until the status changes:

```
election   11/3/2020 State Election
mailed     First: 10/13/2020
received   10/19/2020
status     Accepted
```

## Automated status checks

This repo includes a [daily GitHub Action](.github/workflows/main.yml) that runs the [tests](tests/test_ballot_status.py), which will fail until the ballot status is "Accepted":

```
E       AssertionError: BallotDetails(election='11/3/2020 State Election', mailed='First: 10/13/2020', received='Not returned', status='Not returned')
E       assert 'Not returned' == 'Accepted'
E         - Accepted
E         + Not returned
```

To make it work, create a [GitHub secret](https://docs.github.com/en/free-pro-team@latest/actions/reference/encrypted-secrets#creating-encrypted-secrets-for-a-repository) named "ENV" with the contents of your `.env` file.

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
