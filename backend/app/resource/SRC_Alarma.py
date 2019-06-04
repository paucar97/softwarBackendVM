from flask_restful import Resource
from flask import Flask, request
from app.controller.CTR_Alarma import *
class Crear_alarma(Resource):
    def post(self):
        data = request.get_json()
        idActividad = data['idActividad']
        asunto = data['asunto']
        mensaje = data['mensaje']
        fechaEjecucion = data['fechaEjecucion']
        return crearAlarma(idActividad,asunto, mensaje,fechaEjecucion)