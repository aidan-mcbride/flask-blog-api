from flask import Flask


def init_app(app: Flask):
    """
    register blueprints
    """
    from .articles import articles
    from .root import root

    app.register_blueprint(articles)
    app.register_blueprint(root)
