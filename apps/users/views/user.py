# -*- coding:utf-8 -*-

from flask import Blueprint
from flask import render_template

user_blueprint = Blueprint('user', __name__)


@user_blueprint.route('/login/', methods=('GET', 'POST',))
def login():
    return render_template('test/indexdenglu.html')
