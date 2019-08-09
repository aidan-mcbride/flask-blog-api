mock_articles = [
    {"title": "Blog Post 1", "content": "Post body"},
    {"title": "Blog Post 2", "content": "Post body"},
    {"title": "Blog Post 3", "content": "Post body"},
]


def test_get_all_articles(client):
    """
    GIVEN a flask application
    WHEN a GET request is made to '/articles/'
    THEN return a list of articles
        AND return a 200 status code
    """
    response = client.get("/articles/")

    actual = response.get_json()
    # TODO: replace w/ test db fixture and mock data
    expected = mock_articles
    assert actual == expected

    actual = response.status_code
    expected = 200
    assert actual == expected
