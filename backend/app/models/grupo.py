from . import db

class Grupo(db.Model):
    __tablename__ = 'grupo'
    id_grupo = db.Column('ID_GRUPO',db.Integer,primary_key=True)
    nombre = db.Column('NOMBRE',db.String(255))
    
    def addOne(self,obj):
        db.session.add(obj)
        db.session.flush()
        db.session.commit()
        return obj.id_grupo