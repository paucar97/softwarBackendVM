from . import db

class Permiso(db.Model):
    #name of table in DB
    __tablename__ = "permiso"
    #columns in DB
    id_permiso = db.Column('ID_PERMISO', db.Integer, primary_key=True)
    nombre = db.Column('NOMBRE', db.String(100))
