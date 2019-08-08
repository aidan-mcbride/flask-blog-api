from flask import Flask

def create_app():
    """
    Creates an instance of Flask app
    """
    return Flask(__name__)
