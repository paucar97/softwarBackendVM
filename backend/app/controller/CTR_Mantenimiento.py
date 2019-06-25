from app.models import db
from app.models.semestre import Semestre
from app.models.semestre_especialidad import Semestre_especialidad
from app.models.especialidad import Especialidad
from app.models.curso import Curso

def crearSemestre(nombreSemestre):
    objSemestre = Semestre(nombre = nombreSemestre,flg_activo = 0)
    Semestre().addOne(objSemestre)
    return { 'message' : 'Se agrego correctamente'}

def listarSemestresNoActivos():
    semestres = Semestre().getAllNoActivos().all()
    lstSemestre = []
    for semestre in semestres:
        aux ={}
        aux['nombre'] = semestre.nombre
        aux['idSemestre'] = semestre.id_semestre
        lstSemestre.append(aux)

    return lstSemestre

def activarSemestre(idSemestre):
    Semestre().activar(idSemestre)          
    Semestre_especialidad().activacionSemestre(idSemestre)
    return { 'message' : 'Se agrego correctamente'}




def obtenerlistaSemestresNoActivos():
    listaSemestres = Semestre.getAll()
    lista = list()
    for semestre in listaSemestres:
        c = {}
        c['id_semestre'] = semestre.id_semestre
        c['nombre'] = semestre.nombre
        lista.append(c)

    listaS = {}
    listaS['listaSemestres'] = lista
    
    return listaS


def obtenerEspecialidadxSemestre():
    semestreActivo=Semestre.getOne()
    especialidades= Especialidad().getAll()
    lista = list()
    for especialidad in especialidades:
        #esp = Especialidad.getOne(especialidad.id_especialidad)
        c = {}
        c['id_especialidad'] = especialidad.id_especialidad
        c['nombre'] = especialidad.nombre
        lista.append(c)

    listaE = {}
    
    listaE['listaEspecialidades'] = lista
    print(listaE)
    return listaE


def obtenerCursosxEspecialidad(idespecialidad):
    semestreActivo=Semestre.getOne()
    listaCursos= Curso.getCursosActivosxEspecialidad(semestreActivo.id_semestre,idespecialidad)
    lista=list()
    for curso in listaCursos:
        c={}
        c['id_curso'] = curso.id_curso 
        c['nombre'] = curso.nombre
        c['clave'] = curso.codigo
        lista.append(c)

    listaC={}
    listaC['listaCursos'] = lista
    return listaC

def obtenerNombreSemestreActivo():
    semestreActivo=Semestre.getOne()
    s={}
    s['id_semestre'] = semestreActivo.id_semestre
    s['nombre'] = semestreActivo.nombre

    return s
