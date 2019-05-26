from app.models import db
from app.models.alumno_actividad import Alumno_actividad
from app.models.entregable import Entregable
from app.models.usuario import Usuario
from app.models.alumno_nota_aspecto import Alumno_nota_aspecto
from app.models.alumno_nota_indicador import Alumno_nota_indicador
from sqlalchemy import *

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

def calificarAlumno(idActividad, idAlumno, idRubrica, idJp, nota, listaNotaAspectos,flgFalta):
    aux = Alumno_actividad().calificarAlumno(idActividad, idAlumno, idJp, nota, flgFalta)
    
    for notaAspecto in listaNotaAspectos:
        idAspecto = notaAspecto['idAspecto']
        notaAspectoObjeto = Alumno_nota_aspecto(
            id_actividad = idActividad,
            id_alumno = idAlumno,
            id_rubrica = idRubrica,
            id_aspecto = idAspecto,
            nota = notaAspecto['nota'],
            comentario = notaAspecto['comentario']
        )
        Alumno_nota_aspecto().addOne(notaAspectoObjeto)
        
        listaNotaIndicador = notaAspecto['listaNotaIndicador']
        
        for notaIndicador in listaNotaIndicador:
            notaIndicadorObjeto = Alumno_nota_indicador(
                id_actividad = idActividad,
                id_alumno = idAlumno,
                id_rubrica = idRubrica,
                id_aspecto = idAspecto,
                id_indicador = notaIndicador['idIndicador'],
                nota = notaIndicador['nota'],
                comentario = notaIndicador['comentario'],
            )
            Alumno_nota_indicador().addOne(notaIndicadorObjeto)

    d = {}
    d['message'] = "succeed"
    return d

def editarNotaAlumno(idActividad, idAlumno, idRubrica, idJp, nota, listaNotaAspectos, flgFalta):
    aux = Alumno_actividad().editarNotaAlumno(idActividad, idAlumno, nota, flgFalta)
    for notaAspecto in listaNotaAspectos:
        idAspecto = notaAspecto['idAspecto']
        Alumno_nota_aspecto().updateNota(idActividad, idRubrica, idAspecto, idAlumno, notaAspecto['nota'], notaAspecto['comentario'])
        listaNotaIndicador = notaAspecto['listaNotaIndicador']
        
        for notaIndicador in listaNotaIndicador:
            Alumno_nota_indicador().updateNota(idActividad, idRubrica, idAspecto, idAlumno, notaIndicador['idIndicador'], notaIndicador['nota'], notaIndicador['comentario'])

    d = {}
    d['message'] = "succeed"
    return d

