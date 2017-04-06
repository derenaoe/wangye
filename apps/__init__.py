# -*- coding=utf-8 -*-
"""
初始化 app
"""
from flask import Flask

from apps.ext import register_extensions


def register_blueprints(app):
    """
    加载蓝图
    """
    from apps.index.views.index import index_blueprint
    from apps.users.views.user import user_blueprint

    app.register_blueprint(index_blueprint)
    app.register_blueprint(user_blueprint, url_prefix='/user')


def create_app(cfg):
    """
    初始化系统
    """
    # 初始化 Flask app
    app = Flask(__name__)

    # 加载配置文件
    app.config.from_pyfile(cfg)

    # 注册组件
    register_extensions(app)

    # 注册蓝图
    register_blueprints(app)

    # 处理静态文件
    if app.has_static_folder:
        app.add_url_rule(app.static_url_path + '/<path:filename>', endpoint='static', view_func=app.send_static_file)

    return app

