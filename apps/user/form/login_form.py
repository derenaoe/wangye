# -*- coding:utf-8 -*-
"""
登录表单
"""
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired, Length, Regexp


from apps.user.service.user import get_user_by_username


class LoginForm(FlaskForm):
    """
    用户登录表单
    """
    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.user = None

    username = StringField('username', validators=[
        DataRequired('手机号码不能为空'),
        Length(min=6, max=16, message='用户名的长度为 6 到 16 位'),
        Regexp(regex='^[a-zA-Z][a-zA-z0-9-_]+', message='用户名格式错误')])
    password = StringField('password', validators=[
        DataRequired('密码不能为空'),
        Length(min=6, max=32, message='密码的长度为 6 到 32 位')])

    def validate_password(self, field):
        """
        校验密码
        """
        username = self.username.data
        password = self.password.data
        user = get_user_by_username(username)
        if user:
            if user.check_password(password):
                self.user = user
                return user
        raise ValueError('用户名或密码错误')
