# -*- coding:utf-8 -*-
"""
与用户有关的业务操作
"""
from apps.user.dao.user import mongoengine_get_user_by_username
from apps.user.dao.user import mongoengine_get_user_by_id
from apps.user.dao.user import mongoengine_insert_user
from apps.user.model.user import User


def get_user_by_username(username):
    """
    通过用户名获取用户
    """
    return mongoengine_get_user_by_username(username)


def get_user_by_id(uid):
    """
    通过 id 获取用户
    """
    return mongoengine_get_user_by_id(uid)


def register_new_user(register_form):
    """
    用户注册
    """
    user = User()
    username = register_form.username.data
    password = register_form.password.data

    if username and password:
        user.init_user(username, password)
        return mongoengine_insert_user(user)
    return None
