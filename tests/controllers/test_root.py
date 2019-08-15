"""
TEST API ROOT
"""

####################
#### UNIT TESTS ####
####################


def test_root_content(client):
    """
    GIVEN an app
    WHEN a GET request is made to the application root
    THEN return a list of all available endpoints
    """
    rv = client.get("/")

    actual = rv.status_code
    expected = 200
    assert expected == actual

    actual = rv.get_json()
    expected = dict(endpoints=["/articles/", "/articles/<slug>"])
    assert expected == actual
