from app.models.alumno_actividad import Alumno_actividad
from app.models.alumno_nota_aspecto import Alumno_nota_aspecto
from app.models.alumno_nota_indicador import Alumno_nota_indicador 
from app.models.actividad import Actividad
from app.models.usuario import Usuario
from app.models.grupo import Grupo
from app.models.entregable import Entregable 
from app.models.alumno_actividad_calificacion import Alumno_actividad_calificacion
def obtenerAlumnosEntregableEntregado(idActividad):
    tipoActividad = Actividad().getOne(idActividad).tipo

    if tipoActividad == 'I':
        listaAlumnos = Alumno_actividad().getAllAlumnos(idActividad)
        
        alumnosEntregableEntregado = []
        for alumno in listaAlumnos:
            entregable = Entregable().getAll(idActividad,alumno.id_alumno)
            d = {}
            d['idAlumno'] = alumno.id_alumno
            aux = Usuario().getOneId(alumno.id_alumno)
            d['codigoPUCP'] = aux.codigo_pucp
            d['nombre'] = aux.nombre +  " " + aux.apellido_paterno
            d['entregables'] =[]
            if entregable != None:
                for e in entregable:
                    d['entregables'].append(e.json())
            alumnosEntregableEntregado.append(d)

        rpta = {}
        rpta['lista']= alumnosEntregableEntregado
        rpta['cantidad'] = len(alumnosEntregableEntregado)
        return rpta
    else:
        ##try:
        listarGrupos = Alumno_actividad().getAllGrupos(idActividad)
        
        lstGrupos = []
        for grupo in listarGrupos:
            idGrupo = grupo.id_grupo
            d = dict()
            
            d['idGrupo'] = idGrupo
            
            d['nombreGrupo'] = Grupo().getOne(idGrupo).first().nombre
            lstGrupos.append(d)
        return lstGrupos
        ##except:
        """
        [
            
        ]
        """
        ##    return None 

def registrarCalificaciones(idAlumno,idActividad,idRubrica,listaRubrica):
    for aspecto in listaRubrica:
        idAspecto=aspecto['id_Aspecto']
        notaAlumnoAspectoObjeto = Alumno_nota_aspecto(
            id_actividad = idActividad,
            id_alumno = idAlumno,
            id_rubrica = idRubrica,
            id_aspecto = idAspecto # CREO Q FALTA COMENTARIO DEL ASPECTO O ALGO ASI
                
        )
        if len(aspecto['lista_indicadores']) == 0:
            notaAlumnoAspectoObjeto.nota = aspecto['nota']
            notaAlumnoAspectoObjeto.comentario = aspecto['comentario']
            Alumno_nota_aspecto().addOne(notaAlumnoAspectoObjeto)
        else:
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

def obtenerNotasFinales(idActividad,idRubrica):
    actividad = Actividad().getOne(idActividad)
    tipo = actividad.tipo
    rpta =[]
    if tipo == 'I':
        lstIdAlumnos = [reg.id_alumno  for reg in Alumno_actividad().getAllAlumnos(idActividad)]

        listaAlumnos = Alumno_actividad_calificacion().getAllAlumnos(idActividad,idRubrica)
        for alumno in listaAlumnos:
            d = {}
            auxAl = Usuario().getOneId(alumno.id_alumno)
            d['idAlumno'] = alumno.id_alumno
            lstIdAlumnos.remove(alumno.id_alumno)
            d['codigoPucp'] = auxAl.codigo_pucp
            d['nombreAlumno'] = auxAl.nombre + " " + auxAl.apellido_paterno + " " + auxAl.apellido_materno
            d['nota'] = alumno.nota
            rpta.append(d)
        for idAlumno in lstIdAlumnos:
            d={}
            auxAl = Usuario().getOneId(idAlumno)
            d['idAlumno'] = idAlumno
            d['codigoPucp'] = auxAl.codigo_pucp
            d['nombreAlumno'] = auxAl.nombre + " " + auxAl.apellido_paterno + " " + auxAl.apellido_materno
            d['nota'] = '--'
            rpta.append(d)          
    else:
        listarGrupos = Alumno_actividad().getAllGrupos(idActividad)
        for grupo in listarGrupos:
            d = {}
            auxGrupo = Grupo().getOne(grupo.id_grupo).first()
            d['idGrupo'] = auxGrupo.id_grupo
            d['nombreGrupo' ] = auxGrupo.nombre
            print(d)
            auxAl = Alumno_actividad().getAlumnoGrupo(auxGrupo.id_grupo,idActividad).first()
            auxAl2 = Alumno_actividad_calificacion().getNotaGrupo(idActividad,auxAl.id_alumno,idRubrica)
            if auxAl2 != None:
                d['nota'] = auxAl2.nota
            else:
                d['nota'] = None
            rpta.append(d)        
    r={}
    r['listaNotas'] = rpta 
    return r
