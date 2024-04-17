import unittest
import os
import json
# from your_app_module import app, db
# from your_models_module import User


def is_success_res(client, path):
    rv = client.get(path)
    assert rv.status_code == 200


@pytest.mark.usefixtures("db")
class TestBasicPageCanView:
    def test_404(self, client):
        rv = client.get("/404notfound")
        assert rv.status_code == 404

    def test_homepage(self, client):
        is_success_res(client, "/")

    def test_category_page(self, client):
        is_success_res(client, "/products/category/1")

    def test_product_page(self, client):
        is_success_res(client, "/products/1")

    def test_account_page(self, client):
        is_success_res(client, "/account/")

    def test_login_page(self, client):
        is_success_res(client, "/account/login")

    def test_signup_page(self, client):
        is_success_res(client, "/account/signup")


class UserModelTestCase(unittest.TestCase):
    def setUp(self):
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://'
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_password_hashing(self):
        u = User(username='test', email='test@example.com', password='cat')
        u.hash_password()
        self.assertTrue(u.check_password('cat'))
        self.assertFalse(u.check_password('dog'))

    def test_password_salts_are_random(self):
        u1 = User(username='test1', email='test1@example.com', password='cat')
        u1.hash_password()
        u2 = User(username='test2', email='test2@example.com', password='cat')
        u2.hash_password()
        self.assertTrue(u1.password != u2.password)

class AppTestCase(unittest.TestCase):
    def setUp(self):
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://'
        app.config['TESTING'] = True
        self.client = app.test_client()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_homepage(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Welcome to our webshop!', response.data)

    def test_register(self):
        response = self.client.post('/register', data={
            'username': 'test',
            'email': 'test@example.com',
            'password': 'cat',
            'confirm_password': 'cat'
        })
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/login')
        user = User.query.filter_by(username='test').first()
        self.assertIsNotNone(user)
        self.assertTrue(user.check_password('cat'))

    def test_login(self):
        user = User(username='test', email='test@example.com', password='cat')
        db.session.add(user)
        db.session.commit()
        response = self.client.post('/login', data={
            'username': 'test',
            'password': 'cat'
        }, follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Welcome, test!', response.data)

    def test_logout(self):
        user = User(username='test', email='test@example.com', password='cat')
        db.session.add(user)
        db.session.commit()
        self.client.post('/login', data={
            'username': 'test',
            'password': 'cat'
        }, follow_redirects=True)
        response = self.client.get('/logout', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'You have been logged out.', response.data)