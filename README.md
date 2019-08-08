# flask-blog-api

[![Build Status](https://travis-ci.org/dbanty/python-rest.svg?branch=master)](https://travis-ci.org/dbanty/python-rest)[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)

Simple RESTful api for a simple blog built in Flask; Meant as a learning instrument.

### Tests
All tests are contained in the directory `tests/`. There is a corresponding test file for each controller file.

To run all pytest tests from the project's root directory:
```shell
python -m pytest
```

---

### Stack/Dependencies
* [Pipenv](https://github.com/pypa/pipenv)
* [Flask](https://flask.palletsprojects.com/en/1.1.x/)
* **Continuous Integration**
  * [Travis CI](https://travis-ci.org/)
  * [PyTest](https://pytest.org/en/latest/)
  * [Black](https://github.com/ambv/black)
  * [Safety](https://pyup.io/safety/)

### References
* [Dylan Anthony - Flask REST API tutorial](https://dev.to/dbanty/python-rest-api-flask-basics-3ffn)

---

## Development Notes

### *To-Do List:*

- [ ] [Refactor unit tests to match Eric Elliott style.](https://medium.com/javascript-scene/behavior-driven-development-bdd-and-functional-testing-62084ad7f1f2)
- [ ] Add scalable configuration.
  - [ ] Add configuration for development, testing, production.

### Continuous Integration

>  For this project I will be using TravisCI, since that is what the tutorial I am following uses and I do not yet know enough about CI to make my own decisions.
>  For future projects - and perhaps as a later refactor of this project - I will use GitLab CI, since we already use GitLab internally for other things.
>  I have also found that doing the same thing in two different systems gives you a better understanding of whatever it is you are doing, so it serves the goal of learning to do CI both in TravisCI and in GitLabCI.

#### [Travis CI](https://travis-ci.org/)

* Will automatically build and test committed changes to a GitHub repository.
* Testing specifications are listed in a **`.travis.tml`** file in the root of the project.