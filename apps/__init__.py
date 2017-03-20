# -*- coding=utf-8 -*-
"""
初始化 app
"""
from flask import Flask


def create_app(cfg):
    """
    初始化系统
    """

    # 初始化 Flask app
    app = Flask(__name__)

    # 加载配置文件
    app.config.from_pyfile(cfg)
    return app
