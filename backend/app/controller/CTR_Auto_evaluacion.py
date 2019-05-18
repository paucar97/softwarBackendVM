from app.models.encuesta import Encuesta
from app.models.pregunta import Pregunta
from app.models.actividad import Actividad
from app.models.encuesta_pregunta import Encuesta_pregunta
from app.models.horario_encuesta import Horario_encuesta
def crearAutoEvaluacion(idActividad,listaFamilia):
    encuestaObjecto =Encuesta(
        tipo = 'AUTOEVALUACION',
        nombre = 'Autoevaluacion de la actividad '+str(idActividad),
        descripcion = 'PIMER SERVICIO',
        flg_especial =0
    )
    idEncuesta = Encuesta().addOne(encuestaObjecto)
    listaIdPreguntas=[]
    for familia in listaFamilia:
        
        nombreFamilia = familia['familia']

        listaPregunta = familia['listaPregunta']

        for pregunta in listaPregunta:
            
            auxPreguntaObjecto = Pregunta(
                descripcion = pregunta['pregunta'],
                tipo_pregunta = 3,
                familia = nombreFamilia
            )
            aux = Pregunta().addOne(auxPreguntaObjecto)
            listaIdPreguntas.append(aux)
    
    for idPregunta in listaIdPreguntas:
        Encuesta_preguntaObjecto = Encuesta_pregunta(
            id_encuesta = idEncuesta,
            id_pregunta = idPregunta
        ) 
        Encuesta_pregunta().addOne(Encuesta_preguntaObjecto)
    
    Horario_encuestaObjecto = Horario_encuesta(
        id_horario = 1, # ESTO TIENE Q CAMIAR XQ DEBERIA SER NO OBLIGAROTIOR
        id_encuesta =idEncuesta,
        id_actividad = idActividad 
    )
    Horario_encuesta().addOne(Horario_encuestaObjecto)
    return

def listarObjetosAutoevaluacion(idActividad):   
    listaEncuesta=Horario_encuesta().getAll(idActividad)
    idencuesta=1
    for horario_encuesta in listaEncuesta:
        id=horario_encuesta.id_encuesta
        encuesta=Encuesta().getOne(id)
        if encuesta.tipo=='AUTOEVALUACION':
            idencuesta=encuesta.id_encuesta
            
    print(idencuesta)
    encuesta=Encuesta().getOne(idencuesta)
    l={}
    listaPregunta=[]
    listaFamilia=[]
    listaEP=[]
    id=encuesta.id_encuesta
    listaEP=Encuesta_pregunta().getAll(id)#Lista de todos los objetos preguntas para esa pregunta
    print(listaEP)
    lista=[]
    for EncuestaPregunta in listaEP:
        idPregunta=EncuestaPregunta.id_pregunta
        pregunta=Pregunta().getOne(idPregunta)#sacarpreguntas
        listaPregunta.append(pregunta)
        q=pregunta.familia
        if pregunta.familia not in listaFamilia:#nueva familia encontrada
            c={}
            c["pregunta"]=pregunta.descripcion
            d={}
            listaP=[]
            d['familia']=q
            listaP.append(c)
            d['listaPregunta']=listaP
            lista.append(d)#añades un json con nombre de la familia
            listaFamilia.append(q)#lista solo con nombre de la familia
        else:# si ya se encuentra en la lista familia
            i=0
            for familia in listaFamilia:# lo busca
                if pregunta.familia==familia:# encontro la familia
                    c={}
                    c["pregunta"]=pregunta.descripcion
                    lista[i]['listaPregunta'].append(c)#añade pregunta a esa familia
                    break
                else:
                    i=i+1
                    

    l={}

    l['listaFamilia']=lista     
    return l