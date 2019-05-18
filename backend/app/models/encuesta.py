from . import db

class Encuesta(db.Model):
    __tablename__='encuesta'
    id_encuesta = db.Column('ID_ENCUESTA',db.Integer, primary_key=True)
    tipo = db.Column('TIPO', db.String(15))
    #Tipo es competencia u otra cosa
    nombre = db.Column('NOMBRE', db.String(100))
    descripcion = db.Column('DESCRIPCION',db.String(250))
    flg_especial = db.Column('FLG_ESPECIAL', db.Integer)
    #Esto para cuando sea una plantilla

    def addOne(self,obj):
        db.session.add(obj)
        db.session.flush()
        return obj.id_encuesta
    
    @classmethod
    def getOne(self,idEncuesta):
        return Encuesta.query.filter_by(id_encuesta=idEncuesta).first()

        