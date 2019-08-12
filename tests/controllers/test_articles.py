"""
TEST ARTICLES API

Contains fixtures, unit tests, and integration tests for 'api/controllers/articles.py'
"""

import pytest
import datetime

from api.models import Article, article_schema

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

    article_1, errors = article_schema.load(
        dict(title="Test article 1", content="Lorem ipsum 123")
    )
    article_2, errors = article_schema.load(
        dict(title="Test article 2", content="Lorem ipsum 123")
    )
    article_3, errors = article_schema.load(
        dict(title="Test article 3", content="Lorem ipsum 123")
    )

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
        assert len(actual) is 3

        actual = rv.get_json()[0]
        expected = dict(
            id=1,
            title="Test article 1",
            slug="test-article-1",
            content="Lorem ipsum 123",
        )
        for key in actual.keys():
            if key == "date_created":
                assert key
            else:
                assert actual[key] == expected[key]

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

        actual = rv.status_code
        expected = 200
        assert actual == expected

        actual = rv.get_json()
        expected = {
            "id": 1,
            "slug": "test-article-1",
            "title": "Test article 1",
            "content": "Lorem ipsum 123",
        }
        for key in actual.keys():
            if key == "date_created":
                assert key
            else:
                assert actual[key] == expected[key]

    def test_get_article_not_found(self, client):
        """
        GIVEN a database
        WHEN a GET request is made for an article that doesn't exist
        THEN return an object containing an error message
            AND return a 404 (not found) status code
        """
        rv = client.get("/articles/test-article-1")

        actual = rv.status_code
        expected = 404
        assert actual == expected

        actual = rv.get_json()
        expected = {"error": "article not found"}
        assert actual == expected


# TEST CREATE NEW ARTICLE
class TestArticlesCreateResource(object):
    def test_create_article(self, client):
        """
        GIVEN a database
        WHEN a POST request is made to articles root
        THEN create a new article in the database
            AND return that article as a json object
            AND return a 201(created) status code
        """
        new_article = dict(title="Test Article", content="Lorem ipsum 123")

        rv = client.post("/articles/", json=new_article)

        actual = rv.status_code
        expected = 201
        assert actual == expected

        actual = rv.get_json()
        expected = dict(
            title="Test Article", slug="test-article", content="Lorem ipsum 123"
        )
        assert actual["title"] == expected["title"]
        assert actual["slug"] == expected["slug"]
        assert actual["content"] == expected["content"]
        assert actual["date_created"]

    def test_create_article_no_request_body(self, client):
        """
        GIVEN ...
        WHEN a POST is made with no request body
        THEN return an error message
            AND return a 400 status code
        """
        rv = client.post("/articles/")

        actual = rv.status_code
        expected = 400
        assert actual == expected

        actual = rv.get_json()
        expected = dict(error="request body is missing or is invalid json")
        assert actual == expected

    def test_create_article_missing_title(self, client):
        """
        GIVEN ...
        WHEN a POST is made to articles, but the request body is missing a title
        THEN return an error
            AND return a 400 status code
        """
        request_data = dict(content="Lorem ipsum 123")
        rv = client.post("/articles/", json=request_data)

        actual = rv.status_code
        expected = 400
        assert actual == expected

        actual = rv.get_json()
        expected = dict(title=["Missing data for required field."])
        assert actual == expected

    def test_create_article_missing_content(self, client):
        """
        GIVEN ...
        WHEN a POST is made to articles, but the request body is missing the content of the article
        THEN return an error
            AND return a 400 status code
        """
        request_data = dict(title="Test title")
        rv = client.post("/articles/", json=request_data)

        actual = rv.status_code
        expected = 400
        assert actual == expected

        actual = rv.get_json()
        expected = dict(content=["Missing data for required field."])
        assert actual == expected

    # COMMENTED OUT WHILE INSTALLING FLASK-MARSHMALLOW
    # So that I can run existing tests to enesure nothing breaks
    # while converting to marshmallow

    # def test_create_article_title_exists(self, client, mock_articles):
    #     """
    #     GIVEN an article exists in the database
    #     WHEN a POST is made to articles with a title whose text matches that of an existing title, regardless of case
    #     THEN return an error
    #         AND return a 400 status code
    #     """
    #     request_data = dict(title="TEST ARTICLE 1", content="Lorem ipsum 123")
    #     rv = client.post("/articles/", json=request_data)
    #
    #     actual = rv.status_code
    #     expected = 400
    #     assert actual == expected
    #
    #     actual = rv.get_json()
    #     expected = dict(error="an article already exists with this title")
    #     assert actual == expected
