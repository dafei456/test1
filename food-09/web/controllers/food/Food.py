from flask import Blueprint
from flask import render_template

route_food = Blueprint('food_page', __name__)


@route_food.route("/index")
def index():
    return render_template("food/index.html")


@route_food.route("/info")
def info():
    return render_template("food/info.html")


@route_food.route("/set")
def set():
    return render_template("food/set.html")


@route_food.route("/cat")
def cat():
    return render_template("food/cat.html")


@route_food.route("/cat-set")
def cat_set():
    return render_template("food/cat_set.html")
