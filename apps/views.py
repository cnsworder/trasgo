#!/usr/bin/env python
# -*- coding: utf-8 -*-

from apps import app
from flask import redirect, url_for, session, render_template


@app.route("/")
def main():
    if "user" in session:
        return redirect(url_for("main_app.main"))
    else:
        return redirect(url_for("login"))


@app.route("/login")
def login():
    return render_template("login.html")


@app.route("/auth", methods=["POST"])
def author():
    session['user'] = "User"
    if True:
        return redirect(url_for("main_app.main"))
    else:
        return redirect(url_for("login"))
