from app.models.horario import Horario
from app.models.curso import Curso
from app.models.permiso_usuario_horario import Permiso_usuario_horario

def listarCursos(idUsuario):
    listaPersonaUsuarioHoraro=Permiso_usuario_horario.getAllUsuario(idUsuario)
    listaNombreHorario=[]
    listaIdHorario=[]
    listaCursos=[]
    for PersonaUsuarioHorario in listaPersonaUsuarioHoraro:
        horario=Horario.getOne(PersonaUsuarioHorario.id_horario)
        listaNombreHorario.append(horario.nombre)
        listaIdHorario.append(horario.id_horario)
        curso=Horario.obtenerCurso(PersonaUsuarioHorario.id_horario)
        listaCursos.append(curso)

    c={}
    listaCursoHorario=[]
    num=len(listaCursos)
    for i in range(num):
        d={}
        d['nombreHorario']=listaNombreHorario[i]
        d['idHorario']=listaIdHorario[i]
        curso=listaCursos[i]
        d['nombreCurso']=curso.nombre
        d['codigo']=curso.codigo
        listaCursoHorario.append(d)

    c['listaCursos']=listaCursoHorario

    return c