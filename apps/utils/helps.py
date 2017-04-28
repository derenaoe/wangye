# -*- coding:utf-8 -*-
"""
工具模块
"""
import uuid


def get_uuid():
    """
    获取 uuid
    """
    this_uuid = uuid.uuid1()
    return str(this_uuid).replace('-', '')
