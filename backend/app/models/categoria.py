from . import db
from app.models.registro_esfuerzo import Registro_esfuerzo
from sqlalchemy import *

class Categoria(db.Model):
    __tablename__ = 'categoria'
    id_categoria = db.Column('ID_CATEGORIA',db.Integer,primary_key=True, autoincrement=True)
    
    registro_esfuerzo = db.relationship(Registro_esfuerzo,backref = __tablename__,lazy=True)
    id_registro_esfuerzo = db.Column('ID_REGISTRO_ESFUERZO',db.ForeignKey(Registro_esfuerzo.id_registro_esfuerzo),primary_key=True)
    
    descripcion = db.Column('DESCRIPCION', db.String(255), nullable = False)
    flg_activo = db.Column('FLG_ACTIVO', db.Integer, nullable = False, default = 1)
    fecha_registro = db.Column('FECHA_REGISTRO',db.DateTime, server_default = func.current_timestamp())