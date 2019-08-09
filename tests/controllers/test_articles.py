from http import HTTPStatus

def test_get_all_articles(client):
    """
    GIVEN a flask application
    WHEN a GET request is made to '/articles/'
    THEN a 200 status code should be returned
    """
    response = client.get('/articles/')

    actual = response.status_code
    expected = HTTPStatus.OK
    assert actual == expected
