import os

DEBUG = False
SQLALCHEMY_ECHO = False
SERVER_PORT = 8090

SEO_TITLE = "云猫订餐"
SUPPORT = "慕课吧"

JSON_AS_ASCII = False

# SECRET_KEY = os.urandom(24)

SECRET_KEY = "this is random string"

# session有效时间为7天
PERMANENT_SESSION_LIFETIME = 7 * 24 * 60 * 60

# 登录后需要忽视的URL
IGNORE_URLS = [
    "^/user/login"
]

# 登录前需要忽视的URL
IGNORE_CHECK_LOGIN_URLS = [
    "^/static"
]

PAGE_SIZE = 1

PAGE_DISPLAY = 10

STATUS_MAPPING = {
    "1": "正常",
    "0": "已删除"
}