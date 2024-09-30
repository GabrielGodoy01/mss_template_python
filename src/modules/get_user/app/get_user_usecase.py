from src.shared.domain.entities.user import User
from src.shared.domain.repositories.user_repository_interface import IUserRepository
from src.shared.helpers.errors.domain_errors import EntityError
# from src.shared.infra.external.observability.observability_aws import ObservabilityAWS


class GetUserUsecase:
    def __init__(self, repo: IUserRepository):
        self.repo = repo

    def __call__(self, user_id: int) -> User:
        return self.repo.get_user(user_id=user_id)
