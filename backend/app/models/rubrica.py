from . import db
from app.models.usuario import Usuario
from app.models.actividad import Actividad
from sqlalchemy import *

class Rubrica(db.Model):
    __tablename__='rubrica'
    id_rubrica = db.Column('ID_RUBRICA',db.Integer,primary_key=True, autoincrement=True)
    estado = db.Column('ESTADO', db.Integer, server_default = '1')
    
    actividad = db.relationship(Actividad,backref = __tablename__,lazy=True)
    id_actividad = db.Column('ID_ACTIVIDAD',db.ForeignKey(Actividad.id_actividad),primary_key=True)

    fecha_registro = db.Column('FECHA_REGISTRO',db.DateTime, server_default = func.current_timestamp())
    fecha_validacion = db.Column('FECHA_VALIDACION',db.DateTime)
    fecha_modificacion = db.Column('FECHA_MODIFICACION',db.DateTime)
    flg_rubrica_especial = db.Column('FLG_RUBRICA_ESPECIAL', db.Integer)
    id_usuario_creador = db.Column('ID_USUARIO_CREADOR',db.Integer, nullable = False)
    nombre = db.Column('NOMBRE', db.String(255))
    tipo = db.Column('TIPO', db.Integer, nullable = False)
    # 1 Especial del ciclo
    # 2 Autoevaluacion
    # 3 Coevaluacion
    # 4 Instrumento de evaluacion
    # 5 Registro de Horas
    
    flg_activo = db.Column('FLG_ACTIVO', db.Integer, nullable = False, default = 1)

    def addOne(self,obj):
        db.session.add(obj)
        db.session.commit()
        db.session.flush()

        return obj.id_rubrica

    @classmethod
    def obtenerRubrica(self, idRubrica):
        return Rubrica.query.filter_by(id_rubrica = idRubrica).first()

    @classmethod
    def editarRubrica(self, idRubrica, idFlgEspecial, idUsuarioCreador, nombreRubrica, tipo):
        rubricaAEditar = Rubrica.query.filter_by(id_rubrica = idRubrica).first()
        rubricaAEditar.fecha_modificacion = func.current_timestamp()
        rubricaAEditar.flg_rubrica_especial = idFlgEspecial
        rubricaAEditar.id_usuario_creador = idUsuarioCreador
        rubricaAEditar.nombre = nombreRubrica
        rubricaAEditar.tipo = tipo
        db.session.commit()
        return
        
    @classmethod
    def desactivarRubrica(self, idRubrica):
        rubricaAEditar = Rubrica.query.filter_by(id_rubrica = idRubrica).first()
        rubricaAEditar.flg_activo = 0
        db.session.commit()
        return

    @classmethod
    def getIdRubricaEvaluacion(self,idActividad):
        d = Rubrica.query.filter_by(id_actividad = idActividad, flg_activo = 1, tipo = 4).first()
        return d.id_rubrica