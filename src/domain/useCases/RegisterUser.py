from src.domain.entities.User import Usuario
from src.domain.entities.UserRepository import UserRepository

class AuthUser:
    def __init__(self, repository) -> None:
        self.__repository: UserRepository = repository
    
    def handle(self, matricula: str, nome:str, senha: str):
        usuario = Usuario(matricula, nome, senha)
        self.__repository.register(usuario)
        
        return {
            "sucess": True
        }