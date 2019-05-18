from . import db
from app.models.curso import Curso
from sqlalchemy import and_

#from app.models.permiso_usuario_horario import Permiso_usuario_horario

class Horario(db.Model):
    #name of table in DB
    __tablename__='horario'
    #columns in DB
    id_horario  = db.Column('ID_HORARIO',db.Integer,primary_key = True, autoincrement=True)
    curso = db.relationship(Curso,backref = __tablename__, lazy = True)
    id_curso = db.Column('ID_CURSO',db.ForeignKey(Curso.id_curso),primary_key = True)
    id_semestre = db.Column('ID_SEMESTRE', db.Integer, nullable = False)
    nombre = db.Column('NOMBRE',db.String(10))
    #index2 = db.Index('idx_horario', id_horario, id_curso, id_especialidad, id_semestre, unique=True)

    @classmethod
    def getOne(self,idHorario):
        return Horario.query.filter_by(id_horario=idHorario).first()
    @classmethod
    def obtenerCurso(self, idHorario):
        return db.session.query(Curso, Horario).filter(Horario.id_horario == idHorario).first()

    @classmethod
    def obtenerHorariosXCurso(self, idCurso):
        return Horario.query.filter_by(id_curso == idCurso).all()

    #@classmethod
    #def getHorariosActivosProfesor(self, id_semestre_activo, idProfesor):
    #    puh = Permiso_usuario_horario().getHorarioActivo(id_semestre_activo, idProfesor)
    #    return Horario.query(Horario).join(puh, puh.id_horario == Horario.id_horario).subquery()
  