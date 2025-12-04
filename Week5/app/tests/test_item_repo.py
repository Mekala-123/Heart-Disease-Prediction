import pytest, uuid
from app.repositories.item_repo_mongo import ItemRepoMongo
from app.schemas.item_schema import ItemCreate
from app.core import db

@pytest.mark.asyncio
async def test_insert_find_update_delete():
    repo = ItemRepoMongo(db.db)
    
    # Use a unique name each time
    unique_name = f"test-{uuid.uuid4()}"
    payload = ItemCreate(name=unique_name, description="test description", price=9.99)
    inserted_item = await repo.insert_one(payload)
    
    assert "id" in inserted_item
    assert inserted_item["name"] == payload.name

    item_id = inserted_item["id"]

    found_item = await repo.find_one(item_id)
    assert found_item is not None
    assert found_item["name"] == payload.name

    update_payload = ItemCreate(name=unique_name+"-updated", description="updated", price=19.99)
    updated_item = await repo.update_one(item_id, update_payload)
    assert updated_item["name"] == update_payload.name

    deleted = await repo.delete_one(item_id)
    assert deleted is True

    should_be_none = await repo.find_one(item_id)
    assert should_be_none is None
