from . import db
from app.models.encuesta import Encuesta
from app.models.pregunta import Pregunta
class Encuesta_pregunta(db.Model):
    __tablename__='encuesta_pregunta'
    encuesta = db.relationship(Encuesta, backref = __tablename__, lazy =True)
    pregunta = db.relationship(Pregunta, backref = __tablename__, lazy =True)
    id_encuesta= db.Column('ID_ENCUESTA',db.ForeignKey(Encuesta.id_encuesta),primary_key = True)
    id_pregunta= db.Column('ID_PREGUNTA',db.ForeignKey(Pregunta.id_pregunta),primary_key = True)

    def addOne(self,obj):
        db.session.add(obj)
        db.session.commit()
        return

    def getAll(self,idEncuesta):
        return Encuesta_pregunta.query.filter_by(id_encuesta=idEncuesta).all() 