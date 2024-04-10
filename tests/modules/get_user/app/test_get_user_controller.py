from src.modules.get_user.app.get_user_controller import GetUserController
from src.modules.get_user.app.get_user_usecase import GetUserUsecase
from src.shared.helpers.external_interfaces.http_models import HttpRequest
from src.shared.infra.external.observability.observability_mock import ObservabilityMock
from src.shared.infra.repositories.user_repository_mock import UserRepositoryMock

observability = ObservabilityMock(module_name="get_user")

class Test_GetUserController:
    def test_get_user_controller(self):
        repo = UserRepositoryMock()
        usecase = GetUserUsecase(repo=repo)
        controller = GetUserController(usecase=usecase)

        request = HttpRequest(query_params={
            'id': str(repo.users[1].id)
        })

        response = controller(request=request)

        assert response.status_code == 200
        assert response.body['id'] == repo.users[1].id
        assert response.body['name'] == repo.users[1].name
        assert response.body['state'] == repo.users[1].state.value

    def test_get_user_controller_missing_parameters(self):
        repo = UserRepositoryMock()
        usecase = GetUserUsecase(repo=repo)
        controller = GetUserController(usecase=usecase)

        request = HttpRequest(query_params={})

        response = controller(request=request)

        assert response.status_code == 400
        assert response.body == 'Field id is missing'


    def test_get_user_contoller_wrong_type_parameter(self):
        repo = UserRepositoryMock()
        usecase = GetUserUsecase(repo=repo)
        controller = GetUserController(usecase=usecase)

        request = HttpRequest(query_params={
            'id': 999
        })

        response = controller(request=request)

        assert response.status_code == 400
        assert response.body == "Field id isn't in the right type.\n Received: int.\n Expected: str"

    def test_get_user_contoller_entity_error(self):
        repo = UserRepositoryMock()
        usecase = GetUserUsecase(repo=repo)
        controller = GetUserController(usecase=usecase)

        request = HttpRequest(query_params={
            'id': 'abc'
        })

        response = controller(request=request)

        assert response.status_code == 400
        assert response.body == 'Field id is not valid'

    def test_get_user_controller_no_items_found(self):
        repo = UserRepositoryMock()
        usecase = GetUserUsecase(repo=repo)
        controller = GetUserController(usecase=usecase)

        request = HttpRequest(query_params={
            'id': str(999)
        })

        response = controller(request=request)

        assert response.status_code == 404
        assert response.body == 'No items found for id'
