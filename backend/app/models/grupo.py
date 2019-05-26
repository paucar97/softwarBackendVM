from . import db

class Grupo(db.Model):
    __tablename__ = 'grupo'
    id_grupo = db.Column('ID_GRUPO',db.Integer,primary_key=True,autoincrement = True)
    nombre = db.Column('NOMBRE',db.String(255))
    flg_grupo_general = db.Column('FLG_GRUPO_GENERAL',db.Integer)
    def addOne(self,obj):
        db.session.add(obj)
        db.session.flush()
        db.session.commit()
        return obj.id_grupo

    @classmethod
    def getOne(self,idGrupo):
        return Grupo.query.filter_by(id_grupo= idGrupo)