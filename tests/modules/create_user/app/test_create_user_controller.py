from src.modules.create_user.app.create_user_controller import CreateUserController
from src.modules.create_user.app.create_user_usecase import CreateUserUsecase
from src.shared.helpers.external_interfaces.http_models import HttpRequest
from src.shared.infra.repositories.user_repository_mock import UserRepositoryMock


class Test_CreateUserControler:
    def test_create_user_controller(self):
        repo = UserRepositoryMock()
        usecase = CreateUserUsecase(repo=repo)
        controller = CreateUserController(usecase=usecase)

        request = HttpRequest(body={
            'name': 'Branco do Branco Branco da Silva'
        })

        response = controller(request=request)

        assert response.status_code == 201
        assert response.body['user_id'] == repo.users[-1].user_id
        assert response.body['name'] == repo.users[-1].name
        assert response.body['state'] == repo.users[-1].state.value
        assert response.body['message'] == "the user was created successfully"

    def test_create_user_controller_missing_name(self):
        repo = UserRepositoryMock()
        usecase = CreateUserUsecase(repo=repo)
        controller = CreateUserController(usecase=usecase)

        request = HttpRequest(body={})

        response = controller(request=request)

        assert response.status_code == 400
        assert response.body == "Campo name está faltando"

    def test_create_user_controller_invalid_name(self):
        repo = UserRepositoryMock()
        usecase = CreateUserUsecase(repo=repo)
        controller = CreateUserController(usecase=usecase)

        request = HttpRequest(body={
            'name': 'B'})

        response = controller(request=request)

        assert response.status_code == 400
        assert response.body == "O campo 'name' não é válido"





