# -*- coding:utf-8 -*-
from apps import create_app

app = create_app('config.cfg')

if __name__ == '__main__':
    app.run()
