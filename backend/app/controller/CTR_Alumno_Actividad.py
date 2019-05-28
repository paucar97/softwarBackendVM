from app.models import db
from app.models.alumno_actividad import Alumno_actividad
from app.models.actividad import Actividad
from app.models.entregable import Entregable
from app.models.usuario import Usuario
from app.models.grupo import Grupo
from app.models.curso import Curso
from app.models.horario import Horario
from app.models.notificacion import Notificacion

from app.models.alumno_nota_aspecto import Alumno_nota_aspecto
from app.models.alumno_nota_indicador import Alumno_nota_indicador
from app.commons.messages import ResponseMessage
from sqlalchemy import and_
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
    d = ResponseMessage()
    try:
        reg_comment = Alumno_actividad.query.filter(and_(Alumno_actividad.id_alumno == idAlumno, Alumno_actividad.id_alumno == idActividad)).first()
        if reg_comment is None:
            d.opcode = 1
            d.errcode = 1
            d.message = "Alumno o actividad no válidas"
        else:
            reg_comment.comentario = comentario
            db.session.commit()
            d.message = "Comentario agregado correctamente"
    except Exception as ex:
        d.opcode = 1
        d.errcode = 2
        d.message = str(ex)

    # Alumno_actividad.update().where(Alumno_actividad.id_usuario == idAlumno)
    return d.jsonify()

def responderComentarioAlumno(idActividad, idAlumno, idProfesor, respuesta):
    # test if exists
    d = ResponseMessage()
    try:
        reg_resp = Alumno_actividad.query.filter(and_(Alumno_actividad.id_alumno == idAlumno, Alumno_actividad.id_alumno == idActividad)).first()
        if reg_resp is None:
            d.opcode = 1
            d.errcode = 1
            d.message = "Alumno o actividad no válidas"
        elif reg_resp.id_jp != idProfesor:
            d.opcode = 1
            d.errcode = 1
            d.message = "No tiene autoridad para responder el comentario."
        else:
            reg_resp.comentarioJp = respuesta
            db.session.commit()
            d.message = "Respuesta agregada correctamente"
    except Exception as ex:
        d.opcode = 1
        d.errcode = 2
        d.message = str(ex)
#
    # # Alumno_actividad.update().where(Alumno_actividad.id_usuario == idAlumno)
    return d.jsonify()

def listaAlumnos(idActividad):
    ## ver si es grupal o indiviual
    tipoActividad = Actividad().getOne(idActividad).tipo
    print(idActividad)
    print(tipoActividad)
    if tipoActividad == 'I':
        listaAlumnos = Alumno_actividad().getAllAlumnos(idActividad)
        alumnos = []
        for alumno in listaAlumnos:
            d = {}
            d['idAlumno'] = alumno.id_alumno
            aux = Usuario().getOneId(alumno.id_alumno)
            d['codigoPUCP'] = aux.codigo_pucp
            d['nombre'] = aux.nombre + " " + aux.apellido_paterno
            alumnos.append(d)
        return alumnos
    else:
        try:
            listarGrupos = Alumno_actividad().getAllGrupos(idActividad)
            lstGrupos = []
            for grupo in listarGrupos:
                idGrupo = grupo.id_grupo
                d = dict()
                d['idGrupo'] = idGrupo
                d['nombreGrupo'] = Grupo().getOne(idGrupo).first().nombre
                lstGrupos.append(d)
            return lstGrupos
        except:
            return None 

