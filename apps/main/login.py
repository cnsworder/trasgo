#!/bin/env pythob
# -*- coding: utf-8 -*-
# cnsworder<cnsworder@gmail.com>


from flask import request
from flask import session

from apps.main import main_app


@main_app.route("/login", methods=['POST'])
def login():
    user = request.args.get("user", "")
    passwd = request.args.get("passwd", "")

    if user == '':
        return False
    if passwd == '':
        return False

    session["user"] = user

    return True


@main_app.route("/logout")
def logout():
    del session["user"]


# 是否已经登录
def is_login():
    return True if session["user"] else False
