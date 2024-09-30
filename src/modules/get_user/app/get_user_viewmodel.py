from src.shared.domain.entities.user import User
from src.shared.domain.enums.state_enum import STATE


class GetUserViewmodel:
    user_id: int
    name: str
    state: STATE

    def __init__(self, user: User):
        self.user_id = user.user_id
        self.name = user.name
        self.state = user.state

    def to_dict(self):
        return {
            'user_id': self.user_id,
            'name': self.name,
            'state': self.state.value,
            'message': "the user was retrieved successfully"
        }
