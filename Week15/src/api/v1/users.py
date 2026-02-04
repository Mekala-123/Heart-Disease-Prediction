from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from typing import List, Optional

from src.core.database import get_db
from src.schemas.user import UserOut
from src.services.user_service import get_users

router = APIRouter(tags=["Users"])

@router.get("/users", response_model=List[UserOut])
def list_users(
    page: int = Query(1, ge=1),
    limit: int = Query(10, le=100),
    cursor: Optional[int] = None,
    sort: Optional[str] = "-created_at",
    q: Optional[str] = None,
    db: Session = Depends(get_db)
):
    return get_users(db, page, limit, cursor, sort, q)
