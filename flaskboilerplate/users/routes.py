from flask import Flask,render_template,flash,redirect,url_for,Blueprint
from flaskboilerplate import mysql,bcrypt
import MySQLdb.cursors
from flaskboilerplate.users.forms  import RegistrationForm,LoginForm
users=Blueprint('users',__name__)


@users.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_pswd = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM accounts WHERE email = %s', [form.email.data])
        account = cursor.fetchone()
        # If account exists show error and validation checks
        if account:
            flash(f'Account Already Exist ', 'danger')
        else:
            # Account doesnt exists and the form data is valid, now insert new account into accounts table
            cursor.execute('INSERT INTO accounts VALUES (NULL, %s, %s, %s)',
                           (form.username.data, hashed_pswd, form.email.data))
            mysql.connection.commit()
            flash(f'Account Created for {form.username.data}!', 'success')

        return redirect(url_for('main.home'))

    return render_template('register.html', title='Register', form=form)


@users.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    email = form.email.data
    if form.validate_on_submit():
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM accounts WHERE email = %s', [email])
        account = cursor.fetchone()

        if account and bcrypt.check_password_hash(account['password'], form.password.data):
            flash('You have been logged in!!', 'success')
            return redirect(url_for('main.home'))
        else:
            flash('Login Unsuccessful', 'danger')
    return render_template('login.html', title='Login', form=form)
