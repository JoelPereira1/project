# -*- coding: utf-8 -*-
"""Defines fixtures available to all tests."""
import pytest
# from pathlib import Path
from shop.app import create_app
from shop.database import db as _db
# from random_data import create_menus, create_products_by_schema
# from shop.corelib.utils import jinja_global_varibles
from shop.models.user import User

# @pytest.fixture
# def app():
#     """An application for the tests."""
#     _app = create_app("tests.settings")
#     jinja_global_varibles(_app)
#     ctx = _app.test_request_context()
#     ctx.push()

#     yield _app

#     ctx.pop()

# @pytest.fixture
# def client(app):
#     return app.test_client()

# @pytest.fixture
# def db(app):
#     """A database for the tests."""
#     _db.app = app
#     with app.app_context():
#         _db.create_all()

#         create_menus()
#         create_products_by_schema(
#             placeholder_dir=Path("placeholders"), how_many=1, create_images=False
#         )

#     yield _db

#     # Explicitly close DB connection
#     _db.session.close()
#     _db.drop_all()









# --------
# Fixtures
# --------

# @pytest.fixture(scope='module')
# def new_user():
#     user = User('patkennedy79@gmail.com', 'FlaskIsAwesome')
#     return user


# @pytest.fixture(scope='module')
# def test_client():
#     # Set the Testing configuration prior to creating the Flask application
#     os.environ['CONFIG_TYPE'] = 'config.TestingConfig'
#     flask_app = create_app()

#     # Create a test client using the Flask application configured for testing
#     with flask_app.test_client() as testing_client:
#         # Establish an application context
#         with flask_app.app_context():
#             yield testing_client  # this is where the testing happens!


# @pytest.fixture(scope='module')
# def init_database(test_client):
#     # Create the database and the database table
#     db.create_all()

#     # Insert user data
#     default_user = User(email='patkennedy79@gmail.com', password_plaintext='FlaskIsAwesome')
#     second_user = User(email='patrick@yahoo.com', password_plaintext='FlaskIsTheBest987')
#     db.session.add(default_user)
#     db.session.add(second_user)

#     # Commit the changes for the users
#     db.session.commit()

#     # Insert book data
#     book1 = Book('Malibu Rising', 'Taylor Jenkins Reid', '5', default_user.id)
#     book2 = Book('Carrie Soto is Back', 'Taylor Jenkins Reid', '4', default_user.id)
#     book3 = Book('Book Lovers', 'Emily Henry', '3', default_user.id)
#     db.session.add(book1)
#     db.session.add(book2)
#     db.session.add(book3)

#     # Commit the changes for the books
#     db.session.commit()

#     yield  # this is where the testing happens!

#     db.drop_all()


# @pytest.fixture(scope='function')
# def log_in_default_user(test_client):
#     test_client.post('/login',
#                      data={'email': 'patkennedy79@gmail.com', 'password': 'FlaskIsAwesome'})

#     yield  # this is where the testing happens!

#     test_client.get('/logout')


# @pytest.fixture(scope='function')
# def log_in_second_user(test_client):
#     test_client.post('login',
#                      data={'email': 'patrick@yahoo.com','password': 'FlaskIsTheBest987'})

#     yield   # this is where the testing happens!

#     # Log out the user
#     test_client.get('/logout')


# @pytest.fixture(scope='module')
# def cli_test_client():
#     # Set the Testing configuration prior to creating the Flask application
#     os.environ['CONFIG_TYPE'] = 'config.TestingConfig'
#     flask_app = create_app()

#     runner = flask_app.test_cli_runner()

#     yield runner  # this is where the testing happens!
