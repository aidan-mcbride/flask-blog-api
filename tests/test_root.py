from http import HTTPStatus

def test_endpoint_exists(client):
    rv = client.get('/')
    assert rv.status_code == HTTPStatus.OK
    assert rv.json == {'message': 'Endpoint Exists!'}
