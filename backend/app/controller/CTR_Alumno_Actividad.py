from app.models import db
from app.models.alumno_actividad import Alumno_actividad
from app.models.actividad import Actividad
from app.models.entregable import Entregable
from app.models.usuario import Usuario
from app.models.grupo import Grupo
from sqlalchemy import and_

def entregablesActividadXAlumno(idActividad):
    # get all users for this activity
    alumns_act = Alumno_actividad.query.filter(Alumno_actividad.id_actividad == idActividad).subquery()

    entregables = Entregable.query.join(alumns_act, and_(alumns_act.c.ID_ACTIVIDAD == Entregable.id_actividad, alumns_act.c.ID_ALUMNO == Entregable.id_alumno))  # .subquery()

    lst = []
    # primera implementacion, falta optimizar
    for usr in Usuario.query.filter(Usuario.id_usuario == alumns_act.c.ID_ALUMNO):
        alaux = {}
        alaux['idAlumno'] = usr.id_usuario
        alaux['codigoPUCP'] = usr.codigo_pucp
        auxentreglst = []
        for entrg in entregables.query.filter(entregables.c.ID_ALUMNO == Usuario.id_usuario):
            auxentreg = {}
            Entregable.tipo
            auxentreg['idEntregable'] = entrg.id_entregable
            auxentreg['urlEntregalbe'] = entrg.url_entregable
            auxentreg['nombreArchivo'] = entrg.nombre_archivo
            auxentreg['fechaCredo'] = entrg.fecha_creado
            auxentreg['flgActivo'] = entrg.flg_activo
            auxentreg['path'] = entrg.path
            auxentreg['tipo'] = entrg.tipo
            auxentreglst.append(auxentreg)
        alaux['entregables'] = auxentreglst
        lst.append(alaux)

    d = {}
    d['lista'] = lst
    d['cantidad'] = len(lst)

    return d

def ingresarComentarioAlumno(idActividad, idAlumno, comentario):
    # test if exists
    d = dict

    reg_comment = Alumno_actividad.query.filter(and_(Alumno_actividad.id_alumno == idAlumno, Alumno_actividad.id_alumno == idActividad))
    if reg_comment is None:
        # TODO
        pass  # send error msg ("alumno o actividad no válidas")
        # TODO
    else:
        reg_comment.comentario = comentario
        db.session.commit()

    # Alumno_actividad.update().where(Alumno_actividad.id_usuario == idAlumno)
    return d
def listaAlumnos(idActividad):
    ## ver si es grupal o indiviual
    tipoActividad = Actividad().getOne(idActividad).tipo
    
    if tipoActividad == 'I':
        listaAlumnos = Alumno_actividad().getAllAlumnos(idActividad)
        alumnos = []
        for alumno in listaAlumnos:
            d = {}
            d['idAlumno'] = alumno.id_alumno
            aux = Usuario().getOneId(alumno.id_alumno)
            d['codigoPUCP'] = aux.codigo_pucp
            d['nombre'] = aux.nombre +  " " + aux.apellido_paterno
            alumnos.append(d)
        return alumnos
    else:
        listarGrupos = Grupo().getAll(idActividad).all()
        for grupo in listaAlumnos:
            d=dict()
            ## SE HACE EL DISTINCT 
        ## LISTAR GRUPOS
    return alumnos
