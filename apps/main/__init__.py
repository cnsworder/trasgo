#!/usr/bin/env python
# coding: utf-8
# cnsworder<cnsworder@gmail.com>


from flask import Blueprint


main_app = Blueprint('main_app', __name__, template_folder="templates")


from apps.main import views
from apps.main import login
