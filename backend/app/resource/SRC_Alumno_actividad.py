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
        idActividad = int(data['idActividad'])
        idAlumno = int(data['idAlumno'])
        comentario = data['comentario']
        # VALIDACION
        #
        #
        return controller.ingresarComentarioAlumno(idActividad, idAlumno, comentario)

class Responder_comentario_alumno(Resource):
    def post(self):
        data = request.get_json()
        idActividad = int(data['idActividad'])
        idAlumno = int(data['idAlumno'])
        idProfesor = int(data['idProfesor'])
        respuesta = data['respuesta']
        # VALIDACION
        #
        #
        return controller.responderComentarioAlumno(idActividad, idAlumno, idProfesor, respuesta)

class Obtener_alumnos_actividad(Resource):
    def post(self):
        data = request.get_json()
        idActividad = data['idActividad']

        return controller.listaAlumnos(idActividad)

class Obtener_nota_alumno(Resource):
    def post(self):
        data = request.get_json()
        idAlumno = data['idAlumno']
        idActividad = data['idActividad']
        return controller.obtenerNotaAlumno(idAlumno, idActividad)

class Calificar_alumno_actividad(Resource):
    def post(self):
        data = request.get_json()
        idActividad = data['idActividad']
        idAlumno = data['idAlumno']
        idJp = data['idJp']
        nota = data['nota']
        idRubrica = data['idRubrica']
        flgFalta = data['flgFalta']
        listaNotaAspectos = data['listaNotaAspectos']
        #flgCalifico = data['flgCalifico']

        return controller.calificarAlumno(idActividad, idAlumno, idRubrica, idJp, nota, listaNotaAspectos, flgFalta)

class Editar_nota_alumno_actividad(Resource):
    def post(self):
        data = request.get_json()
        idActividad = data['idActividad']
        idAlumno = data['idAlumno']
        nota = data['nota']
        idRubrica = data['idRubrica']
        listaNotaAspectos = data['listaNotaAspectos']

        return controller.editarNotaAlumno(idActividad, idAlumno, idRubrica, idJp, nota, listaNotaAspectos, flgFalta)

class Publicar_calificacion_para_revision(Resource):
    def post(self):
        data = request.get_json()
        idActividad = data['idActividad']
        idJpReviso = data['idJpReviso']
        return controller.publicarParaRevision(idActividad, idJpReviso)

class Listar_alumnos_destacados(Resource):
    def post(self):
        data = request.get_json()
        idActividad = data['idActividad']

        return controller.listarAlumnosDestacados(idActividad)

class Obtener_estadistica_actividad(Resource):
    def post(self):
        data = request.get_json()
        idActividad = data['idActividad']

        return controller.obtenerEstadisticaActividad(idActividad)


#class Enviar_notificacion_profesor(Resource):
#    def post(self):
#        data = request.get_json()


