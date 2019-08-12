from datetime import datetime

from api.models import Article, article_schema


def test_create_article():
    """
    GIVEN the model for an article
    WHEN article data is passed in
    THEN return a database model for that article.
    """

    # create time here so that actual and expected have same time; if created in model, time will differ.
    time = datetime.utcnow()

    actual = Article(title="Test Title", content="Post body", date_created=time)
    expected = {
        "title": "Test Title",
        "slug": "test-title",
        "content": "Post body",
        "date_created": time,
    }

    assert actual.title == expected["title"]
    assert actual.slug == expected["slug"]
    assert actual.content == expected["content"]
