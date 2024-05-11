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
* **jenkins** - Jenkins – an open source automation server which enables developers around the world to reliably build, test, and deploy their software
* **minio** - MinIO's High Performance Object Storage is Open Source, Amazon S3 compatible, Kubernetes Native and is designed for cloud native workloads like AI

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
$ docker compose up -d --build
``````sh
$ docker-compose exec web sh
flask createdb
flask seed
```
with this you will run all necessary instances as well all the configuration needed to that
## Key Python Modules Used
* **redis**:
* **postgres**:
* **pgadmin4**:
* **rethinkdb**:

_NOTE_:
* infisical access
  * **infisical@infisical.pt**
  * **infisicaladmin**

* jenkins
  * **16f45d739d02460bafe80573f7955e5a**
  * **jenkins**
  * **jenkinsadmin**
  * **jenkins@jenkins.pt**

* pgadmin access
  * **infisical@infisical.pt**
  * **infisical**
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



024-05-07 22:45:43,557 INFO sqlalchemy.engine.Engine [generated in 0.00026s] {'username_1': 'HeatherMacdonald', 'email_1': 'william.williams@example.com', 'password_1': 'password', 'param_1': 1}
2024-05-07 22:45:44,006 INFO sqlalchemy.engine.Engine INSERT INTO account_user (username, email, _password, nick_name, is_active, open_id, session_key, created_at, updated_at) VALUES (%(username)s, %(email)s, %(_password)s, %(nick_name)s, %(is_active)s, %(open_id)s, %(session_key)s, %(created_at)s, %(updated_at)s) RETURNING account_user.id
2024-05-07 22:45:44,006 INFO sqlalchemy.engine.Engine [generated in 0.00028s] {'username': 'HeatherMacdonald', 'email': 'william.williams@example.com', '_password': '$2b$13$Q9dTuCcdkDtRHC.uxhh8vOJIFdhuW0VPSnPlULx0ByXC4rHY7nQ8C', 'nick_name': None, 'is_active': True, 'open_id': None, 'session_key': None, 'created_at': datetime.datetime(2024, 5, 7, 21, 45, 40, 8795, tzinfo=datetime.timezone.utc), 'updated_at': datetime.datetime(2024, 5, 7, 21, 45, 40, 8938, tzinfo=datetime.timezone.utc)}
2024-05-07 22:45:44,030 INFO sqlalchemy.engine.Engine [cached since 0.4737s ago] {'username_1': 'DennisCrawford', 'email_1': 'james.gonzalez@example.com', 'password_1': 'password', 'param_1': 1}
2024-05-07 22:45:44,469 INFO sqlalchemy.engine.Engine INSERT INTO account_user (username, email, _password, nick_name, is_active, open_id, session_key, created_at, updated_at) VALUES (%(username)s, %(email)s, %(_password)s, %(nick_name)s, %(is_active)s, %(open_id)s, %(session_key)s, %(created_at)s, %(updated_at)s) RETURNING account_user.id
2024-05-07 22:45:44,469 INFO sqlalchemy.engine.Engine [cached since 0.4638s ago] {'username': 'DennisCrawford', 'email': 'james.gonzalez@example.com', '_password': '$2b$13$QXhu5brVuFf9u88OakLXT.6GPMTOEoduP7MU4EBtZoeQuUHhzRjNm', 'nick_name': None, 'is_active': True, 'open_id': None, 'session_key': None, 'created_at': datetime.datetime(2024, 5, 7, 21, 45, 40, 8795, tzinfo=datetime.timezone.utc), 'updated_at': datetime.datetime(2024, 5, 7, 21, 45, 40, 8938, tzinfo=datetime.timezone.utc)}
2024-05-07 22:45:44,483 INFO sqlalchemy.engine.Engine [cached since 0.927s ago] {'username_1': 'JuanGreene', 'email_1': 'diana.taylor@example.com', 'password_1': 'password', 'param_1': 1}
2024-05-07 22:45:44,930 INFO sqlalchemy.engine.Engine INSERT INTO account_user (username, email, _password, nick_name, is_active, open_id, session_key, created_at, updated_at) VALUES (%(username)s, %(email)s, %(_password)s, %(nick_name)s, %(is_active)s, %(open_id)s, %(session_key)s, %(created_at)s, %(updated_at)s) RETURNING account_user.id
2024-05-07 22:45:44,930 INFO sqlalchemy.engine.Engine [cached since 0.9247s ago] {'username': 'JuanGreene', 'email': 'diana.taylor@example.com', '_password': '$2b$13$7Q2JCxiZoDiIQxc1x577JeecMVM5PgrRy/CXeqYE7LH4cS5b/ocRm', 'nick_name': None, 'is_active': True, 'open_id': None, 'session_key': None, 'created_at': datetime.datetime(2024, 5, 7, 21, 45, 40, 8795, tzinfo=datetime.timezone.utc), 'updated_at': datetime.datetime(2024, 5, 7, 21, 45, 40, 8938, tzinfo=datetime.timezone.utc)}
2024-05-07 22:45:44,944 INFO sqlalchemy.engine.Engine [cached since 1.388s ago] {'username_1': 'AlexanderJackson', 'email_1': 'jeffrey.bruce@example.com', 'password_1': 'password', 'param_1': 1}
2024-05-07 22:45:45,391 INFO sqlalchemy.engine.Engine INSERT INTO account_user (username, email, _password, nick_name, is_active, open_id, session_key, created_at, updated_at) VALUES (%(username)s, %(email)s, %(_password)s, %(nick_name)s, %(is_active)s, %(open_id)s, %(session_key)s, %(created_at)s, %(updated_at)s) RETURNING account_user.id
2024-05-07 22:45:45,391 INFO sqlalchemy.engine.Engine [cached since 1.386s ago] {'username': 'AlexanderJackson', 'email': 'jeffrey.bruce@example.com', '_password': '$2b$13$Z6z2HImHnea.2r7Dajt2ke3/pPXK8t7iXBy9PxAlDe1sqpZHAZR6S', 'nick_name': None, 'is_active': True, 'open_id': None, 'session_key': None, 'created_at': datetime.datetime(2024, 5, 7, 21, 45, 40, 8795, tzinfo=datetime.timezone.utc), 'updated_at': datetime.datetime(2024, 5, 7, 21, 45, 40, 8938, tzinfo=datetime.timezone.utc)}
2024-05-07 22:45:45,406 INFO sqlalchemy.engine.Engine [cached since 1.849s ago] {'username_1': 'BrandiWyatt', 'email_1': 'deborah.price@example.com', 'password_1': 'password', 'param_1': 1}
2024-05-07 22:45:45,840 INFO sqlalchemy.engine.Engine INSERT INTO account_user (username, email, _password, nick_name, is_active, open_id, session_key, created_at, updated_at) VALUES (%(username)s, %(email)s, %(_password)s, %(nick_name)s, %(is_active)s, %(open_id)s, %(session_key)s, %(created_at)s, %(updated_at)s) RETURNING account_user.id
2024-05-07 22:45:45,841 INFO sqlalchemy.engine.Engine [cached since 1.835s ago] {'username': 'BrandiWyatt', 'email': 'deborah.price@example.com', '_password': '$2b$13$quUvsknQWQFQLXV8ZZmU3uwdR5RZ9gQfZ8sFCoqtOZNzZ92TCvU36', 'nick_name': None, 'is_active': True, 'open_id': None, 'session_key': None, 'created_at': datetime.datetime(2024, 5, 7, 21, 45, 40, 8795, tzinfo=datetime.timezone.utc), 'updated_at': datetime.datetime(2024, 5, 7, 21, 45, 40, 8938, tzinfo=datetime.timezone.utc)}
2024-05-07 22:45:45,857 INFO sqlalchemy.engine.Engine [cached since 2.301s ago] {'username_1': 'RaymondMartinez', 'email_1': 'jason.jacobs@example.com', 'password_1': 'password', 'param_1': 1}
2024-05-07 22:45:46,291 INFO sqlalchemy.engine.Engine INSERT INTO account_user (username, email, _password, nick_name, is_active, open_id, session_key, created_at, updated_at) VALUES (%(username)s, %(email)s, %(_password)s, %(nick_name)s, %(is_active)s, %(open_id)s, %(session_key)s, %(created_at)s, %(updated_at)s) RETURNING account_user.id
2024-05-07 22:45:46,291 INFO sqlalchemy.engine.Engine [cached since 2.286s ago] {'username': 'RaymondMartinez', 'email': 'jason.jacobs@example.com', '_password': '$2b$13$OY.RbbJLCO7GoDddFsqxn.bpEjaUM02G0z/rfTw84OOYOPObf4vzm', 'nick_name': None, 'is_active': True, 'open_id': None, 'session_key': None, 'created_at': datetime.datetime(2024, 5, 7, 21, 45, 40, 8795, tzinfo=datetime.timezone.utc), 'updated_at': datetime.datetime(2024, 5, 7, 21, 45, 40, 8938, tzinfo=datetime.timezone.utc)}
2024-05-07 22:45:46,306 INFO sqlalchemy.engine.Engine [cached since 2.75s ago] {'username_1': 'JaySmith', 'email_1': 'tony.jimenez@example.com', 'password_1': 'password', 'param_1': 1}
2024-05-07 22:45:46,734 INFO sqlalchemy.engine.Engine INSERT INTO account_user (username, email, _password, nick_name, is_active, open_id, session_key, created_at, updated_at) VALUES (%(username)s, %(email)s, %(_password)s, %(nick_name)s, %(is_active)s, %(open_id)s, %(session_key)s, %(created_at)s, %(updated_at)s) RETURNING account_user.id
2024-05-07 22:45:46,734 INFO sqlalchemy.engine.Engine [cached since 2.728s ago] {'username': 'JaySmith', 'email': 'tony.jimenez@example.com', '_password': '$2b$13$S74gFa2MrNGR60CXS7CF6OZfuB0sI4tpbfYEbariFwfb71uj90H0G', 'nick_name': None, 'is_active': True, 'open_id': None, 'session_key': None, 'created_at': datetime.datetime(2024, 5, 7, 21, 45, 40, 8795, tzinfo=datetime.timezone.utc), 'updated_at': datetime.datetime(2024, 5, 7, 21, 45, 40, 8938, tzinfo=datetime.timezone.utc)}
{'username': 'admin', 'email': 'admin@163.com', '_password': '$2b$13$RSsxtcmmXhFwpcUbUToqhOGq78pSURyVxkLl3zMfxUoXFmCqduJ3O', 'nick_name': None, 'is_active': True, 'open_id': None, 'session_key': None, 'created_at': datetime.datetime(2024, 5, 7, 21, 45, 40, 8795, tzinfo=datetime.timezone.utc), 'updated_at': datetime.datetime(2024, 5, 7, 21, 45, 40, 8938, tzinfo=datetime.timezone.utc)}