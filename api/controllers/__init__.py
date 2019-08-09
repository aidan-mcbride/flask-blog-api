from flask import Flask


def init_app(app: Flask):
    """
    register blueprints
    """
    from .root import root

    app.register_blueprint(root)
