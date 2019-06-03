from . import db
from app.models.nivel import Nivel
from app.models.rubrica_aspecto_indicador import Rubrica_aspecto_indicador
from sqlalchemy import *

class Rubrica_aspecto_indicador_nivel(db.Model):
    __tablename__='rubrica_aspecto_indicador_nivel'

    rubrica_aspecto_indicador = db.relationship(Rubrica_aspecto_indicador, backref = __tablename__,lazy=True)
    id_rubrica= db.Column('ID_RUBRICA',db.Integer,primary_key=True)
    id_aspecto  = db.Column('ID_ASPECTO',db.Integer,primary_key = True)
    id_indicador = db.Column('ID_INDICADOR',db.Integer,primary_key = True)

    __table_args__= (
        db.ForeignKeyConstraint(
            ['ID_RUBRICA','ID_ASPECTO', 'ID_INDICADOR'],
            [Rubrica_aspecto_indicador.id_rubrica, Rubrica_aspecto_indicador.id_aspecto, Rubrica_aspecto_indicador.id_indicador]
        ),
    )
    
    nivel = db.relationship(Nivel,backref = __tablename__,lazy=True)
    id_nivel = db.Column('ID_NIVEL', db.ForeignKey(Nivel.id_nivel),primary_key = True)

    def addOne(self,obj):
        db.session.add(obj)
        db.session.commit()
        db.session.flush()
        return
    
    @classmethod
    def obtenerNiveles(self, idRubrica, idIndicador):
        stmt = Rubrica_aspecto_indicador_nivel.query.filter(and_(Rubrica_aspecto_indicador_nivel.id_rubrica == idRubrica, Rubrica_aspecto_indicador_nivel.id_indicador == idIndicador)).subquery()
        aux = Nivel.query.join(stmt, Nivel.id_nivel == stmt.c.ID_NIVEL).all()
        
        if aux is None:
            return []
        else:
            return aux