from flask_restful import Resource
from flask import Flask, request
from app.controller.CTR_Auto_evaluacion import *
class Crear_auto_evaluacion(Resource):
    def post(self):
        data = request.get_json()
        idFlgEspecial = data['flgRubricaEspecial']
        idUsuarioCreador = data['idUsuarioCreador']
        nombreRubrica = data['nombreRubrica']
        idActividad = data['idActividad']
        listaAspectos = data['listaAspectos']
        tipo = data['tipo']
        
        # VALIDACION
        #
        #
        
        return crearAutoEvaluacion(idActividad, idFlgEspecial, idUsuarioCreador, nombreRubrica, listaAspectos, tipo)

class ListarObjetos(Resource):
    def post(self):
        data = request.get_json()
        idActividad=data['idActividad']
        return listarObjetosAutoevaluacion(idActividad)

class Editar_auto_evaluacion(Resource):
    def post(self):
        data = request.get_json()
        idActividad = data['idActividad']
        listaFamilia  = data['listaFamilia']
        # VALIDACION
        #
        #
        return editarAutoEvaluacion(idActividad,listaFamilia)

class Eliminar_auto_evaluacion(Resource):
    def post(self):
        data = request.get_json()
        idActividad = data['idActividad']
        return eliminarAutoEvaluacion(idActividad)


class Existe_autoevaluacion(Resource):
    def post(self):
        data = request.get_json()
        idActividad = data['idActividad']
        return existeAutoevaluacion(idActividad)