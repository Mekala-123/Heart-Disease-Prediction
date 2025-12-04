import pytest
from app.core import db

@pytest.mark.asyncio
async def test_connection():
    await db.connect_to_mongo()
    collections = await db.db.list_collection_names()
    assert isinstance(collections, list)
    await db.close_mongo_connection()
