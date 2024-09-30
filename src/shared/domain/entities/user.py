import abc
import re

from src.shared.domain.enums.state_enum import STATE
from src.shared.helpers.errors.domain_errors import EntityError


class User(abc.ABC):
    name: str
    state: STATE
    user_id: int
    MIN_NAME_LENGTH = 2

    def __init__(self, name: str, state: STATE, user_id: int):
        if not User.validate_name(name):
            raise EntityError("name")
        self.name = name

        if type(user_id) != int:
            raise EntityError("user_id")
        self.user_id = user_id

        if type(state) != STATE:
            raise EntityError("state")
        self.state = state

    @staticmethod
    def validate_name(name: str) -> bool:
        if name is None:
            return False
        elif type(name) != str:
            return False
        elif len(name) < User.MIN_NAME_LENGTH:
            return False

        return True

    def __repr__(self):
        return f"User(name={self.name}, user_id={self.user_id}, state={self.state})"
