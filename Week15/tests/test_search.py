def test_search(client):
    res = client.get("/api/v1/users?q=python")
    assert res.status_code == 200
    assert any("python" in user["name"].lower() for user in res.json())
