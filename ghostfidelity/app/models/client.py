from app import db
import uuid
from sqlalchemy.dialects.postgresql import UUID
from datetime import date

class Client(db.Model):
    __tablename__ = "clients"

    uuid = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    prenom = db.Column(db.String(100), nullable=False)
    nom = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
    birthday_date = db.Column(db.Date, nullable=False)
    nombre_visites = db.Column(db.Integer, default=0)
    avancement_visite = db.Column(db.Integer, default=0)
    filleuls = db.Column(db.Integer, default=0)
    avancement_parrainage = db.Column(db.Integer, default=0)
