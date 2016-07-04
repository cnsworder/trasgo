#!/usr/bin/env python

import os
import logging

from datetime import datetime

from flask import Flask
from apps.main import main_app


logging.basicConfig(filename="logs/{0}.log".format(datetime.now().date()),
                    level=logging.DEBUG)


app = Flask(__name__,
            template_folder="../templates",
            static_folder="../static")
app.register_blueprint(main_app)
app.config['SECRET_KEY'] = os.urandom(24)

from apps import views
