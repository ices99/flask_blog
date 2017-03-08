#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Created by PyCharm
# User: ices Email: 97598155@qq.com
# Date: 2017/3/8 11:01
# FileName：__init__.py
# 
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)

from app import views, models
