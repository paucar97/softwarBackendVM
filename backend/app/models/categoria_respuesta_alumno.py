from . import db
from app.models.usuario import Usuario
from app.models.categoria import Categoria
from sqlalchemy import *

class Categoria_respuesta_alumno(db.Model):
    __tablename__= 'categoria_respuesta_alumno'
    
    categoria = db.relationship(Categoria,backref = __tablename__,lazy=True)
    id_categoria = db.Column('ID_CATEGORIA',db.ForeignKey(Categoria.id_categoria),primary_key=True)
    
    
    id_alumno = db.Column('ID_ALUMNO',db.Integer,primary_key=True, autoincrement = False)

    descripcion = descripcion = db.Column('DESCRIPCION', db.String(255), nullable = False)
    horas_planificadas = db.Column('HORAS_PLANIFICADAS',db.Integer, nullable = False)
    horas_reales = db.Column('HORAS_REALES',db.Integer, nullable = False)
    