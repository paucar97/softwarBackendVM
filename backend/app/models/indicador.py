from . import db

class Indicador(db.Model):
    __tablename__='indicador'
    id_indicador = db.Column('ID_INDICADOR',db.Integer,primary_key=True)
    descripcion = db.Column('DESCRIPCION',db.String(500))
    informacion = db.Column('INFORMACION',db.String(500))
    puntaje_max = db.Column('PUNTAJE_MAX',db.Float)
    tipo = db.Column('TIPO', db.String(100))
    #NOTA
    #COTEJO
    #DESEMPEÑO

    def addOne(self,obj):
        db.session.add(obj)
        db.session.commit()
        db.session.flush()
        return obj.id_indicador