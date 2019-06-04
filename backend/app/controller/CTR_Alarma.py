from app.commons.utils import *
from app.models.alarma import Alarma
from app.models.actividad_alarma import Actividad_alarma
def crearAlarma(idActividad,nombre,asunto, mensaje,fechaEjecucion):
    objAlarma = Alarma(
        fecha_ejecucion =convertDatetime(fechaEjecucion),
        flg_disponible = 1, # XQ CUANDO SE CREA SE ACTIVA , se puede usar como ver si ya se envio el mensaje nomas digo 
        mensaje = mensaje,
        asunto = asunto,
        nombre = nombre
    )
    idAlarma = Alarma().addOne(objAlarma)
    objActividaAlarma= Actividad_alarma(id_alarma = idAlarma, id_actividad = idActividad)
    Actividad_alarma().addOne(objActividaAlarma)
    return { "message" : "se registro correctamente"}


def listarAlarma(idActividad):
    lstAlarma = Actividad_alarma().getAll(idActividad)
    rpta = []
    for _,alarma in lstAlarma:
        rpta.append(alarma.json())
    return rpta