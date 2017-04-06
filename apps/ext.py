#coding=utf-8
"""
用于注册应用组件
"""
from flask_mongoengine import MongoEngine

# MongoEngine 组件
mongodb = MongoEngine()


def register_extensions(app):
    """
    注册组件
    """
    mongodb.init_app(app)
