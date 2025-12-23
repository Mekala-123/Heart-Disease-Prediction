import jwt

SECRET_KEY = "secret"
ALGORITHM = "HS256"

admin_token = jwt.encode(
    {"sub": "admin@test.com", "roles": ["admin"]},
    SECRET_KEY,
    algorithm=ALGORITHM
)

user_token = jwt.encode(
    {"sub": "user@test.com", "roles": ["user"]},
    SECRET_KEY,
    algorithm=ALGORITHM
)

print("ADMIN TOKEN:\n", admin_token)
print("\nUSER TOKEN:\n", user_token)
