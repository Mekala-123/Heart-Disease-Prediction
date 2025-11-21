from pathlib import Path
# tests/test_services/test_item_service.py
from src.services.item_service import ItemService, NotFoundError
from src.repositories.item_repo import ItemRepository

def make_service(tmp_path: Path):
    f = tmp_path / "items.json"
    f.write_text("[]", encoding="utf-8")
    repo = ItemRepository(data_file=f)
    return ItemService(repo=repo)

def test_service_create_and_get(tmp_path):
    svc = make_service(tmp_path)
    created = svc.create_item({"name": "Book", "description": "A good book"})
    assert created["id"] == 1
    got = svc.get_item(1)
    assert got["name"] == "Book"

def test_service_list_and_pagination(tmp_path):
    svc = make_service(tmp_path)
    for i in range(25):
        svc.create_item({"name": f"Item{i}", "description": f"desc{i}"})
    page1 = svc.list_items(q=None, page=1, size=10)
    assert page1["page"] == 1
    assert len(page1["items"]) == 10
    page3 = svc.list_items(q=None, page=3, size=10)
    assert page3["page"] == 3
    assert len(page3["items"]) == 5

def test_service_update_and_delete(tmp_path):
    svc = make_service(tmp_path)
    svc.create_item({"name": "A", "description": "a"})
    updated = svc.update_item(1, {"name": "B"})
    assert updated["name"] == "B"
    svc.delete_item(1)
    try:
        svc.get_item(1)
        raise AssertionError("expected NotFoundError")
    except NotFoundError:
        pass
