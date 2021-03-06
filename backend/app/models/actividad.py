from . import db
from app.models.horario import Horario
from sqlalchemy import *
# FALTA NOMBRE A ACTIVIDAD
class Actividad(db.Model):
    __tablename__='actividad'
    id_actividad= db.Column('ID_ACTIVIDAD',db.Integer,primary_key=True, unique = True,autoincrement =True)
    horario = db.relationship(Horario, backref = __tablename__, lazy=True)
    id_horario  = db.Column('ID_HORARIO',db.ForeignKey(Horario.id_horario),primary_key = True)
    
    id_semestre = db.Column('ID_SEMESTRE', db.Integer, nullable = False)
    nombre = db.Column('NOMBRE',db.String(255))
    descripcion = db.Column('DESCRIPCION', db.String(500), nullable = True)
    flg_activo = db.Column('FLG_ACTIVO',db.Integer, server_default = '1')
    
    flg_entregable = db.Column('FLG_ENTREGABLE',db.Integer)
    fecha_inicio = db.Column('FECHA_INICIO',db.DateTime)
    fecha_fin = db.Column('FECHA_FIN',db.DateTime)
    fecha_modificacion = db.Column('FECHA_MODIFICACION',db.DateTime)
    tipo = db.Column('TIPO', db.String(1))
    fecha_creacion = db.Column('FECHA_CREACION', db.DateTime, server_default = func.current_timestamp())
    id_usuario_creador = db.Column('ID_USUARIO_CREADOR', db.Integer, nullable = False)
    flg_confianza = db.Column('FLG_CONFIANZA', db.Integer)
    flg_puede_revisar = db.Column('FLG_PUEDE_REVISAR', db.Integer)
    flg_multicalificable = db.Column('FLG_MULTICALIFICABLE', db.Integer, default = 0)
    #tipo I de individual y G de grupal

    def json(self):
        d = {}
        d['idActividad'] = self.id_actividad
        d['nombre'] = self.nombre
        d['descripcion'] = self.descripcion
        d['flgEntregable'] = self.flg_entregable
        d['fechaInicio'] = self.fecha_inicio.__str__()
        d['fechaFin'] = self.fecha_fin.__str__()
        d['tipo'] = self.tipo
        d['fechaCreacion'] = self.fecha_creacion.__str__()
        d['idUsuarioCreador'] = self.id_usuario_creador        
        d['flgConfianza'] = self.flg_confianza
        d['flgMulticalificable'] = self.flg_multicalificable
        d['flgPuedeRevisar'] = self.flg_puede_revisar
        return d

    def addOne(self,obj):
        db.session.add(obj)
        db.session.flush()
        db.session.commit()
        return obj.id_actividad
    
    @classmethod
    def updateOne(self,idActividad,Nombre,tipo1,descripcion,hora_inicio,hora_fin,flag_confianza,flag_entregable, flg_multicalificable):
        actividad=Actividad.query.filter_by(id_actividad = idActividad).first()
        actividad.nombre=Nombre
        actividad.tipo=tipo1
        actividad.fecha_inicio=hora_inicio
        actividad.fecha_fin=hora_fin
        actividad.fecha_modificacion = func.current_timestamp()
        actividad.flg_confianza = flag_confianza
        actividad.flg_entregable=flag_entregable
        actividad.flg_multicalificable = flg_multicalificable 
        db.session.commit()
        return

    @classmethod
    def getOne(self,idActividad):
        return Actividad.query.filter_by(id_actividad = idActividad).first()

    @classmethod
    def obtenerRubricasXIdUsuario(self, idHorario, idUsuario):
        return db.session.query(Rubrica).join(Actividad).filter(and_(Actividad.id_horario == idHorario, Rubrica.id_usuario_creador == idUsuario)).all()
    
    @classmethod
    def actualizarRubrica(self, idActividad, idRubrica):
        actividad = Actividad.query.filter_by(id_actividad = idActividad).first()
        actividad.id_rubrica = idRubrica
        db.session.commit()
        return

    @classmethod
    def listar(self,idHorario):
        return Actividad.query.order_by(Actividad.fecha_inicio).filter_by(id_horario = idHorario,flg_activo = 1)

    @classmethod
    def deleteOne(self,idActividad):
        actividad = Actividad.query.filter_by(id_actividad = idActividad).first()
        actividad.flg_activo = 0
        db.session.commit()
        return 
        
