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
    id_rubrica_especial = db.Column('ID_RUBRICA_ESPECIAL', db.Integer, nullable = True)
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
    
    @classmethod
    def addOne(self,nombreH,idCurso,idSemestre):
        d = Horario.query.filter(and_(Horario.id_curso == idCurso,Horario.id_semestre == idSemestre,Horario.nombre == nombreH )).first()
        if d is None:
            objHorario = Horario(id_curso = idCurso,id_semestre=idSemestre,nombre = nombreH)
            db.session.add(objHorario)
            db.session.commit()
            db.session.flush()
            return objHorario.id_horario
        else:
            return d.id_horario
    #@classmethod
    #def getHorariosActivosProfesor(self, id_semestre_activo, idProfesor):
    #    puh = Permiso_usuario_horario().getHorarioActivo(id_semestre_activo, idProfesor)
    #    return Horario.query(Horario).join(puh, puh.id_horario == Horario.id_horario).subquery()
    @classmethod
    def getOneClave(self,idCurso,idSemestre,horario):
        d = Horario.query.filter(and_(Horario.id_curso == idCurso,Horario.id_semestre == idSemestre,Horario.nombre == horario)).first()
        return d.id_horario
        
    @classmethod
    def getAll(self,idCurso,idSemestre):
        d = Horario.query.filter(and_(Horario.id_curso== idCurso, Horario.id_semestre == idSemestre)).all()
        return d