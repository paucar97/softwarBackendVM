from . import db

class Especialidad(db.Model):
    #name of table in DB
    __tablename__ = 'especialidad'
    #columns in DB
    id_especialidad = db.Column('ID_ESPECIALIDAD', db.Integer, primary_key=True)
    nombre = db.Column('NOMBRE_ESPECIALIDAD', db.String(25))
    facultad = db.Column('NOMBRE_FACULTAD', db.String(25))
    #index1 = db.Index('idx_especialidad', id_especialidad, unique=True)

    @classmethod
    def getIdInformatica(self):
        return Especialidad.query.filter(nombre = 'Ingeniería Informática').first()

    @classmethod
    def getAll(self):
        return Especialidad.query.all() 
    def getOne(self,idespecialidad):
        return Especialidad.query.filter(id_especialidad=idespecialidad).first()  
