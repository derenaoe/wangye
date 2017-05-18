# -*- coding:utf-8 -*-

from flask import Blueprint, current_app
from flask import request, redirect, flash
from flask import render_template, jsonify
from apps.user.service.user import get_index_picture
from apps.user.service.user import get_picture_by_keyword

index_blueprint = Blueprint('index', __name__)


@index_blueprint.route('/')
def index():
    """
    首页
    """
    per_page = current_app.config.get('PER_PAGE', 12)
    index_pictures = get_index_picture(1, per_page)
    return render_template('index/index.html', index_pictures=index_pictures, page=1)


@index_blueprint.route('/pictures/<int:page>')
def index_json(page=1):
    """
    获取所有图片的 json 数据
    """
    per_page = current_app.config.get('PER_PAGE', 12)
    index_pictures = get_index_picture(page, per_page)
    return jsonify(index_pictures)


@index_blueprint.route('/pictures/search/')
def index_search():
    """
    搜索图片
    """
    per_page = current_app.config.get('PER_PAGE', 12)
    keyword = request.args.get('keyword')
    if not keyword or not keyword.replace(' ', ''):
        flash('关键字不能为空！')
        return redirect('/')
    pictures = get_picture_by_keyword(1, per_page, keyword)
    return render_template('index/index.html', index_pictures=pictures, page=1, keyword=keyword)


@index_blueprint.route('/pictures/search/json/<int:page>')
def index_search_json(page=1):
    """
    搜索图片
    """
    per_page = current_app.config.get('PER_PAGE', 12)
    keyword = request.args.get('keyword')
    if not keyword or not keyword.replace(' ', ''):
        return jsonify([])
    pictures = get_picture_by_keyword(page, per_page, keyword)
    return jsonify(pictures)
