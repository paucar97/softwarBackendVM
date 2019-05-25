from . import db
from app.models.usuario import Usuario
from sqlachemy import *

class Notificacion(db.Model):
    #name of table in DB
    __tablename__ = 'notificacion'

    #columns in DB
    id_notificacion = db.Column('ID_NOTIFICACION', db.Integer, primary_key = True, autoincrement = True)
    id_semestre = db.Column('ID_SEMESTRE', db.ForeignKey(Semestre.id_semestre), primary_key = True)
    id_usuario = db.Column('ID_USUARIO', db.ForeignKey(Usuario.id_usuario), primary_key = True)
    nombre = db.Column('NOMBRE', db.String(255))
    fecha_creacion = db.Column('FECHA_CREACION', db.DateTime, server_default = func.current_timestamp()) 
    id_actividad = db.Column('ID_ACTIVIDAD', db.Integer, nullable = False)

    def addOne(self,obj):
        db.session.add(obj)
        db.session.flush()
        db.session.commit()
        return obj.id_actividad