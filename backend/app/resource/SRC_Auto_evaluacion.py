from flask_restful import Resource
from flask import Flask, request
from app.controller.CTR_Auto_evaluacion import *
class Crear_auto_evaluacion(Resource):
    def post(self):
        data = request.get_json()
        idActividad = data['idActividad']
        listaFamilia  = data['listaFamilia']
        # VALIDACION
        #
        #
        return crearAutoEvaluacion(idActividad,listaFamilia)

class ListarObjetos(Resource):
    def post(self):
        data = request.get_json()
        idActividad=data['idActividad']
        return listarObjetosAutoevaluacion(idActividad)