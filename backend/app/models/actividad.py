from . import db
from app.models.horario import Horario
from app.models.rubrica import Rubrica
from sqlalchemy import *
# FALTA NOMBRE A ACTIVIDAD
class Actividad(db.Model):
    __tablename__='actividad'
    id_actividad= db.Column('ID_ACTIVIDAD',db.Integer,primary_key=True, unique = True,autoincrement =True)
    horario = db.relationship(Horario, backref = __tablename__, lazy=True)
    id_horario  = db.Column('ID_HORARIO',db.ForeignKey(Horario.id_horario),primary_key = True)
    rubrica = db.relationship(Rubrica, backref = __tablename__, lazy=True)
    id_rubrica = db.Column('ID_RUBRICA',db.ForeignKey(Rubrica.id_rubrica),primary_key = True)

    id_semestre = db.Column('ID_SEMESTRE', db.Integer, nullable = False)
    nombre = db.Column('NOMBRE',db.String(255))
    flg_activo = db.Column('FLG_ACTIVO',db.Integer, server_default = '1')
    etapa = db.Column('ETAPA',db.Integer)
    flg_entregable = db.Column('FLG_ENTREGABLE',db.Integer)
    fecha_inicio = db.Column('FECHA_INICIO',db.DateTime)
    fecha_fin = db.Column('FECHA_FIN',db.DateTime)
    fecha_modificacion = db.Column('FECHA_MODIFICACION',db.DateTime)
    tipo = db.Column('TIPO', db.String(1))
    #tipo I de individual y G de grupal

    def addOne(self,obj):
        db.session.add(obj)
        db.session.flush()
        db.session.commit()
        return obj.id_actividad
    
    @classmethod
    def updateOne(self,idActividad,Nombre,tipo1,descripcion,fecha,hora_inicio,hora_fin,flag_entregable):
        actividad=Actividad.query.filter_by(id_actividad = idActividad).first()
        actividad.nombre=Nombre
        actividad.tipo=tipo1
        actividad.descripcion=descripcion
        actividad.fecha_inicio=hora_inicio
        actividad.fecha_fin=hora_fin
        actividad.fecha_modificacion=fecha
        actividad.flg_entregable=flag_entregable
        db.session.commit()
        return
    @classmethod
    def getOne(self,idActividad):
        return Actividad.query.filter_by(id_actividad = idActividad).first()

    @classmethod
    def obtenerRubricasXIdUsuario(self, idHorario, idUsuario):
        return db.session.query(Rubrica).join(Actividad).filter(and_(Actividad.id_horario == idHorario, Rubrica.id_usuario_creador == idUsuario)).all()
    
