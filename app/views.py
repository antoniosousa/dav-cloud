from flask import render_template
from app import app
from app.models import executar_consulta


@app.route("/")
def index():
    consulta = executar_consulta()
    return render_template(
        "index.html",
        consulta=consulta,
    )