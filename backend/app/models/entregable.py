from . import db 
from app.models.alumno_actividad import Alumno_actividad
from sqlalchemy import and_
class Entregable(db.Model):
    #name of table in DB
    __tablename__ = 'entregable'
    
    id_entregable = db.Column('ID_ENTREGABLE',db.Integer,primary_key = True, autoincrement=True)

    alumno_actividad = db.relationship(Alumno_actividad,backref = __tablename__ ,lazy = True)

    id_actividad = db.Column('ID_ACTIVIDAD',db.Integer,primary_key = True)
    id_alumno = db.Column('ID_ALUMNO',db.Integer,primary_key = True)
    
    __table_args__=(
        db.ForeignKeyConstraint(
            ['ID_ACTIVIDAD','ID_ALUMNO'],
            [Alumno_actividad.id_actividad, Alumno_actividad.id_alumno]
        ),
    )
    
    url_entregable = db.Column('URL_ENTREGABLE',db.String(500),nullable = True)
    nombre_archivo = db.Column('NOMBRE_ARCHIVO',db.String(255),nullable = True)
    fecha_creado = db.Column('FECHA_CREADO', db.DateTime)
    flg_activo = db.Column('FLG_ACTIVO',db.Integer, default = 1)
    path = db.Column('PATH',db.String(255),nullable = True)
    tipo = db.Column('TIPO',db.Integer,nullable = False)
    documento = db.Column('DOCUMENTO',db.LargeBinary(length=(2**32)-1))
    #1 para documento y 2 para url
    
    def json(self):
        d={}
        d['idEntregable']=self.id_entregable
        d['urlEntregalbe'] =self.url_entregable
        d['nombreArchivo'] = self.nombre_archivo
        d['fechaCredo'] = self.fecha_creado.__str__()
        d['flgActivo'] = self.flg_activo
        d['path'] = self.path
        d['tipo'] = self.tipo
        return d

    def addOne(self,obj):
        db.session.add(obj)
        db.session.commit()
        return

    @classmethod
    def getAll(self,idActividad,idAlumno):
        r=Entregable.query.filter(and_(Entregable.id_actividad==idActividad,Entregable.id_alumno == idAlumno,
        Entregable.flg_activo ==1))
        return r

    @classmethod
    def getOne(self,idEntregable):
        return #Entregable.query.filter_by(Entregable.id_entregable = idEntregable).first()