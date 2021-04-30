from datetime import datetime
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from flask import current_app
from flaskboilerplate import db, login_manager,bcrypt
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))



class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=False, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)

    def __init__(self,username,email, password):
        """Create a new User object using the email address and hashing the
        plaintext password using Bcrypt.
        """
        self.username=username
        self.email = email
        self.password = bcrypt.generate_password_hash(password).decode('utf-8')


    def is_correct_password(self, plaintext_password: str):
        return bcrypt.check_password_hash(self.hashed_password, plaintext_password)

    def set_password(self, plaintext_password):
        self.hashed_password = bcrypt.generate_password_hash(plaintext_password).decode('utf-8')

    def __repr__(self):
        return f'<User: {self.email}>'