def obtenerNotaAlumno(idAlumno, idActividad):
    aux = Alumno_actividad.query.filter(and_(Alumno_actividad.id_alumno == idAlumno, Alumno_actividad.id_alumno == idActividad)).first()
    d = {}

    if aux.flg_calificado == 1:
        d['flgCalificado'] = 1
        d['idActividad']= idActividad
        d['idAlumno']= idAlumno
        d['idJp']= aux.id_jp
        d['idGrupo']= aux.id_grupo
        d['nota']= aux.nota
        d['flgEntregable']= aux.flag_entregable
        d['comentario']= aux.comentario
        d['comentarioJp']= aux.comentarioJp
        d['flgFalta']= aux.flg_falta
        listaNotaAsp = []
        aux2 = Alumno_nota_aspecto.query.filter(and_(Alumno_nota_aspecto.id_alumno == idAlumno, Alumno_nota_aspecto.id_alumno == idActividad)).all()
        for notaAspecto in aux2:
            e = {}
            e['nota'] = notaAspecto.nota
            e['comentario'] = notaAspecto.comentario
            e['idRubrica'] = notaAspecto.id_rubrica
            e['idAspecto'] = notaAspecto.id_aspecto
            listaNotaInd = []
            aux3 = Alumno_nota_indicador.query.filter(and_(Alumno_nota_indicador.id_alumno == idAlumno, Alumno_nota_indicador.id_alumno == idActividad, Alumno_nota_indicador.id_aspecto == notaAspecto.id_aspecto)).all()
            for notaIndicador in aux3:
                f = {}
                f['idIndicador'] = notaIndicador.id_indicador
                f['nota'] = notaIndicador.nota
                f['comentario'] = notaIndicador.comentario
                listaNotaInd.append(f)
            e['listaNotaIndicador'] = listaNotaInd
            listaNotaAsp.append(e)
        d['listaNotaAspectos'] = listaNotaAsp
        return d
    else:
        d['flgCalificado'] = 0
        d['idActividad']= idActividad
        d['idAlumno']= idAlumno
        d['idJp']= aux.id_jp
        d['idGrupo']= aux.id_grupo
        d['nota']= aux.nota
        d['flgEntregable']= aux.flag_entregable
        d['comentario']= aux.comentario
        d['comentarioJp']= aux.comentarioJp
        d['flgFalta']= aux.flg_falta
        return d


def calificarAlumno(idActividad, idAlumno, idRubrica, idJp, nota, listaNotaAspectos, flgFalta):
    aux = Alumno_actividad().calificarAlumno(idActividad, idAlumno, idJp, nota, flgFalta)

    for notaAspecto in listaNotaAspectos:
        idAspecto = notaAspecto['idAspecto']
        notaAspectoObjeto = Alumno_nota_aspecto(
            id_actividad=idActividad,
            id_alumno=idAlumno,
            id_rubrica=idRubrica,
            id_aspecto=idAspecto,
            nota=notaAspecto['nota'],
            comentario=notaAspecto['comentario']
        )
        Alumno_nota_aspecto().addOne(notaAspectoObjeto)

        listaNotaIndicador = notaAspecto['listaNotaIndicador']

        for notaIndicador in listaNotaIndicador:
            notaIndicadorObjeto = Alumno_nota_indicador(
                id_actividad=idActividad,
                id_alumno=idAlumno,
                id_rubrica=idRubrica,
                id_aspecto=idAspecto,
                id_indicador=notaIndicador['idIndicador'],
                nota=notaIndicador['nota'],
                comentario=notaIndicador['comentario'],
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

def publicarNotificacionesAlumnos(idActividad):
    alumnosCalificados = Alumno_actividad.query.filter(and_(Alumno_actividad.id_actividad == idActividad, Alumno_actividad.flg_falta == 0))
    nombreCurso = db.session.query(Actividad.id_actividad, Curso.codigo).filter(Actividad.id_actividad == idActividad).join(Horario, Actividad.id_horario == Horario.id_horario).join(Curso, Horario.id_curso == Curso.id_curso).first()
    print(nombreCurso.codigo)
    return
    
def publicarParaRevision(idActividad, idJpReviso):
    publicarNotificacionesAlumnos(idActividad)
    return
    #flgConfianza = Actividad().getOne(idActividad).flg_confianza
    #
    #if flgConfianza == 1:
    #    publicarNotificacionesAlumnos(idActividad)
    #else:
    #    publicarNotificacionProfesor(idActividad, idJpReviso)

def listarAlumnosDestacados(idActividad):
    almact_fltr = Alumno_actividad.query.filter(Alumno_actividad.id_actividad == idActividad).subquery()

    #data = db.session.query(Usuario.codigo_pucp, Usuario.nombre_completo, almact_fltr.c.NOTA).join(almact_fltr, Usuario.id_usuario == Alumno_actividad.id_alumno).filter(almact_fltr.c.NOTA is not None).order_by(almact_fltr.c.NOTA.desc()).limit(5)
    print("message")
    data = db.session.query(Usuario.codigo_pucp, Usuario.nombre_completo, almact_fltr.c.NOTA).join(almact_fltr, almact_fltr.c.ID_ALUMNO == Usuario.id_usuario).order_by(almact_fltr.c.NOTA.desc()).limit(5)

    d = {}
    lst = []
    for cod, nom, nota in data.all():
        elem = {}
        elem['codigo'] = cod
        elem['nombre'] = nom
        elem['nota'] = nota
        lst.append(elem)

    d['lista5Alumnos'] = lst

    return d
