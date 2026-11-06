from fastapi.testclient import TestClient
from app import app

client = TestClient(app)

def test_health():
    response = client.get('/health')
    assert response.status_code == 200
    assert response.json() == {'status': 'healthy'}

def test_root():
    response = client.get('/')
    assert response.status_code == 200
    assert 'message' in response.json()

def test_version():
    response = client.get('/version')
    assert response.status_code == 200
    assert response.json()['version'] == '1.0.0'
