class Usuario:
    def __init__(self, matricula: int, nome: str, senha: str) -> None:
        self.matricula = matricula
        self.nome = nome
        self.senha = self.isValidPassword(senha)
    
    def __isValid(self, _):
        return True

    def isValidPassword(self, password):
        #password
        if(self.__isValid(password)):
            return password
        else:
            raise AttributeError("Password is wrong!")