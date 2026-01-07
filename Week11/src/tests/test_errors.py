import pytest
from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

# ----------------------------
# 200 OK - Health
# ----------------------------
def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}

# ----------------------------
# 400 Validation Error
# ----------------------------
def test_validation_error():
    # missing 'age' field
    response = client.post("/validate", json={"name": "Alice"})
    assert response.status_code == 400
    json_data = response.json()
    assert "error" in json_data
    assert "trace_id" in json_data

# ----------------------------
# 401 Unauthorized
# ----------------------------
def test_unauthorized():
    response = client.get("/unauthorized")
    assert response.status_code == 401
    json_data = response.json()
    assert "error" in json_data
    assert "trace_id" in json_data

# ----------------------------
# 403 Forbidden
# ----------------------------
def test_forbidden():
    response = client.get("/forbidden")
    assert response.status_code == 403
    json_data = response.json()
    assert "error" in json_data
    assert "trace_id" in json_data

# ----------------------------
# 404 Not Found
# ----------------------------
def test_not_found():
    response = client.get("/anything")
    assert response.status_code == 404
    json_data = response.json()
    assert "error" in json_data
    assert "trace_id" in json_data

# ----------------------------
# 409 Conflict
# ----------------------------
def test_conflict():
    response = client.get("/conflict")
    assert response.status_code == 409
    json_data = response.json()
    assert "error" in json_data
    assert "trace_id" in json_data

# ----------------------------
# 500 Internal Server Error
# ----------------------------
def test_internal_server_error():
    # Expect ZeroDivisionError when hitting /crash
    with pytest.raises(ZeroDivisionError):
        client.get("/crash")
