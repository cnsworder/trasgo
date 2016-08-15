#!/usr/bin/env python
# coding: UTF-8

from flask import render_template
from flask import request
from flask import jsonify


from apps.user import user_app
from apps.data.transgodatabase import User
from apps.data.transgodatabase import make_session


@user_app.route("/add_user")
def add_user():
    return render_template("add_user.html")


@user_app.route("/insert_user", methods=["POST"])
def insert_user():
    user_name = request.form["name"]
    user_id = request.form["user_id"]
    user_type = request.form["user_type"]
    user_passwd = request.form["user_passwd"]

    user = User(user_id, user_name, user_type, user_passwd)

    try:
        session = make_session()
        session.add(user)
        session.commit()
    except Exception as e:
        print(e.message)
        session.rollback()
        return jsonify(result=False)

    return jsonify(result=True)
