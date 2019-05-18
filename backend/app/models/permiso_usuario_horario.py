from . import db
from app.models.permiso import Permiso
from app.models.usuario import Usuario
from app.models.horario import Horario

class Permiso_usuario_horario(db.Model):
    #name of table in DB
    __tablename__ = "permiso_usuario_horario"
    #columns in DB
    permiso = db.relationship(Permiso, backref=__tablename__, lazy=True)
    usuario = db.relationship(Usuario, backref=__tablename__, lazy=True)
    horario = db.relationship(Horario, backref=__tablename__, lazy=True)
    id_horario = db.Column('ID_HORARIO', db.ForeignKey(Horario.id_horario), primary_key=True)
    id_usuario = db.Column('ID_USUARIO', db.ForeignKey(Usuario.id_usuario), primary_key=True)
    id_permiso = db.Column('ID_PERMISO', db.ForeignKey(Permiso.id_permiso), nullable=False)
    id_semestre = db.Column('ID_SEMESTRE', db.Integer)

    def json(self):
        d = {}
        d['id_horario'] = self.id_horario
        d['id_usuario'] = self.id_usuario
        d['id_permiso'] = self.id_permiso


    def addOne(self,obj):
        db.session.add(obj)
        db.session.flush()
        return 

    @classmethod
    def getHorarioActivo(self,idSemestre,idUsuario):
        return Permiso_usuario_horario.query.filter_by(id_semestre = idSemestre,id_usuario=idUsuario)
    
    @classmethod
    def getAll(self,idSemestre,idHorario):
        return Permiso_usuario_horario.query.filter_by(id_semestre = idSemestre,id_horario=idHorario).all()

    @classmethod
    def getAllUsuario(self,idUsuario):
        return Permiso_usuario_horario.query.filter_by(id_usuario=idUsuario).all()
