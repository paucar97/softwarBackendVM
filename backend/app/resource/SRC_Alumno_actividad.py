from flask_restful import Resource
from flask import Flask, request
from app.controller import CTR_Alumno_Actividad as controller

class Obtener_entregables_actividad_por_alumno(Resource):
    def post(self):
        data = request.get_json()
        print(data)
        idActividad = data['idActividad']
        # VALIDACION
        #
        #
        return controller.entregablesActividadXAlumno(idActividad)

class Obtener_alumnos_actividad(Resource):
    def post(self):
        data = request.get_json()
        idActividad = data['idActividad']

        return controller.listaAlumnos(idActividad)