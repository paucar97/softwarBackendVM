from app.models.actividad import Actividad 
from app.models.rubrica import Rubrica 
from app.models.aspecto import Aspecto
from app.models.indicador import Indicador
from app.models.rubrica_aspecto_indicador import Rubrica_aspecto_indicador
from app.models.rubrica_aspecto import Rubrica_aspecto
from app.models.horario import Horario
from app.models.actividad_alarma import Actividad_alarma
from app.models.encuesta_pregunta import Encuesta_pregunta
from app.models.horario_encuesta import Horario_encuesta
from app.models.permiso_usuario_horario import Permiso_usuario_horario
from app.models.feedback_actividad import Feedback_actividad
from app.models.alumno_actividad import Alumno_actividad
from app.models.semestre import Semestre

def obtenerRubricaXidRubrica(idRubrica):
    nombreRubrica = Rubrica.obtenerRubrica(idRubrica).nombre
    d = {}
    d['nombre_rubrica'] = nombreRubrica

    aspectos = []
    listaAspectos = Rubrica_aspecto.obtenerAspectos(idRubrica)

    for aspecto in listaAspectos:
        aux = {}
        aux['id_aspecto'] = aspecto.id_aspecto
        aux['descripcion'] = aspecto.descripcion
        aux['informacion'] = aspecto.informacion
        aux['puntaje_max'] = aspecto.puntaje_max
        aux['tipo_clasificacion'] = aspecto.tipo_clasificacion
        indicadores = []
        listaIndicadores = Rubrica_aspecto_indicador.obtenerIndicadores(idRubrica, aspecto.id_aspecto)
        for indicador in listaIndicadores:
            aux2 = {}
            aux2['id_indicador'] = indicador.id_indicador
            aux2['descripcion'] = indicador.descripcion
            aux2['informacion'] = indicador.informacion
            aux2['puntaje_max'] = indicador.puntaje_max
            aux2['tipo'] = indicador.tipo
            indicadores.append(aux2)
        aux['lista_indicadores'] = indicadores
        aux['cant_indicadores'] = len(indicadores)
        aspectos.append(aux)
    d['lista_aspectos'] = aspectos
    d['cant_aspectos'] = len(aspectos)

    return d

def obtenerRubricaXIdActividad(idActividad):
    idRubrica = Actividad.getOne(idActividad).id_rubrica

    return obtenerRubricaXidRubrica(idRubrica)

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

def crearRubrica(idFlgEspecial, idUsuarioCreador, nombreRubrica, listaAspectos):
        rubricaObjeto = Rubrica(
            flg_rubrica_especial = idFlgEspecial,
            id_usuario_creador = idUsuarioCreador,
            nombre = nombreRubrica
        )

        idRubrica = Rubrica().addOne(rubricaObjeto)

        for aspecto in listaAspectos:
            aspectoObjeto = Aspecto(
                descripcion = aspecto['descripcion'],
                informacion  = aspecto['informacion'],
                puntaje_max = aspecto['puntajeMax'],
                tipo_clasificacion = aspecto['tipoClasificacion']
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
                    puntaje_max = indicador['puntajeMax'],
                    tipo = indicador['tipo']
                )
                idIndicador = Indicador().addOne(indicadorObjeto)

                rubricaAspectoIndicadorObj = Rubrica_aspecto_indicador(
                    id_rubrica = idRubrica,
                    id_aspecto = idAspecto,
                    id_indicador = idIndicador
                )
                aux2 = Rubrica_aspecto_indicador().addOne(rubricaAspectoIndicadorObj)
        
        d = {}
        d['idRubrica'] = idRubrica

        return d


def CrearActividad(idhorario,Nombre,tipo1,descripcion,fecha,flag_entregable1):
    semestre=Semestre().getOne()
    idSemestre=semestre.id_semestre
    actividadObjeto=Actividad(
        id_horario=idhorario,
        id_rubrica=1,
        id_semestre = idSemestre,
        nombre=Nombre,
        flg_activo=1,
        etapa=1,
        flg_entregable=flag_entregable1,
        fecha_modificacion=fecha,
        tipo=tipo1)

    idActividad= Actividad().addOne(actividadObjeto)

    #Cuando creamos el objeta, habrán alarmas predefinidas suponemos(?)
    #actividad_alarmaObjeto=Actividad_Alarma(
    #    id_actividad=idActividad,
    #    id_alarma=1,
    #)
    #Actividad_Alarma().addOne(actividad_alarmaObjeto)

    listaAlumnos= Permiso_usuario_horario().getAll(idSemestre,idhorario)
    listaIdAlumnos=[]
    idjp= 0
    idprofesor=0
    for usuario in listaAlumnos:
        if usuario.id_permiso== 3: #Alumnos
            listaIdAlumnos.append(usuario.id_usuario)
        if usuario.id_permiso == 2: #Jefe de Práctica
            idjp=usuario.id_usuario
        if usuario.id_permiso==1:
            idprofesor=usuario.id_usuario

    for idalumno in listaIdAlumnos:
        alumnoActividadObjeto=Alumno_actividad(
            id_actividad=idActividad,
            id_alumno=idalumno,
            id_jp=idjp,
            flg_activo=1,
            etapa=1,
            flag_entregable=flag_entregable1,
            comentario='')

        Alumno_actividad().addOne(alumnoActividadObjeto)

    #Feedback
    feedbackActividadObjeto=Feedback_actividad(
            id_profesor=idprofesor,
            id_actividad=idActividad,
            comentario='',
            flag_aprobado=0)

    Feedback_actividad().addOne(feedbackActividadObjeto)
    return 

def EditarActividad(idactividad,Nombre,tipo1,descripcion,fecha,hora_inicio,hora_fin,flag_entregable):
    Actividad.updateOne(idactividad,Nombre,tipo1,descripcion,fecha,hora_inicio,hora_fin,flag_entregable)
    Alumno_actividad.updateOne(idactividad,flag_entregable)