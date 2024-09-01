from src.shared.helpers.errors.base_error import BaseError


class MissingParameters(BaseError):
    def __init__(self, message: str):
        super().__init__(f'Campo {message} está faltando')
class WrongTypeParameter(BaseError):
    def __init__(self, fieldName: str, fieldTypeExpected: str, fieldTypeReceived: str):
        super().__init__(f"O campo '{fieldName}' deveria ser do tipo '{fieldTypeExpected}', mas foi recebido '{fieldTypeReceived}'")