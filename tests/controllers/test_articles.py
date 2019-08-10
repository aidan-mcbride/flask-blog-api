"""
TEST ARTICLES API

Contains fixtures, unit tests, and integration tests for 'api/controllers/articles.py'
"""

import pytest

from api.models import Article

"""
Use these fixtures for every test in this module:
client
database
---
It will be assumed for unit and integration tests that the application is running and that a database exists. If these conditions are false then there are problems beyond the scope of unit testing.
"""

pytestmark = pytest.mark.usefixtures("client", "database")


##################
#### FIXTURES ####
##################


@pytest.fixture
def mock_articles(database):
    db = database

    article_1 = Article(title="Test article 1", content="Lorem ipsum 123")
    article_2 = Article(title="Test article 2", content="Lorem ipsum 123")
    article_3 = Article(title="Test article 3", content="Lorem ipsum 123")

    db.session.add(article_1)
    db.session.add(article_2)
    db.session.add(article_3)

    db.session.commit()

    yield

    db.session.query(Article).delete()
    db.session.commit()


####################
#### UNIT TESTS ####
####################

# None Yet
# Not sure what kinds of actual unit tests you could do
# for an API this basic, since controllers are basically
# just interfaces for the database.


###########################
#### INTEGRATION TESTS ####
#### Or maybe these are still unit tests, since
#### they only integrate a single function
#### with an empty database?
###########################


class TestArticlesGetCollection(object):
    # must specify client fixture as argument
    # because it is used explicitly within the test
    # to do GET request.
    def test_get_empty_articles(self, client):
        """
        GIVEN a database containing no articles
        WHEN a GET request is made to the articles root
        THEN return an empty json array
            AND return a 200 status code
        """
        rv = client.get("/articles/")

        actual = rv.get_json()
        expected = []
        assert actual == expected

        actual = rv.status_code
        expected = 200
        assert actual == expected
