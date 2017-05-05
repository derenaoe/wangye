# -*- coding:utf-8 -*-
"""
与用户有关的业务操作
"""
from apps.ext import photos
from apps.user.dao.user import mongoengine_get_user_by_username
from apps.user.dao.user import mongoengine_get_user_by_id
from apps.user.dao.user import mongoengine_insert_user
from apps.user.dao.user import mongoengine_insert_picture
from apps.user.dao.user import mongoengine_get_pictures_by_username
from apps.user.dao.user import mongoengine_get_pictures_count_by_username
from apps.user.model.user import User
from apps.user.model.picture import Picture
from apps.utils.helps import get_uuid
from apps.utils.page import Page


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


def upload_picture(picture_form, picture_file, username):
    """
    上传图片 
    """
    picture = Picture()
    title = picture_form.title.data
    description = picture_form.description.data
    tag = picture_form.tag.data

    picture.init_picture(title=title, description=description, tag=tag, username=username)

    picture_url = save_picture(picture_file)
    picture.pict_ulr = picture_url

    return mongoengine_insert_picture(picture)


def save_picture(picture_file):
    """
    保存图片 
    """
    if not picture_file:
        return None
    picture_name = get_uuid() + '.'
    return photos.save(picture_file, name=picture_name[:1] + '/' + picture_name[1:2] + '/' + picture_name)


def get_user_pictures(username, page, num):
    """
    获取用户的图片
    """
    if not username:
        return None
    if page <= 0:
        page = 1

    count = mongoengine_get_pictures_count_by_username(username)
    if not count:
        return None

    pictures = mongoengine_get_pictures_by_username(username, page, num)

    new_pictures = []
    for picture in pictures:
        picture.pict_ulr = photos.url(picture.pict_ulr)
        new_pictures.append(picture)

    picture_page = Page(page=page, num=num, total=count, data=new_pictures)

    return picture_page
