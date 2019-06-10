from app.models.actividad import Actividad 
from app.models.rubrica import Rubrica 
from app.models.aspecto import Aspecto
from app.models.indicador import Indicador
from app.models.rubrica_aspecto_indicador import Rubrica_aspecto_indicador
from app.models.rubrica_aspecto import Rubrica_aspecto
from app.models.rubrica_aspecto_indicador_nivel import Rubrica_aspecto_indicador_nivel
from app.models.horario import Horario
from app.models.actividad_alarma import Actividad_alarma
from app.models.grupo import Grupo
from app.models.grupo_alumno_horario import Grupo_alumno_horario
from app.models.encuesta_pregunta import Encuesta_pregunta
from app.models.encuesta import Encuesta
from app.models.pregunta import Pregunta
from app.models.horario_encuesta import Horario_encuesta
from app.models.permiso_usuario_horario import Permiso_usuario_horario
from app.models.feedback_actividad import Feedback_actividad
from app.models.alumno_actividad import Alumno_actividad
from app.models.semestre import Semestre
from app.models.nivel import Nivel
from app.commons.utils import *
from app.commons.messages import ResponseMessage
from sqlalchemy import *

def obtenerRubricaXidRubrica(idRubrica):
    nombreRubrica = Rubrica.obtenerRubrica(idRubrica)
    d = {}
    d['idRubrica'] = idRubrica
    d['nombreRubrica'] = nombreRubrica.nombre
    d['fechaRegistro'] = nombreRubrica.fecha_registro.__str__()
    d['flgRubricaEspecial'] = nombreRubrica.flg_rubrica_especial
    d['idUsuarioCreador'] = nombreRubrica.id_usuario_creador
    d['tipo'] = nombreRubrica.tipo    

    aspectos = []
    listaAspectos = Rubrica_aspecto.obtenerAspectos(idRubrica)

    for aspecto in listaAspectos:
        aux = {}
        aux['idAspecto'] = aspecto.id_aspecto
        aux['descripcion'] = aspecto.descripcion
        aux['informacion'] = aspecto.informacion
        aux['puntajeMax'] = aspecto.puntaje_max
        aux['tipoClasificacion'] = aspecto.tipo_clasificacion
        aux['flgGrupal'] = aspecto.flg_grupal
        indicadores = []
        listaIndicadores = Rubrica_aspecto_indicador.obtenerIndicadores(idRubrica, aspecto.id_aspecto)
        for indicador in listaIndicadores:
            aux2 = {}
            aux2['idIndicador'] = indicador.id_indicador
            aux2['descripcion'] = indicador.descripcion
            aux2['informacion'] = indicador.informacion
            aux2['puntajeMax'] = indicador.puntaje_max
            #aux2['tipo'] = indicador.tipo
            niveles = []
            listaNiveles = Rubrica_aspecto_indicador_nivel.obtenerNiveles(idRubrica, indicador.id_indicador)
            for nivel in listaNiveles:
                aux3 = {}
                aux3['idNivel'] = nivel.id_nivel
                aux3['descripcion'] = nivel.descripcion
                aux3['grado'] = nivel.grado
                aux3['puntaje'] = nivel.puntaje
                niveles.append(aux3)
            aux2['listaNiveles'] = niveles
            aux2['cantNiveles'] = len(niveles)
            indicadores.append(aux2)
        aux['listaIndicadores'] = indicadores
        aux['cantIndicadores'] = len(indicadores)
        aspectos.append(aux)
    d['listaAspectos'] = aspectos
    d['cantAspectos'] = len(aspectos)
    return d

def obtenerRubrica(idActividad, tipo):
    idRubrica = Rubrica.query.filter(and_(Rubrica.id_actividad == idActividad, Rubrica.tipo == tipo, Rubrica.flg_activo == 1)).first()
    if idRubrica is not None:
        return obtenerRubricaXidRubrica(idRubrica.id_rubrica)
    else:
        d = {}
        d['succeed'] = False
        d['message'] = "No existe Rubrica"
        return d
    
