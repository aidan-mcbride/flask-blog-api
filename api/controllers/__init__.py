from flask import Flask


def init_app(app: Flask):
    """
    register blueprints
    """
    from .articles import articles
    app.register_blueprint(articles)
