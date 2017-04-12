# -*- coding:utf-8 -*-
"""
用于注册应用组件
"""
from flask_mongoengine import MongoEngine
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
from flask_wtf import CSRFProtect

# MongoEngine 组件
mongodb = MongoEngine()

# flask_login 组件
login_manager = LoginManager()

# 加密组件
bcrypt = Bcrypt()

# csrf 组件
csrf = CSRFProtect()


def register_extensions(app):
    """
    注册组件
    """
    # mongoengine
    mongodb.init_app(app)

    # 加密
    bcrypt.init_app(app)

    # flask_login
    login_manager.init_app(app)

    # csrf 保护
    csrf.init_app(app)

    # 登录回调函数
    @login_manager.user_loader
    def load_user(user_id):
        from apps.user.model.user import User
        return User.objects(id=user_id).first()

    # 登录入口
    login_manager.login_view = '/user/login/'
