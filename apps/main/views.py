#!/usr/bin/env python
# coding: UTF-8

from apps.main import main_app
from flask import render_template


@main_app.route("/main")
def main():
    name = "my"
    return render_template("main.html", name=name)
