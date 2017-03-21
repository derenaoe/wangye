# -*- coding:utf-8 -*-

from flask import Blueprint

index_blueprint = Blueprint('index', __name__)


@index_blueprint.route('/')
def index():
    return '你好, 这是 wangye 的首页'
