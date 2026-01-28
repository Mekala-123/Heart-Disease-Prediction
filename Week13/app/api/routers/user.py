from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.database import get_db
from app.schemas.user import UserCreate, UserResponse
from app.services.user_service import UserService
from app.utils.concurrency import safe_external_call

router = APIRouter()
service = UserService()

@router.post("/", response_model=UserResponse)
async def create_user(user: UserCreate, db: AsyncSession = Depends(get_db)):
    return await service.create_user(db, user)

@router.get("/{user_id}")
async def get_user(user_id: str, db: AsyncSession = Depends(get_db)):
    user = await service.get_user(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.get("/{user_id}/dashboard")
async def dashboard(user_id: str, db: AsyncSession = Depends(get_db)):
    return await service.get_dashboard(db, user_id)

@router.get("/{user_id}/external-profile")
async def external_profile():
    return await safe_external_call()
