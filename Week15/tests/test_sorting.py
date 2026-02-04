def test_sorting(client):
    res = client.get("/api/v1/users?sort=name")
    data = res.json()
    assert data == sorted(data, key=lambda x: x["name"])
