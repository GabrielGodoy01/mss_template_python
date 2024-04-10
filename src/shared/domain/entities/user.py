import abc
import re

from src.shared.domain.enums.state_enum import STATE
from src.shared.helpers.errors.domain_errors import EntityError


class User(abc.ABC):
    name: str
    state: STATE
    id: int
    MIN_NAME_LENGTH = 2

    def __init__(self, name: str, state: STATE, id: int = None):
        if not User.validate_name(name):
            raise EntityError("name")
        self.name = name

        if type(id) == int:
            if id < 0:
                raise EntityError("id")

        if type(id) != int and id is not None:
            raise EntityError("id")

        self.id = id

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
        return f"User(name={self.name}, id={self.id}, state={self.state})"
