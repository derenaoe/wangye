# -*- coding:utf-8 -*-

from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired


class PictureForm(FlaskForm):
    """
    图片表单
    """
    title = StringField('title', validators=[DataRequired('标题不能为空')])
    description = StringField('description')
    tag = StringField('tag')
