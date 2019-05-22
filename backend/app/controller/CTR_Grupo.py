from app.models.grupo import Grupo
from app.models.actividad import Actividad
from app.models.alumno_actividad import Alumno_actividad
from app.models.grupo_alumno_horario import Grupo_alumno_horario

def crearGrupo(idActividad,grupos):
    idHorario = Actividad().getOne(idActividad).id_horario
    
    for grupo in grupos:
        objGrupo = Grupo(nombre = grupo['nombre'])
        idGrupo = Grupo().addOne(objGrupo) # agrego grupo a la bd
        for alumno in grupo['lstAlumnos']:
            objAlumnoInGrupo = Grupo_alumno_horario(id_grupo = idGrupo,id_horario = idHorario,id_usuario = alumno['idAlumno'])
            Grupo_alumno_horario().addOne(objAlumnoInGrupo)
            #MODULO ACTUALIZAR SUS ID GRUPOS EN ALUMNO ACTIVIDAD