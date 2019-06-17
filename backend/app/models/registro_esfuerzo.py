from . import db
from app.models.usuario import Usuario
from app.models.actividad import Actividad
from sqlalchemy import *

class Registro_esfuerzo(db.Model):
    __tablename__ = 'registro_esfuerzo'
    id_registro_esfuerzo = db.Column('ID_REGISTRO_ESFUERZO', db.Integer,primary_key=True, autoincrement=True)
    
    actividad = db.relationship(Actividad,backref = __tablename__,lazy=True)
    id_actividad = db.Column('ID_ACTIVIDAD',db.ForeignKey(Actividad.id_actividad),primary_key=True)

    flg_activo = db.Column('FLG_ACTIVO', db.Integer, nullable = False, default = 1)