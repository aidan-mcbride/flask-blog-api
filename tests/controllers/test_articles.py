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

# GET ARTICLES COLLECTION (ALL ARTICLES)
class TestArticlesGetCollection(object):
    # must specify client fixture as argument
    # because it is used explicitly within the test
    # to do GET request.
    def test_get_empty_articles(self, client):
        """
        GIVEN a database containing no articles
        WHEN a GET request is made to '/articles/'
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

    def test_get_all_articles(self, client, mock_articles):
        """
        GIVEN a database containing three mock articles
        WHEN a GET request is made to '/articles/'
        THEN return an array of articles
            AND return a 200 status code
        """
        rv = client.get("/articles/")

        actual = rv.get_json()
        expected = [
            {
                "id": 1,
                "slug": "test-article-1",
                "title": "Test article 1",
                "content": "Lorem ipsum 123",
            },
            {
                "id": 2,
                "slug": "test-article-2",
                "title": "Test article 2",
                "content": "Lorem ipsum 123",
            },
            {
                "id": 3,
                "slug": "test-article-3",
                "title": "Test article 3",
                "content": "Lorem ipsum 123",
            },
        ]
        assert actual == expected

        actual = rv.status_code
        expected = 200
        assert actual == expected


# GET ARTICLE RESOURCE (SINGLE ARTICLE)
class TestArticlesGetResource(object):
    def test_get_article_by_slug(self, client, mock_articles):
        """
        GIVEN a database containing three mock articles
        WHEN a GET request is made to '/articles/<slug>'
        THEN return an object containing the requested article.
            AND return a 200 status code
        """
        rv = client.get("/articles/test-article-1")

        actual = rv.get_json()
        expected = {
            "id": 1,
            "slug": "test-article-1",
            "title": "Test article 1",
            "content": "Lorem ipsum 123",
        }
        assert actual == expected

        actual = rv.status_code
        expected = 200
        assert actual == expected
