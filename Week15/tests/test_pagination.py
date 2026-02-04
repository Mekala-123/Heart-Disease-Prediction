def test_offset_pagination(client):
    res = client.get("/api/v1/users?page=1&limit=2")
    assert res.status_code == 200
    assert len(res.json()) <= 2
