#!/usr/bin/env python
# coding: utf-8

from flask import Blueprint
# from flask import request
# from flask import make_response
# from flask import render_template

main_app = Blueprint('main_app', __name__, template_folder="templates")

from apps.main import views
