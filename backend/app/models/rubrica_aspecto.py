from . import db
from app.models.rubrica import Rubrica
from app.models.aspecto import Aspecto
from sqlalchemy import *

class Rubrica_aspecto(db.Model):
    __tablename__='rubrica_aspecto'
    rubrica = db.relationship(Rubrica, backref = __tablename__, lazy =True)
    aspecto = db.relationship(Aspecto, backref = __tablename__, lazy =True)
    id_rubrica= db.Column('ID_RUBRICA',db.ForeignKey(Rubrica.id_rubrica),primary_key = True)
    id_aspecto= db.Column('ID_ASPECTO',db.ForeignKey(Aspecto.id_aspecto),primary_key = True)
    #descripcion = db.Column('DESCRIPCION',db.String(500))

    def addOne(self,obj):
        db.session.add(obj)
        db.session.commit()
        db.session.flush()
        return

    @classmethod
    def obtenerAspectos(self, idRubrica):
        aux = db.session.query(Aspecto).join(Rubrica_aspecto).filter(Rubrica_aspecto.id_rubrica == idRubrica).all()

        if aux is None:
            return []
        else:
            return aux

    @classmethod
    def borrarAspectos(self, idRubrica):
        listaAspectos = Rubrica_aspecto.query.filter_by(id_rubrica = idRubrica).all()
        Rubrica_aspecto.query.filter_by(id_rubrica = idRubrica).delete()
        for aspecto in listaAspectos:
            Aspecto.query.filter_by(id_aspecto = aspecto.id_aspecto).delete()
        db.session.commit()
        return