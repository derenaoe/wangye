# -*- coding:utf-8 -*-
"""
分页类
"""


class Page(object):

    def __init__(self, page, num, total, data):
        self.page = page
        self.num = num
        self.total = total
        self.items = data

    @property
    def pages(self):
        if self.total % self.num:
            return self.total // self.num + 1
        return self.total // self.num
