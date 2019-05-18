from . import db
from sqlalchemy import and_

class Usuario(db.Model):
    #name of table in DB
    __tablename__ = 'usuario'
    #columns in DB
    id_usuario = db.Column('ID_USUARIO', db.Integer, primary_key=True)
    nombre = db.Column('NOMBRE', db.String(50), nullable=False)
    #codigPUCP = db.Column('CODIGOPUCP', db.String(50))
    email = db.Column('EMAIL', db.String(100), nullable=False)
    clave = db.Column('CLAVE', db.String(100), nullable=False)
    apellido_paterno = db.Column('APELLIDO_PATERNO', db.String(100))
    apellido_materno = db.Column('APELLIDO_MATERNO', db.String(100))
    flg_activo = db.Column('FLG_ACTIVO', db.Integer, default=1)
    flg_admin = db.Column('FLG_ADMIN', db.Integer)

    @classmethod
    def getOne(self, emailC, claveC):
        return Usuario.query.filter(and_(Usuario.email == emailC, Usuario.clave == claveC)).first()

    def getOneId(self,idUsuario):
        return Usuario.query.filter_by(id_usuario = idUsuario).first()