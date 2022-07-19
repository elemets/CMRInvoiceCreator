from flask import render_template, url_for, flash, redirect, request
from cmrflask import app, db, bcrypt
from cmrflask.models import User, CMR, Goods
from cmrflask.forms import registration_form, login_form, cmr_form
from cmrflask.cmr_builder import drawCMR
from flask_login import login_user, current_user, logout_user, login_required
import time


posts = [
    {
        'author': 'Arthur Funnell',
        'title': 'Blog post 1',
        'content': 'First Post conent',
        'date_posted': 'April 20, 2019'
    },
    {
        'author': 'John Doe',
        'title': 'Blog post 2',
        'content': 'second Post conent',
        'date_posted': 'April 21, 2019'
    }
]



@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)


@app.route("/pdfbuilder", methods=["GET", "POST"])
def pdfbuilder():
    form = cmr_form()
    try:
        drawCMR(form.data, date, user_name)
    except:
        pass
    time.sleep(3)
    return render_template('pdfbuilder.html', title='PDF Builder', form=form)


## creating the registration route
@app.route("/register", methods=["GET", "POST"])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = registration_form()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash(f'Your account has been created you can now login!', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title="Register", form=form)


## creating the login route
@app.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = login_form()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            flash('Login unsuccessful please check email and password', 'danger')
    return render_template('login.html', title="Login", form=form)

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route("/account")
@login_required
def account():
    return render_template('account.html', title="Account")


