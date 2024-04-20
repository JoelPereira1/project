## Overview

This Flask application contains the basic user management functionality (register, login, logout) to demonstrate how to test a Flask project using [pytest](https://docs.pytest.org/en/stable/).

For details on how to test a Flask app using pytest, check out my blog post on [TestDriven.io](https://testdriven.io/):

* [https://testdriven.io/blog/flask-pytest/](https://testdriven.io/blog/flask-pytest/)

![Testing Flask Applications with Pytest](project/static/img/flask_pytest_social.png?raw=true "Testing Flask Applications with Pytest")

## Motivation

## Installation Instructions

### Installation

Pull down the source code from this GitLab repository:

```sh
$ git clone git@gitlab.com:patkennedy79/flask_user_management_example.git
```
If you are running in local machine, we advice to use linux, and for that you will need to install some dependencies
```sh
$ sudo apt install libpq-dev alembic
```
Create a new virtual environment:

```sh
$ cd <PATH_TO_YOUR_CLONE>
$ python3 -m venv .venv
```

Activate alembic:
```sh
$ alembic init alembic
$ cp alembic/env.py alembic/versions/env.py
```

Create database:
```sh
$ python ./database_init.py
```

Activate the virtual environment:
```sh
$ source .venv/bin/activate
```

Install the python packages specified in requirements.txt:

```sh
(venv) $ pip install -r requirements.txt
```

### Database Initialization

This Flask application needs a SQLite database to store data.  The database should be initialized using:

```
(venv) $ flask createdb
(venv) $ flask seed
```

### Running the Flask Application

Run development server to serve the Flask application:

```sh
(venv) $ flask --app app --debug run
(venv) $ python -m flask run --debugger --port="8088" --reload
```

Navigate to 'http://127.0.0.1:8088' in your favorite web browser to view the website!

## Key Python Modules Used

* **Flask**: micro-framework for web application development which includes the following dependencies:
  * click: package for creating command-line interfaces (CLI)
  * itsdangerous: cryptographically sign data
  * Jinja2: templating engine
  * MarkupSafe: escapes characters so text is safe to use in HTML and XML
  * Werkzeug: set of utilities for creating a Python application that can talk to a WSGI server
* **pytest**: framework for testing Python projects
* **Flask-SQLAlchemy** - ORM (Object Relational Mapper) for Flask
* **Flask-Login** - support for user management (login/logout) in Flask
* **Flask-WTF** - simplifies forms in Flask
* **flake8** - static analysis tool
* **isort** - sorts Python package imports
* **safety** - checks Python dependencies for known security vulnerabilities
* **bandit** - tool designed to find common security issues in Python code

This application is written using Python 3.10.

## Testing

To run all the tests:

```sh
(venv) $ python -m pytest -v
```

To check the code coverage of the tests:

```sh
(venv) $ python -m pytest --cov-report term-missing --cov=project
```

