from flask import render_template, redirect, url_for, flash
from sqlalchemy.exc import IntegrityError
from app import app, db
from app.models.models import Artista, Contrato
from app.forms import ContratoForm

@app.route("/artistas/<int:artista_id>/contrato", methods=["GET", "POST"])
def gerenciar_contrato(artista_id):
    artista = Artista.query.get_or_404(artista_id)
    contrato = artista.contrato
    form = ContratoForm(obj=contrato)
    if form.validate_on_submit():
        if contrato is None:
            contrato = Contrato(artista=artista)
            db.session.add(contrato)
        contrato.cache = form.cache.data
        contrato.data_assinatura = form.data_assinatura.data
        try:
            db.session.commit()
            flash("Contrato salvo!", "success")
            return redirect(url_for("lista_artistas"))
        except IntegrityError:
            db.session.rollback()
            flash("Este artista já possui um contrato.", "warning")
    return render_template("contratos/form.html", form=form, artista=artista)
