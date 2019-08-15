# Flask Blog API

[![Build Status](https://travis-ci.org/dbanty/python-rest.svg?branch=master)](https://travis-ci.org/dbanty/python-rest) [![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black) [![Checked with mypy](http://www.mypy-lang.org/static/mypy_badge.svg)](http://mypy-lang.org/)

Simple REST-ful-ish api built in flask; built as a learning project to learn the basics of CI, as well as to create a project to use for learning docker for flask apps.

Contains a collection of articles(blog posts), and supports GET, POST, PUT, and DELETE requests. Includes **continuous integration** with **Travis CI** and has a full suite of tests with **PyTest**.

---

#### Installation
```shell
pip install pipenv  # if not already installed
pipenv install
```

#### To Run
```shell
export FLASK_APP=api
export FLASK_ENV=development
pipenv run flask run
```

#### Tests
All tests are contained in the directory `tests/`. There is a corresponding test file for each controller file.

To run all pytest tests from the project's root directory:
```shell
pipenv run python -m pytest
```

Tests were written based on [this official flask guide.](https://flask.palletsprojects.com/en/1.1.x/testing/)

#### Other Useful Commands

```shell
pipenv shell			# activate virtual environment
(env)$ exit				# exit current virtual environment

pipenv run mypy api		# static type check
pipenv run black <dir>	# format all code in <dir> with black

# TOOL BASH SCRIPTS
tools/quicktest.sh		# format w/ black, run mypy, pytest
tools/integrate.sh		# runs same scripts as .travis.yml
```

---

### Stack/Dependencies
* [Pipenv](https://github.com/pypa/pipenv)
* [Flask](https://flask.palletsprojects.com/en/1.1.x/)
  * [Flask-sqlalchemy](https://flask-sqlalchemy.palletsprojects.com/en/2.x/)
  * [Flask-marshmallow](https://flask-marshmallow.readthedocs.io/en/latest/)
    * [Marshmallow](https://marshmallow.readthedocs.io/en/3.0/)
  * [marshmallow-sqlalchemy](https://marshmallow-sqlalchemy.readthedocs.io/en/latest/)
* [SQLite3](https://sqlite.org/index.html)
* **Continuous Integration**
  * [Travis CI](https://travis-ci.org/)
  * [PyTest](https://pytest.org/en/latest/)
  * [Black](https://github.com/ambv/black)
  * [Safety](https://pyup.io/safety/)

### References
* [Dylan Anthony - Flask REST API tutorial](https://dev.to/dbanty/python-rest-api-flask-basics-3ffn)
* [Vincent Marcal - Dockerize a flask app](https://www.vicentemarcal.com/2019/03/05/dockerize-a-flask-app/)
