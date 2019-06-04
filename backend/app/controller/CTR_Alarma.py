from app.commons.utils import *
from app.models.alarma import Alarma
from app.models.actividad_alarma import Actividad_alarma
def crearAlarma(idActividad,asunto, mensaje,fechaEjecucion):
    objAlarma = Alarma(
        fecha_ejecucion =convertDatetime(fechaEjecucion),
        flg_disponible = 1, # XQ CUANDO SE CREA SE ACTIVA , se puede usar como ver si ya se envio el mensaje nomas digo 
        mensaje = mensaje,
        asunto = asunto
    )
    idAlarma = Alarma().addOne(objAlarma)
    objActividaAlarma= Actividad_alarma(id_alarma = idAlarma, id_actividad = idActividad)
    Actividad_alarma().addOne(objActividaAlarma)
    return { "message" ; "se registro correctamente"}