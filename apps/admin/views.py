#!/usr/bin/env python
# -*- coding: utf-8 -*-
# cnsworder<cnsworder@gmail.com>


from flask import redirect
from flask import render_template
from flask import url_for

from apps.admin import admin_app


def is_admin():
    return True


@admin_app.route("/admin")
def admin():
    if not is_admin():
        return redirect(url_for("not_admin"))
    return redirect(url_for("admin_apps.admin_main"))


@admin_app.route("/not_admin")
def not_admin():
    return render_template("not_admin.html")


@admin_app.route("/admin_main")
def admin_main():
    return render_template("admin_main.html")
