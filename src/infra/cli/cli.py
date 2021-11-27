import sys
from src.presentation.adapters.AuthUserAdapter import authUserAdapter

class App:
    def __init__(self) -> None:
        self.args = sys.argv[1:]
    
    def autenticar(self):
        user = self.args[0]
        password = self.args[1]

        authUserAdapter.adapt(user, password)