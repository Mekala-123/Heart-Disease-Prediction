from src.repositories.item_repository import get_all_items

def test_get_all_items():
    items = get_all_items()
    assert len(items) >= 1
