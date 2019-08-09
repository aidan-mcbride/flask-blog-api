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

#### Unit Testing

##### [TDD The RITE Way](https://medium.com/javascript-scene/tdd-the-rite-way-53c9b46f45e3)

> IMPORTANT:
>
> The following is essentially a summary of [this article by Eric Elliott](https://medium.com/javascript-scene/tdd-the-rite-way-53c9b46f45e3), but in bullet form so I can reference it later.

* **Readable**
  * **Five questions every unit test must answer:**
    1. What component is being tested?
    2. What behavior of that component is being tested? (fixtures?)
    3. What are the **expected** results?
    4. What are the **actual** results?
    5. How can the actual results be reproduced?
  * **TIP:** keep test code to a minimum
     1. Use factory functions /fixtures to initialize  whatever state you need for your test, rather than doing that *within* the test code itself.
  * **TIP:** use equality assertions instead of fancypants assertion types.
  * **TIP:** explicitly name your `actual` and `expected` values.
* **Isolated** or **Integrated**
  * **Unit tests** test **isolated** components.
    * Deterministic: same input into same component *always* gives same output.
    * Speedy-quick to run.
    * **Black Box:** something goes in, and something comes out - the test doesn't care what happens in between.
  * **Integration** and **functional/E2E** tests test components that are **integrated**.
    * For components with side-effects, such as API calls, writing to disk, etc.
  * Regardless of type, **all tests** must be isolated from other tests.
  * ***Mocking is a code smell*** that signals that your functions are too tightly coupled.
    * <u>***Functions that communicate with a database/API/network should be separate from the logic that processes the response.***</u>
* **Thorough**
  * Critical [happy paths](https://en.wikipedia.org/wiki/Happy_path) (user registration, purchasing, payment processing) should be [smoke tested](https://www.techopedia.com/definition/4354/smoke-testing) immediately after deployment to production.
  * Your test suite should test all unhappy paths:
    * test incorrect inputs and inputs of the *incorrect type* - e.g. if an input takes a number, it should be tested with `0`, negative numbers, out-of-range large numbers, and floats.
    * Test malicious inputs.
* **Explicit**
  * The unit test report should contain all the information necessary for the person reading it to reproduce the  results.
  * **Unit test report should act as a detailed bug report.**

#### [Given-When-Then](https://martinfowler.com/bliki/GivenWhenThen.html)

* Formula for writing unit tests. Also works better as a formula for creating acceptance tests at a high level.
  * **Given** a pre-existing state
  * **When** some event occurs or some input is given
  * **Then** some change will occur or some output will be given.



#### [Travis CI](https://travis-ci.org/)

* Will automatically build and test committed changes to a GitHub repository.
* Testing specifications are listed in a **`.travis.tml`** file in the root of the project.

#### Static Typing in Python

* Python 3.5 adds the [*typing*](https://docs.python.org/3/library/typing.html?highlight=typing#module-typing) module, which lets you add hints about what the expected type for a variable should be.
* Type hinting acts as in-line documentation for what the expected inputs and outputs for functions are.
* **Mypy** is a tool that can scan your code for typing errors based on the type hints, which could lead to difficult-to-find bugs.
* *A bonus of using type hinting is that - like with TDD - doing it forces you to slow down and consider what exactly you are coding.*
