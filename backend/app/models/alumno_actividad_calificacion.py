from . import db
from app.models.alumno_actividad import Alumno_actividad
from app.models.permiso_usuario_horario import Permiso_usuario_horario
from sqlalchemy import *

class Alumno_actividad_calificacion(db.Model):
    __tablename__ = 'alumno_actividad_calificacion'

    alumno_actividad = db.relationship(Alumno_actividad,backref = __tablename__,lazy=True)

    id_actividad = db.Column('ID_ACTIVIDAD',db.Integer,primary_key=True)
    id_alumno = db.Column('ID_ALUMNO',db.Integer,primary_key=True)

    __table_args__ =(
        db.ForeignKeyConstraint(
            ['ID_ACTIVIDAD','ID_ALUMNO'],
            [Alumno_actividad.id_actividad, Alumno_actividad.id_alumno]
        ),
    )

    id_calificador = db.Column('ID_CALIFICADOR',db.Integer, nullable=False)
    nota = db.Column('NOTA',db.Float,nullable= True)
    fecha_revisado = db.Column('FECHA_REVISADO',db.DateTime)
    fecha_modificado = db.Column('FECHA_MODIFICADO', db.DateTime)
    flg_completo = db.Column('FLG_COMPLETO', db.Integer, nullable = False)