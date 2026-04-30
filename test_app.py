# test_app.py
import app as application
import pytest

@pytest.fixture
def client():
    application.app.testing = True
    with application.app.test_client() as c:
        yield c

def test_root(client):
    r = client.get('/')
    assert r.status_code == 200

def test_guess_returns_hint(client):
    r = client.get('/guess/42')
    assert r.status_code == 200
    data = r.get_json()
    assert data['msg'] in ('Higher', 'Lower', 'Correct!')