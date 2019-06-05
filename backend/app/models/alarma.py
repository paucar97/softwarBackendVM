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

    def json(self):
        d =dict()
        d['idAlarma'] = self.id_alarma
        d['fechaEjecucion'] = self.fecha_ejecucion.__str__()
        d['nombre'] = self.nombre
        d['mensaje'] = self.mensaje
        d['asunto'] = self.asunto
        return d

    @classmethod
    def addOne(self, obj):
        db.session.add(obj)
        db.session.flush()
        db.session.commit()
        return obj.id_alarma

    @classmethod
    def updateOne(self,idAlarma,nombre,asunto,mensaje,fechaEjecucion):
        alarma = Alarma.query.filter_by(id_alarma = idAlarma).first()
        alarma.nombre = nombre
        alarma.asunto = asunto
        alarma.mensaje = mensaje
        alarma.fecha_ejecucion = fechaEjecucion
        db.session.commit()
        return