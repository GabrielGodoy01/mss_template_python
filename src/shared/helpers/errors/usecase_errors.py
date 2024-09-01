from src.shared.helpers.errors.base_error import BaseError

class NoItemsFound(BaseError):
    def __init__(self, message: str):
        super().__init__(f'Nenhum item encontrado: {message}')

class DuplicatedItem(BaseError):
    def __init__(self, message: str):
        super().__init__(f'O item já existe: {message}')
        
class ForbiddenAction(BaseError):
    def __init__(self, message: str):
        super().__init__(f'Essa ação é proibida: {message}')
