from . import db
from app.models.permiso_usuario_horario import Permiso_usuario_horario 
from sqlalchemy import *
from app.models.grupo import Grupo
class Grupo_alumno_horario(db.Model):
    __tablename__ = 'grupo_alumno_horario'
    grupo = db.relationship(Grupo,backref = __tablename__,lazy=True)
    usuario_horario = db.relationship(Permiso_usuario_horario,backref = __tablename__,lazy=True)

    id_grupo = db.Column('ID_GRUPO',db.ForeignKey(Grupo.id_grupo),primary_key =True)
    id_horario = db.Column('ID_HORARIO',db.Integer,primary_key= True)
    id_usuario = db.Column('ID_USUARIO',db.Integer,primary_key =True)
    
    __table_args__ = (
        db.ForeignKeyConstraint(
            ['ID_HORARIO','ID_USUARIO'],
            [Permiso_usuario_horario.id_horario,Permiso_usuario_horario.id_usuario]
        ),
    )

    def addOne(self,obj):
        db.session.add(obj)
        db.session.flush()
        db.session.commit()
        return 

    @classmethod
    def getAll(self,idGrupo):
        return Grupo_alumno_horario.query.filter_by(id_grupo = idGrupo)

    @classmethod
    def getAllGeneral(self,idHorario):
        l = db.session.query(Grupo_alumno_horario,Grupo).join(Grupo).filter( and_(Grupo_alumno_horario.id_horario == idHorario,Grupo.flg_grupo_general == 1) )
        
        return l