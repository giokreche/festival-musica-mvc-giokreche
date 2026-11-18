from flask import render_template, redirect, url_for, flash
from sqlalchemy.exc import IntegrityError
from app import app, db
from app.models.models import Palco
from app.forms import PalcoForm

@app.route("/palcos")
def lista_palcos():
    return render_template("palcos/lista.html", palcos=Palco.query.order_by(Palco.nome).all())

@app.route("/palcos/novo", methods=["GET", "POST"])
def novo_palco():
    form = PalcoForm()
    if form.validate_on_submit():
        db.session.add(Palco(nome=form.nome.data, localizacao=form.localizacao.data, capacidade=form.capacidade.data))
        try:
            db.session.commit()
            flash("Palco cadastrado!", "success")
            return redirect(url_for("lista_palcos"))
        except IntegrityError:
            db.session.rollback()
            flash("Já existe um palco com esse nome.", "warning")
    return render_template("palcos/form.html", form=form, titulo="Novo palco")

@app.route("/palcos/editar/<int:id>", methods=["GET", "POST"])
def editar_palco(id):
    palco = Palco.query.get_or_404(id)
    form = PalcoForm(obj=palco)
    if form.validate_on_submit():
        palco.nome, palco.localizacao, palco.capacidade = form.nome.data, form.localizacao.data, form.capacidade.data
        try:
            db.session.commit()
            flash("Palco atualizado!", "success")
            return redirect(url_for("lista_palcos"))
        except IntegrityError:
            db.session.rollback()
            flash("Já existe um palco com esse nome.", "warning")
    return render_template("palcos/form.html", form=form, titulo="Editar palco")

@app.route("/palcos/deletar/<int:id>", methods=["POST"])
def deletar_palco(id):
    palco = Palco.query.get_or_404(id)
    db.session.delete(palco)
    db.session.commit()
    flash("Palco e suas apresentações foram removidos.", "success")
    return redirect(url_for("lista_palcos"))
