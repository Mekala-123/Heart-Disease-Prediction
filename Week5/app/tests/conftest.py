import pytest_asyncio
from app.core import db

@pytest_asyncio.fixture(scope="module", autouse=True)
async def setup_db():
    await db.connect_to_mongo()
    yield
    await db.close_mongo_connection()
