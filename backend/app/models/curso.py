from . import db
from app.models.semestre_especialidad import Semestre_especialidad

class Curso(db.Model):
    #name of table in DB
    __tablename__ = 'curso'

    #columns in DB
    id_curso = db.Column('ID_CURSO', db.Integer, primary_key=True, autoincrement=True)
    id_especialidad = db.Column('ID_ESPECIALIDAD', db.Integer, primary_key=True)
    id_semestre = db.Column('ID_SEMESTRE', db.Integer, primary_key=True)
    semestre_x_especialidad = db.relationship(Semestre_especialidad, backref=__tablename__)
    __table_args__ = (
        db.ForeignKeyConstraint(
            ['ID_ESPECIALIDAD', 'ID_SEMESTRE'],
            [Semestre_especialidad.id_especialidad, Semestre_especialidad.id_semestre]
        ),
    )
    tipo_admin = db.Column('TIPO_ADMIN', db.String(20))
    nombre = db.Column('NOMBRE', db.String(255))
    codigo = db.Column('CODIGO', db.String(15))

    @classmethod
    def getCursosActivos(self, id_semestre_activo):
        return Curso.query.filter_by(id_semestre=id_semestre_activo).subquery()
