from flask import render_template, flash,redirect, url_for

from . import bp 
from app.forms import RegisterForm
from app.models import User
from app import db
@bp.route('/signin')
def signin():
    return render_template('signin.jinja')

@bp.route('/register', methods=['GET','POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        username= form.username.data
        user=User.query.filter_by(username=username).first()
        email = User.query.filter_by(email=form.email.data).first()
        if not email and not user:
            u= User(username=form.username.data,email=form.email.data,password=form.password.data)
            u.commit()
            flash(f'{form.username.data} registered')
            return redirect(url_for('main.home'))
        if user:
            flash(f'{form.username.data} already taken, try again')
        else:
            flash(f'{form.email.data} already taken, try again')
    return render_template('register.jinja',form=form)


