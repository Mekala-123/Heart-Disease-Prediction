from fastapi import APIRouter, Depends
from src.core.permissions import require_role


router = APIRouter(prefix="/items", tags=["Items"])

@router.post(
    "",
    dependencies=[Depends(require_role(["admin"]))],
    responses={
        401: {"description": "Unauthorized"},
        403: {"description": "Forbidden"},
    },
)
def create_item():
    return {"message": "Item created successfully"}
