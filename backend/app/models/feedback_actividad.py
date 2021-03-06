from . import db
from app.models.permiso_usuario_horario import Permiso_usuario_horario
from app.models.actividad import Actividad
from sqlalchemy import *

class Feedback_actividad(db.Model):
    __tablename__='feedback_actividad'
    id_feedback_actividad = db.Column('ID_FEDDBACK_ACTIVIDAD',db.Integer,primary_key=True, autoincrement=True)

    actividad = db.relationship(Actividad, backref = __tablename__, lazy =True)

    id_actividad= db.Column('ID_ACTIVIDAD',db.ForeignKey(Actividad.id_actividad),primary_key = True)
    
    id_profesor_aprobo = db.Column('ID_PROFESOR', db.Integer, nullable = True)
    id_jp_reviso = db.Column('ID_JP_REVISO', db.Integer, nullable = False)
    fecha_aprobado = db.Column('FECHA_APROBADO', db.DateTime, nullable = True)
    fecha_creacion = db.Column('FECHA_CREACION', db.DateTime, nullable = False, server_default = func.current_timestamp())
    comentario = db.Column('COMENTARIO',db.String(100))
    flag_aprobado = db.Column('FLAG_APROBADO',db.Integer)
    flg_respondido = db.Column('FLG_RESPONDIDO', db.Integer, default = 0) 
    
    def addOne(self,obj):
        db.session.add(obj)
        db.session.flush()
        return 
    
    @classmethod
    def responderFeedback(self, idFeedbackActividad, comentario, flgAprobado, idProfesor):
        feedbackAnalizando = Feedback_actividad.query.filter(and_(Feedback_actividad.id_feedback_actividad == idFeedbackActividad)).first()
        feedbackAnalizando.comentario = comentario
        feedbackAnalizando.flag_aprobado = flgAprobado
        feedbackAnalizando.id_profesor_aprobo = idProfesor
        aux = db.session.commit()
        return aux