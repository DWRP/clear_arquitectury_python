from src.domain.entities.User import Usuario
from src.domain.entities.UserRepository import UserRepository

class UserRepositoryInMemory(UserRepository):
    def auth(self, matricula: int, senha:str):
        return {
            "sucess": True
        }
    
    def register(self, usuario: Usuario) -> None:
        pass