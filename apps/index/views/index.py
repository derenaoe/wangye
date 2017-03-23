# -*- coding:utf-8 -*-

from flask import Blueprint
from flask import render_template

index_blueprint = Blueprint('index', __name__)


@index_blueprint.route('/')
def index():
    return render_template('test/index.html')
