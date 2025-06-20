from flask import Blueprint, render_template, redirect, url_for, flash
from app.forms.Forms import LoginForm, RegisterForm
from werkzeug.security import generate_password_hash, check_password_hash
from app.models.Db_models import *
from flask_login import login_required, login_user, logout_user, current_user

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
  if current_user.is_authenticated:
    return redirect(url_for('main.index'))
  form = LoginForm()
  if form.validate_on_submit():
    data = Crud(session)
    username = form.username.data
    password = form.password.data
    user = data.read_by_id(User, 'username', username)
    if user and check_password_hash(user.password, password):
      login_user(user)
      return redirect(url_for('main.index'))
    else:
      flash("Username atau password salah", 'danger')
  return render_template('login.html', form=form)
  
@auth.route('/register', methods=['GET', 'POST'])
def register():
  if current_user.is_authenticated:
    return redirect(url_for('main.index'))
  form = RegisterForm()
  if form.validate_on_submit():
    username = form.username.data
    password = form.password.data
    hashed = generate_password_hash(password)
    data = Crud(session)
    user = User(
        username = username,
        password = hashed
      )
    add = data.add(user)
    if add > 0:
      flash('Register Sukses', 'success')
    else:
      flash('Register Gagal', 'danger')
  return render_template('register.html', form=form)

@auth.route('/logout')
@login_required
def logout():
  logout_user()
  return redirect(url_for('auth.login'))