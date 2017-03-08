#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Created by PyCharm
# User: ices Email: 97598155@qq.com
# Date: 2017/3/8 13:36
# FileName：db_create.py
#

from migrate.versioning import api
from config import SQLALCHEMY_DATABASE_URI
from config import SQLALCHEMY_MIGRATE_REPO
from app import db
import os.path

db.create_all()
# 当数据库不存在的时候创建新的数据库
if not os.path.exists(SQLALCHEMY_MIGRATE_REPO):
    api.create(SQLALCHEMY_MIGRATE_REPO, 'database repository')
    api.version_control(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO)
# 否则直接更新
else:
    api.version_control(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO, api.version(SQLALCHEMY_MIGRATE_REPO))