# -*- coding:utf-8 -*-

from flask import Blueprint
from flask import render_template

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
