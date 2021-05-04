import unittest
from flask_testing import TestCase
from flaskboilerplate import create_app,db
from flaskboilerplate.Config import TestConfig
app=create_app()

class BaseTestCase(TestCase):

    def create_app(self):
        # app.config.from_object('Config.TestConfig')
        return app

    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()