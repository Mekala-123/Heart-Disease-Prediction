import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

def test_auth_flow():
    # Register
    r = client.post("/auth/register", json={"email": "a@a.com", "password": "pass1234"})
    assert r.status_code == 201

    # Login
    r = client.post("/auth/login", data={"username": "a@a.com", "password": "pass1234"})
    assert r.status_code == 200
    tokens = r.json()

    # Access protected route
    access = tokens["access_token"]
    r = client.get("/auth/me", headers={"Authorization": f"Bearer {access}"})
    assert r.status_code == 200

    # Refresh
    r = client.post("/auth/refresh", json={"refresh_token": tokens["refresh_token"]})
    assert r.status_code == 200