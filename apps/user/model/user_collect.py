# -*- coding=utf-8 -*-
import time

from mongoengine import StringField, IntField, ObjectIdField

from apps.ext import mongodb

"""
用收藏的图片
"""

class UserCollectPicture(mongodb.Document):
    """
    图片模型
    """
    meta = {
        'collection': 'user_collect_pictures',
        'strict': False
    }
    title = StringField(name='title')
    description = StringField(name='description')
    pict_ulr = StringField(name='pict_url')
    tag = StringField(name='tag')
    collect_time = IntField(name='collect_time')
    username = StringField(name='username')
    create_time = IntField(name='create_time')
    collect_username = StringField(name='collect_username')
    p_id = ObjectIdField(name='p_id')

    def init_picture(self, picture, username):
        self.title = picture.title
        self.description = picture.description
        self.tag = picture.tag
        self.username = picture.username
        self.collect_time = int(time.time())
        self.create_time = picture.create_time
        self.collect_username = username
        self.p_id = picture.id
        self.pict_ulr = picture.pict_ulr
