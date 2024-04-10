from src.shared.domain.entities.user import User
from src.shared.domain.repositories.user_repository_interface import IUserRepository
from src.shared.helpers.errors.domain_errors import EntityError


class UpdateUserUsecase:
    def __init__(self, repo: IUserRepository):
        self.repo = repo

    def __call__(self, id: int, new_name: str) -> User:

        if type(id) != int:
            raise EntityError("id")
        
        if type(new_name) != str:
            raise EntityError("new_name")

        updated_user = self.repo.update_user(id=id, new_name=new_name)

        return updated_user
