# -*- coding:utf-8 -*-
"""
用户模块的持久层操作
"""
from apps.user.model.user import User
from apps.user.model.picture import Picture
from apps.user.model.user_collect import UserCollectPicture


def mongoengine_get_user_by_username(username):
    """通过用户名获取用户"""
    user = User.objects(username=username).first()
    return user


def mongoengine_insert_user(user):
    """添加用户"""
    if user:
        return user.save()
    return None


def mongoengine_get_user_by_id(uid):
    """通过用户 id 获取用户"""
    user = User.objects(id=uid).first()
    return user


def mongoengine_insert_picture(picture):
    """插入图片"""
    if picture:
        return picture.save()
    return None


def mongoengine_get_pictures_by_username(username, page, num):
    """获取用户的所有图片"""
    return Picture.objects(username=username).order_by('-create_time').skip((page - 1) * num).limit(num)


def mongoengine_get_pictures_count_by_username(username):
    """获取用户的图片数量"""
    return Picture.objects(username=username).count()


def mongoengine_get_picture_by_username_and_pid(username, pid):
    """通过图片 id 获取图片"""
    return Picture.objects(username=username, id=pid).first()


def mongoengine_remove_picture_by_pid(pid):
    """删除图片"""
    return Picture.objects(id=pid).delete()


def mongoengine_get_index_picture(page, num):
    """获取首页的图片"""
    return Picture.objects().order_by('-create_time').skip((page - 1) * num).limit(num)


def mongoengine_get_picture_by_keyword(page, num, keyword):
    """
    通过关键字获取图片
    """
    return Picture.objects(title__icontains=keyword).order_by('-create_time').skip((page - 1) * num).limit(num)


def mongoengine_get_picture_by_id(pid):
    """通过图片 id 获取图片"""
    return Picture.objects(id=pid).first()


def mongoengine_save_collect_picture(picture, username):
    """
    收藏图片
    """
    collectPicture = UserCollectPicture()
    collectPicture.init_picture(picture, username)
    return collectPicture.save()


def mongoengine_get_collect_picture_by_pid(p_id, username):
    """
    收藏图片
    """
    return UserCollectPicture.objects(p_id=p_id, collect_username=username).first()


def mongoengine_get_collect_picture_by_id(p_id, username):
    """
    收藏图片
    """
    return UserCollectPicture.objects(id=p_id, collect_username=username).first()


def mongoengine_get_collect_pictures_by_username(username, page, num):
    """
    获取收藏图片
    """
    return UserCollectPicture.objects(collect_username=username).order_by('-collect_time')\
        .skip((page - 1) * num).limit(num)


def mongoengine_get_collect_pictures_count_by_username(username):
    """
    获取收藏图片的数量
    """
    return UserCollectPicture.objects(collect_username=username).count()


def mongoengine_delete_collect_picture(picture):
    """
    删除图片
    """
    return UserCollectPicture.objects(id=picture.id).delete()
