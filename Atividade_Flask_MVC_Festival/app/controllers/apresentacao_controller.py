from flask import render_template, redirect, url_for, flash
from app import app, db
from app.models.models import Apresentacao, Artista
from app.forms import ApresentacaoForm

@app.route("/apresentacoes")
def lista_apresentacoes():
    return render_template("apresentacoes/lista.html", apresentacoes=Apresentacao.query.order_by(Apresentacao.id.desc()).all())

@app.route("/apresentacoes/novo", methods=["GET", "POST"])
def nova_apresentacao():
    form = ApresentacaoForm()
    if form.validate_on_submit():
        item = Apresentacao(titulo=form.titulo.data, data_hora=form.data_hora.data, palco_id=form.palco_id.data)
        item.artistas = Artista.query.filter(Artista.id.in_(form.artistas.data)).all() if form.artistas.data else []
        db.session.add(item)
        db.session.commit()
        flash("Apresentação cadastrada!", "success")
        return redirect(url_for("lista_apresentacoes"))
    return render_template("apresentacoes/form.html", form=form, titulo="Nova apresentação")

@app.route("/apresentacoes/editar/<int:id>", methods=["GET", "POST"])
def editar_apresentacao(id):
    item = Apresentacao.query.get_or_404(id)
    form = ApresentacaoForm(obj=item)
    if not form.is_submitted():
        form.artistas.data = [a.id for a in item.artistas]
    if form.validate_on_submit():
        item.titulo, item.data_hora, item.palco_id = form.titulo.data, form.data_hora.data, form.palco_id.data
        item.artistas = Artista.query.filter(Artista.id.in_(form.artistas.data)).all() if form.artistas.data else []
        db.session.commit()
        flash("Apresentação atualizada!", "success")
        return redirect(url_for("lista_apresentacoes"))
    return render_template("apresentacoes/form.html", form=form, titulo="Editar apresentação")

@app.route("/apresentacoes/deletar/<int:id>", methods=["POST"])
def deletar_apresentacao(id):
    item = Apresentacao.query.get_or_404(id)
    db.session.delete(item)
    db.session.commit()
    flash("Apresentação removida.", "success")
    return redirect(url_for("lista_apresentacoes"))
