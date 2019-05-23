from flask_restful import Resource
from flask import Flask, request
from app.controller import CTR_Alumno_Actividad as controller

class Obtener_entregables_actividad_por_alumno(Resource):
    def post(self):
        data = request.get_json()
        idActividad = data['idActividad']
        # VALIDACION
        #
        #
        return controller.entregablesActividadXAlumno(idActividad)

class Ingresar_comentario_alumno(Resource):
    def post(self):
        data = request.get_json()
        idActividad = data['idActividad']
        idAlumno = data['idAlumno']
        comentario = data['comentario']
        # VALIDACION
        #
        #
        return controller.ingresarComentarioAlumno(idActividad, idAlumno, comentario)
class Obtener_alumnos_actividad(Resource):
    def post(self):
        data = request.get_json()
        idActividad = data['idActividad']

        return controller.listaAlumnos(idActividad)
