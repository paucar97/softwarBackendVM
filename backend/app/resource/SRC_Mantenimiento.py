from flask_restful import Resource
from flask import Flask, request
from app.controller.CTR_Mantenimiento import *

class Lista_Semestres_NoActivos(Resource):
    def post(self):
        return obtenerlistaSemestresNoActivos()

class EspecialidadesxSemestre(Resource):
    def post(self):
        return obtenerEspecialidadxSemestre()

class CursosXEspecialidad(Resource):
    def post(self):
        data  = request.get_json()
        idEspecialidad = data['idEspecialidad']
        return obtenerCursosxEspecialidad(idEspecialidad)

class NombreSemestreActivo(Resource):
    def post(self):
        return obtenerNombreSemestreActivo()

