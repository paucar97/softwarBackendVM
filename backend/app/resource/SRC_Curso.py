from flask_restful import Resource
from flask import Flask, request
from app.controller.CTR_Curso import *

class Listar_Cursos(Resource):
    def get(self):
        data = request.get_json()
        idUsuario = data['idUsuario']
        # VALIDACION
        #
        #
        return listarCursos(idUsuario)