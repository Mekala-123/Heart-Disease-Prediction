class UserRepository:
    """
    Simulated database layer
    """

    def __init__(self):
        self._users = {
            1: {"id": 1, "name": "Mekala"},
            2: {"id": 2, "name": "Arya"}
        }

    def get_user(self, user_id: int):
        return self._users.get(user_id)
