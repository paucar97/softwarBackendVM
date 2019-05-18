from flask_restful import Resource
from flask import Flask, request
from app.controller import CTR_Permiso_usuario_horario

from app.controller import CTR_TEST_ListarCursos

class Obtener_cursos_activos_alumno(Resource):
    def post(self):
        data = request.get_json()
        idAlumno = data['idAlumno']

        # VALIDACION
        #
        #

        return CTR_Permiso_usuario_horario.obtenerCursosActivosXAlumno(idAlumno)

class Listar_cursos_dictando(Resource):
    def get(self):
        data = request.get_json()
        idProfesor = data['idProfesor']  # ver si el nombre es ese o idusuario

        # if idProfesor == None:
        #     pass

        return CTR_TEST_ListarCursos.obtenerCursosActivosXProfesor(idProfesor)
        #return CTR_Permiso_usuario_horario.obtenerCursosActivosXProfesor(idProfesor)
