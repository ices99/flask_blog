#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Created by PyCharm
# User: ices Email: 97598155@qq.com
# Date: 2017/3/8 11:01
# FileName：views.py
# 
from flask import render_template,flash,redirect
from forms import LoginForm
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'Miguel'}
    posts = [
        {
            'author': {'nickname': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'nickname': 'Susan'},
            'body': 'The is a test'
        }
    ]
    return render_template("index.html",
                           title = 'Home',
                           user = user,
                           posts = posts)

@app.route('/login', methods= ['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for Name: ' + form.name.data)
        flash('passwd: ' + str(form.password.data))
        flash('remember_me: ' + str(form.remember_me.data))
        return redirect('/index')
    return render_template('login.html',
        title = 'Sign In',
        form = form)
