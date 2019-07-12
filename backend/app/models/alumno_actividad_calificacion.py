from . import db
from app.models.alumno_actividad import Alumno_actividad
from app.models.permiso_usuario_horario import Permiso_usuario_horario
from app.models.rubrica import Rubrica
from sqlalchemy import *

class Alumno_actividad_calificacion(db.Model):
    __tablename__ = 'alumno_actividad_calificacion'

    alumno_actividad = db.relationship(Alumno_actividad,backref = __tablename__,lazy=True)

    id_actividad = db.Column('ID_ACTIVIDAD',db.Integer,primary_key=True)
    id_alumno = db.Column('ID_ALUMNO',db.Integer,primary_key=True)
    id_rubrica = db.Column('ID_RUBRICA', db.ForeignKey(Rubrica.id_rubrica), primary_key = True)
    __table_args__ =(
        db.ForeignKeyConstraint(
            ['ID_ACTIVIDAD','ID_ALUMNO'],
            [Alumno_actividad.id_actividad, Alumno_actividad.id_alumno]
        ),
    )

    
    id_calificador = db.Column('ID_CALIFICADOR',db.Integer, primary_key=True, nullable=False)
    nota = db.Column('NOTA',db.Float, nullable= True)
    fecha_revisado = db.Column('FECHA_REVISADO',db.DateTime)
    fecha_modificado = db.Column('FECHA_MODIFICADO', db.DateTime)
    flg_completo = db.Column('FLG_COMPLETO', db.Integer, nullable = False)
    comentario_alumno = db.Column('COMENTARIO_ALUMNO',db.String(150),nullable = True)
    comentario_jp = db.Column('COMENTARIO_JP',db.String(150),nullable = True)
    flg_falta = db.Column('FLG_FALTA', db.Integer, default = 0)
    
    def addOne(self, obj):
        db.session.add(obj)
        db.session.flush()
        db.session.commit()
        return True
    
    @classmethod
    def updateOne(self, idActividad, flag_entregable1):
        alumnoActividad = Alumno_actividad.query.filter_by(id_actividad=idActividad).first()
        alumnoActividad.flag_entregable = flag_entregable1
        db.session.commit()
        return
    @classmethod
    def updateComentarioAlumno(self,idActividad,idAlumno,comentario):
        alumnoActividad = Alumno_actividad.query.filter_by(id_actividad=idActividad,id_alumno=idAlumno).first()
        alumnoActividad.comentario_alumno=comentario
        db.session.commit()
        return

    @classmethod
    def updateComentarioJP(self,idActividad,idAlumno,idProfesor,comentario):
        alumnoActividad = Alumno_actividad.query.filter_by(id_actividad=idActividad,id_alumno=idAlumno,id_calificador=idProfesor).first()
        alumnoActividad.comentario_jp=comentario
        db.session.commit()
        return

    @classmethod
    def editarNotaAlumno(self, idActividad, idAlumno, idJpAnt, idJpN ,nota, flgFalta, flgCompleto):
        print(idActividad, idAlumno, idJpAnt)
        alumnoActividad = Alumno_actividad_calificacion.query.filter_by(id_actividad = idActividad, id_alumno = idAlumno, id_calificador = idJpAnt).first()
        alumnoActividad.nota = nota
        alumnoActividad.flg_falta = flgFalta
        alumnoActividad.fecha_modificado = func.current_timestamp()
        alumnoActividad.id_calificador = idJpN
        alumnoActividad.flg_completo = flgCompleto
        db.session.commit()
        return True

    @classmethod
    def getAllAlumnos(self,idActividad,idRubrica):
        return Alumno_actividad_calificacion.query.filter_by(id_actividad = idActividad,id_rubrica = idRubrica).all()
    
    @classmethod
    def getNotaGrupo(self,idActividad,idAlumno,idRubrica):
        return Alumno_actividad_calificacion.query.filter_by(id_actividad = idActividad, id_alumno = idAlumno,id_rubrica = idRubrica).first()

    @classmethod
    def updateOneNota(self,idActividad,idAlumno,idRubrica,nota):
        alumnoAspectoNota = Alumno_actividad_calificacion.query.filter_by(id_actividad = idActividad, id_alumno = idAlumno, id_rubrica = idRubrica).first()
        #print("=ANTES=",alumnoAspectoNota.nota)
        alumnoAspectoNota.nota = nota
        #print("=DSP=",alumnoAspectoNota.nota)
        db.session.commit()
        return