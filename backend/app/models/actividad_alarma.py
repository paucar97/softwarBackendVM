from . import db
from app.models.actividad import Actividad
from app.models.alarma import Alarma
from sqlalchemy import *
class Actividad_alarma(db.Model):
    __tablename__='actividad_alarma'
    actividad = db.relationship(Actividad,backref = __tablename__,lazy=True)
    alarma = db.relationship(Alarma,backref = __tablename__,lazy=True)
    id_actividad  = db.Column('ID_ACTIVIDAD',db.ForeignKey(Actividad.id_actividad),primary_key = True)
    id_alarma= db.Column('ID_ALARMA',db.ForeignKey(Alarma.id_alarma),primary_key=True)

    @classmethod
    def addOne(self,obj):
        db.session.add(obj)
        db.session.flush()
        db.session.commit()
        return

    @classmethod
    def getAll(self,idActividad):
        l= db.session.query(Actividad_alarma,Alarma).join(Alarma).filter(and_(Actividad_alarma.id_actividad == idActividad,Alarma.flg_disponible== 1))
        return l 

    @classmethod
    def deleteOne(self,idAlarma):
        Actividad_alarma.query.filter_by(id_alarma=idAlarma).delete()
        db.session.commit()
        return 