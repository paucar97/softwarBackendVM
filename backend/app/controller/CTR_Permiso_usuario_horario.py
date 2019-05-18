#from . import db
from app.models import db

from app.models.permiso_usuario_horario import Permiso_usuario_horario
from app.models.semestre import Semestre
from app.models.horario import Horario
from app.models.curso import Curso

def obtenerCursosActivosXAlumno(idAlumno):
    semestreActivo = Semestre().getOne()
    listaHorarios = Permiso_usuario_horario().getHorarioActivo(semestreActivo.id_semestre, idAlumno)

    res = []

    for horario in listaHorarios:
        if horario.id_permiso == 2:
            curso, hor = Horario().obtenerCurso(horario.id_horario)
            print(curso)
            aux = {}
            aux['id_curso'] = curso.id_curso
            aux['nombre'] = curso.nombre
            aux['codigo'] = curso.codigo
            aux['tipo'] = curso.tipo_admin
            aux['nombre_horario'] = hor.nombre
            aux['id_horario'] = hor.id_horario
            res.append(aux)

    d = {}
    d['listaCursos'] = res
    d['cantCursos'] = len(res)

    return d

def obtenerCursosActivosXProfesor(idProfesor):
    semestreActivo = Semestre().getOne()
    listaHorarios = Permiso_usuario_horario().getHorarioActivo(semestreActivo.id_semestre, idProfesor)

    res = []

    for horario in listaHorarios:
        if horario.id_permiso == 1:
            curso, hor = Horario().obtenerCurso(horario.id_horario)
            aux = {}
            aux['id_horario'] = horario.id_horario
            #t = Horario().getOne(horario.id_horario)
            aux['nombre_horario']=  hor.nombre
            aux['id_curso'] = curso.id_curso
            aux['nombre_curso'] = curso.nombre
            aux['codigo'] = curso.codigo
            aux['tipo'] = curso.tipo_admin
            res.append(aux)

    d = {}
    d['listaCursos'] = res
    d['cantCursos'] = len(res)
    """
    #listaHorarios = Permiso_usuario_horario().getHorarioActivo(semestreActivo.id_semestre, idProfesor)
    puh = Permiso_usuario_horario().getHorarioActivo(semestreActivo.id_semestre, idProfesor)
    print(puh)
    #listaHorarios = db.session.query(Horario).join(puh, puh.id_horario == Horario.id_horario).subquery()
    listaHorarios = db.session.query(Horario).join(puh, puh.ID_HORARIO == Horario.id_horario).subquery()
    listaCursos = Curso().getCursosActivos(semestreActivo)

    data = db.session.query(listaCursos.id_curso, listaCursos.nombre, listaCursos.codigo, listaHorarios.nombre).join(listaHorarios, listaCursos.id_curso == listaHorarios.id_curso)
    #data = db.session.query(Curso.id_curso, Curso.nombre, Curso.codigo, listaHorarios.nombre).join(listaHorarios, listaCursos.id_curso == listaHorarios.id_curso)

    res = []

    for idc, nomc, cod, nomh in data.all():
        aux = {}
        aux['idcurso'] = idc
        aux['nombre'] = nomc
        aux['codigo'] = cod
        aux['horario'] = nomh
        res.append(aux)

    d = {}
    d['listaCursos'] = res
    d['cantCursos'] = len(res)
    """
    return d
