from flask import Flask

from . import controllers

# '-> Flask' indicates the type that this function should return
def create_app() -> Flask:
    """
    Creates an instance of Flask app
    """
    app = Flask(__name__)

    controllers.init_app(app)

    return app
