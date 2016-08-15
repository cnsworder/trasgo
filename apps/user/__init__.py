#!/usr/bin/env python
# coding: utf-8
# cnsworder<cnsworder@gmail.com>


from flask import Blueprint


user_app = Blueprint('user_app', __name__, template_folder="templates")


from apps.user import views
