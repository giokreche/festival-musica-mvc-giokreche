from app import db

apresentacao_artista = db.Table(
    "apresentacao_artista",
    db.Column("apresentacao_id", db.Integer, db.ForeignKey("apresentacoes.id"), primary_key=True),
    db.Column("artista_id", db.Integer, db.ForeignKey("artistas.id"), primary_key=True),
)

class Palco(db.Model):
    __tablename__ = "palcos"
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False, unique=True)
    localizacao = db.Column(db.String(120), nullable=False)
    capacidade = db.Column(db.Integer, nullable=False)
    apresentacoes = db.relationship("Apresentacao", back_populates="palco", cascade="all, delete-orphan")

class Apresentacao(db.Model):
    __tablename__ = "apresentacoes"
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(120), nullable=False)
    data_hora = db.Column(db.String(30), nullable=False)
    palco_id = db.Column(db.Integer, db.ForeignKey("palcos.id"), nullable=False)
    palco = db.relationship("Palco", back_populates="apresentacoes")
    artistas = db.relationship("Artista", secondary=apresentacao_artista, back_populates="apresentacoes")

class Artista(db.Model):
    __tablename__ = "artistas"
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(120), nullable=False)
    genero_musical = db.Column(db.String(80), nullable=False)
    apresentacoes = db.relationship("Apresentacao", secondary=apresentacao_artista, back_populates="artistas")
    contrato = db.relationship("Contrato", back_populates="artista", uselist=False, cascade="all, delete-orphan")

class Contrato(db.Model):
    __tablename__ = "contratos"
    id = db.Column(db.Integer, primary_key=True)
    cache = db.Column(db.Numeric(12, 2), nullable=False)
    data_assinatura = db.Column(db.String(20), nullable=False)
    artista_id = db.Column(db.Integer, db.ForeignKey("artistas.id"), nullable=False, unique=True)
    artista = db.relationship("Artista", back_populates="contrato")
