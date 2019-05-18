from . import db
from app.models.encuesta_pregunta import Encuesta_pregunta
from app.models.permiso_usuario_horario import Permiso_usuario_horario
from app.models.horario_encuesta import Horario_encuesta

class Alumno_encuesta_respuesta(db.Model):
    __tablename__='alumno_encuesta_respuesta'
    encuesta_respuesta = db.relationship(Encuesta_pregunta, backref=__tablename__, lazy = True)
    permiso_usuario_horario = db.relationship(Permiso_usuario_horario,backref=__tablename__, lazy = True)
    horario_encuesta = db.relationship(Horario_encuesta,backref=__tablename__, lazy = True)

    id_horario = db.Column('ID_HORARIO',db.Integer,primary_key=True)
    id_encuesta = db.Column('ID_ENCUESTA',db.Integer,primary_key=True)

    __table_args__ =(
        db.ForeignKeyConstraint(
            ['ID_HORARIO','ID_ENCUESTA'],
            [Horario_encuesta.id_horario,Horario_encuesta.id_encuesta]
        ),
    )

    id_alumno = db.Column('ID_ALUMNO',db.ForeignKey(Permiso_usuario_horario.id_usuario),primary_key=True)
    id_pregunta = db.Column('ID_PREGUNTA',db.ForeignKey(Encuesta_pregunta.id_pregunta),primary_key=True)
    respuesta = db.Column('RESPUESTA', db.String(500))
    desempenho  = db.Column('DESEMPENHO',db.String(25))
    