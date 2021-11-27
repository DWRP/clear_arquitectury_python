from src.domain.entities.UserRepository import UserRepository

class AuthUser:
    def __init__(self, repository) -> None:
        self.__repository: UserRepository = repository
    
    def handle(self, matricula: str, senha: str):
        return self.__repository.auth(matricula, senha)