#!/usr/bin/env python
# -*- coding: utf-8 -*-
# cnsworder<cnsworder@gmail.com>

from flask import Blueprint

admin_app = Blueprint("admin_app",
                      __name__,
                      url_prefix="admin")

from apps.admin import views
