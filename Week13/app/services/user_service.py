import asyncio
from app.models.user import User
from app.repositories.user_repo import UserRepository

repo = UserRepository()

class UserService:

    async def create_user(self, db, data):
        user = User(**data.dict())
        return await repo.create_user(db, user)

    async def get_user(self, db, user_id):
        return await repo.get_user(db, user_id)

    async def get_dashboard(self, db, user_id):
        async def fetch_profile():
            await asyncio.sleep(0.2)
            return await repo.get_user(db, user_id)

        async def fetch_activity():
            await asyncio.sleep(0.3)
            return {"posts": 10, "last_login": "2026-01-26"}

        async def fetch_settings():
            await asyncio.sleep(0.1)
            return {"theme": "dark"}

        profile, activity, settings = await asyncio.gather(
            fetch_profile(),
            fetch_activity(),
            fetch_settings()
        )

        return {
            "profile": profile,
            "activity": activity,
            "settings": settings
        }
