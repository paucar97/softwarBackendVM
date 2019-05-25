from flask_restful import Resource
from flask import Flask, request
from app.controller.CTR_Actividad import *
class Obtener_rubrica_idactividad(Resource):
    def post(self):
        data = request.get_json()
        idActividad = data['idActividad']
        # VALIDACION
        #
        #
        return obtenerRubricaXIdActividad(idActividad)

class Obtener_rubricas_pasadas(Resource):
    def get(self):
        data = request.get_json()
        idUsuario = data['idUsuario']
        idCurso = data['idCurso']
        # VALIDACION
        #
        #
        return obtenerRubricasPasadas(idUsuario, idCurso)

class Crear_rubrica(Resource):
    def post (self):
        data = request.get_json()
        idFlgEspecial = data['flgRubricaEspecial']
        idUsuarioCreador = data['idUsuarioCreador']
        nombreRubrica = data['nombreRubrica']
        idActividad = data['idActividad']
        listaAspectos = data['listaAspectos']
        # VALIDACION
        #
        #
        return crearRubrica(idActividad, idFlgEspecial, idUsuarioCreador, nombreRubrica, listaAspectos)

class Crear_Actividad(Resource):
    def post(self):
        data=request.get_json()
        idHorario=data['idHorario']
        nombre=data['nombre']
        tipo=data['tipo']
        #descripcion=data['descripcion']
        fechaInicio=data['fechaInicio']
        fechaFin=data['fechaFin']
        flag_entregable=data['flgEntregable']

        return CrearActividad(idHorario,nombre,tipo,descripcion,fechaInicio,fechaFin,flag_entregable)

class Editar_Actividad(Resource):
    def post(self):
        data=request.get_json()
        idActividad=data['idActividad']
        nombre=data['nombre']
        tipo=data['tipo']
        #descripcion=data['descripcion']
        fecha_inicio=data['fechaInicio']
        fecha_final=data['fechaFinal']
        flag_entregable=data['flagEntregable']

        return EditarActividad(idActividad,nombre,tipo,descripcion,fecha_mod,fecha_inicio,fecha_final,flag_entregable)

class Listar_Actividad(Resource):
    def post(self):
        data = request.get_json()
        idHorario = data['idhorario']
        return listarActividad(idHorario)