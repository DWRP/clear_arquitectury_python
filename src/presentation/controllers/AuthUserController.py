from src.presentation.controllers.AuthUserDTO import AuthUserDTO
from src.domain.useCases.AuthUser import AuthUser

class AuthUserController:
    def __init__(self, authUserUseCase) -> None:
        self.authUserUseCase: AuthUser = authUserUseCase

    def command(self, data:AuthUserDTO):
        return self.authUserUseCase.handle(*data.getUserAndPass())