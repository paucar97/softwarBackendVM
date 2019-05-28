from flask_restful import Resource
from flask import Flask, request
from app.controller.CTR_Co_evaluacion import *

class Crear_co_evaluacion(Resource):
    def post(self):
        data = request.get_json()
        idActividad = data['idActividad']
        listaPregunta  = data['listaPreguntas']
        # VALIDACION
        #
        #
        return crearCoEvaluacion(idActividad,listaPregunta)

class ListarPreguntas(Resource):
    def post(self):
        data = request.get_json()
        idActividad=data['idActividad']
        return listarObjetosCoevaluacion(idActividad)

class Editar_co_evaluacion(Resource):
    def post(self):
        data = request.get_json()
        idActividad = data['idActividad']
        listaPregunta  = data['listaPreguntas']
        # VALIDACION
        #
        #
        return editarCoEvaluacion(idActividad,listaPregunta)

class Eliminar_co_evaluacion(Resource):
    def post(self):
        data = request.get_json()
        idActividad=data['idActividad']
        return eliminarCoEvaluacion(idActividad)

class Existe_Co_evaluacion(Resource):
    def post(self):
        data = request.get_json()
        idActividad=data['idActividad']
        return existeCoevaluacion(idActividad)