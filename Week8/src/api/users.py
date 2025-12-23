from fastapi import APIRouter, Depends, Query
from src.services.user_service import list_users
from src.core.permissions import require_role


router = APIRouter(prefix="/users", tags=["Users"])

@router.get(
    "",
    dependencies=[Depends(require_role(["admin"]))],
    responses={
        401: {"description": "Unauthorized"},
        403: {"description": "Forbidden"},
    },
)
def get_users(
    page: int = Query(1, ge=1),
    size: int = Query(10, le=50),
):
    return {
        "page": page,
        "size": size,
        "users": list_users(page, size)
    }
