DEBUG = True
SQLALCHEMY_ECHO = True

DIALECT = 'mysql'  # 数据库类型
DRIVER = 'pymysql'  # 数据库驱动
USERNAME = 'root'  # 用户名
PASSWORD = 'hao123'  # 密码
HOST = '192.168.92.129'  # 服务器
PORT = '3306'  # 端口
DATABASE = 'food_db'  # 数据库名
CHARSET = 'utf8mb4'

SQLALCHEMY_DATABASE_URI = "{}+{}://{}:{}@{}:{}/{}?charset={}".format(DIALECT,
                                                                     DRIVER,
                                                                     USERNAME,
                                                                     PASSWORD,
                                                                     HOST,
                                                                     PORT,
                                                                     DATABASE,
                                                                     CHARSET)
SQLALCHEMY_TRACK_MODIFICATIONS = False