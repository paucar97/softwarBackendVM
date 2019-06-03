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
        return obtenerRubricaEvaluacion(idActividad)

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
        tipo = data['tipo']
        # VALIDACION
        #
        #
        return crearRubrica(idActividad, idFlgEspecial, idUsuarioCreador, nombreRubrica, listaAspectos, tipo)

class Editar_rubrica(Resource):
    def post(self):
        data = request.get_json()
        idRubrica = data['idRubricaActual']
        idFlgEspecial = data['flgRubricaEspecial']
        idUsuarioCreador = data['idUsuarioCreador']
        nombreRubrica = data['nombreRubrica']
        idActividad = data['idActividad']
        listaAspectos = data['listaAspectos']
        return editarRubrica(idRubrica, idFlgEspecial, idUsuarioCreador, nombreRubrica, listaAspectos)

class Crear_Actividad(Resource):
    def post(self):
        data = request.get_json()
        idHorario = data['idHorario']
        nombre = data['nombre']
        tipo = data['tipo']
        descripcion = data['descripcion']
        fechaInicio = data['fechaInicio']
        fechaFin = data ['fechaFin']
        flag_confianza= data['flgConfianza'] 
        flag_entregable = data['flgEntregable']
        idUsuarioCreador = data['idUsuarioCreador']
        flg_multicalificable = data['flgMulticalificable']
        return CrearActividad(idHorario,nombre,tipo,descripcion,fechaInicio,fechaFin,flag_confianza,flag_entregable,idUsuarioCreador, flg_multicalificable)

class Editar_Actividad(Resource):
    def post(self):
        data=request.get_json()
        idActividad=data['idActividad']
        nombre=data['nombre']
        tipo=data['tipo']
        descripcion=data['descripcion']
        fecha_inicio=data['fechaInicio']
        fecha_final=data['fechaFinal']
        flag_confianza=data['flgConfianza']
        flag_entregable=data['flgEntregable']
        idUsuarioCreador = data['idUsuarioCreador']
        flg_multicalificable = data['flgMulticalificable']

        return EditarActividad(idActividad,nombre,tipo,descripcion,fecha_inicio,fecha_final,flag_confianza,flag_entregable, flg_multicalificable)

class Listar_Actividad(Resource):
    def post(self):
        data = request.get_json()
        idHorario = data['idHorario']
        return listarActividad(idHorario)


class Eliminar_actividad(Resource):
    def post(self):
        data = request.get_json()
        idActividad = data['idActividad']


        return eliminarActividad(idActividad)