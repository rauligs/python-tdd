# Learning Python
Learning Python. TDD approach

## Installation
1. Install python `$ brew install python3`
1. Install `[pipenv](https://pipenv.readthedocs.io/en/latest/install/#installing-pipenv)`
1. Activate the environment: `$ pipenv shell`
1. Install dependencies from `Pipfile`: `$ pipenv install --dev`

## Installing Additional Packages
```
$ pipenv install <package>
```
```
$ pipenv install --dev <package>
```
See [here](https://pipenv.readthedocs.io/en/latest/install/#installing-packages-for-your-project) for more.

## Testing
```
$ pytest -v --cov-report term-missing --cov=. --cov-fail-under=100
```

## Code Formatting
```
$ yapf --style=google -i *.py
```