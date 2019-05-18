from . import db

class Especialidad(db.Model):
    #name of table in DB
    __tablename__ = 'especialidad'
    #columns in DB
    id_especialidad = db.Column('ID_ESPECIALIDAD', db.Integer, primary_key=True)
    nombre = db.Column('NOMBRE_ESPECIALIDAD', db.String(25))
    facultad = db.Column('NOMBRE_FACULTAD', db.String(25))
    #index1 = db.Index('idx_especialidad', id_especialidad, unique=True)
