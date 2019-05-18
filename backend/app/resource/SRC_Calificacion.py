from flask_restful import Resource
from flask import Flask, request
from app.controller.CTR_Calificacion import *
class Obtener_alumnos_entregable_entregado(Resource):
    def post(self):
        data  = request.get_json()
        idActividad = data["idActividad"]

        return obtenerAlumnosEntregableEntregado(idActividad)

class Registrar_calificaciones(Resource):
    def post(self):
        data = request.get_json()
        idAlumno= data['idAlumno']
        idActividad = data['idActividad']
        idRubrica = data['idRubrica']
        listaRubrica = data['listaRubrica']

        return registrarCalificaciones(idAlumno,idActividad,idRubrica,listaRubrica)