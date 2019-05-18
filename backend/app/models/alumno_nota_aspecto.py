from . import db 
from app.models.alumno_actividad import Alumno_actividad
from app.models.permiso_usuario_horario import Permiso_usuario_horario
from app.models.rubrica_aspecto import Rubrica_aspecto

class Alumno_nota_aspecto(db.Model):
    __tablename__ ='alumno_nota_aspecto'

    alumno_actividad =  db.relationship(Alumno_actividad,backref = __tablename__,lazy =True)
    rubrica_aspecto = db.relationship(Rubrica_aspecto,backref = __tablename__,lazy =True)
    
    id_actividad = db.Column('ID_ACTIVIDAD',db.Integer,primary_key = True)
    id_alumno = db.Column('ID_ALUMNO',db.Integer,primary_key = True)
    id_rubrica = db.Column('ID_RUBRICA',db.Integer,primary_key = True)
    id_aspecto = db.Column('ID_ASPECTO',db.Integer,primary_key = True)
   
    __table_args__=(
        db.ForeignKeyConstraint(
            ['ID_ACTIVIDAD','ID_ALUMNO'],
            [Alumno_actividad.id_actividad, Alumno_actividad.id_alumno]
        ),
        db.ForeignKeyConstraint(
            ['ID_RUBRICA','ID_ASPECTO'],
            [Rubrica_aspecto.id_rubrica, Rubrica_aspecto.id_aspecto]
        ),
    )

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

    @classmethod
    def updateNota(self,nota):
        self.nota = nota
        db.session.commit()
        return