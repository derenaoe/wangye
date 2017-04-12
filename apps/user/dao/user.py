# -*- coding:utf-8 -*-
"""
用户模块的持久层操作
"""
from apps.user.model.user import User


def mongoengine_get_user_by_username(username):
    user = User.objects(username=username).first()
    return user


def mongoengine_insert_user(user):
    if user:
        return user.save()
    return None


def mongoengine_get_user_by_id(uid):
    user = User.objects(id=uid).first()
    return user