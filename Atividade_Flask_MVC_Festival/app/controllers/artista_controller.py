from flask import render_template, redirect, url_for, flash
from app import app, db
from app.models.models import Artista
from app.forms import ArtistaForm

@app.route("/artistas")
def lista_artistas():
    return render_template("artistas/lista.html", artistas=Artista.query.order_by(Artista.nome).all())

@app.route("/artistas/novo", methods=["GET", "POST"])
def novo_artista():
    form = ArtistaForm()
    if form.validate_on_submit():
        db.session.add(Artista(nome=form.nome.data, genero_musical=form.genero_musical.data))
        db.session.commit()
        flash("Artista cadastrado!", "success")
        return redirect(url_for("lista_artistas"))
    return render_template("artistas/form.html", form=form, titulo="Novo artista")

@app.route("/artistas/editar/<int:id>", methods=["GET", "POST"])
def editar_artista(id):
    artista = Artista.query.get_or_404(id)
    form = ArtistaForm(obj=artista)
    if form.validate_on_submit():
        artista.nome, artista.genero_musical = form.nome.data, form.genero_musical.data
        db.session.commit()
        flash("Artista atualizado!", "success")
        return redirect(url_for("lista_artistas"))
    return render_template("artistas/form.html", form=form, titulo="Editar artista")

@app.route("/artistas/deletar/<int:id>", methods=["POST"])
def deletar_artista(id):
    artista = Artista.query.get_or_404(id)
    db.session.delete(artista)
    db.session.commit()
    flash("Artista removido.", "success")
    return redirect(url_for("lista_artistas"))
