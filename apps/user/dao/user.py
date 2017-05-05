# -*- coding:utf-8 -*-
"""
用户模块的持久层操作
"""
from apps.user.model.user import User
from apps.user.model.picture import Picture


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


def mongoengine_insert_picture(picture):
    if picture:
        return picture.save()
    return None


def mongoengine_get_pictures_by_username(username, page, num):
    return Picture.objects(username=username).order_by('-create_time').skip((page - 1) * num).limit(num)


def mongoengine_get_pictures_count_by_username(username):
    return Picture.objects(username=username).count()
