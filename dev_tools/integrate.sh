#!/bin/bash
# runs continuous integration script from .travis.yml
# so you can see the output without committing any changes,
pipenv run safety check
pipenv run black . --check
pipenv run mypy api
pipenv run python -m pytest
echo "INTEGRATE.SH COMPLETE"
