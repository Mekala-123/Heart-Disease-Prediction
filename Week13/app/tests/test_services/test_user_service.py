import pytest
import asyncio
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.database import AsyncSessionLocal, engine
from app.models.user import Base, User
from app.services.user_service import UserService

@pytest.mark.asyncio
async def test_dashboard():
    # 1. Create tables for testing
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    # 2. Create a test user in DB
    async with AsyncSessionLocal() as db:
        user = User(name="Test", email="test@example.com", age=20)
        db.add(user)
        await db.commit()
        await db.refresh(user)

        # 3. Call service with real db
        service = UserService()
        result = await service.get_dashboard(db, user.id)

        assert "profile" in result
        assert "activity" in result
        assert "settings" in result
