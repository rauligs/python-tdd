# Learning Python

Following examples from **Learning Python, 5th Ed.** By **Mark Lutz** 

## Installation
1. Install python `$ brew install python3`
2. Install `[pipenv](https://pipenv.readthedocs.io/en/latest/install/#installing-pipenv)`
3. Activate the environment: `$ pipenv shell`
4. Install dependencies from `Pipfile`: `$ pipenv install --dev`

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