from app.models.semestre import Semestre
from app.models.semestre_especialidad import Semestre_especialidad

def crearSemestre(nombreSemestre):
    objSemestre = Semestre(nombre = nombreSemestre,flag_activo = 0)
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