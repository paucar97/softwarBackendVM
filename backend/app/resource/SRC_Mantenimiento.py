from flask_restful import Resource
from flask import Flask, request
from app.controller.CTR_Mantenimiento import *

class Crear_semestre(Resource):
    def post(self):
        data = request.get_json()
        nombreSemestre = data['nombreSemestre']
        return crearSemestre(nombreSemestre)

class Listar_semestres_no_activos(Resource):
    def post(self):
        data = request.get_json()
        return listarSemestresNoActivos()

class Activar_semestre(Resource):
    def post(self):
        data = request.get_json()
        idSemestre = data['idSemestre']
        return activarSemestre(idSemestre)
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

