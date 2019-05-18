from app.models.alumno_actividad import Alumno_actividad
from app.models.alumno_nota_aspecto import Alumno_nota_aspecto
from app.models.alumno_nota_indicador import Alumno_nota_indicador 
from app.models.usuario import Usuario
from app.models.entregable import Entregable 
def obtenerAlumnosEntregableEntregado(idActividad):
    listaAlumnos = Alumno_actividad().getAllAlumnos(idActividad)
    
    alumnosEntregableEntregado = []
    for alumno in listaAlumnos:
        entregable = Entregable().getAll(idActividad,alumno.id_alumno)
        if entregable != None:
            d = {}
            d['idAlumno'] = alumno.id_alumno
            d['codigoPUCP'] = alumno.id_alumno
            aux = Usuario().getOneId(alumno.id_alumno)
            d['nombre'] = aux.nombre +  " " + aux.apellido_paterno
            d['entregables'] =[]
            for e in entregable:
                d['entregables'].append(e.json())
            alumnosEntregableEntregado.append(d)

    rpta = {}
    rpta['lista']= alumnosEntregableEntregado
    rpta['cantidad'] = len(alumnosEntregableEntregado)
    return rpta

def registrarCalificaciones(idAlumno,idActividad,idRubrica,listaRubrica):
    for aspecto in listaRubrica:
        idAspecto=aspecto['id_Aspecto']
        notaAlumnoAspectoObjeto = Alumno_nota_aspecto(
            id_actividad = idActividad,
            id_alumno = idAlumno,
            id_rubrica = idRubrica,
            id_aspecto = idAspecto # CREO Q FALTA COMENTARIO DEL ASPECTO O ALGO ASI
        )
        Alumno_nota_aspecto().addOne(notaAlumnoAspectoObjeto)
        notaTotal = 0
        for indicador in aspecto['lista_indicadores']:
            idIndicador=indicador['id_indicador']
            nota =indicador['nota']
            comentario =indicador['comentario']
            notaAlumnoIndicadorObjeto = Alumno_nota_indicador(
                    id_actividad = idActividad,
                    id_alumno = idAlumno,
                    id_rubrica = idRubrica,
                    id_aspecto= idAspecto,
                    id_indicador = idIndicador,
                    nota = nota,
                    comentario = comentario
            )
            Alumno_nota_indicador().addOne(notaAlumnoIndicadorObjeto)
            notaTotal = notaTotal + nota
        notaAlumnoAspectoObjeto.updateNota(notaTotal)
    return {'message': 'termino'}