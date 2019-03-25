#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-03-25 20:40
# @Author  : LUO YING
# @Site    : 
# @File    : __init__.py.py
# @Detail    :

import os
from flask import Flask
from . import db
from . import auth
from . import blog

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    db.init_app(app)
    app.register_blueprint(auth.bp)
    app.register_blueprint(blog.bp)
    app.add_url_rule('/', endpoint='index')

    """
    instance_relative_config=True 告诉应用配置文件是相对于 instance folder 的相对路径。实例文件夹在 flaskr 包的外面，
    用于存放本地数据（例如配置密钥和数据库），不应当 提交到版本控制系统

    """
    app.config.from_mapping(
        SECRET_KEY='dev',

        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )
    """
           SECRET_KEY 是被 Flask 和扩展用于保证数据安全的。在开发过程中， 为了方便可以设置为 'dev' ，
           但是在发布的时候应当使用一个随机值来 重载它。
    """

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

        # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

        # a simple page that says hello

    @app.route('/hello')
    def hello():
        return 'Hello, World!'


    return app
