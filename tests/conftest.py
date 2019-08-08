"""
Pytest configuration file:
Imported before any tests are run
contains global fixtures
"""

import pytest
from flask import Flask


@pytest.fixture
def app():
    """
    create instance of application
    """
    from api import create_app

    return create_app()
