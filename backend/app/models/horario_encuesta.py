from . import db
from app.models.encuesta import Encuesta
from app.models.horario import Horario
from app.models.actividad import Actividad
from sqlalchemy import and_

#NO CREO Q DEBERIA ESTAR LA RELACION CON EL HORARIO, O ALMENOOS Q SEA NO OBLIGATORIA. PAUCAR    
class Horario_encuesta(db.Model):
    __tablename__='horario_encuesta'
    horario = db.relationship(Horario, backref = __tablename__, lazy =True)
    encuesta = db.relationship(Encuesta, backref = __tablename__, lazy =True)
    actividad = db.relationship(Actividad, backref = __tablename__)
    
    id_horario = db.Column('ID_HORARIO',db.ForeignKey(Horario.id_horario), primary_key = True)
    id_encuesta = db.Column('ID_ENCUESTA',db.ForeignKey(Encuesta.id_encuesta), primary_key = True)
    id_actividad = db.Column('ID_ACTIVIDAD',db.ForeignKey(Actividad.id_actividad), nullable = True)
    
    

    def addOne(self,obj):
        db.session.add(obj)
        db.session.commit()
        return 

    @classmethod
    def getAll(self,idActividad):
        return Horario_encuesta.query.filter_by(id_actividad=idActividad).all()

    