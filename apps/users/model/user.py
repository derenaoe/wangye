# -*- coding:utf-8 -*-
"""
与用户有关的模型对象
"""
from mongoengine import StringField, IntField
from apps.ext import mongodb


class User(mongodb.Document):
    """
    用户模型
    """
    meta = {
        'collection': 'users',
        'strict': False
    }
    username = StringField(db_field='username')    # 用户名
    password = StringField(db_field='password')    # 密码
    mobile = IntField(db_field='mobile')    # 手机号
