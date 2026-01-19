import pytest
from fastapi.testclient import TestClient
from unittest.mock import MagicMock
from src.main import app

@pytest.fixture
def test_app():
    return app

@pytest.fixture
def client(test_app):
    return TestClient(test_app)

@pytest.fixture
def mock_repo():
    return MagicMock()
