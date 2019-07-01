import pandas as pd
import codecs
from app.commons.paths import *
from app.models.usuario import Usuario
from app.models.permiso_usuario_horario import Permiso_usuario_horario
from app.models.semestre import Semestre
from app.models.curso import Curso
from app.models.horario import Horario
from app.models.especialidad import Especialidad
from app.models.permiso_usuario_horario import Permiso_usuario_horario
def SplitNombres( nombre ):
    u"""
    Autor original en código PHP: eduardoromero.
    https://gist.github.com/eduardoromero/8495437
    
    Separa los nombres y los apellidos y retorna una tupla de tres
    elementos (string) formateados para nombres con el primer caracter
    en mayuscula. Esto es suponiendo que en la cadena los nombres y 
    apellidos esten ordenados de la forma ideal:
 
    1- nombre o nombres.
    2- primer apellido.
    3- segundo apellido.
 
    SplitNombres( '' )
    >>> ('Nombres', 'Primer Apellido', 'Segundo Apellido')
    """
    a1,a2 = nombre.split(',')
    a2 = a2[1:]
    nombre = a2 +' ' + a1
    # Separar el nombre completo en espacios.
    tokens = nombre.split(" ")
 
    # Lista donde se guarda las palabras del nombre.
    names = []
 
    # Palabras de apellidos y nombres compuestos.
    especial_tokens = ['da', 'de', 'di', 'do', 'del', 'la', 'las', 
    'le', 'los', 'mac', 'mc', 'van', 'von', 'y', 'i', 'san', 'santa']
 
    prev = ""
    for token in tokens:
        _token = token.lower()
 
        if _token in especial_tokens:
            prev += token + " "
 
        else:
            names.append(prev + token)
            prev = ""
 
    num_nombres = len(names)
    nombres, apellido1, apellido2 = "", "", ""
 
    # Cuando no existe nombre.
    if num_nombres == 0:
        nombres = ""
 
    # Cuando el nombre consta de un solo elemento.
    elif num_nombres == 1:
        nombres = names[0]
 
    # Cuando el nombre consta de dos elementos.
    elif num_nombres == 2:
        nombres = names[0]
        apellido1 = names[1]
 
    # Cuando el nombre consta de tres elementos.
    elif num_nombres == 3:
        nombres = names[0]
        apellido1 = names[1]
        apellido2 = names[2]
 
    # Cuando el nombre consta de más de tres elementos.
    else:
        nombres = names[0] + " " + names[1]
        apellido1 = names[2]
        apellido2 = names[3]
 
    # Establecemos las cadenas con el primer caracter en mayúscula.
    nombres = nombres.title()
    apellido1 = apellido1.title()
    apellido2 = apellido2.title()
 
    return (nombres, apellido1, apellido2)

def getCorreoPucp(correos):
    if ',' in correos:
        cpucp,_ = correos.split(',')
        return cpucp
    else:
        return correos


def cargaMasivaHorarios(datos,idCurso,idEspecialidad):
    semestre=Semestre().getOne()
    idSemestre=semestre.id_semestre
    print("="*20)
    print(idSemestre)
    name = pathCargaMasivaAlumnoHorario+datos.filename
    data = datos.read()
    with open(name,'wb') as file:
        file.write(data)
    doc= codecs.open(name,'rU','latin1')
    for i in range(6):
        doc.readline()
    df = pd.read_csv(doc ,sep ='\t',encoding = 'latin1')
    #print(df)
    df['E-mail'] = df['E-mail'].apply( lambda x: getCorreoPucp(x))
    df['nombres'] = df['Nombre'].apply(lambda x : SplitNombres(x)[0])
    df['apellido_paterno']= df['Nombre'].apply(lambda x : SplitNombres(x)[1]) 
    df['apellido_materno'] = df['Nombre'].apply(lambda x : SplitNombres(x)[2]) 
    longitud = len(df)
    
    
    
    for i in range(longitud):
        idHorario = Horario().addOne(str(df.iat[i,2]),idCurso,idSemestre)  
        codigoPucp = str(df.iat[i,0])
        nombre = str(df.iat[i,5])
        email = str(df.iat[i,4])
        apellidoPaterno = str(df.iat[i,6])
        apellidoMaterno = str(df.iat[i,7])
        objUsuario = Usuario(nombre = nombre,email = email,apellido_paterno = apellidoPaterno , 
        apellido_materno = apellidoMaterno, flg_admin =0 ,codigo_pucp = codigoPucp, clave = codigoPucp)
        idUsuario = Usuario().addOne(objUsuario) 
        objAlumnoHorario = Permiso_usuario_horario(id_horario = idHorario,id_usuario = idUsuario, id_permiso = 2,id_semestre = idSemestre)
        Permiso_usuario_horario().addOne(objAlumnoHorario)
    
    return {'message' : 'leyo bien'}

