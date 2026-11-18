from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Importar os models registra as tabelas no SQLAlchemy.
from app.models.models import Palco, Apresentacao, Artista, Contrato  # noqa: E402,F401

# Os controllers ficam no fim: eles importam app e db deste pacote.
from app.controllers import (  # noqa: E402,F401
    index_controller,
    palco_controller,
    artista_controller,
    apresentacao_controller,
    contrato_controller,
)
