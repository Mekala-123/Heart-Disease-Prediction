import pytest
from src.services.item_service import ItemService
from src.schemas.item_dto import ItemCreateDTO, ItemResponseDTO
from src.core.errors import ConflictError

def test_create_item_success(mocker):
    # 1️⃣ Create a mock repository
    mock_repo = mocker.Mock()

    # 2️⃣ Mock exists_by_name to return False (no conflict)
    mock_repo.exists_by_name.return_value = False

    # 3️⃣ Mock create() to return an ItemResponseDTO, NOT a dict
    mock_repo.create.return_value = ItemResponseDTO(
        id=1,
        name="Test",
        description="Desc"
    )

    # 4️⃣ Create the service with the mocked repository
    service = ItemService(mock_repo)

    # 5️⃣ Call service method
    result = service.create_item(ItemCreateDTO(name="Test", description="Desc"))

    # 6️⃣ Assertions
    assert result.id == 1
    assert result.name == "Test"
    assert result.description == "Desc"
