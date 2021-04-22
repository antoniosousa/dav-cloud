from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from src.models import executar_consulta


app = Flask(__name__)
bootstratp = Bootstrap(app)


@app.route("/")
def index():
    consulta = executar_consulta()
    return render_template(
        "index.html",
        consulta=consulta,
    )
