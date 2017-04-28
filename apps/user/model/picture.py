# -*- coding:utf-8 -*-
import time

from mongoengine import StringField, IntField

from apps.ext import mongodb


class Picture(mongodb.Document):
    """
    图片模型
    """
    meta = {
        'collection': 'pictures',
        'strict': False
    }
    title = StringField(name='title')
    description = StringField(name='description')
    pict_ulr = StringField(name='pict_url')
    tag = StringField(name='tag')
    create_time = IntField(name='create_time')
    username = StringField(name='username')

    def init_picture(self, title, description, tag, username):
        self.title = title
        self.description = description
        self.tag = tag
        self.username = username
        self.create_time = int(time.time())
