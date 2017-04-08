# -*- coding:utf-8 -*-
"""
与用户有关的模型对象
"""
from mongoengine import StringField, IntField
from flask_login import UserMixin

from apps.ext import mongodb, bcrypt


class User(mongodb.Document, UserMixin):
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
    nickname = StringField(db_field='nickname')    # 昵称
    gender = StringField(db_field='gender')    # 性别

    def check_password(self, un_check_password):
        """
        校验密码
        """
        return bcrypt.check_password_hash(self.password, un_check_password)

    def encrypt_password(self):
        """
        加密密码
        """
        self.password = bcrypt.generate_password_hash(self.password, 10).decode('utf-8')

    def init_user(self, username, password, mobile=None):
        """
        初始用户
        """
        self.username = username
        self.password = password
        self.mobile = mobile
        self.encrypt_password()
