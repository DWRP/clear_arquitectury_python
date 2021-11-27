from src.infra.repositories.UserRepositoryInMemory import UserRepositoryInMemory
from src.domain.useCases.AuthUser import AuthUser
from src.presentation.controllers.AuthUserController import AuthUserController

def factory():
    repository = UserRepositoryInMemory()
    useCase = AuthUser(repository)
    controller = AuthUserController(useCase)
    return controller

makeAuthUserController = factory()