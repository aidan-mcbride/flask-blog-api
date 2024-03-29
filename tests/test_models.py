from datetime import datetime, timezone

from api.models import Article, article_schema


def test_create_article():
    """
    GIVEN the model for an article
    WHEN article data is passed in
    THEN return a database model for that article.
    """

    # create time here so that actual and expected have same time; if created in model, time will differ.
    time: datetime = datetime.now(timezone.utc)

    actual: Article = Article(
        title="Test Title", content="Post body", date_created=time
    )
    expected: dict = {
        "title": "Test Title",
        "slug": "test-title",
        "content": "Post body",
        "date_created": time,
    }

    assert actual.title == expected["title"]
    assert actual.slug == expected["slug"]
    assert actual.content == expected["content"]


def test_serialize_article_to_dict():
    """
    GIVEN an Article object created from a dictionary
    WHEN that object is serialized
    THEN return a dictionary containing the data from that object, including data that is initialized in the Article constructor
    """
    time: datetime = datetime.now(timezone.utc)
    article: Article = Article(
        title="Test Title", content="Post body", date_created=time
    )

    actual: dict = article_schema.dump(article).data
    expected: dict = dict(
        title="Test Title",
        slug="test-title",
        content="Post body",
        date_created=time.isoformat(),
    )
    for key in expected.keys():
        assert actual[key] == expected[key]


# must use database fixture for title validation
def test_deserialize_article_to_article_instance(client, database):
    time: datetime = datetime.now()
    input_time: str = time.isoformat()
    article_data: dict = dict(
        title="Test Title", content="Post body", date_created=input_time
    )

    actual: Article = article_schema.load(article_data).data
    expected: Article = Article(
        title="Test Title", content="Post body", date_created=time
    )

    assert actual.title == expected.title
    assert actual.slug == expected.slug
    assert actual.content == expected.content
    assert actual.date_created == expected.date_created
