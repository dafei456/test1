from flask import Blueprint
from flask import render_template
from flask import request
from flask import redirect
from common.models.User import User
from common.libs.Helper import ops_render, iPagination
from common.libs.UrlManager import UrlManager
from application import app
from sqlalchemy import or_

route_account = Blueprint('account_page', __name__)


@route_account.route("/index")
def index():
    resp_data = {}

    # 接收args参数
    values = request.values

    # app.logger.info(values)

    # 当前页码，默认为1
    page = int(values['p']) if ('p' in values and values['p']) else 1

    # app.logger.info(page)

    query = User.query

    # 按搜索条件查询

    # 根据状态
    if 'status' in values and int(values['status']) > -1:
        # query = query.filter(User.status == int(values['status']))
        query = query.filter_by(status=int(values['status']))

    # 根据昵称或手机号
    if 'mix_kw' in values:
        rule = or_(User.nickname.ilike("%{}%".format(values['mix_kw'])),
                   User.mobile.ilike("%{}%".format(values['mix_kw'])))
        query = query.filter(rule)

    # 总记录数
    total = query.count()

    # full_path = request.full_path

    # app.logger.info(full_path)

    # 组装分页的参数
    page_params = {
        "total": total,
        "page_size": app.config['PAGE_SIZE'],
        "display": app.config['PAGE_DISPLAY'],
        "page": page,
        "url": request.full_path.replace("&p={}".format(page), "")   # 保证url值等于/account/index?
    }

    pages = iPagination(page_params)

    # 分页原理

    # SELECT 字段1, 字段2,… FROM 表名 LIMIT[起始数,] 记录数;
    # LIMIT后面可以跟两个参数，第一个参数表示起始数，如果起始数为0则从查询结果的第1条记录开始，
    # 如果为10则从查询结果的第11条记录开始，以次类推。起始位置为可选，如果不指定其默认值为0。
    # 第二个参数为记录条数表示返回查询记录的条数。

    limit = app.config['PAGE_SIZE']
    # 偏移量 = ( 当前页码 - 1 ) * limit
    offset = (page - 1) * limit

    lists = query.offset(offset).limit(limit).all()

    resp_data['lists'] = lists
    resp_data['pages'] = pages
    resp_data['search_values'] = values
    resp_data['status_mapping'] = app.config['STATUS_MAPPING']
    return ops_render("account/index.html", resp_data)


@route_account.route("/info")
def info():
    values = request.values

    app.logger.info(values)

    id = values['id'] if 'id' in values else None

    if id is None:
        return redirect(UrlManager.build_url("/account/index"))

    user = User.query.get(id)

    if user is None:
        return redirect(UrlManager.build_url("/account/index"))

    return render_template("account/info.html", data=user)


@route_account.route("/set")
def set():
    return render_template("account/set.html")
