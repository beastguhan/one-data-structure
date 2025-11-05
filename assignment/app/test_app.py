import pytest
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_health(client):
    resp = client.get('/health')
    assert resp.status_code == 200
    assert resp.data == b'OK'

def test_index(client):
    resp = client.get('/')
    assert resp.status_code == 200
    assert b"Hello" in resp.data
