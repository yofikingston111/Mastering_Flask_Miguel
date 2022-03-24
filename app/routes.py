from flask import render_template
from app import app
from flask_login import current_user, login_user
from app.models import User
from app.forms import LoginForm
from flask import render_template, flash, redirect, url_for
from flask_login import logout_user
from flask_login import login_required
from flask import request
from werkzeug.urls import url_parse


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign in', form=form)


# route
@app.route('/')
@app.route('/index')
@login_required
def index():
    return render_template("index.html", title='Home Page', posts=posts)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))