def cargaMasivaCursos(datos,idEspecialidad):
    semestre = Semestre().getOne()
    idSemestre = semestre.id_semestre #
    print(datos)
    print(idEspecialidad)
    name = pathCargaMasivaCursoHorario + datos.filename
    data = datos.read()
    with open(name,'wb') as file:
        file.write(data)
    df = pd.read_excel(name,enconding = 'latin1')
    longitud = len(df)

    for i in range(longitud):
        nombreCurso = df.iat[i,0]
        codigoCurso = df.iat[i,1]
        horarios = []
        horarios = str(df.iat[i,2]).split(',')
        objCurso = Curso(id_especialidad = idEspecialidad,id_semestre =idSemestre,nombre = nombreCurso,codigo = codigoCurso)
        idCurso = Curso().addOne(objCurso)
        for horario in horarios:
            horario = horario.replace(' ','')
            Horario().addOne(horario,idCurso,idSemestre)
    return {'message' : 'leyo bien'}

def cargaMasivaProfesorJP(datos,idEspecialidad):
    semestre=Semestre().getOne()
    idSemestre=semestre.id_semestre
    name = pathCargaMasivaCursoHorario + datos.filename
    data = datos.read()
    with open(name,'wb') as file:
        file.write(data)
    df = pd.read_excel(name,enconding = 'latin1')
    
    longitud = len(df)

    for i in range(longitud):
        codigoCurso= str(df.iat[i,0])
        codigoPucp = str(df.iat[i,1])
        nombreCompleto = str(df.iat[i,2])
        aux = SplitNombres(nombreCompleto)
        nombres = aux[0]
        apellidoPaterno = aux[1]
        apellidoMaterno = aux[2]
        email = str(df.iat[i,3])
        objUsuario = Usuario(nombre = nombres,codigo_pucp = codigoPucp,email= email,clave = codigoPucp, apellido_paterno = apellidoPaterno, apellido_materno = apellidoMaterno,flg_admin =0)
        idUsuario = Usuario().addOne(objUsuario)
        idCurso = Curso().getOneClave(codigoCurso,idSemestre)
        tipo = str(df.iat[i,4])
        if tipo == "1":
            horarios = str( df.iat[i,5]).split(',')
            for horario in horarios:   
                horario = horario.replace(' ','')
                print(idCurso,horario,idSemestre)
                idHorario = Horario().getOneClave(idCurso,idSemestre,horario)
                objUsuaHorario = Permiso_usuario_horario(id_horario = idHorario,id_usuario =idUsuario, id_permiso = 1,id_semestre = idSemestre)
                Permiso_usuario_horario().addOne(objUsuaHorario)
            
        else:
            horarios = Horario().getAll(idCurso,idSemestre)
            for horario in horarios:
                
                idHorario = horario.id_horario
                objUsuaHorario = Permiso_usuario_horario(id_horario = idHorario,id_usuario =idUsuario, id_permiso = 3,id_semestre = idSemestre)
                Permiso_usuario_horario().addOne(objUsuaHorario)
            


    return {'message' : 'leyo bien'}