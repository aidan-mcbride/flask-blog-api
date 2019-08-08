from flask import Flask

from . import controllers

def create_app():
    """
    Creates an instance of Flask app
    """
    app = Flask(__name__)

    controllers.init_app(app)

    return app
