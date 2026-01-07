from pydantic import BaseModel
from fastapi import APIRouter

router = APIRouter()

# Existing health route
@router.get("/health")
def health():
    return {"status": "ok"}

# -------------------------------
# Week 11 Test: 400 Validation
# -------------------------------
class InputData(BaseModel):
    name: str
    age: int

@router.post("/validate")
def validate_input(data: InputData):
    return {"message": "Valid input"}
