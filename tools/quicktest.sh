#!/bin/bash
# runs mypy, pytest, and formats with black
pipenv run black .
pipenv run mypy api
pipenv run python -m pytest
