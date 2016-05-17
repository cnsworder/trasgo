#!/usr/bin/env python

from flask import Flask
from apps.main import main_app

app = Flask(__name__, template_folder="../templates")
app.register_blueprint(main_app)
