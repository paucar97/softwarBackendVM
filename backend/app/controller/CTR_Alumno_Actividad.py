from app.models import db
from app.models.alumno_actividad import Alumno_actividad
from app.models.actividad import Actividad
from app.models.entregable import Entregable
from app.models.usuario import Usuario
from app.models.grupo import Grupo
from app.models.curso import Curso
from app.models.horario import Horario
from app.models.notificacion import Notificacion
from app.models.semestre import Semestre
from app.models.permiso_usuario_horario import Permiso_usuario_horario
from app.models.alumno_nota_aspecto import Alumno_nota_aspecto
from app.models.alumno_nota_indicador import Alumno_nota_indicador
from app.models.rubrica import Rubrica
from app.models.aspecto import Aspecto
from app.models.indicador import Indicador
from app.models.rubrica_aspecto_indicador import Rubrica_aspecto_indicador
from app.models.rubrica_aspecto import Rubrica_aspecto
from app.commons.messages import ResponseMessage
from sqlalchemy import *
from statistics import *

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
    """
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
    """

def obtenerNotaAlumno(idAlumno, idActividad):
    aux = Alumno_actividad.query.filter(and_(Alumno_actividad.id_alumno == idAlumno, Alumno_actividad.id_actividad == idActividad)).first()
    actividadAnalizada = Actividad.getOne(idActividad)
    d = {}

    d['flgCalificado'] = aux.flg_calificado
    d['idActividad']= idActividad
    d['idAlumno']= idAlumno
    d['idJp']= aux.id_jp
    d['idGrupo']= aux.id_grupo
    d['nota']= aux.nota
    d['flgEntregable']= aux.flag_entregable
    d['comentario']= aux.comentario
    d['comentarioJp']= aux.comentarioJp
    d['flgFalta']= aux.flg_falta
    d['idRubrica'] = actividadAnalizada.id_rubrica

    listaNotaAsp = []
    aux2 = Rubrica_aspecto.query.filter(Rubrica_aspecto.id_rubrica == actividadAnalizada.id_rubrica).all()
    for aspecto in aux2:
        e = {}
        notaAspecto = Alumno_nota_aspecto.query.filter(and_(Alumno_nota_aspecto.id_alumno == idAlumno, Alumno_nota_aspecto.id_actividad == idActividad, Alumno_nota_aspecto.id_aspecto == aspecto.id_aspecto)).first()
        aspectoDetalle = Aspecto.query.filter_by(id_aspecto = aspecto.id_aspecto).first()
        e['descripcion'] = aspectoDetalle.descripcion
        e['informacion'] = aspectoDetalle.informacion
        e['puntajeMax'] = aspectoDetalle.puntaje_max
        e['tipoClasificacion'] = aspectoDetalle.tipo_clasificacion
        e['idAspecto'] = aspectoDetalle.id_aspecto
        if notaAspecto is not None:
            e['nota'] = notaAspecto.nota
            e['comentario'] = notaAspecto.comentario
        else:
            e['nota'] = None
            e['comentario'] = None

        listaNotaInd = []
        aux3 = Rubrica_aspecto_indicador.query.filter(Rubrica_aspecto_indicador.id_aspecto == aspecto.id_aspecto).all()
        for indicador in aux3:
            notaIndicador = Alumno_nota_indicador.query.filter(and_(Alumno_nota_indicador.id_alumno == idAlumno, Alumno_nota_indicador.id_actividad == idActividad, Alumno_nota_indicador.id_aspecto == aspecto.id_aspecto, Alumno_nota_indicador.id_indicador == indicador.id_indicador)).first()
            f = {}
            indicadorDetalle = Indicador.query.filter_by(id_indicador = indicador.id_indicador).first()
            f['descripcion'] = indicadorDetalle.descripcion
            f['informacion'] = indicadorDetalle.informacion
            f['puntajeMax'] = indicadorDetalle.puntaje_max
            f['tipo'] = indicadorDetalle.tipo
            f['idIndicador'] = indicadorDetalle.id_indicador
            if notaIndicador is not None:
                f['nota'] = notaIndicador.nota
                f['comentario'] = notaIndicador.comentario
            else:
                f['nota'] = None
                f['comentario'] = None
            listaNotaInd.append(f)
        e['listaNotaIndicador'] = listaNotaInd
        listaNotaAsp.append(e)
    d['listaNotaAspectos'] = listaNotaAsp
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
    aux = Alumno_actividad().editarNotaAlumno(idActividad, idAlumno, idJp, nota, flgFalta)
    for notaAspecto in listaNotaAspectos:
        idAspecto = notaAspecto['idAspecto']
        Alumno_nota_aspecto().updateNota(idActividad, idRubrica, idAspecto, idAlumno, notaAspecto['nota'], notaAspecto['comentario'])
        listaNotaIndicador = notaAspecto['listaNotaIndicador']

        for notaIndicador in listaNotaIndicador:
            Alumno_nota_indicador().updateNota(idActividad, idRubrica, idAspecto, idAlumno, notaIndicador['idIndicador'], notaIndicador['nota'], notaIndicador['comentario'])

    d = {}
    d['message'] = "succeed"
    return d

