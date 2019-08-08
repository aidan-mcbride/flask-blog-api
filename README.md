# flask-blog-api
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
* [PyTest](https://pytest.org/en/latest/)

### References
* [Dylan Anthony - Flask REST API tutorial](https://dev.to/dbanty/python-rest-api-flask-basics-3ffn)

---

### Development Notes

#### To-Do List:

- [ ] [Refactor unit tests to match Eric Elliott style.](https://medium.com/javascript-scene/behavior-driven-development-bdd-and-functional-testing-62084ad7f1f2)
- [ ] Add scalable configuration.
  - [ ] Add configuration for development, testing, production.