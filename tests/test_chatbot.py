import pytest
from app import create_app

from flask.testing import FlaskClient

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


def test_chatbot_response(client: FlaskClient):
    response = client.post("/chat", json={"message": "Olá"})
    assert response.status_code == 200
    assert "response" in response.get_json()
