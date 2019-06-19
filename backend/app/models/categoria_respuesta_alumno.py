from . import db
from app.models.usuario import Usuario
from app.models.categoria import Categoria
from sqlalchemy import *
from app.commons.utils import *

class Categoria_respuesta_alumno(db.Model):
    __tablename__= 'categoria_respuesta_alumno'
    
    id_respuesta = db.Column('ID_RESPUESTA',db.Integer,primary_key=True, autoincrement = True)

    categoria = db.relationship(Categoria,backref = __tablename__,lazy=True)
    id_categoria = db.Column('ID_CATEGORIA',db.ForeignKey(Categoria.id_categoria),primary_key=True)
    
    id_alumno = db.Column('ID_ALUMNO',db.Integer,primary_key=True, autoincrement = False)

    
    descripcion = descripcion = db.Column('DESCRIPCION', db.String(255), nullable = False)
    horas_planificadas = db.Column('HORAS_PLANIFICADAS',db.Integer, nullable = False)
    horas_reales = db.Column('HORAS_REALES',db.Integer, nullable = False)
    flg_activo = db.Column('FLG_ACTIVO', db.Integer, nullable = False, default = 1)

    def addOne(self,obj):
        db.session.add(obj)
        db.session.flush()
        db.session.commit()
        return obj.id_categoria

    @classmethod
    def apagarCategorias(self,idRegistroEsfuerzo,idAlumno):
        categoriasActivas = Categoria.query.filter(and_(Categoria.id_registro_esfuerzo == idRegistroEsfuerzo, Categoria.flg_activo == 1)).subquery()
        if categoriasActivas is not None:
            categoriasRespuestas = Categoria_respuesta_alumno.query.join(categoriasActivas, categoriasActivas.c.ID_CATEGORIA == Categoria_respuesta_alumno.id_categoria).filter(and_(Categoria_respuesta_alumno.id_alumno == idAlumno, Categoria_respuesta_alumno.flg_activo == 1)).all()
        else:
            categoriasRespuestas = None
        if categoriasRespuestas is not None:
            for categoriaRpt in categoriasRespuestas:
                categoriaRpt.flg_activo = 0
                db.session.commit()
            return True
        return True
