import unittest

from flask_login import current_user
from flask import request

from .base import BaseTestCase
from flaskboilerplate import bcrypt
from flaskboilerplate.models import User


class TestUser(BaseTestCase):
    # Ensure user can register
    def test_user_registeration(self):
            response = self.client.post('/register', data=dict(
                username='Michael', email='michael@realpython.com',
                password='python', confirm_password='python'
            ), follow_redirects=True)

            self.assertEqual(response.status_code, 200)
            self.assertIn(b'Your account has been created! You are now able to log in',response.data)

    # Ensure given password is correct after unhashing
    def test_check_password(self):
        user = User.query.filter_by(email='jam@g.c').first()
        self.assertTrue(bcrypt.check_password_hash(user.password, 'admin'))
        self.assertFalse(bcrypt.check_password_hash(user.password, 'foobar'))