def obtenerRubricasPasadas(idUsuario, idCurso):
    listaHorarios = Horario.obtenerHorariosXCurso(idCurso)

    d = {}
    aux = []
    for horario in listaHorarios:    
        listaRubricas = Actividad.obtenerRubricasXIdUsuario(horario.id_horario, idUsuario)
        if len(listaRubricas) != 0:
            for rubrica in listaRubricas:
                aux.append(rubrica)

    aux2 = []
    for rubrica in aux:
        aux3 = obtenerRubricaXidRubrica(rubrica.id_rubrica)
        aux2.append(aux3)
    
    if len(aux2) == 0:
        d['respuesta'] = 0
    else:
        d['respuesta'] = 1
        d['rubricas'] = aux2
    
    return d

def editarRubrica(idRubrica, idFlgEspecial, idUsuarioCreador, nombreRubrica, listaAspectos, tipo):
    Rubrica().editarRubrica(idRubrica, idFlgEspecial, idUsuarioCreador, nombreRubrica, tipo)
    Rubrica_aspecto_indicador_nivel().borrarNiveles(idRubrica)
    Rubrica_aspecto_indicador().borrarIndicadores(idRubrica)
    Rubrica_aspecto().borrarAspectos(idRubrica)
    
    for aspecto in listaAspectos:
        aspectoObjeto = Aspecto(
            descripcion = aspecto['descripcion'],
            informacion  = aspecto['informacion'],
            puntaje_max = aspecto['puntajeMax'],
            tipo_clasificacion = aspecto['tipoClasificacion'],
            flg_grupal = aspecto['flgGrupal']
        )
        listaIndicadores = aspecto['listaIndicadores']
        idAspecto = Aspecto().addOne(aspectoObjeto)

        rubricaAspectoObjeto = Rubrica_aspecto(
            id_rubrica = idRubrica,
            id_aspecto = idAspecto
        )
        aux = Rubrica_aspecto().addOne(rubricaAspectoObjeto)

        for indicador in listaIndicadores:
            indicadorObjeto = Indicador(
                descripcion = indicador['descripcion'],
                informacion = indicador['informacion'],
                puntaje_max = indicador['puntajeMax']
            )
            idIndicador = Indicador().addOne(indicadorObjeto)

            rubricaAspectoIndicadorObj = Rubrica_aspecto_indicador(
                id_rubrica = idRubrica,
                id_aspecto = idAspecto,
                id_indicador = idIndicador
            )
            aux2 = Rubrica_aspecto_indicador().addOne(rubricaAspectoIndicadorObj)
            
            listaNiveles = indicador['listaNiveles']

            for nivel in listaNiveles:
                nivelObjeto = Nivel(
                    descripcion = nivel['descripcion'],
                    grado = nivel['grado'],
                    puntaje = nivel['puntaje']
                )
                idNivel = Nivel().addOne(nivelObjeto)
                rubricaAspectoIndicadorNivelObj = Rubrica_aspecto_indicador_nivel(
                    id_rubrica = idRubrica,
                    id_aspecto = idAspecto,
                    id_indicador = idIndicador,
                    id_nivel = idNivel
                )
                Rubrica_aspecto_indicador_nivel().addOne(rubricaAspectoIndicadorNivelObj)
    
    d = {}
    d['message'] = True
    return d

def obtenerEncuestaCoevaluacion(idActividad, idAlumno):
    d = {}
    listaEncuesta = Encuesta.query.filter(and_(Encuesta.id_usuario == idAlumno, Encuesta.id_actividad == idActividad, Encuesta.flg_activo == 1)).first()
    if listaEncuesta is not None:
        d['nombre'] = listaEncuesta.nombre
        d['idEncuesta'] = listaEncuesta.id_encuesta
        d['descripcion'] = listaEncuesta.descripcion
        listaPreguntas = Encuesta_pregunta.query.filter(and_(Encuesta_pregunta.id_encuesta == listaEncuesta.id_encuesta)).all()
        listaPreguntasDesglozadas = []
        for pregunta in listaPreguntas:
            preguntaAnalizada = Pregunta.query.filter(Pregunta.id_pregunta == pregunta.id_pregunta).first()
            e = {}
            e['descripcion'] = preguntaAnalizada.descripcion
            listaPreguntasDesglozadas.append(e)
        d['listaPreguntas'] = listaPreguntasDesglozadas
        return d
    else:
        d = {}
        d['succeed'] = False
        d['message'] = "No existe la coevaluacion."
        return d

