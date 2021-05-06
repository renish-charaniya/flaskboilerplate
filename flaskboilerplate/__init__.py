from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_testing import TestCase
from flaskboilerplate.Config import Config


db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view = "users.login"
login_manager.login_message_category = "info"


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config["TESTING"] = True
    app.config.from_object(Config)
    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)

    from flaskboilerplate.users.routes import users
    from flaskboilerplate.main.routes import main

    app.register_blueprint(users)
    app.register_blueprint(main)
    # with app.app_context():
    #     db.create_all()
    return app
