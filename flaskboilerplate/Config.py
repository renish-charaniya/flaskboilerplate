import os


class Config:
  SECRET_KEY = '9da42c87d7292bd9f8089c39463c2532'
  SQLALCHEMY_DATABASE_URI = 'sqlite:///auth.db'
  SQLALCHEMY_TRACK_MODIFICATIONS = False

class TestConfig(Config):
  DEBUG = True
  TESTING = True
  WTF_CSRF_ENABLED = False
  SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'