from app.models.grupo import Grupo
from app.models.actividad import Actividad
from app.models.alumno_actividad import Alumno_actividad
from app.models.usuario import Usuario
from app.models.grupo_alumno_horario import Grupo_alumno_horario
from app.commons.messages import *

def crearGrupo(idActividad,grupos):
    idHorario = Actividad().getOne(idActividad).id_horario
    
    for grupo in grupos:
        objGrupo = Grupo(nombre = grupo['nombre'],flg_grupo_general = 0)
        idGrupo = Grupo().addOne(objGrupo) # agrego grupo a la bd
        for alumno in grupo['lstAlumnos']:
                
            objAlumnoInGrupo = Grupo_alumno_horario(id_grupo = idGrupo,id_horario = idHorario,id_usuario = alumno['idAlumno'])
            Grupo_alumno_horario().addOne(objAlumnoInGrupo)
            Alumno_actividad().updateGrupo(idActividad,alumno['idAlumno'],idGrupo)

            #MODULO ACTUALIZAR SUS ID GRUPOS EN ALUMNO ACTIVIDAD

    return {"message": "realizado"}

def listarIntegrantes(idGrupo):
    listaIntegrante = Grupo_alumno_horario().getAll(idGrupo)
    rpta = []
    for integrante in listaIntegrante:
        d=dict()
        alumno = Usuario().getOneId(integrante.id_usuario)
        d['nombre'] = alumno.nombre
        d['codigoPucp'] = alumno.codigo_pucp
        d['apellidoPaterno'] = alumno.apellido_paterno
        d['apellidoMaterno'] = alumno.apellido_materno
        d['idUsuario'] = alumno.id_usuario
        rpta.append(d)

    return rpta 

def crearGrupoGeneral(idHorario,grupos):

    for grupo in grupos:
        objGrupo = Grupo(nombre = grupo['nombre'],flg_grupo_general=1)
        idGrupo = Grupo().addOne(objGrupo) # agrego grupo a la bd
        for alumno in grupo['lstAlumnos']:
                
            objAlumnoInGrupo = Grupo_alumno_horario(id_grupo = idGrupo,id_horario = idHorario,id_usuario = alumno['idAlumno'])
            Grupo_alumno_horario().addOne(objAlumnoInGrupo)
            # SE CREO EL GRUPO GENERAL 

    return {"message": "realizado"}