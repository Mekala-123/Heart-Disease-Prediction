import time
import jwt
from passlib.context import CryptContext

SECRET = "CHANGE_THIS_SECRET"
ALGORITHM = "HS256"

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str):
    return pwd_context.hash(password)

def verify_password(password: str, hashed: str):
    return pwd_context.verify(password, hashed)

def create_token(sub: str, token_type="access", expires=900):
    payload = {
        "sub": sub,
        "type": token_type,
        "exp": int(time.time()) + expires
    }
    return jwt.encode(payload, SECRET, algorithm=ALGORITHM)

def decode_token(token: str):
    return jwt.decode(token, SECRET, algorithms=[ALGORITHM])