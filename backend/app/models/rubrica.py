from . import db
from app.models.usuario import Usuario
from sqlalchemy import *

class Rubrica(db.Model):
    __tablename__='rubrica'
    id_rubrica = db.Column('ID_RUBRICA',db.Integer,primary_key=True, autoincrement=True)
    estado = db.Column('ESTADO', db.Integer, server_default = '1')
    fecha_registro = db.Column('FECHA_REGISTRO',db.DateTime, server_default = func.current_timestamp())
    fecha_validacion = db.Column('FECHA_VALIDACION',db.DateTime)
    fecha_modificacion = db.Column('FECHA_MODIFICACION',db.DateTime)
    flg_rubrica_especial = db.Column('FLG_RUBRICA_ESPECIAL', db.Integer)
    id_usuario_creador = db.Column('ID_USUARIO_CREADOR',db.Integer, nullable = False)
    nombre = db.Column('NOMBRE', db.String(255))

    def addOne(self,obj):
        db.session.add(obj)
        db.session.commit()
        db.session.flush()

        return obj.id_rubrica

    @classmethod
    def obtenerRubrica(self, idRubrica):
        return Rubrica.query.filter_by(id_rubrica = idRubrica).first()