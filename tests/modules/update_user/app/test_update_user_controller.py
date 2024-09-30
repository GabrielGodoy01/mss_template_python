from src.modules.update_user.app.update_user_controller import UpdateUserController
from src.modules.update_user.app.update_user_usecase import UpdateUserUsecase
from src.shared.helpers.external_interfaces.http_models import HttpRequest
from src.shared.infra.repositories.user_repository_mock import UserRepositoryMock


class Test_UpdateUserController:
    def test_update_user_controller(self):
        repo = UserRepositoryMock()
        usecase = UpdateUserUsecase(repo=repo)
        controller = UpdateUserController(usecase=usecase)

        request = HttpRequest(body={
            'user_id': "1",
            'new_name': 'Branco do Branco Branco da Silva'
        })

        response = controller(request=request)

        assert response.status_code == 200
        assert response.body['user_id'] == repo.users[0].user_id
        assert response.body['name'] == 'Branco do Branco Branco da Silva'
        assert response.body['state'] == repo.users[0].state.value
        assert response.body['message'] == "the user was updated successfully"

    def test_update_user_controller_missing_id(self):
        repo = UserRepositoryMock()
        usecase = UpdateUserUsecase(repo=repo)
        controller = UpdateUserController(usecase=usecase)

        request = HttpRequest(body={
            'new_name': 'Branco do Branco Branco da Silva'
        })

        response = controller(request=request)

        assert response.status_code == 400
        assert response.body == "Campo user_id está faltando"

    def test_update_user_controller_missing_new_name(self):
        repo = UserRepositoryMock()
        usecase = UpdateUserUsecase(repo=repo)
        controller = UpdateUserController(usecase=usecase)

        request = HttpRequest(body={
            'user_id': "1"
        })

        response = controller(request=request)

        assert response.status_code == 400
        assert response.body == "Campo new_name está faltando"

    def test_update_user_not_found(self):
        repo = UserRepositoryMock()
        usecase = UpdateUserUsecase(repo=repo)
        controller = UpdateUserController(usecase=usecase)

        request = HttpRequest(body={
            'user_id': "69",
            'new_name': 'Branco do Branco Branco da Silva'
        })

        response = controller(request=request)

        assert response.status_code == 404
        assert response.body == 'Nenhum item encontrado: user_id'
