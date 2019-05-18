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
