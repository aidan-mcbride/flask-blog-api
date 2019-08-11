from datetime import datetime

from api.models import Article


def test_create_article():
    """
    GIVEN the model for an article
    WHEN article data is passed in
    THEN return a database model for that article.
    """

    actual = Article(title="Test Title", content="Post body")

    expected = {"title": "Test Title", "slug": "test-title", "content": "Post body"}

    assert actual.title == expected["title"]
    assert actual.slug == expected["slug"]
    assert actual.content == expected["content"]
