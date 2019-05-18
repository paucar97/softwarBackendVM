from flask_restful import Resource
from flask import Flask, request
from app.controller.CTR_Usuario import Login_Controlador
class Login(Resource):
    def post(self):
        #print(type(request))
        #print(request)
        print(request.json)
        data = request.get_json()
        
        clave = data['clave']
        email = data['email']
        
        # controlador verificador
        #
        #
        # fin de validacion
        return Login_Controlador(email,clave)
        
