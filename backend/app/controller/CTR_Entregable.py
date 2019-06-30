from app.models.entregable import Entregable
from app.commons.paths import pathTest,urlDecarga
from app.models.actividad import Actividad
import io
def crearEntregableObjeto(idActividad,idUsuario,fechaEntrega,tipo,nombreArchivo = None,url=None,path=None,doc=None):
    if doc == None:
        data = None
    else:
        data = doc.read()

    entregableObjeto = Entregable(
        id_actividad = idActividad,
        id_alumno = idUsuario,
        url_entregable = url,
        nombre_archivo = nombreArchivo,  
        fecha_creado=fechaEntrega,
        flg_activo = 1,
        path = path,
        tipo = tipo,
        documento = data
        )
    return entregableObjeto

def subirEntregable(idActividad,idUsuario,listaFiles,url,tipo,fechaEntrega =None):

    if tipo == 1 :
        for file in listaFiles:
            entregableObjeto = crearEntregableObjeto(idActividad,idUsuario,fechaEntrega,tipo,file.filename,path=pathTest,doc=file)
            Entregable().addOne(entregableObjeto)
    elif tipo == 2 :
        entregableObjeto = crearEntregableObjeto(idActividad,idUsuario,fechaEntrega,tipo,url = url)
        Entregable().addOne(entregableObjeto)
    else:
        for file in listaFiles:
            entregableObjeto = crearEntregableObjeto(idActividad,idUsuario,fechaEntrega,tipo,file.filename,path=pathTest,doc=file)
            Entregable().addOne(entregableObjeto)
        entregableObjeto = crearEntregableObjeto(idActividad,idUsuario,fechaEntrega,tipo,url = url)
        Entregable().addOne(entregableObjeto)
    return {'message':'subio'}       
    


def mostrarEntregable(idActividad,idUsuario):
    actividad  = Actividad().getOne(idActividad).tipo
    if tipo == 'I':
        listaEntregables = Entregable().getAll(idActividad,idUsuario)
        d=[]
        
        for entregable in listaEntregables:
            #print(entregable.json())
            d.append(entregable.json())
        return d
    else:
        listaIntegrante = Grupo_alumno_horario().getAll(idUsuario)
        d = []
        for integrante in listaIntegrante:
            listaEntregables = Entregable().getAll(idActividad,integrante.id_usuario)
            for entregable in listaEntregables:
                d.append(entregable.json())
        return d 



def descargaEntregable(idEntregable):
    entregableObjeto = Entregable().getOne(idEntregable)
    data = entregableObjeto.documento
    filename =entregableObjeto.nombre_archivo
    _,extension = filename.split('.') 
    with open(pathTest+filename,'wb') as file:
        file.write(data)
    filename = filename.replace(' ','%20') 
    return { 'url' : urlDecarga+filename, 'extension':extension }
    #PROCESO DE DESCARGA
    #
    #
    #
    """
    return send_file(
    io.BytesIO(image_binary),
    mimetype='image/jpeg',
    as_attachment=True,
    attachment_filename='%s.jpg' % pid)
    """
    return
