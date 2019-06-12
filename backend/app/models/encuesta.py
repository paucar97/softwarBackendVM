from . import db
from app.models.actividad import Actividad
from app.models.usuario import Usuario

class Encuesta(db.Model):
    __tablename__='encuesta'
    id_encuesta = db.Column('ID_ENCUESTA',db.Integer, primary_key = True, autoincrement = 1)
    tipo = db.Column('TIPO', db.Integer)
    #Tipo es competencia u otra cosa
    nombre = db.Column('NOMBRE', db.String(100))
    descripcion = db.Column('DESCRIPCION',db.String(250))
    flg_especial = db.Column('FLG_ESPECIAL', db.Integer)
    id_actividad = db.Column('ID_ACTIVIDAD', db.ForeignKey(Actividad.id_actividad), primary_key = True)
    id_usuario = db.Column('ID_USUARIO', db.ForeignKey(Actividad.id_actividad), primary_key = True)
    flg_activo = db.Column('FLG_ACTIVO', db.Integer, nullable = False, default = 1)
    #Esto para cuando sea una plantilla

    def addOne(self,obj):
        db.session.add(obj)
        db.session.flush()
        return obj.id_encuesta
    
    @classmethod
    def getOne(self,idEncuesta):
        return Encuesta.query.filter_by(id_encuesta=idEncuesta).first()

    @classmethod
    def eliminarEncuesta(self,idEncuesta):
        Encuesta.query.filter_by(id_encuesta=idEncuesta).delete()
        db.session.commit()
        return True

        