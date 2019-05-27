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
    id_rubrica = db.Column('ID_RUBRICA',db.ForeignKey(Rubrica.id_rubrica), nullable = True)

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
    #tipo I de individual y G de grupal

    def json(self):
        d = {}
        d['idActividad'] = self.id_actividad
        d['idRubrica'] = self.id_rubrica
        d['descripcion'] = self.descripcion
        d['flgConfianza'] = self.flg_confianza
        d['flgPuedeRevisar'] = self.flg_puede_revisar
        d['nombre'] = self.nombre
        d['flgEntregable'] = self.flg_entregable
        d['fechaInicio'] = self.fecha_inicio.__str__()
        d['fechaFin'] = self.fecha_fin.__str__()
        d['tipo'] = self.tipo
        return d

    def addOne(self,obj):
        db.session.add(obj)
        db.session.flush()
        db.session.commit()
        return obj.id_actividad
    
    @classmethod
    def updateOne(self,idActividad,Nombre,tipo1,descripcion,hora_inicio,hora_fin,flag_confianza,flag_entregable):
        actividad=Actividad.query.filter_by(id_actividad = idActividad).first()
        actividad.nombre=Nombre
        actividad.tipo=tipo1
        actividad.fecha_inicio=hora_inicio
        actividad.fecha_fin=hora_fin
        actividad.fecha_modificacion=func.current_timestamp()
        actividad.flg_confianza = flag_confianza
        actividad.flg_entregable=flag_entregable
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
        return Actividad.query.filter_by(id_horario = idHorario,flg_activo = 1)