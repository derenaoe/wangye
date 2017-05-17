# -*- coding:utf-8 -*-

from flask import Blueprint, current_app
from flask import render_template, jsonify
from apps.user.service.user import get_index_picture

index_blueprint = Blueprint('index', __name__)


@index_blueprint.route('/')
def index():
    per_page = current_app.config.get('PER_PAGE', 12)
    index_pictures = get_index_picture(1, per_page)
    return render_template('index/index.html', index_pictures=index_pictures, page=1)

@index_blueprint.route('/pictures/<int:page>')
def index_json(page=1):

    per_page = current_app.config.get('PER_PAGE', 12)
    index_pictures = get_index_picture(page, per_page)
    return jsonify(index_pictures)

