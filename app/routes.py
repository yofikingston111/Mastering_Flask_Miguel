from flask import render_template
from app import app
from app.forms import LoginForm
from flask import render_template, flash, redirect, url_for

#Home page route

@app.route('/login', methods=['GET', 'POST'])

def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, dont missed '.format( form.username.data))
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign in', form=form)

@app.route('/')
def index():
    user = {'username': 'Miguel'}
    return render_template('index.html', title='Home', user=user)

