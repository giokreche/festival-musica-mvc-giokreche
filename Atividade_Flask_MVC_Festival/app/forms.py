from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, DecimalField, SelectField, SelectMultipleField, SubmitField
from wtforms.validators import DataRequired, NumberRange, Length
from app.models.models import Palco, Artista

class PalcoForm(FlaskForm):
    nome = StringField("Nome do palco", validators=[DataRequired(), Length(max=100)])
    localizacao = StringField("Localização", validators=[DataRequired(), Length(max=120)])
    capacidade = IntegerField("Capacidade", validators=[DataRequired(), NumberRange(min=1)])
    submit = SubmitField("Salvar")

class ArtistaForm(FlaskForm):
    nome = StringField("Nome do artista/banda", validators=[DataRequired(), Length(max=120)])
    genero_musical = StringField("Gênero musical", validators=[DataRequired(), Length(max=80)])
    submit = SubmitField("Salvar")

class ApresentacaoForm(FlaskForm):
    titulo = StringField("Título da apresentação", validators=[DataRequired(), Length(max=120)])
    data_hora = StringField("Data e horário (ex.: 2026-12-10 20:00)", validators=[DataRequired(), Length(max=30)])
    palco_id = SelectField("Palco", coerce=int, validators=[DataRequired()])
    artistas = SelectMultipleField("Artistas participantes", coerce=int)
    submit = SubmitField("Salvar")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.palco_id.choices = [(p.id, p.nome) for p in Palco.query.order_by(Palco.nome).all()]
        self.artistas.choices = [(a.id, a.nome) for a in Artista.query.order_by(Artista.nome).all()]

class ContratoForm(FlaskForm):
    cache = DecimalField("Cachê (R$)", places=2, validators=[DataRequired(), NumberRange(min=0)])
    data_assinatura = StringField("Data de assinatura (AAAA-MM-DD)", validators=[DataRequired(), Length(max=20)])
    submit = SubmitField("Salvar")
