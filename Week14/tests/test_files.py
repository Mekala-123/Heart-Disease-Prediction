from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

def test_upload_file():
    with open("tests/sample.pdf", "wb") as f:
        f.write(b"test data")

    with open("tests/sample.pdf", "rb") as f:
        response = client.post(
            "/files",
            files={"file": ("sample.pdf", f, "application/pdf")}
        )

    assert response.status_code == 200
    assert "file_id" in response.json()