def crearEncuestasCoevaluacion(idActividad):
    listaGrupos = Alumno_actividad.query(Alumno_actividad.id_grupo).filter(Alumno_actividad.id_actividad == idActividad).distinct().all()
    actividadAnalizada = Actividad.query.filter(Actividad.id_actividad == idActividad).first()

    for grupo in listaGrupos:
        listaAlumnos = Grupo_alumno_horario.query(Grupo_alumno_horario.id_usuario).filter(Grupo_alumno_horario.id_grupo == grupo.id_grupo)
        for alumno in listaAlumnos:
            encuestaObjeto = Encuesta(
                tipo = 3,
                nombre = "CoEvaluacion de la actividad: " + actividadAnalizada.nombre,
                id_actividad = idActividad,
                id_usuario = alumno.id_usuario
            )
            idEncuesta = Encuesta.addOne(encuestaObjeto)
            for alumno2 in listaAlumnos:
                if alumno.id_usuario != alumno2.id_usuario:
                    alumnoCompanero = Usuario.query.filter(Usuario.id_usuario == alumno2.id_usuario)
                    preguntaTipo = Pregunta(
                        descripcion = "¿Qué tan bien crees que trabajó " + alumnoCompanero.nombre + " " + alumnoCompanero.apellido_paterno + "?",
                        tipo_pregunta = 3
                    )
                    idPregunta = Pregunta.addOne(preguntaTipo)
                    encuestaPreguntaObjeto = Encuesta_pregunta(
                        id_encuesta = idEncuesta,
                        id_pregunta = idPregunta
                    )
                    Encuesta_pregunta.addOne(encuestaPreguntaObjeto)


def crearRubrica(idActividad, idFlgEspecial, idUsuarioCreador, nombreRubrica, listaAspectos, tipo):
    
    if tipo == 3:
        crearEncuestasCoevaluacion(idActividad)

    rubricaActual = Rubrica.query.filter(Rubrica.id_actividad == idActividad, Rubrica.flg_activo == 1, Rubrica.tipo == tipo).first()

    if rubricaActual is not None:
        Rubrica.desactivarRubrica(rubricaActual.id_rubrica)
    
    rubricaObjeto = Rubrica(
        flg_rubrica_especial = idFlgEspecial,
        id_usuario_creador = idUsuarioCreador,
        nombre = nombreRubrica,
        tipo = tipo,
        id_actividad = idActividad
    )
    idRubrica = Rubrica().addOne(rubricaObjeto)

    for aspecto in listaAspectos:
        aspectoObjeto = Aspecto(
            descripcion = aspecto['descripcion'],
            informacion  = aspecto['informacion'],
            puntaje_max = aspecto['puntajeMax'],
            tipo_clasificacion = aspecto['tipoClasificacion'],
            flg_grupal = aspecto['flgGrupal']
        )
        listaIndicadores = aspecto['listaIndicadores']
        idAspecto = Aspecto().addOne(aspectoObjeto)

        rubricaAspectoObjeto = Rubrica_aspecto(
            id_rubrica = idRubrica,
            id_aspecto = idAspecto
        )
        aux = Rubrica_aspecto().addOne(rubricaAspectoObjeto)

        for indicador in listaIndicadores:
            indicadorObjeto = Indicador(
                descripcion = indicador['descripcion'],
                informacion = indicador['informacion'],
                puntaje_max = indicador['puntajeMax']
            )
            idIndicador = Indicador().addOne(indicadorObjeto)

            rubricaAspectoIndicadorObj = Rubrica_aspecto_indicador(
                id_rubrica = idRubrica,
                id_aspecto = idAspecto,
                id_indicador = idIndicador
            )
            aux2 = Rubrica_aspecto_indicador().addOne(rubricaAspectoIndicadorObj)
            
            listaNiveles = indicador['listaNiveles']

            for nivel in listaNiveles:
                nivelObjeto = Nivel(
                    descripcion = nivel['descripcion'],
                    grado = nivel['grado'],
                    puntaje = nivel['puntaje']
                )
                idNivel = Nivel().addOne(nivelObjeto)
                rubricaAspectoIndicadorNivelObj = Rubrica_aspecto_indicador_nivel(
                    id_rubrica = idRubrica,
                    id_aspecto = idAspecto,
                    id_indicador = idIndicador,
                    id_nivel = idNivel
                )
                Rubrica_aspecto_indicador_nivel().addOne(rubricaAspectoIndicadorNivelObj)


    d = {}
    d['idRubrica'] = idRubrica

    return d


