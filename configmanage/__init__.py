from flask import Flask
from configmanage.controllers import *

def create_configmanage_app():
    app = Flask(__name__)
    app.config.from_pyfile('cmconfig.py')
    app.jinja_env.variable_start_string = '(('
    app.jinja_env.variable_end_string = '))'

    return app