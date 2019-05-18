from . import db
from app.models.indicador import Indicador
from app.models.rubrica_aspecto import Rubrica_aspecto
from sqlalchemy import and_

class Rubrica_aspecto_indicador(db.Model):
    __tablename__='rubrica_aspecto_indicador'
    
    rubrica_aspecto = db.relationship(Rubrica_aspecto, backref = __tablename__,lazy=True)
    id_rubrica= db.Column('ID_RUBRICA',db.Integer,primary_key=True)
    id_aspecto  = db.Column('ID_ASPECTO',db.Integer,primary_key = True)
    
    __table_args__= (
        db.ForeignKeyConstraint(
            ['ID_RUBRICA','ID_ASPECTO'],
            [Rubrica_aspecto.id_rubrica, Rubrica_aspecto.id_aspecto]
        ),
    )
    
    indicador = db.relationship(Indicador,backref = __tablename__,lazy=True)
    id_indicador = db.Column('ID_INDICADOR',db.ForeignKey(Indicador.id_indicador),primary_key = True)

    def addOne(self,obj):
        db.session.add(obj)
        db.session.commit()
        db.session.flush()
        return

    @classmethod
    def obtenerIndicadores(self,idRubrica, idAspecto):
        return db.session.query(Indicador).join(Rubrica_aspecto_indicador).filter(and_(Rubrica_aspecto_indicador.id_rubrica == idRubrica, Rubrica_aspecto_indicador.id_aspecto == idAspecto)).all()