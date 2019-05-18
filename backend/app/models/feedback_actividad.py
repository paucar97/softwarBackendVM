from . import db
from app.models.permiso_usuario_horario import Permiso_usuario_horario
from app.models.actividad import Actividad
class Feedback_actividad(db.Model):
    __tablename__='feedback_actividad'
    id_feedback_actividad = db.Column('ID_FEDDBACK_ACTIVIDAD',db.Integer,primary_key=True, autoincrement=True)

    permiso_usuario_horario = db.relationship(Permiso_usuario_horario,backref=__tablename__)
    actividad = db.relationship(Actividad, backref = __tablename__, lazy =True)

    id_profesor = db.Column('ID_PROFESOR', db.ForeignKey(Permiso_usuario_horario.id_usuario), primary_key=True)
    id_actividad= db.Column('ID_ACTIVIDAD',db.ForeignKey(Actividad.id_actividad),primary_key = True)
    
    comentario = db.Column('COMENTARIO',db.String(100))
    flag_aprobado = db.Column('FLAG_APROBADO',db.Integer)

    def addOne(self,obj):
        db.session.add(obj)
        db.session.flush()
        return 