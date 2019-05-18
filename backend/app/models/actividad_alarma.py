from . import db
from app.models.actividad import Actividad
from app.models.alarma import Alarma

class Actividad_alarma(db.Model):
    __tablename__='actividad_alarma'
    actividad = db.relationship(Actividad,backref = __tablename__,lazy=True)
    alarma = db.relationship(Alarma,backref = __tablename__,lazy=True)
    id_actividad  = db.Column('ID_ACTIVIDAD',db.ForeignKey(Actividad.id_actividad),primary_key = True)
    id_alarma= db.Column('ID_ALARMA',db.ForeignKey(Alarma.id_alarma),primary_key=True)