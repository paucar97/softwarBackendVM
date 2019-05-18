from . import db
from app.models.alumno_nota_aspecto import Alumno_nota_aspecto
from app.models.rubrica_aspecto_indicador import Rubrica_aspecto_indicador
class Alumno_nota_indicador(db.Model):

    #name of table in DB
    __tablename__ = 'alumno_nota_indicador'
    #columns in DB
    alumno_nota_aspecto = db.relationship(Alumno_nota_aspecto,backref=__tablename__,lazy = True)
    rubrica_aspecto_indicador = db.relationship(Rubrica_aspecto_indicador,backref=__tablename__,lazy = True)
    
    id_actividad = db.Column('ID_ACTIVIDAD',db.Integer,primary_key = True)
    id_alumno = db.Column('ID_ALUMNO',db.Integer,primary_key = True)
    id_rubrica = db.Column('ID_RUBRICA',db.Integer,primary_key = True)
    id_aspecto = db.Column('ID_ASPECTO',db.Integer,primary_key = True)
    
    #constraints
    __table_args__ =(
        db.ForeignKeyConstraint(
            ['ID_ACTIVIDAD','ID_ALUMNO','ID_RUBRICA', 'ID_ASPECTO'],
            [Alumno_nota_aspecto.id_actividad, Alumno_nota_aspecto.id_alumno, Alumno_nota_aspecto.id_rubrica, Alumno_nota_aspecto.id_aspecto]
        ),
    )
   
    id_indicador = db.Column('ID_INDICADOR',db.ForeignKey(Rubrica_aspecto_indicador.id_indicador),primary_key = True)
    nota = db.Column('NOTA',db.Float,nullable = True)
    comentario = db.Column('COMENTARIO',db.String(500),nullable = True)
    
    """
    jp = db.relationship(Permiso_usuario_horario,backref = __tablename__,lazy =True)
    id_jp = db.Column('ID_JP',db.ForeignKey(Permiso_usuario_horario.id_usuario))
    """
    @classmethod
    def addOne(self,obj):
        db.session.add(obj)
        db.session.commit()
        return