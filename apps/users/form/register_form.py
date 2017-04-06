# -*- coding:utf-8 -*-
"""
登录表单
"""
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired, Length, EqualTo

from apps.users.service.user import get_user_by_username


class RegisterForm(FlaskForm):
    """
    用户注册表单
    """
    username = StringField('username', validators=[
        DataRequired('手机号码不能为空'),
        Length(min=6, max=16, message='用户名的长度为 6 到 16 位')])

    password = StringField('password', validators=[
        DataRequired('密码不能为空'),
        Length(min=6, max=32, message='密码的长度为 6 到 32 位')])

    re_password = StringField('re_password', validators=[
        DataRequired('请再次输入密码'),
        EqualTo('password', message='两次输入的密码不一致')
    ])

    def validate_username(self, field):
        """
        校验密码
        """
        username = self.username.data
        user = get_user_by_username(username=username)
        if user:
            raise ValueError('改用户名已被注册')
