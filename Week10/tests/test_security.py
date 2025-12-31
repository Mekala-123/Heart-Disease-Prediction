import pytest
from fastapi.testclient import TestClient
from src.main import app
import json

@pytest.fixture
def client():
    return TestClient(app)

def test_request_size_limit(client):
    large_data = {"data": "A" * 200_000}  # 200 KB > 100 KB limit
    payload = json.dumps(large_data).encode("utf-8")

    response = client.post(
        "/items/",
        content=payload,
        headers={"Content-Type": "application/json"}
    )
    assert response.status_code == 413
