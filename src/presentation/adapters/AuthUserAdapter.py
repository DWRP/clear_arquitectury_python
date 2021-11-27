from src.presentation.controllers.AuthUserDTO import AuthUserDTO
from src.presentation.factories.AuthFactory import makeAuthUserController

class AuthUserAdapter:
    def adapt(self, matricula, senha):
        userDTO = AuthUserDTO(matricula, senha)
        return makeAuthUserController.command(userDTO)

authUserAdapter = AuthUserAdapter()