#!/usr/bin/env python
# -*- coding: utf-8 -*-

from app import app
from flask import render_template, flash, redirect
from .forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
        user = {'nickname': 'BenWhite'} #用户名
        posts = [ #提交内容
                {
                        'author': {'nickname': 'BenWhite'},
                        'body': 'Beautiful day in Beijing!'
                },
                {
                        'author': {'nickname': 'Susan'},
                        'body': 'The Avengers movie was so cool!'
                }
        ]

        return render_template('index.html',
                               title = 'Home',
                               user = user,
                               posts = posts)

@app.route('/login', methods = ['GET', 'POST'])
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
