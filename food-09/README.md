# Flask构建订餐小程序系统

* 打造一个高可用Flask MVC框架

```
|——application.py  定义和创建Flask应用实例

|——common
        |——libs    公共函数、公共类
        |——models  模型        
        
|——config
        |——base_setting.py   基础配置文件
        |——local_setting.py  本地环境配置文件
        
|——manager.py  命令行脚本文件

|——README.md   项目说明文档

|——requirements.txt   Python环境依赖包

|——web
       |——controlles  控制器（蓝图文件）
       |——static      静态资源
       |——templates   模板   
       
|——www.py  统一注册蓝图的文件
```
        
* 点餐系统后台页面搭建
    * 链接管理器和版本管理
    
* 点餐小程序前台界面搭建

* 后台管理账号模块开发（登录、编辑、修改密码、退出）
    * 导入数据库文件
    * 后台初始账户
    * 利用flask-sqlacodegen快速生成ORM类
    
    ``` 
    1.pip install flask-sqlacodegen
    
    2.执行flask-sqlacodegen命令
    
    flask-sqlacodegen "mysql+pymysql://root:hao123@192.168.92.129:3306/food_db" --tables user --outfile "common/models/User.py" --flask
    
    3.修改自动生成的model中的db变量
    
    from application import db
    
    ```
    
    
## 启动

* python manager.py runserver

## 思考题

* 用户登录后，停在页面1小时不操作，则强制退出