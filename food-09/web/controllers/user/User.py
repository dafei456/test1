from flask import Blueprint
from flask import render_template
from flask import request
from flask import jsonify
from flask import session
from flask import g
from flask import redirect
from common.models.User import User
from common.libs.UrlManager import UrlManager
from werkzeug.security import generate_password_hash, check_password_hash
from application import db

route_user = Blueprint("user_page", __name__)


# 登录
@route_user.route("/login", methods=['GET', 'POST'])
def login():
    response = {"result": 0, "reason": "登录成功！", "data": {}}

    if request.method == "GET":

        # 判断全局变量g中的current_user是否为None
        if g.current_user:
            # 如果不为None，说明已经登录了，则重定向到后台首页
            return redirect(UrlManager.build_url("/"))

        return render_template("user/login.html")

    login_name = request.values['login_name'] if 'login_name' in request.values else ''
    login_pwd = request.values['login_pwd'] if 'login_pwd' in request.values else ''

    # return "{}:{}".format(login_name, login_pwd)

    user = User.query.filter_by(login_name=login_name).first()

    # 判断是否登陆成功
    if user and check_password_hash(user.login_pwd, login_pwd):
        # 判断账户是否正常
        if user.status == 0:
            response['result'] = -1
            response['reason'] = "此账户暂停使用，请联系管理员！"
            return jsonify(response)

        # 如果账户是正常的，则保存登录账号的ID到session里面
        session['user_id'] = user.uid
        session.permanent = True  # 设置会话长期有效，默认有效期为31天
        return jsonify(response)
    else:
        response['result'] = -1
        response['reason'] = "账号或密码不对！"
        return jsonify(response)


# 编辑
@route_user.route("/edit", methods=['GET', 'POST'])
def edit():
    response = {"result": 0, "reason": "编辑成功！", "data": {}}
    if request.method == "GET":
        return render_template("user/edit.html", current_user={})

    values = request.values

    user_info = g.current_user
    user_info.moblie = values['moblie'] if 'moblie' in values else ''
    user_info.nickname = values['nickname'] if 'nickname' in values else ''
    user_info.email = values['email'] if 'email' in values else ''
    try:
        db.session.add(user_info)
        db.session.commit()
    except:
        response['result'] = -1
        response['reason'] = "编辑失败！"

    return jsonify(response)

# 修改密码
@route_user.route("/reset-pwd", methods=['GET', 'POST'])
def reset_pwd():
    response = {"result": 0, "reason": "修改密码成功！", "data": {}}
    if request.method == "GET":
        return render_template("user/reset_pwd.html")

    values = request.values
    old_password = values['old_password'] if 'old_password' in values else ''
    new_password = values['new_password'] if 'new_password' in values else ''

    user_info = g.current_user
    if not check_password_hash(user_info.login_pwd, old_password):
        response['result'] = -1
        response['reason'] = "原始密码不对！"
    else:
        user_info.login_pwd = generate_password_hash(new_password)
        db.session.add(user_info)
        db.session.commit()

    return jsonify(response)


# 退出
@route_user.route("/logout")
def logout():
    session.clear()
    return redirect(UrlManager.build_url("/user/login"))
