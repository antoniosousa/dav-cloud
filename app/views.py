from flask import render_template, redirect, flash, url_for
from app import app, db
from app.models import executar_consulta, Url
from app.forms import UrlForm


@app.route("/index")
@app.route("/")
def index():
    consulta = executar_consulta()
    return render_template(
        "index.html",
        consulta=consulta,
    )

@app.route("/dns", methods=['GET', 'POST'])
def dns():
    form = UrlForm()
    if form.validate_on_submit():
        url = Url.query.filter_by(nome=form.nome.data).first()
        if url is None:
            url = Url(nome=form.nome.data)
            url.atualizar_ip_atual()
            db.session.add(url)
            db.session.commit()
        else:
            flash('URL JÁ CADASTRADA')

    urls = Url.query.all()
    for url in urls:
        url.atualizar_ip_novo()
    return render_template("dns.html", url=urls, form=form)