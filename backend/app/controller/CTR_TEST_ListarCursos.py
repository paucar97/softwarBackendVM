#from . import db
from app.models import db

from app.models.permiso_usuario_horario import Permiso_usuario_horario
from app.models.semestre import Semestre
from app.models.horario import Horario
from app.models.curso import Curso
from sqlalchemy import and_

def obtenerCursosActivosXProfesor(idProfesor):
    try:
        semestreActivo = Semestre().getOne().id_semestre
    except:        
        d = {}
        d['listaCursos'] = []
        d['cantCursos'] = 0
        return d
    #listaHorarios = Permiso_usuario_horario().getHorarioActivo(semestreActivo.id_semestre, idProfesor)
    #puh = Permiso_usuario_horario.query.filter(and_(Permiso_usuario_horario.id_semestre == semestreActivo.id_semestre, Permiso_usuario_horario.id_usuario == idProfesor)).subquery()
    #puh = Permiso_usuario_horario().getHorarioActivo(semestreActivo.id_semestre, idProfesor)
    puh = Permiso_usuario_horario.query.filter(and_(Permiso_usuario_horario.id_semestre == semestreActivo, Permiso_usuario_horario.id_usuario == idProfesor)).subquery()
    #print(puh)
    #listaHorarios = db.session.query(Horario,Permiso_usuario_horario).join(puh, puh.id_horario == Horario.id_horario).subquery()
    listaHorarios = db.session.query(Horario,Permiso_usuario_horario.id_permiso).join(Permiso_usuario_horario, Permiso_usuario_horario.id_horario == Horario.id_horario).filter(and_(Permiso_usuario_horario.id_semestre == semestreActivo, Permiso_usuario_horario.id_usuario == idProfesor)).subquery()
    #listaHorarios = Horario.query.join(puh, puh.c.ID_HORARIO == Horario.id_horario).subquery()
    #print(listaHorarios)
    ##FURTHER QUERIES##
    #listaHorarios = db.session.query(Horario).join(puh, puh.ID_HORARIO == Horario.id_horario).subquery()
    listaCursos = Curso().getCursosActivos(semestreActivo).subquery()

    #print(listaCursos)

<<<<<<< HEAD
<<<<<<< HEAD
    data = db.session.query(listaCursos.c.ID_ESPECIALIDAD,listaCursos.c.ID_CURSO, listaCursos.c.NOMBRE, listaCursos.c.CODIGO, listaHorarios.c.ID_HORARIO, listaHorarios.c.NOMBRE).join(listaHorarios, listaCursos.c.ID_CURSO == listaHorarios.c.ID_CURSO)
=======
    data = db.session.query(listaCursos.c.ID_CURSO, listaCursos.c.ID_ESPECIALIDAD, listaCursos.c.NOMBRE, listaCursos.c.CODIGO, listaHorarios.c.ID_HORARIO, listaHorarios.c.NOMBRE).join(listaHorarios, listaCursos.c.ID_CURSO == listaHorarios.c.ID_CURSO)
>>>>>>> 18a9dd58601fd38b183bbf52c4548fdcc7eb667d
=======
    data = db.session.query(listaCursos.c.ID_ESPECIALIDAD,listaCursos.c.ID_CURSO, listaCursos.c.NOMBRE, listaCursos.c.CODIGO, listaHorarios.c.ID_HORARIO, listaHorarios.c.NOMBRE,listaHorarios.c.ID_PERMISO).join(listaHorarios, listaCursos.c.ID_CURSO == listaHorarios.c.ID_CURSO)
>>>>>>> 4ed90663e4c219c217163d6172d5799a5d4b3539
    #data = db.session.query(listaCursos.c.id_curso, listaCursos.c.nombre, listaCursos.c.codigo, listaHorarios.c.nombre).join(listaHorarios, listaCursos.c.id_curso == listaHorarios.c.id_curso)
    #data = db.session.query(listaCursos.id_curso, listaCursos.nombre, listaCursos.codigo, listaHorarios.nombre).join(listaHorarios, listaCursos.id_curso == listaHorarios.id_curso)
    #data = db.session.query(Curso.id_curso, Curso.nombre, Curso.codigo, listaHorarios.nombre).join(listaHorarios, listaCursos.id_curso == listaHorarios.id_curso)
    #print(data)

    res = []

<<<<<<< HEAD
<<<<<<< HEAD
    for ide,idc, nomc, cod, idh, nomh in data.all():
=======
    for idc, ide, nomc, cod, idh, nomh in data.all():
>>>>>>> 18a9dd58601fd38b183bbf52c4548fdcc7eb667d
=======
    for ide,idc, nomc, cod, idh, nomh,idpe in data.all():
>>>>>>> 4ed90663e4c219c217163d6172d5799a5d4b3539
        aux = {}
        aux['idEspecialidad'] = ide
        aux['idcurso'] = idc
        aux['idespecialidad'] = ide
        aux['nombre'] = nomc
        aux['codigo'] = cod
        aux['idhorario'] = idh
        aux['horario'] = nomh
        aux['permiso'] = idpe
        res.append(aux)

    d = {}
    d['listaCursos'] = res
    d['cantCursos'] = len(res)

    #print(d)
    return d
