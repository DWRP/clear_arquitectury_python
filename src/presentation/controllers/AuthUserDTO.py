class AuthUserDTO:
    def __init__(self, matricula:str, senha: str) -> None:
        self.__matricula = matricula
        self.__senha = senha

    def getUserAndPass(self):
        return [self.__matricula, self.__senha]