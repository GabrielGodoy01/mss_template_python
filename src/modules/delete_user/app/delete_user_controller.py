from src.shared.helpers.errors.usecase_errors import NoItemsFound
from src.shared.helpers.external_interfaces.external_interface import IRequest, IResponse
from .delete_user_usecase import DeleteUserUsecase
from .delete_user_viewmodel import DeleteUserViewmodel
from src.shared.helpers.errors.controller_errors import MissingParameters, WrongTypeParameter
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.helpers.external_interfaces.http_codes import OK, NotFound, BadRequest, InternalServerError


class DeleteUserController:

    def __init__(self, usecase: DeleteUserUsecase):
        self.DeleteUserUsecase = usecase

    def __call__(self, request: IRequest) -> IResponse:
        try:
            if request.data.get('id') is None:
                raise MissingParameters('id')

            if type(request.data.get('id')) != str:
                raise WrongTypeParameter(
                    fieldName="id",
                    fieldTypeExpected="str",
                    fieldTypeReceived=request.data.get('id').__class__.__name__
                )
            if not request.data.get('id').isdecimal():
                raise EntityError("id")

            user = self.DeleteUserUsecase(
                id=int(request.data.get('id'))
            )

            viewmodel = DeleteUserViewmodel(user=user)

            return OK(viewmodel.to_dict())

        except NoItemsFound as err:

            return NotFound(body=err.message)

        except MissingParameters as err:

            return BadRequest(body=err.message)

        except WrongTypeParameter as err:

            return BadRequest(body=err.message)

        except EntityError as err:

            return BadRequest(body=err.message)

        except Exception as err:

            return InternalServerError(body=err.args[0])
