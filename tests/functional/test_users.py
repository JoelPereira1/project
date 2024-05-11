"""
This file (test_users.py) contains the functional tests for the `users` blueprint.

These tests use GETs and POSTs to different URLs to check for the proper behavior
of the `users` blueprint.
"""
import os
import pytest

@pytest.fixture(scope='function')
def log_in_default_user(client):
  client.post('/account/login', data={'email': 'patkennedy79@gmail.com', 'password': 'FlaskIsAwesome'})
  yield  # this is where the testing happens!
  client.get('/account/logout')

@pytest.fixture(scope='function')
def log_in_second_user(client):
  client.post('login',data={'email': 'patrick@yahoo.com','password': 'FlaskIsTheBest987'})
  yield   # this is where the testing happens!
  # Log out the user
  client.get('/account/logout')


def test_login_page(client):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/login' page is requested (GET)
    THEN check the response is valid
    """
    response = client.get('/account/login')
    assert response.status_code == 200

    # assert b'Login' in response.data
    # assert b'Email' in response.data
    # assert b'Password' in response.data

def test_valid_login_logout(client, init_database):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/login' page is posted to (POST)
    THEN check the response is valid
    """
    response = client.post('/account/login',
                                data=dict(email='patkennedy79@gmail.com', password='FlaskIsAwesome'),
                                follow_redirects=True)
    assert response.status_code == 200
    assert b'Thank you for logging in, patkennedy79@gmail.com!' in response.data
    assert b'Flask User Management' in response.data
    assert b'Logout' in response.data
    assert b'Login' not in response.data
    assert b'Register' not in response.data

    """
    GIVEN a Flask application configured for testing
    WHEN the '/logout' page is requested (GET)
    THEN check the response is valid
    """
    response = client.get('/account/logout', follow_redirects=True)
    assert response.status_code == 200
    assert b'Goodbye!' in response.data
    assert b'Flask User Management' in response.data
    assert b'Logout' not in response.data
    assert b'Login' in response.data
    assert b'Register' in response.data

def test_invalid_login(client, init_database):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/login' page is posted to with invalid credentials (POST)
    THEN check an error message is returned to the user
    """
    response = client.post('/login',
                                data=dict(email='patkennedy79@gmail.com', password='FlaskIsNotAwesome'),
                                follow_redirects=True)
    assert response.status_code == 200
    assert b'ERROR! Incorrect login credentials.' in response.data
    assert b'Flask User Management' in response.data
    assert b'Logout' not in response.data
    assert b'Login' in response.data
    assert b'Register' in response.data

def test_login_already_logged_in(client, init_database, log_in_default_user):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/login' page is posted to (POST) when the user is already logged in
    THEN check an error message is returned to the user
    """
    response = client.post('/login',
                                data=dict(email='patkennedy79@gmail.com', password='FlaskIsNotAwesome'),
                                follow_redirects=True)
    assert response.status_code == 200
    assert b'Already logged in!  Redirecting to your User Profile page...' in response.data
    assert b'Flask User Management' in response.data
    assert b'Logout' in response.data
    assert b'Login' not in response.data
    assert b'Register' not in response.data

def test_valid_registration(client, init_database):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/register' page is posted to (POST)
    THEN check the response is valid and the user is logged in
    """
    response = client.post('/register',
                                data=dict(email='patkennedy79@yahoo.com',
                                          password='FlaskIsGreat',
                                          confirm='FlaskIsGreat'),
                                follow_redirects=True)
    assert response.status_code == 200
    assert b'Registration successful. You can now log in.' in response.data

def test_invalid_registration(client, init_database):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/register' page is posted to with invalid credentials (POST)
    THEN check an error message is returned to the user
    """
    response = client.post('/register',
                                data=dict(email='patkennedy79@hotmail.com',
                                          password='FlaskIsGreat',
                                          confirm='FlskIsGreat'),   # Does NOT match!
                                follow_redirects=True)
    assert response.status_code == 200
    assert b'Thank you for registering, patkennedy79@hotmail.com!' not in response.data
    assert b'[This field is required.]' not in response.data
    assert b'Flask User Management' in response.data
    assert b'Logout' not in response.data
    assert b'Login' in response.data
    assert b'Register' in response.data

def test_duplicate_registration(client, init_database):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/register' page is posted to (POST) using an email address already registered
    THEN check an error message is returned to the user
    """
    # Register the new account
    client.post('/register',
                     data=dict(email='pkennedy@hey.com',
                               password='FlaskIsTheBest',
                               confirm='FlaskIsTheBest'),
                     follow_redirects=True)

    # Since the registration process results in the user being logged in, log out the user
    client.get('/logout', follow_redirects=True)

    # Try registering with the same email address
    response = client.post('/register',
                                data=dict(email='pkennedy@hey.com',
                                          password='FlaskIsStillTheBest',
                                          confirm='FlaskIsStillTheBest'),
                                follow_redirects=True)
    assert response.status_code == 200
    assert b'ERROR! Email (pkennedy@hey.com) already exists in the database.' in response.data
    assert b'Thank you for registering, pkennedy@hey.com!' not in response.data

def test_registration_when_logged_in(client, log_in_default_user):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/register' page is posted to (POST) when the user is logged in
    THEN check an error message is returned to the user
    """
    response = client.post('/register',
                                data=dict(email='pkennedy@hey.com',
                                          password='FlaskIsStillTheBest',
                                          confirm='FlaskIsStillTheBest'),
                                follow_redirects=True)
    assert response.status_code == 200
    # assert b'Already logged in!  Redirecting to your User Profile page...' in response.data
    # assert b'Thank you for registering, pkennedy@hey.com!' not in response.data

def test_status_page(client):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/status' page is requested (GET)
    THEN check the response is valid
    """
    response = client.get('/status')
    assert response.status_code == 200
    assert b'Web Application: Active' in response.data
    assert b'Configuration Type: config.TestingConfig' in response.data
    assert b'Database initialized: True' in response.data
    assert b'Database `users` table created: True' in response.data
    assert b'Database `books` table created: True' in response.data
