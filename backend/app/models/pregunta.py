from . import db

class Pregunta(db.Model):
    __tablename__='pregunta'
    id_pregunta = db.Column('ID_PREGUNTA',db.Integer,primary_key=True)
    descripcion = db.Column('DESCRIPCION',db.String(100))
    tipo_pregunta = db.Column('TIPO_PREGUNTA',db.Integer)
     # si es checkbox(1) o texto(2)  o medidor de desempeño (3)
    familia = db.Column('FAMILIA',db.String(25)) #sirve para la la coevaluación (APRENDIZAJE,PREPARACION)


    def addOne(self,obj):
        db.session.add(obj)
        db.session.flush()
        return obj.id_pregunta

    @classmethod
    def getOne(self,idPregunta):
        return Pregunta.query.filter_by(id_pregunta=idPregunta).first()