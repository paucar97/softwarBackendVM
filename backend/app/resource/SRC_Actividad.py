from flask_restful import Resource
from flask import Flask, request
from app.controller import CTR_Actividad as controller
class Obtener_rubrica(Resource):
    def post(self):
        data = request.get_json()
        idActividad = data['idActividad']
        tipo = data['tipo']
        if tipo <= 4 and tipo > 0:
            return controller.obtenerRubrica(idActividad, tipo)
        else:
            d = {}
            d['succeed'] = False
            d['message'] = "No se puede obtener este tipo de rubrica."
            return d

class Obtener_rubricas_pasadas(Resource):
    def get(self):
        data = request.get_json()
        idUsuario = data['idUsuario']
        idCurso = data['idCurso']
        # VALIDACION
        #
        #
        return controller.obtenerRubricasPasadas(idUsuario, idCurso)

class Crear_rubrica(Resource):
    def post (self):
        data = request.get_json()
        idFlgEspecial = data['flgRubricaEspecial']
        idUsuarioCreador = data['idUsuarioCreador']
        nombreRubrica = data['nombreRubrica']
        idActividad = data['idActividad']
        listaAspectos = data['listaAspectos']
        tipo = data['tipo']
        
        if tipo <= 4 and tipo > 0:
            return controller.crearRubrica(idActividad, idFlgEspecial, idUsuarioCreador, nombreRubrica, listaAspectos, tipo)
        else:
            d = {}
            d['succeed'] = False
            d['message'] = "No se puede crear este tipo de rubrica."
            return d

class Editar_rubrica(Resource):
    def post(self):
        data = request.get_json()
        idRubrica = data['idRubricaActual']
        idFlgEspecial = data['flgRubricaEspecial']
        idUsuarioCreador = data['idUsuarioCreador']
        nombreRubrica = data['nombreRubrica']
        listaAspectos = data['listaAspectos']
        tipo = data['tipo']
        return controller.editarRubrica(idRubrica, idFlgEspecial, idUsuarioCreador, nombreRubrica, listaAspectos, tipo)

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
        return controller.CrearActividad(idHorario,nombre,tipo,descripcion,fechaInicio,fechaFin,flag_confianza,flag_entregable,idUsuarioCreador, flg_multicalificable)

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

        return controller.EditarActividad(idActividad,nombre,tipo,descripcion,fecha_inicio,fecha_final,flag_confianza,flag_entregable, flg_multicalificable)

class Listar_Actividad(Resource):
    def post(self):
        data = request.get_json()
        idHorario = data['idHorario']
        return controller.listarActividad(idHorario)


class Eliminar_actividad(Resource):
    def post(self):
        data = request.get_json()
        idActividad = data['idActividad']


        return controller.eliminarActividad(idActividad)

class Obtener_registro_horas(Resource):
    def post(self):
        data = request.get_json()
        tipo = data['tipo'] 
        idActividadUHorario = data['idActividadUHorario']
        idAlumno = data['idAlumno']
        return controller.obtenerRegistroEsfuerzo(idAlumno, tipo, idActividadUHorario)

class Obtener_registro_horas_individual(Resource):
    def post(self):
        data = request.get_json()
        tipo = data['tipo'] 
        idActividadUHorario = data['idActividadUHorario']
        return controller.obtenerRegistroEsfuerzoIndividual(tipo, idActividadUHorario)

class Crear_registro_horas(Resource):
    def post(self):
        data = request.get_json()
        idActividadUHorario = data['idActividadUHorario']
        idUsuarioCreador = data['idUsuarioCreador']
        tipo = data['tipo']
        listaCategorias = data['listaCategorias']
        return controller.crearRegistroHoras(idUsuarioCreador, tipo, idActividadUHorario, listaCategorias)

class Registrar_horas(Resource):
    def post(self):
        data = request.get_json()
        idRegistroEsfuerzo = data['idRegistroEsfuerzo']
        idAlumno = data['idAlumno']
        listaCategorias = data['listaCategorias']
        return controller.registrarHoras(idRegistroEsfuerzo, idAlumno, listaCategorias)

class Obtener_profesores_calificados(Resource):
    def post(self):
        data = request.get_json()
        idActividad = data['idActividad']
        idAlumno = data['idAlumno']
        return controller.obtenerProfesoresPublicados(idActividad, idAlumno)