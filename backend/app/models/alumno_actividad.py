from . import db
from app.models.permiso_usuario_horario import Permiso_usuario_horario
from app.models.actividad import Actividad
from app.models.grupo import Grupo
from sqlalchemy import *

class Alumno_actividad(db.Model):
    __tablename__ = 'alumno_actividad'

    actividad = db.relationship(Actividad,backref = __tablename__,lazy=True)
    alumno = db.relationship(Permiso_usuario_horario,backref = __tablename__,lazy=True)
    grupo = db.relationship(Grupo,backref = __tablename__,lazy=True)

    id_actividad = db.Column('ID_ACTIVIDAD',db.ForeignKey(Actividad.id_actividad),primary_key=True)
    id_alumno = db.Column('ID_ALUMNO',db.ForeignKey(Permiso_usuario_horario.id_usuario),primary_key=True)
    id_grupo = db.Column('ID_GRUPO',db.ForeignKey(Grupo.id_grupo), nullable=True)

    #Preguntar cual es la etapa
    flag_entregable = db.Column('FLG_ENTREGABLE', db.Integer)
    #Indica si el alumno subio el entregable o no
    flg_calificado = db.Column('FLG_CALIFICADO', db.Integer, default = 0)
    #Verifica si el alumno falto a la sesion o no
    flg_publicado = db.Column('FLG_PUBLICADO', db.Integer, default = 0)

    def addOne(self, obj):
        db.session.add(obj)
        db.session.flush()
        db.session.commit()
        return

    @classmethod
    def updateOne(self, idActividad, flag_entregable1):
        alumnoActividad = Alumno_actividad.query.filter_by(id_actividad=idActividad).first()
        alumnoActividad.flag_entregable = flag_entregable1
        db.session.commit()
        return

    @classmethod
    def getAllAlumnos(self,idActividad):
        return Alumno_actividad.query.filter_by(id_actividad = idActividad).all()

    @classmethod
    def updateGrupo(self,idActividad,idAlumno,idGrupo):
        alumnoActividad=Alumno_actividad.query.filter_by(id_actividad = idActividad,id_alumno = idAlumno).first()
        alumnoActividad.id_grupo = idGrupo
        db.session.commit()
        return
    
    @classmethod
    def calificarAlumno(self, idActividad, idAlumno):
        alumnoActividad = Alumno_actividad.query.filter_by(id_actividad = idActividad, id_alumno = idAlumno).first()
        alumnoActividad.flg_calificado = 1
        db.session.commit()
        return True        

    @classmethod
    def getAllGrupos(self, idActividad):
        return db.session.query(Alumno_actividad.id_grupo).filter(and_(Alumno_actividad.id_actividad == idActividad ,Alumno_actividad.id_grupo.isnot(None) )).distinct()
    
    @classmethod
    def publicarNotas(self, idActividad):
        listaAlumnosActividad = Alumno_actividad.query.filter_by(id_actividad = idActividad).all()
        for alumnoActividad in listaAlumnosActividad:
            alumnoActividad.flg_publicado = 1
        db.session.commit()
        return True

    @classmethod
    def getIdGrupo(self,idActividad,idUsuario):
        d = Alumno_actividad.query.filter_by(id_actividad = idActividad,id_alumno = idUsuario).first()
        print(d)
        return d.id_grupo