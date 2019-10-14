from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
import os
from common.libs.UrlManager import UrlManager


class Application(Flask):
    def __init__(self, import_name, template_folder=None, static_folder=None, root_path=None):
        super().__init__(import_name=import_name,
                         template_folder=template_folder,
                         root_path=root_path,
                         static_folder=static_folder)
        self.config.from_object("config.base_setting")
        self.config.from_object("config.local_setting")
        db.init_app(self)


db = SQLAlchemy()
# os.getcwd() 获取当前脚本所在的目录
app = Application(__name__,
                  template_folder=os.getcwd()+"/web/templates/",
                  static_folder=os.getcwd()+"/web/static",
                  root_path=os.getcwd())

manager = Manager(app)


"""注册函数模板"""

app.add_template_global(UrlManager.build_url, "buildUrl")
app.add_template_global(UrlManager.build_static_url, "buildStaticUrl")
