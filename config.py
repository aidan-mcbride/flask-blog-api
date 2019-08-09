"""
config.py
"""


class Config(object):
    """
    Base Config: All other configs override this
    """

    DEBUG = False  # default to false as failsafe
    TESTING = False

    SQLALCHEMY_DATABASE_URI = "sqlite:///../flask_blog_api.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = False


class ProductionConfig(Config):
    """
    Production Config
    simply inherits base class
    """

    pass


class DevelopmentConfig(Config):
    """
    Development Config
    """

    DEBUG = True


class TestingConfig(Config):
    """
    Testing Config
    """

    TESTING = True

    SQLALCHEMY_DATABASE_URI = "sqlite:///../flask_blog_api_testing.db"
