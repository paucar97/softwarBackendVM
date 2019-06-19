from . import db
from app.models.usuario import Usuario
from app.models.actividad import Actividad
from app.models.horario import Horario
from sqlalchemy import *

class Registro_esfuerzo(db.Model):
    __tablename__ = 'registro_esfuerzo'
    id_registro_esfuerzo = db.Column('ID_REGISTRO_ESFUERZO', db.Integer,primary_key=True, autoincrement=True)
    
    tipo = db.Column('TIPO', db.Integer, nullable = False)
    #1 para actividad y 2 para el horario
    
    actividad = db.relationship(Actividad,backref = __tablename__,lazy=True)
    horario = db.relationship(Horario,backref = __tablename__,lazy=True)
    
    id_actividad = db.Column('ID_ACTIVIDAD',db.ForeignKey(Actividad.id_actividad),primary_key=False, nullable = True)
    id_horario = db.Column('ID_HORARIO',db.ForeignKey(Horario.id_horario),primary_key=False, nullable = True)
    
    flg_activo = db.Column('FLG_ACTIVO', db.Integer, nullable = False, default = 1)
    id_usuario_creador = db.Column('ID_USUARIO_CREADOR', db.Integer, nullable = False)
    fecha_modificacion = db.Column('FECHA_MODIFICACION',db.DateTime)
    fecha_creacion = db.Column('FECHA_CREACION', db.DateTime, server_default = func.current_timestamp())
    
    def addOne(self,obj):
        db.session.add(obj)
        db.session.flush()
        db.session.commit()
        return obj.id_registro_esfuerzo