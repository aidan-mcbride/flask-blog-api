"""
__init__.py
Contains APPLICATION FACTORY
Indicates that api directory is a python package
---
structure based on patrick's:
https://www.patricksoftwareblog.com/structuring-a-flask-project/
"""
from typing import Optional

from flask import Flask
from flask_sqlalchemy import SQLAlchemy  # type: ignore
from flask_marshmallow import Marshmallow

from . import controllers

# create instances of extensions
# instances are global, but are not yet attached to the app
db = SQLAlchemy()
ma = Marshmallow()

#################################
## ~*~ APPLICATION FACTORY ~*~ ##
#################################
def create_app(config_class: Optional[str] = None) -> Flask:
    # accept optional string for config class, default is None
    # return instance of Flask class
    """
    Creates an instance of Flask app
    """
    app = Flask(__name__)
    configure_app(config_class, app)
    initialize_extensions(app)

    # create database
    with app.app_context():
        db.create_all()

    # register blueprints in controllers
    controllers.init_app(app)

    return app


##########################
#### HELPER FUNCTIONS ####
##########################

# TODO: different name, other than 'helper functions'... blegh.


def configure_app(config_class: Optional[str], app: Flask):
    """
    set configuration for app
    use passed-in config class;
    otherwise, fallback to using FLASK_ENV to determine config
    """
    if config_class is None:
        config_class = app.config["ENV"]

    if config_class == "development":
        app.config.from_object("config.DevelopmentConfig")
    elif config_class == "testing":
        app.config.from_object("config.TestingConfig")
    else:
        app.config.from_object("config.ProductionConfig")


def initialize_extensions(app: Flask):
    """
    bind instances of extensions to flask app instance
    """
    db.init_app(app)
    ma.init_app(app)
