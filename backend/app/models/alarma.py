from . import db
from sqlalchemy import *

class Alarma(db.Model):
    __tablename__='alarma'
    id_alarma = db.Column('ID_ALARMA',db.Integer, primary_key=True, autoincrement=True)
    fecha_registro = db.Column('FECHA_REGISTRO',db.DateTime, server_default=func.current_timestamp()) #Manegarlo como String es mas facil xd
    fecha_ejecucion = db.Column('FECHA_EJECUCION',db.DateTime)
    fecha_eliminado = db.Column('FECHA_ELIMINADO', db.DateTime)
    flg_disponible = db.Column('FLG_DISPONIBLE',db.Integer)
    mensaje = db.Column('MENSAJE', db.String(500))
    asunto = db.Column('ASUNTO',db.String(100))
    nombre = db.Column('NOMBRE',db.String(20))

    @classmethod
    def addOne(self, obj):
        db.session.add(obj)
        db.session.flush()
        db.session.commit()
        return obj.id_alarma