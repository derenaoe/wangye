# -*- coding:utf-8 -*-
"""
用户模块的持久层操作
"""
from apps.users.model.user import User


def mongoengine_get_user_by_username(username):
    user = User.objects(username=username).first()
    return user
