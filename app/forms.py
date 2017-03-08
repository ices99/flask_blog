#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Created by PyCharm
# User: ices Email: 97598155@qq.com
# Date: 2017/3/8 12:34
# FileName：forms.py
# 

from flask_wtf import Form
from wtforms import TextField,BooleanField,PasswordField
from wtforms.validators import Required

class LoginForm(Form):
    name = TextField('Name', validators=[Required()])
    password = PasswordField('password', validators=[Required()])
    remember_me = BooleanField('remember_me', default=False)

