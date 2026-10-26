import pytest
from app import create_app

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home(client):
    response = client.get('/')
    assert response.status_code == 200
    data = response.get_json()
    assert data["application"] == "SecureFlow"
    assert data["message"] == "Automated DevSecOps Security Pipeline"
    assert data["status"] == "running"

def test_health(client):
    response = client.get('/health')
    assert response.status_code == 200
    assert response.get_json()["status"] == "healthy"
