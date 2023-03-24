import pytest


def test_dev_api(client):
    response = client.get('/test_dev')
    assert response.status_code == 200
    assert response.data == b'Deployment success! '