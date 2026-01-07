import logging
from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

def test_logging_middleware(caplog):
    caplog.set_level(logging.INFO, logger="uvicorn.error")
    
    client.get("/health")

    # Assert that logs were created
    assert any("path" in record.message for record in caplog.records)
