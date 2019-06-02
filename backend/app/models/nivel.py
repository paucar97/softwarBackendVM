from . import db
from app.models.curso import Curso
from sqlalchemy import and_

#from app.models.permiso_usuario_horario import Permiso_usuario_horario

class Nivel(db.Model):
    #name of table in DB
    __tablename__='nivel'
    id_nivel  = db.Column('ID_NIVEL',db.Integer,primary_key = True, autoincrement=True)
    descripcion = db.Column('DESCRIPCION', db.String(255), nullable = False)
    grado = db.Column('GRADO', db.Integer, nullable = False)
    puntaje = db.Column('PUNTAJE', db.Integer, nullable = False)

    def addOne(self,obj):
        db.session.add(obj)
        db.session.commit()
        db.session.flush()
        return obj.id_nivel