from app.repositories.sample_repo import SampleRepository

def test_repo_data():
    repo = SampleRepository()
    data = repo.get_by_id(1)
    assert data["id"] == 1
