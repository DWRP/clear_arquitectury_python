from flask import Flask

from src.presentation.adapters.AuthUserAdapter import authUserAdapter


app = Flask(__name__)

@app.route('/', methods=["GET"])
def hello():
    return authUserAdapter.adapt("1234", "pudim")