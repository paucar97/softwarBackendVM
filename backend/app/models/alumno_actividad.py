from . import db
from app.models.permiso_usuario_horario import Permiso_usuario_horario
from app.models.actividad import Actividad

class Alumno_actividad(db.Model):
    __tablename__ = 'alumno_actividad'

    actividad = db.relationship(Actividad,backref = __tablename__,lazy=True)
    alumno = db.relationship(Permiso_usuario_horario,backref = __tablename__,lazy=True)
    
    id_actividad = db.Column('ID_ACTIVIDAD',db.ForeignKey(Actividad.id_actividad),primary_key=True)    
    id_alumno = db.Column('ID_ALUMNO',db.ForeignKey(Permiso_usuario_horario.id_usuario),primary_key=True)
    id_jp = db.Column('ID_JP',db.Integer,nullable=True)
    
    nota  = db.Column('NOTA',db.Float,nullable= True)
    flg_activo = db.Column('FLG_ACTIVO',db.Integer, default = 1)
    etapa = db.Column('ETAPA',db.Integer)
    #Preguntar cual es la etapa
    flag_entregable = db.Column('FLG_ENTREGABLE',db.Integer)
    #Indica si el alumno subio el entregable o no
    fecha_modificado = db.Column('FECHA_MODIFICADO',db.DateTime)
    fecha_revisado = db.Column('FECHA_REVISADO',db.DateTime)
    comentario = db.Column('COMENTARIO',db.String(150),nullable = True)

    def addOne(self,obj):
        db.session.add(obj)
        db.session.flush()
        return 

    @classmethod
    def updateOne(self,idActividad,flag_entregable1):
        alumnoActividad=Alumno_actividad.query.filter_by(id_actividad = idActividad).first()
        alumnoActividad.flag_entregable=flag_entregable1
        db.session.commit()
        return


    @classmethod
    def getAllAlumnos(self,idActividad):
        return Alumno_actividad.query.filter_by(id_actividad = idActividad).all()