from flask import Flask
from flask_bcrypt import Bcrypt
from flask_mysqldb import MySQL
from flaskboilerplate.Config import Config



# Intialize MySQL
mysql = MySQL()
bcrypt=Bcrypt()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)
    mysql.init_app(app)
    bcrypt.init_app(app)

    from flaskboilerplate.users.routes import users
    from flaskboilerplate.main.routes import main
    app.register_blueprint(users)
    app.register_blueprint(main)

    return app