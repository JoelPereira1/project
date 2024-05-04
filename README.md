### ✨ Overview <a name="overview"></a>
This a basic Flask application, it demonstrate a eshop and a basic ci/cd flow.

## Motivation
Present the final project for the rumos academy

## 🚀 Setup <a name="setup"></a>
1. [Install Docker](https://docs.docker.com/engine/install/), then start Docker locally.

2. Pull down the source code from this GitLab repository:
```sh
$ git clone git@github.com:JoelPereira1/project.git
```
this project has the ability to run locally or through a docker compose file, if you try to run it locally isolated you must be sure to have, some installed requirements.
## Key Python Modules Used
* **Flask**: micro-framework for web application development which includes the following dependencies:
* **click**: package for creating command-line interfaces (CLI)
* **itsdangerous**: cryptographically sign data
* **Jinja2**: templating engine
* **MarkupSafe**: escapes characters so text is safe to use in HTML and XML
* **Werkzeug**: set of utilities for creating a Python application that can talk to a WSGI server
* **pytest**: framework for testing Python projects
* **Flask-SQLAlchemy** - ORM (Object Relational Mapper) for Flask
* **Flask-Login** - support for user management (login/logout) in Flask
* **Flask-WTF** - simplifies forms in Flask
* **Faker** - tool to produce fake data
* **infisical** - tool to connect to infisical instance, Open Source Secret Management * [https://infisical.com/](https://infisical.com/)
* **rethinkdb** - RethinkDB is the first open-source scalable database built for realtime applications * [https://pypi.org/project/rethinkdb/](https://pypi.org/project/rethinkdb/)
* **elasticsearch** - Python client for Elasticsearch

This application is written using Python 3.10.

You will need a postgres server installed, and change se settings.py file, to use your definitions
We advice to use linux, and for that you will need to install also some system packages
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
Activate the virtual environment:
```sh
$ source .venv/bin/activate
```
Install the python packages specified in requirements.txt:
```sh
(venv) $ pip install -r requirements.txt
```
### Database Initialization
Create database:
```sh
(venv) $ python ./database_init.py
```
This Flask application needs a postgres database to store data.  The database should be initialized using:
```
(venv) $ flask createdb
(venv) $ flask seed
```
### Running the Flask Application
Run development server to serve the Flask application:
```sh
(venv) $ python -m flask run --debugger --port="8088" --reload
```
Navigate to 'http://127.0.0.1:8088' in your favorite web browser to view the website!

3. If you opt by the docker way, grant that docker is installed and run
```sh
$ docker compose build
```
```sh
$ docker compose up -d
```
with this you will run all necessary instances as well all the configuration needed to that
## Key Python Modules Used
* **redis**:
* **postgres**:
* **pgadmin4**:
* **rethinkdb**:

_NOTE_: infisical access
infisical@infisical.pt
infisicaladmin

## Testing

To run all the tests:

```sh
(venv) $ python -m pytest -v
```

To check the code coverage of the tests:

```sh
(venv) $ python -m pytest --cov-report term-missing --cov=project
```

## Run by docker compose

To run the app and all instances needed to function you should run it by docker compose, grant that you have the docker installed
docker compose up -d