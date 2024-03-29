from flask import Blueprint
from flask import render_template

route_member = Blueprint('member_page', __name__)


@route_member.route("/index")
def index():
    return render_template("member/index.html")


@route_member.route("/info")
def info():
    return render_template("member/info.html")


@route_member.route("/set")
def set():
    return render_template("member/set.html")


@route_member.route("/comment")
def comment():
    return render_template("member/comment.html")
