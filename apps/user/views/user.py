# -*- coding:utf-8 -*-

from flask import Blueprint
from flask import request
from flask import render_template
from flask import redirect
from flask import flash
from flask import url_for
from flask_login import login_user
from flask_login import logout_user
from flask_login import login_required
from flask_login import current_user

from apps.user.form.register_form import RegisterForm
from apps.user.form.login_form import LoginForm
from apps.user.form.picture_form import PictureForm
from apps.user.service.user import register_new_user
from apps.user.service.user import mongoengine_get_user_by_id
from apps.user.service.user import upload_picture
from apps.user.service.user import get_user_pictures

user_blueprint = Blueprint('user', __name__)


@user_blueprint.route('/login/', methods=('GET', 'POST',))
def login():
    """
    登录路由
    """
    if request.method == 'GET':
        return render_template('user/login.html')
    form = LoginForm(request.form)

    if form.validate_on_submit():
        login_user(form.user)
        if request.args.get('next'):
            return redirect(request.args.get('next'))
        return redirect('/')

    return render_template('user/login.html', form=form)


@user_blueprint.route('/register/', methods=('GET', 'POST',))
def register():
    """
    注册路由
    """
    if request.method == 'GET':
        return render_template('user/register.html')
    form = RegisterForm(request.form)

    if form.validate_on_submit():
        user = register_new_user(form)
        login_user(user)
        return redirect('/')

    return render_template('user/register.html', form=form)


@user_blueprint.route('/logout/', methods=('GET', 'POST',))
def logout():
    """
    用户登录
    """
    logout_user()
    return redirect('/')


@user_blueprint.route('/profile/', methods=('GET', 'POST',))
@user_blueprint.route('/profile/<int:page>', methods=('GET', 'POST',))
@login_required
def user_profile(page=1):
    """
    用户详情
    """
    user_id = current_user.id
    user = mongoengine_get_user_by_id(user_id)

    picture_page = get_user_pictures(user.username, page, 8)
    return render_template('test/personalpage.html', user=user, picture_page=picture_page)


@user_blueprint.route('/upload/picture/', methods=('GET', 'POST',))
@login_required
def user_upload_picture():
    """
    用户上传图片
    """
    if request.method == 'GET':
        return render_template('user/upload.html')

    form = PictureForm(request.form)

    if 'photo' not in request.files:
        flash('图片不能为空')
        return render_template('user/upload.html', form=form)

    if form.is_submitted():
        upload_picture(form, request.files['photo'], current_user.username)
        flash('上传成功')
        return redirect(url_for('user.user_upload_picture'))
    return render_template('user/upload.html', form=form)
