"""
Route paths to login & register
"""
from flask import render_template, url_for, flash, redirect, Blueprint
from flask_login import login_user, current_user, logout_user
from flaskboilerplate import db, bcrypt
from flaskboilerplate.models import User
from flaskboilerplate.users.forms import RegistrationForm, LoginForm

users = Blueprint("users", __name__)
"""Routes"""


@users.route("/register", methods=["GET", "POST"])
def register():
    print(current_user.is_authenticated)
    if current_user.is_authenticated:
        flash("Already Logged In", "success")
        return redirect(url_for("main.home"))
    form = RegistrationForm()
    if form.validate_on_submit():
        check_user = User.query.filter_by(email=form.email.data).first()
        if check_user:
            flash("Account already Exist", "success")
        else:
            hashed_password = bcrypt.generate_password_hash(form.password.data).decode(
                "utf-8"
            )
            user = User(
                username=form.username.data,
                email=form.email.data,
                password=hashed_password,
            )
            db.session.add(user)
            db.session.commit()
            flash(
                "Your account has been created! You are now able to log in", "success"
            )
            return redirect(url_for("users.login"))

    return render_template("register.html", title="Register", form=form)


@users.route("/login", methods=["GET", "POST"])
# function for user login
def login():
    if current_user.is_authenticated:
        flash("Already Logged IN", "success")
        return redirect(url_for("main.home"))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            flash("Login Successful.", "success")
            return redirect(url_for("main.home"))
        else:
            flash("Login Unsuccessful. Please check email and password", "danger")

    return render_template("login.html", title="Login", form=form)


@users.route("/logout")
# function for user logout
def logout():
    logout_user()
    return redirect(url_for("main.home"))
