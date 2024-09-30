

import random
from uuid import uuid4
from src.shared.domain.entities.user import User
from src.shared.domain.enums.state_enum import STATE
from src.shared.domain.repositories.user_repository_interface import IUserRepository
from src.shared.helpers.errors.domain_errors import EntityError


class CreateUserUsecase:
    def __init__(self, repo: IUserRepository):
        self.repo = repo

    def __call__(self, name: str) -> User:

        if not User.validate_name(name):
            raise EntityError("name")

        user = User(
            user_id=int(random.randint(0, 1000000)),
            name=name,
            state=STATE.PENDING
        )

        return self.repo.create_user(user)
