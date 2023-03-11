import pytest


def test_index_api(client):
    response = client.get('/')
    assert response.status_code == 200
    assert response.data == b'Hello, World!'