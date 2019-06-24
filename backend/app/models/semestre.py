from . import db

class Semestre(db.Model):
    #name of table in DB
    __tablename__ = 'semestre'
    #columns in DB
    id_semestre = db.Column('ID_SEMESTRE', db.Integer, primary_key=True)
    nombre = db.Column('NOMBRE', db.String(10))
    flg_activo = db.Column('FLG_ACTIVO',db.Integer,default = 1)
    ##additional field: length/duration##

    @classmethod
    def getOne(self):
        return Semestre.query.filter_by(flg_activo=1).first()

    @classmethod
    def addOne(self,obj):
        db.session.add(obj)
        db.session.commit()
        db.session.flush()
        return 

    @classmethod
    def getAllNoActivos(self):
        s = Semestre.query.filter_by(flg_activo = 0)
        return s
    @classmethod
    def getAll(self):
        return Semestre.query.filter_by(flg_activo=0).all()

    @classmethod
    def activar(self,idSemestre):
        aux = Semestre.query.filter_by(flg_activo =1).first()
        if aux != None:
            aux.flg_activo = 0
        sem = Semestre.query.filter_by(id_semestre = idSemestre).first()
        sem.flg_activo = 1
        db.session.commit()
        return