# 后台权限统一拦截器

from common.models.User import User
from application import app
from flask import session
from flask import request
from flask import g
from flask import redirect
from common.libs.UrlManager import UrlManager
import re

# 使用before_request来做权限和用户检查


@app.before_request
def before_request():

    ignore_urls = app.config['IGNORE_URLS']

    ignore_check_login_urls = app.config['IGNORE_CHECK_LOGIN_URLS']

    path = request.path

    # app.logger.debug(path)

    pattern = re.compile("|".join(ignore_check_login_urls))

    if pattern.match(path):
        return

    # 判断是否登录
    user_info = check_login()

    g.current_user = None

    if user_info:
        # 如果已经登录，则将用户数据存储到全局变量g里面的current_user
        g.current_user = user_info

    # 忽视/user/login请求
    pattern = re.compile("|".join(ignore_urls))

    if pattern.match(path):
        return

    # 如果没有登录，则重定向到登录页
    if not user_info:
        return redirect(UrlManager.build_url("/user/login"))

    return


"""判断用户是否登录"""


def check_login():
    user_id = session['user_id'] if 'user_id' in session else None

    if user_id is None:
        return False

    try:
        # 根据user_id查询登录用户的数据
        user_info = User.query.get(user_id)
    except Exception as e:
        return False

    if user_info is None:
        return False

    if user_info.status != 1:
        return False

    return user_info