def publicarNotificacionGeneral(idSemestre, idUsuario, mensaje, idActividad):
    notificacion = Notificacion(
        id_semestre = idSemestre,
        id_usuario = idUsuario,
        nombre = mensaje,
        id_actividad = idActividad
    )
    Notificacion.addOne(notificacion)
    return True

def publicarNotificacionesAlumnos(idActividad):
    alumnosFaltantesCalificados = Alumno_actividad.query.filter(and_(Alumno_actividad.id_actividad == idActividad, Alumno_actividad.flg_falta == 0, Alumno_actividad.flg_calificado == 0)).all()

    if len(alumnosFaltantesCalificados) > 0:
        return 0

    alumnosCalificados = Alumno_actividad.query.filter(and_(Alumno_actividad.id_actividad == idActividad, Alumno_actividad.flg_falta == 0)).all()
    cursoActividad = db.session.query(Actividad.id_actividad, Curso.codigo).filter(Actividad.id_actividad == idActividad).join(Horario, Actividad.id_horario == Horario.id_horario).join(Curso, Horario.id_curso == Curso.id_curso).first()
    actividadEvaluada = Actividad.query.filter_by(id_actividad = idActividad).first()
    mensaje = cursoActividad.codigo + " - Se registro la nota de la Actividad: " + actividadEvaluada.nombre
    semestre = Semestre.getOne()

    for alumno in alumnosCalificados:
        publicarNotificacionGeneral(semestre.id_semestre, alumno.id_alumno, mensaje, idActividad)

    Alumno_actividad.publicarNotas(idActividad)
    idHorario = db.session.query(Actividad.id_actividad, Horario.id_horario).filter(Actividad.id_actividad == idActividad).join(Horario, Actividad.id_horario == Horario.id_horario).first()
    profesoresHorario = Permiso_usuario_horario.query.filter(and_(Permiso_usuario_horario.id_horario == idHorario.id_horario, Permiso_usuario_horario.id_permiso == 1))

    for profesor in profesoresHorario:
        publicarNotificacionGeneral(semestre.id_semestre, profesor.id_usuario, cursoActividad.codigo + " - Se registraron las notas de la Actividad: " + actividadEvaluada.nombre, idActividad)
    return 1

def publicarParaRevision(idActividad, idJpReviso):
    d = {}
    actividad = Actividad.getOne(idActividad)
    if actividad.flg_confianza == 1:
        aux = publicarNotificacionesAlumnos(idActividad)
        if aux == 0:
            d['succeed'] = False
            d['message'] = "Falta corregir alumnos en la Actividad"
            return d
        else:
            d['succeed'] = True
            d['message'] = "Notas publicadas"
            return d


    #flgConfianza = Actividad().getOne(idActividad).flg_confianza
    #
    #if flgConfianza == 1:
    #    publicarNotificacionesAlumnos(idActividad)
    #else:
    #    publicarNotificacionProfesor(idActividad, idJpReviso)

def listarAlumnosDestacados(idActividad):
    almact_fltr = Alumno_actividad.query.filter(Alumno_actividad.id_actividad == idActividad).subquery()

    #data = db.session.query(Usuario.codigo_pucp, Usuario.nombre_completo, almact_fltr.c.NOTA).join(almact_fltr, almact_fltr.c.ID_ALUMNO == Usuario.id_usuario).order_by(almact_fltr.c.NOTA.desc()).limit(5)
    #data = db.session.query(Usuario.codigo_pucp, Usuario.nombre_completo, almact_fltr.c.NOTA).join(almact_fltr, almact_fltr.c.ID_ALUMNO == Usuario.id_usuario).filter(almact_fltr.c.NOTA != None).order_by(almact_fltr.c.NOTA.desc()).limit(5)
    data = db.session.query(Usuario.codigo_pucp, Usuario.nombre_completo, almact_fltr.c.NOTA).join(almact_fltr, almact_fltr.c.ID_ALUMNO == Usuario.id_usuario).filter(and_(almact_fltr.c.FLG_CALIFICADO == True, almact_fltr.c.FLG_FALTA == False, almact_fltr.c.NOTA != None)).order_by(almact_fltr.c.NOTA.desc()).limit(5)

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

def obtenerEstadisticaActividad(idActividad):
    d = {}

    try:
        sqlquery = db.session.query(Alumno_actividad.nota).filter(Alumno_actividad.id_actividad == idActividad).order_by(Alumno_actividad.nota.desc())
        lst = [nota for nota, in sqlquery]
        fltr_lst = list(filter(lambda x: x is not None, lst))
    except Exception as ex:
        d = ResponseMessage(1, 2, str(ex))
        return d.jsonify()

    try:
        d['media'] = mean(fltr_lst)
        d['desciavionEstandar'] = stdev(fltr_lst)
        d['porcentajeAprobados'] = len(list(filter(lambda x: x > 10, fltr_lst))) * 100.0 / len(fltr_lst)
        d['notaMax'] = max(fltr_lst)
        d['notaMin'] = min(fltr_lst)
        d['numNotas'] = len(fltr_lst)
    except Exception as ex:
        d = ResponseMessage(1, 1, str(ex))
        return d.jsonify()

    return d
