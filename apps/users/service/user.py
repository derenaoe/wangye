# -*- coding:utf-8 -*-
"""
与用户有关的业务操作
"""
from apps.users.dao.user import mongoengine_get_user_by_username


def get_user_by_username(username):
    """
    通过用户名获取用户
    """
    return mongoengine_get_user_by_username(username)
