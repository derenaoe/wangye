# -*- coding:utf-8 -*-

from flask import Blueprint
from flask import request
from flask import render_template
from flask import redirect
from flask import flash
from flask import url_for
from flask import jsonify
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
from apps.user.service.user import get_user_picture
from apps.user.service.user import remove_user_picture
from apps.user.service.user import get_picture_by_id
from apps.user.service.user import get_collect_picture_by_pid
from apps.user.service.user import get_collect_picture_by_id
from apps.user.service.user import collect_picture
from apps.user.service.user import delete_collect_picture
from apps.user.service.user import get_collect_pictures_by_username

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
    用户登出
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
    return render_template('user/personalpage.html', user=user, picture_page=picture_page)


@user_blueprint.route('/upload/picture/', methods=('GET', 'POST',))
@login_required
def user_upload_picture():
    """
    用户上传图片
    """
    if request.method == 'GET':
        return render_template('user/upload.html')

    form = PictureForm(request.form)

    if 'photo' not in request.files or not request.files['photo']:
        flash('图片不能为空')
        return render_template('user/upload.html', form=form)

    if form.is_submitted():
        upload_picture(form, request.files['photo'], current_user.username)
        flash('上传成功')
        return redirect(url_for('user.user_upload_picture'))
    return render_template('user/upload.html', form=form)


@user_blueprint.route('/delete/picture/', methods=('POST',))
@login_required
def user_delete_picture():
    """
    用户删除图片
    """
    picture_id = request.form.get('p_id')
    username = current_user.username
    picture = get_user_picture(username, picture_id)

    if not picture_id or not picture:
        flash("没有该图片!")
    else:
        remove_user_picture(picture.id)
        flash('删除成功')
    return redirect(url_for('user.user_profile'))


@user_blueprint.route('/collect/picture/', methods=('POST',))
@login_required
def user_collect_picture():
    """
    收藏图片
    """
    p_id = request.form.get('p_id')

    picture = get_picture_by_id(p_id)
    if not picture:
        return jsonify({'code': 202, 'msg': '查无此图片！'})

    username = current_user.username
    if picture.username == username:
        return jsonify({'code': 202, 'msg': '不能收藏自己的图片！'})

    this_picture = get_collect_picture_by_pid(p_id, username)
    if this_picture:
        return jsonify({'code': 202, 'msg': '你已经收藏了这个商品！'})

    collect_picture(picture, username)

    return jsonify({'code': 200, 'msg': '收藏成功！'})


@user_blueprint.route('/profile/collect/pictures/', methods=('GET',))
@user_blueprint.route('/profile/collect/pictures/<int:page>', methods=('GET',))
@login_required
def user_get_collect_pictures(page=1):
    """
    获取收藏的图片
    """
    username = current_user.username
    user_id = current_user.id
    user = mongoengine_get_user_by_id(user_id)

    picture_page = get_collect_pictures_by_username(username, page,8)

    return render_template('user/personalpage.html', user=user, picture_page=picture_page, type='collect')


@user_blueprint.route('/delete/collect/picture/', methods=('POST',))
def user_remove_collect_picture():
    """
    删除收藏
    """
    username = current_user.username
    p_id = request.form.get('p_id')

    picture = get_collect_picture_by_id(p_id, username)

    print(picture)
    if not p_id or not picture:
        flash('你没有收藏这张图片！')
        return redirect(url_for('user.user_get_collect_pictures'))

    delete_collect_picture(picture)
    flash('删除收藏图片成功！')
    return redirect(url_for('user.user_get_collect_pictures'))
