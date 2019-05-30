from app.models.encuesta import Encuesta
from app.models.pregunta import Pregunta
from app.models.actividad import Actividad
from app.models.encuesta_pregunta import Encuesta_pregunta
from app.models.horario_encuesta import Horario_encuesta

def crearCoEvaluacion(idActividad,listaPregunta):
    encuestaObjecto =Encuesta(
        tipo = 'COEVALUACION',
        nombre = 'Coevaluacion de la actividad '+str(idActividad),
        descripcion = 'SEGUNDO SERVICIO',
        flg_especial =0
    )
    idEncuesta = Encuesta().addOne(encuestaObjecto)
    listaIdPreguntas=[]
    for pregunta in listaPregunta:
            
            auxPreguntaObjecto = Pregunta(
                descripcion = pregunta['pregunta'],
                tipo_pregunta = 3
            )
            aux = Pregunta().addOne(auxPreguntaObjecto)
            listaIdPreguntas.append(aux)
    
    for idPregunta in listaIdPreguntas:
        Encuesta_preguntaObjecto = Encuesta_pregunta(
            id_encuesta = idEncuesta,
            id_pregunta = idPregunta
        ) 
        Encuesta_pregunta().addOne(Encuesta_preguntaObjecto)
    idHorario = Actividad().getOne(idActividad).id_horario
    Horario_encuestaObjecto = Horario_encuesta(
        id_horario = idHorario,
        id_encuesta =idEncuesta,
        id_actividad = idActividad 
    )
    Horario_encuesta().addOne(Horario_encuestaObjecto)
    return

def listarObjetosCoevaluacion(idActividad):   
    listaEncuesta = Horario_encuesta().getAll(idActividad)
    idencuesta = 0
    for horario_encuesta in listaEncuesta:
        id = horario_encuesta.id_encuesta
        encuesta = Encuesta().getOne(id)
        if encuesta.tipo == 'COEVALUACION':
            idencuesta = encuesta.id_encuesta
            
    print(idencuesta)
    if idencuesta == 0:
        print('error')
        return

    encuesta = Encuesta().getOne(idencuesta)
    listaPregunta = []
    listaEP = []
    id = encuesta.id_encuesta
    listaEP=Encuesta_pregunta().getAll(id)#Lista de todos los objetos preguntas para esa pregunta
    for EncuestaPregunta in listaEP:
        idPregunta=EncuestaPregunta.id_pregunta
        pregunta=Pregunta().getOne(idPregunta)#sacarpreguntas
        d = {}
        d['pregunta'] = pregunta.descripcion
        listaPregunta.append(d)
                    
    l={}

    l['listaPreguntas'] = listaPregunta   
    return l

def editarCoEvaluacion(idActividad,listaPregunta):
    listaEncuesta = Horario_encuesta().getAll(idActividad)
    idencuesta = 0
    for horario_encuesta in listaEncuesta:
        id = horario_encuesta.id_encuesta
        encuesta = Encuesta().getOne(id)
        if encuesta.tipo == 'COEVALUACION':
            idencuesta = encuesta.id_encuesta
            
      
    if idencuesta==0:
        print('error')
        return

    listaEncuestaPregunta = Encuesta_pregunta().getAll(idencuesta)
    Encuesta_pregunta().eliminarFilas(idencuesta)
    for encuestapregunta in listaEncuestaPregunta:
        idpregunta = encuestapregunta.id_pregunta
        Pregunta().eliminarPregunta(idpregunta)
    
    listaIdPreguntas=[]
    for pregunta in listaPregunta:
            
            auxPreguntaObjecto = Pregunta(
                descripcion = pregunta['pregunta'],
                tipo_pregunta = 3
            )
            aux = Pregunta().addOne(auxPreguntaObjecto)
            listaIdPreguntas.append(aux)

    for idPregunta in listaIdPreguntas:
        Encuesta_preguntaObjecto = Encuesta_pregunta(
            id_encuesta = idencuesta,
            id_pregunta = idPregunta
        ) 
        Encuesta_pregunta().addOne(Encuesta_preguntaObjecto)
    
    return

def eliminarCoEvaluacion(idActividad):
    listaEncuesta =Horario_encuesta().getAll(idActividad)
    idencuesta=0
    for horario_encuesta in listaEncuesta:
        id=horario_encuesta.id_encuesta
        encuesta=Encuesta().getOne(id)
        if encuesta.tipo == 'COEVALUACION':
            idencuesta=encuesta.id_encuesta
            
    if idencuesta == 0:
        print('error')
        return
        
    listaEncuestaPregunta = Encuesta_pregunta().getAll(idencuesta)
    Encuesta_pregunta().eliminarFilas(idencuesta)
    for encuestapregunta in listaEncuestaPregunta:
        idpregunta = encuestapregunta.id_pregunta
        Pregunta().eliminarPregunta(idpregunta)

    Horario_encuesta().eliminarHorarioEncuesta(idencuesta)
    flag = Encuesta().eliminarEncuesta(idencuesta)
    

    return flag

def existeCoevaluacion(idActividad):
    listaEncuesta = Horario_encuesta().getAll(idActividad)
    if listaEncuesta is None:
        return {'message':'False'}
    else:
        for horario_encuesta in listaEncuesta:
            id = horario_encuesta.id_encuesta
            encuesta = Encuesta().getOne(id)
            if encuesta.tipo == 'COEVALUACION':
                return {'message':'True'}

    return {'message':'False'}   