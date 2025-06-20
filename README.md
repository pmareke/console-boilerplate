# Console Boilerplate ![status](https://github.com/pmareke/console-boilerplate/actions/workflows/app.yml/badge.svg)

- This repository is meant to be used as a fast starter point.
- The Python version is the 3.12.8.
- The project has configured a [Github Action](https://github.com/pmareke/console-boilerplate/actions) which runs on every push to the `main` branch.
- The project has a `Dockerfile` ready to use to deploy the app in production.

## Requirements

- You only need to have [uv](https://docs.astral.sh/uv) installed.
- In order to work in the project you need to activate the **virtual environment**, you can do it:
    - Manually with the following command `source .venv/bin/activate`.
    - Automatically with [pyautoenv](https://github.com/hsaunders1904/pyautoenv).

## Folder structure

- There is a `tests` folder with the tests files.
    - The `unit` folder contains the unit tests, also known as [F.I.R.S.T](https://dzone.com/articles/writing-your-first-unit-tests#:~:text=First%20class%20developers%20write%20their,self%2Dvalidating%2C%20and%20timely.&text=Unit%20tests%20are%20required%20to%20test%20singular%20sections%20of%20code.).
    - The `integration` folder contains the tests that will validate the connection between our app and the external services.
    - The `acceptance` folder contains the tests that validate the app behavior from the outside.
- The production code goes inside the `src` folder.
    - The `delivery` folder contains the `console` logic.
    - The `domain` folder contains the domain classes of the app.
    - The `infrastructure` folder contains the classes that interact with the external services.
    - The `use_cases` folder contains the business logic.
    - The `common` folder contains the shared logic.
- Inside the `scripts` folder you can find the git hooks files.

## Project commands

The project uses [Makefiles](https://www.gnu.org/software/make/manual/html_node/Introduction.html) to run the most common tasks:

- `add-package package=XXX`: Installs the package XXX in the app, ex: `make install package=requests`.
- `build` : Builds the app using the Dockerfile.
- `up` : Runs the app using the Dockerfile.
- `check-typing`: Runs a static analyzer over the code in order to find issues.
- `check-format`: Checks the code format.
- `check-lint`: Checks the code style.
- `checks`: Run all the checks.
- `coverage` : Generates the coverage report.
- `format`: Formats the code.
- `lint`: Lints the code.
- `help` : Shows this help.
- `install`: Installs the app packages.
- `local-setup`: Sets up the local environment (e.g. install git hooks).
- `run`: Runs the app without Docker.
- `test`: Run all the tests.
- `update`: Updates the app packages.
- `watch`: Run all the tests in watch mode.

**Important: Please run the `make local-setup` command before starting with the code.**

_In order to create a commit you have to pass the pre-commit phase which runs the check and test commands._

## Packages

This project uses [uv](https://docs.astral.sh/uv) as the package manager.

### Testing

- [pytest](https://docs.pytest.org/en/7.1.x/contents.html): Testing runner.
- [expects](https://expects.readthedocs.io/en/stable/): An expressive and extensible TDD/BDD assertion library for Python.
- [doublex](https://pypi.org/project/doublex-expects/): A powerful test doubles framework for Python.

### Code style

- [ty](https://github.com/astral-sh/ty): A static type checker.
- [ruff](https://docs.astral.sh/ruff/installation/): A Python linter and formatter.

