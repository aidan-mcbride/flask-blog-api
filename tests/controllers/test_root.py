from http import HTTPStatus


def test_endpoint_exists(client):
    """
    GIVEN: a Flask application
    WHEN: a GET request is made to '/'
    THEN: a message should be returned
        AND an ok status code should be returned.
    """
    response = client.get("/")

    actual = response.status_code
    expected = HTTPStatus.OK
    assert actual == expected

    actual = response.json
    expected = {"message": "Endpoint Exists!"}
    assert actual == expected
