from fastapi import APIRouter, HTTPException, Depends
from fastapi.security import OAuth2PasswordRequestForm, HTTPBearer
from src.schemas.user_schema import UserCreate, UserOut, Token
from src.services.auth_service import (
    register_user,
    authenticate,
    create_tokens,
    refresh_token
)
from src.core.security import decode_token

router = APIRouter(prefix="/auth", tags=["auth"])
security = HTTPBearer()



@router.post("/register", response_model=UserOut, status_code=201)
def register(payload: UserCreate):
    try:
        user = register_user(payload.email, payload.password)
        return UserOut(
            email=user["email"],
            roles=user["roles"]
        )
    except ValueError:
        raise HTTPException(status_code=409, detail="User already exists")


@router.post("/login", response_model=Token)
def login(form: OAuth2PasswordRequestForm = Depends()):
    user = authenticate(form.username, form.password)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    return Token(**create_tokens(user["email"]))


@router.post("/refresh", response_model=Token)
def refresh(data: dict):
    if "refresh_token" not in data:
        raise HTTPException(status_code=400, detail="Refresh token required")

    try:
        return Token(**refresh_token(data["refresh_token"]))
    except Exception:
        raise HTTPException(status_code=401, detail="Invalid refresh token")


@router.get("/me", response_model=UserOut)
def me(credentials=Depends(security)):
    payload = decode_token(credentials.credentials)
    return UserOut(
        email=payload["sub"],
        roles=["user"]
    )
