#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Created by PyCharm
# User: ices Email: 97598155@qq.com
# Date: 2017/3/8 14:23
# FileName：db_upgrade.py
# 

from migrate.versioning import api
from config import SQLALCHEMY_DATABASE_URI
from config import SQLALCHEMY_MIGRATE_REPO

api.upgrade(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO)
print 'Current database version: ' + str(api.db_version(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO))