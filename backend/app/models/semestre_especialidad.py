from . import db
from app.models.especialidad import Especialidad
from app.models.semestre import Semestre
from app.models.usuario import Usuario

class Semestre_especialidad(db.Model):
    #name of table in DB
    __tablename__ = 'semestre_especialidad'
    
    #relationships
    especialidad = db.relationship(Especialidad, backref=__tablename__, lazy=True)
    usuario = db.relationship(Usuario, backref=__tablename__)
    semestre = db.relationship(Semestre, backref=__tablename__)

    #columns in DB
    id_coordinador = db.Column('ID_COORDINADOR', db.ForeignKey(Usuario.id_usuario))
    id_especialidad = db.Column('ID_ESPECIALIDAD', db.ForeignKey(Especialidad.id_especialidad), primary_key=True)
    id_semestre = db.Column('ID_SEMESTRE', db.ForeignKey(Semestre.id_semestre), primary_key=True)

    @classmethod
    def activacionSemestre(idSemestre):
         aux = Semestre_especialidad.query.filter_by(id_semestre = idSemestre).all()

         if aux == [] :
             especialidades = especialidades().getAll()
             for especialidad in especialidades:
                 objSemestreEsp = Semestre_especialidad(id_especialidad = especialidad.id_especialidad,id_semestre = idSemestre)
                 Semestre_especialidad().addOne(objSemestreEsp) 
        else:
            return
    def obtenerEspecialidadActivo(self,idsemestre):
        return Semestre.query.filter_by(id_semestre=idsemestre).all()
