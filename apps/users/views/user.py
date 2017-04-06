# -*- coding:utf-8 -*-

from flask import Blueprint
from flask import render_template

from apps.users.service.user import get_user_by_username

user_blueprint = Blueprint('user', __name__)


@user_blueprint.route('/login/', methods=('GET', 'POST',))
def login():
    """
    登录路由
    """
    return render_template('user/login.html')


@user_blueprint.route('/register/', methods=('GET', 'POST',))
def register():
    """
    注册路由
    """
    return render_template('user/register.html')


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

