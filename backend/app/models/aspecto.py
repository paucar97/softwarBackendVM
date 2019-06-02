from . import db 

class Aspecto(db.Model):
    __tablename__= 'aspecto'
    id_aspecto = db.Column('ID_ASPECTO', db.Integer, primary_key=True)
    descripcion = db.Column('DESCRIPCION', db.String(500))
    informacion = db.Column('INFORMACION', db.String(500))
    puntaje_max = db.Column('PUNTAJE_MAX', db.Float)
    tipo_clasificacion = db.Column('TIPO_CLASIFICACION', db.Integer)
    flg_grupal = db.Column('FLG_GRUPAL', db.Integer, nullable = False)
    # me indica si la clasificacion deberia ser individual o grupal
    # 1 nivel de desempeno, 2 lista de criterios, 3 checklist

    def addOne(self,obj):
        db.session.add(obj)
        db.session.commit()        
        db.session.flush()
        return obj.id_aspecto