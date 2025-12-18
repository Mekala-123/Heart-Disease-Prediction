from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from src.core.security import decode_token
from src.repositories.user_repository import UserRepository

router = APIRouter(prefix="/users", tags=["users"])
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")
user_repo = UserRepository()

def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        payload = decode_token(token)
        email = payload.get("sub")
        user = user_repo.get_by_email(email)
        if not user:
            raise HTTPException(status_code=401, detail="User not found")
        return user
    except Exception:
        raise HTTPException(status_code=401, detail="Invalid token")

# GET /me
@router.get("/me")
def read_me(current_user: dict = Depends(get_current_user)):
    return {"email": current_user["email"], "roles": current_user["roles"]}

# GET /all (example)
@router.get("/all")
def list_users(current_user: dict = Depends(get_current_user)):
    return user_repo.users
