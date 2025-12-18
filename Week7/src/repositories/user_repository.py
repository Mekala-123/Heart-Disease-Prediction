from src.schemas.user_schema import UserResponseDTO

class UserRepository:
    def __init__(self):
        self.users = {}  # email -> user dict
        self.id_counter = 1

    def create_user(self, email: str, hashed_password: str, roles: list = ["user"]):
        user = {
            "id": self.id_counter,
            "email": email,
            "hashed_password": hashed_password,
            "roles": roles
        }
        self.users[email] = user
        self.id_counter += 1
        return UserResponseDTO(id=user["id"], email=email, roles=roles)

    def get_by_email(self, email: str):
        return self.users.get(email)
