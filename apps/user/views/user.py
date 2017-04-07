# -*- coding:utf-8 -*-

from flask import Blueprint
from flask import request
from flask import render_template
from flask import redirect
from flask_login import login_user
from flask_login import logout_user

from apps.user.service.user import get_user_by_username
from apps.user.form.register_form import RegisterForm
from apps.user.form.login_form import LoginForm
from apps.user.service.user import register_new_user

user_blueprint = Blueprint('user', __name__)


@user_blueprint.route('/login/', methods=('GET', 'POST',))
def login():
    """
    登录路由
    """
    if request.method == 'GET':
        return render_template('test/login.html')
    form = LoginForm(request.form)

    if form.validate_on_submit():
        login_user(form.user)
        return redirect('/')

    return render_template('test/login.html', form=form)


@user_blueprint.route('/register/', methods=('GET', 'POST',))
def register():
    """
    注册路由
    """
    if request.method == 'GET':
        return render_template('test/register.html')
    form = RegisterForm(request.form)

    if form.validate_on_submit():
        user = register_new_user(form)
        login_user(user)
        return redirect('/')

    return render_template('test/register.html', form=form)


@user_blueprint.route('/logout/', methods=('GET', 'POST',))
def logout():
    """
    用户登录
    """
    logout_user()
    return redirect('/')


@user_blueprint.route('/profile/<string:username>/', methods=('GET', 'POST',))
def user_profile(username):
    """
    用户详情
    """
    user = None
    if username:
        user = get_user_by_username(username)
    if user is not None:
        return user.username
    return '没有该用户'

