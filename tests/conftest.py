"""
Pytest configuration file:
Imported before any tests are run
contains global fixtures
"""

import pytest
from flask import Flask
from api import create_app, db


@pytest.fixture
def client():
    """
    create instance of flask app with test client
    """
    flask_app = create_app("testing")
    test_client = flask_app.test_client()

    # create app context
    ctx = flask_app.app_context()
    ctx.push()

    yield test_client
    """
    TESTS RUN HERE
    """

    ctx.pop()


@pytest.fixture
def database():
    db.create_all()

    yield db
    """
    TESTS RUN HERE
    """

    db.drop_all()
