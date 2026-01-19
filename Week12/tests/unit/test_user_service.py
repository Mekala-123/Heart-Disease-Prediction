from src.services.user_service import get_user_by_id

def test_get_user_by_id_found(mock_repo):
    mock_repo.get_user.return_value = {"id": 1, "name": "Mekala"}

    result = get_user_by_id(1, mock_repo)

    assert result["name"] == "Mekala"
    mock_repo.get_user.assert_called_once_with(1)

def test_get_user_by_id_not_found(mock_repo):
    mock_repo.get_user.return_value = None

    result = get_user_by_id(99, mock_repo)

    assert result is None
