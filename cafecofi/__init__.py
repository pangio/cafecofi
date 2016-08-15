from flask import Flask, redirect, request, abort, send_from_directory
from flask.ext.babel import Babel
from flask.ext.sqlalchemy import SQLAlchemy

import os

# Config and App setups
app = Flask(__name__, static_folder='static')
app.config.from_object('config-default')
app.config.update(dict(
    PREFERRED_URL_SCHEME='https'
))
app.debug = app.config.get('DEBUG')

# Initalize DB object
db = SQLAlchemy(app)

babel = Babel(app)


# Initalize Bcrypt object for password hashing
# bcrypt = Bcrypt(app)

# Initalize flask mail object for email notifications
# flask_mail = Mail(app)

# Import all models
from models import *

#  Import all views here
from views import *

# @app.after_request
# def after_request(response):
#     response.headers.add('Access-Control-Allow-Origin', '*')
#     response.headers.add('Access-Control-Allow-Methods', 'GET,POST')
#     return response


# # Route to serve static asset files via Flask
# @app.route('/static/<filename>')
# def send_js(filename):
#     return send_from_directory(app.static_folder, filename)


# @app.route('/favicon.ico')
# def favicon():
#     return send_from_directory(os.path.join(app.root_path, 'static'),
#                                'favicon.ico', mimetype='image/vnd.microsoft.icon')

