from src.modules.delete_user.app.delete_user_controller import DeleteUserController
from src.modules.delete_user.app.delete_user_usecase import DeleteUserUsecase
from src.shared.helpers.external_interfaces.http_models import HttpRequest
from src.shared.infra.repositories.user_repository_mock import UserRepositoryMock


class Test_DeleteUserController:
    def test_delete_user_controller(self):
            repo = UserRepositoryMock()
            usecase = DeleteUserUsecase(repo=repo)
            controller = DeleteUserController(usecase=usecase)

            request = HttpRequest(body={
                'id': '1'
            })

            response = controller(request=request)

            assert response.status_code == 200
            assert response.body['message'] == 'the user was deleted successfully'

    def test_delete_user_controller_wrong_type(self):
            repo = UserRepositoryMock()
            usecase = DeleteUserUsecase(repo=repo)
            controller = DeleteUserController(usecase=usecase)

            request = HttpRequest(body={
                'id': 'a'
            })

            response = controller(request=request)

            assert response.status_code == 400
            assert response.body == "O campo 'id' não é válido"

    def test_delete_user_controller_missing_parameter(self):
            repo = UserRepositoryMock()
            usecase = DeleteUserUsecase(repo=repo)
            controller = DeleteUserController(usecase=usecase)

            request = HttpRequest(body={
            })

            response = controller(request=request)

            assert response.status_code == 400
            assert response.body == 'Campo id está faltando'

    def test_delete_user_controller_invalid_id(self):
            repo = UserRepositoryMock()
            usecase = DeleteUserUsecase(repo=repo)
            controller = DeleteUserController(usecase=usecase)

            request = HttpRequest(body={
                'id': 2
            })

            response = controller(request=request)

            assert response.status_code == 400
            assert response.body == "O campo 'id' deveria ser do tipo 'str', mas foi recebido 'int'"

    def test_delete_user_controller_no_items_found(self):
            repo = UserRepositoryMock()
            usecase = DeleteUserUsecase(repo=repo)
            controller = DeleteUserController(usecase=usecase)

            request = HttpRequest(body={
                'id': '69'
            })

            response = controller(request=request)

            assert response.status_code == 404
            assert response.body == 'Nenhum item encontrado: id'


