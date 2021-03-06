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
from apps.user.dao.user import mongoengine_get_picture_by_username_and_pid
from apps.user.dao.user import mongoengine_remove_picture_by_pid
from apps.user.dao.user import mongoengine_get_index_picture
from apps.user.dao.user import mongoengine_get_picture_by_keyword
from apps.user.dao.user import mongoengine_get_picture_by_id
from apps.user.dao.user import mongoengine_save_collect_picture
from apps.user.dao.user import mongoengine_get_collect_picture_by_pid
from apps.user.dao.user import mongoengine_get_collect_picture_by_id
from apps.user.dao.user import mongoengine_get_collect_pictures_by_username
from apps.user.dao.user import mongoengine_get_collect_pictures_count_by_username
from apps.user.dao.user import mongoengine_delete_collect_picture
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

    new_pictures = get_pictures_url(pictures)

    picture_page = Page(page=page, num=num, total=count, data=new_pictures)

    return picture_page


def get_user_picture(username, pid):
    """通过图片 id 获取用户的一张图片"""
    if pid:
        return mongoengine_get_picture_by_username_and_pid(username, pid)
    return None


def get_pictures_url(pictures):
    """获取图片的路径"""
    new_pictures = []
    for picture in pictures:
        picture.pict_ulr = photos.url(picture.pict_ulr)
        new_pictures.append(picture)
    return new_pictures


def remove_user_picture(pid):
    """删除图片"""
    if pid:
        return mongoengine_remove_picture_by_pid(pid)
    return None


def get_index_picture(page, num):
    """
    获取首页的图片
    """
    if not page or page < 1:
        page = 1

    pictures = mongoengine_get_index_picture(page, num)

    new_pictures = get_pictures_url(pictures)

    return new_pictures


def get_picture_by_keyword(page, num, keyword):
    """
    搜索图片
    """
    if not page or page < 1:
        page = 1

    pictures = mongoengine_get_picture_by_keyword(page, num, keyword)
    new_pictures = get_pictures_url(pictures)
    return new_pictures


def get_picture_by_id(p_id):
    """
    通过图片 id 获取图片
    """
    if not p_id:
        return None
    return mongoengine_get_picture_by_id(p_id)


def collect_picture(picture, username):
    """
    收藏图片
    """
    return mongoengine_save_collect_picture(picture, username)


def get_collect_picture_by_pid(p_id, username):
    """
    获取收藏图片
    """
    if not p_id or not username:
        return None
    return mongoengine_get_collect_picture_by_pid(p_id, username)


def get_collect_picture_by_id(p_id, username):
    """
    获取收藏图片
    """
    if not p_id or not username:
        return None
    return mongoengine_get_collect_picture_by_id(p_id, username)


def get_collect_pictures_by_username(username, page, num):
    """
    获取用户收藏的图片
    """
    if not page or page < 1:
        page = 1

    count = mongoengine_get_collect_pictures_count_by_username(username)
    if not count:
        return None

    pictures =  mongoengine_get_collect_pictures_by_username(username, page, num)

    new_pictures = get_pictures_url(pictures)

    picture_page = Page(page=page, num=num, total=count, data=new_pictures)

    return picture_page


def delete_collect_picture(picture):
    """
    删除收藏图片
    """
    return mongoengine_delete_collect_picture(picture)
