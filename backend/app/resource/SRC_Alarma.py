from flask_restful import Resource
from flask import Flask, request
from app.controller.CTR_Alarma import *
class Crear_alarma(Resource):
    def post(self):
        data = request.get_json()
        idActividad = data['idActividad']
        nombre = data['nombre']
        asunto = data['asunto']
        mensaje = data['mensaje']
        fechaEjecucion = data['fechaEjecucion']
        return crearAlarma(idActividad,nombre,asunto, mensaje,fechaEjecucion)

class Listar_alarma(Resource):
    def post(self):
        data = request.get_json()
        idActividad = data['idActividad']
        return listarAlarma(idActividad)


class Editar_alarma(Resource);
    def post(self):
        data = request.get_json()
        idAlarma = data['idAlarma']
        nombre = data['nombre']
        asunto = data['asunto']
        mensaje = data['mensaje']
        fechaEjecucion = data['fechaEjecucion']

        return editarAlarma(idAlarma,nombre,asunto,mensaje,fechaEjecucion)