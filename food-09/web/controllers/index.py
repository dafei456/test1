from flask import Blueprint
from flask import render_template

route_index = Blueprint('index_page', __name__)


# 后台首页
@route_index.route("/")
def index():
    return render_template("index/index.html")