def CrearActividad(idhorario, Nombre, tipo1, descripcion, fechaInicio, fechaFin, flag_confianza, flag_entregable1,idUsuarioCreador, flgMulticalificable):
    semestre=Semestre().getOne()
    idSemestre=semestre.id_semestre

    actividadObjeto = Actividad(
        id_horario = idhorario,
        descripcion = descripcion,
        id_semestre = idSemestre,
        nombre = Nombre,
        flg_activo = 1,
        flg_entregable = flag_entregable1,
        flg_confianza = flag_confianza,
        fecha_inicio = convertDatetime(fechaInicio),
        fecha_fin = convertDatetime(fechaFin),
        id_usuario_creador=idUsuarioCreador,
        tipo=tipo1,
        flg_multicalificable = flgMulticalificable)

    idActividad= Actividad().addOne(actividadObjeto)

    #Cuando creamos el objeta, habran alarmas predefinidas suponemos(?)
    #actividad_alarmaObjeto=Actividad_Alarma(
    #    id_actividad=idActividad,
    #    id_alarma=1,
    #)
    #Actividad_Alarma().addOne(actividad_alarmaObjeto)

    listaAlumnos= Permiso_usuario_horario().getAll(idSemestre,idhorario)
    listaIdAlumnos=[]
    for usuario in listaAlumnos:
        if usuario.id_permiso== 2: #Alumnos
            listaIdAlumnos.append(usuario.id_usuario)

    for idalumno in listaIdAlumnos:
        alumnoActividadObjeto = Alumno_actividad(
            id_actividad = idActividad,
            id_alumno = idalumno)
        try:
            Alumno_actividad().addOne(alumnoActividadObjeto)
        except:
            pass

    return 

def EditarActividad(idactividad,Nombre,tipo1,descripcion,hora_inicio,hora_fin,flag_confianza,flag_entregable, flg_multicalificable):
    fecha_inicio= convertDatetime(hora_inicio)
    fecha_fin=convertDatetime(hora_fin)
    Actividad().updateOne(idactividad,Nombre,tipo1,descripcion,fecha_inicio,fecha_fin,flag_confianza,flag_entregable, flg_multicalificable)
    return


def listarActividad(idHorario):
    listaActividad = Actividad().listar(idHorario).all()
    rpta = []

    for actividad in listaActividad:
        d = actividad.json()
        try:
            d['idRubrica'] = Rubrica.query.filter(and_(Rubrica.id_actividad == d['idActividad'], Rubrica.tipo == 4)).first().id_rubrica
        except:
            d['idRubrica'] = None    
        rpta.append(d)
    return rpta

def eliminarActividad(idActividad):
    actividad = Actividad().getOne(idActividad)
    nowStr = datetime.datetime.now().__str__()
    print(nowStr)
    now  = datetime.datetime.strptime(nowStr,'%Y-%m-%d %H:%M:%S.%f')
    fechaInicioActividad = datetime.datetime.strptime(actividad.fecha_inicio,'%Y-%m-%d %H:%M:%S.%f')
    if (now >= fechaInicioActividad):
        return {'message' : 'error - Actividad en proceso'}
    else:
        try:
            Actividad().deleteOne(idActividad)
            return {'message' : 'Se elimino correctamente'}
        except:
            return {'message' : 'Error no se elimino correctamente'}

def desactivarRubrica(idRubrica):
    try:
        Rubrica.desactivarRubrica(idRubrica)
        d = {}
        d['succeed'] = True
        d['message'] = "Rubrica desactivada"
        return d
    except Exception as ex:
        d = {}
        d['succeed'] = False
        d['message'] = str(ex)
        return d

#def preguntasFijasCoevaluacion