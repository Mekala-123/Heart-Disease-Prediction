from pathlib import Path
from src.repositories.item_repo import ItemRepository

def test_repo_create_get_update_delete(tmp_path: Path):
    f = tmp_path / "items.json"
    f.write_text("[]", encoding="utf-8")
    repo = ItemRepository(data_file=f)

    # create
    item = repo.create({"name": "Pen", "description": "Blue pen"})
    assert item["id"] == 1
    assert item["name"] == "Pen"

    # get
    got = repo.get(1)
    assert got["id"] == 1
    assert got["name"] == "Pen"

    # update
    updated = repo.update(1, {"name": "Pencil"})
    assert updated is not None
    assert updated["name"] == "Pencil"

    # delete
    ok = repo.delete(1)
    assert ok is True
    assert repo.get(1) is None
