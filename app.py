# from src.infra.http.Flask import app
# app.run(port=8080)

from src.infra.cli.cli import App

app = App()
app.autenticar()