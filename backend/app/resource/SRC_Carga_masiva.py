from flask_restful import Resource
from flask import Flask, request
from app.controller.CTR_Carga_Masiva import *
class Carga_masiva_horarios(Resource):
    def post(self):
        key = 'file 1'
        file  = request.files.get(key)

        return cargaMasivaHorarios(file)