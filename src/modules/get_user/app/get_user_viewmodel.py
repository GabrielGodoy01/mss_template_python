from src.shared.domain.entities.user import User
from src.shared.domain.enums.state_enum import STATE


class GetUserViewmodel:
    id: int
    name: str
    state: STATE

    def __init__(self, user: User):
        self.id = user.id
        self.name = user.name
        self.state = user.state

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'state': self.state.value,
            'message': "the user was retrieved successfully"
        }
