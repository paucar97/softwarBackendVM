from flask_restful import Resource
from flask import Flask, request

#from sqlalchemy import create_engine
from app.controller.userCTR import *

class agregarUsuarioSRC(Resource):

    def post(self):

        datos= request.get_json()

        return agregarUsuarioCTR(datos)

class listarUser(Resource):
    def get(self,idU=None):
        if idU is None:
            return allUser()
        else:
            return oneUser(idU)

        
