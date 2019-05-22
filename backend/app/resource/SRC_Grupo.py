from flask_restful import Resource
from flask import Flask, request
from app.controller.CTR_Grupo import *
class Crear_grupo(Resource):
    def post(self):
        data  = request.get_json()
        idActividad = data['idActividad']
        grupos = data['grupos']
        return crearGrupo(idActividad,grupos)


"""
{
    "idActividad" : "1",
    "grupos": [
                {"nombre": "florestack",
                "lstAlumnos" : [
                    {"idAlumno" : "1",
                    "nombre" : "carlos"
                    },
                    {"idAlumno" : "2",
                    "nombre" : "carlos"
                    }
                    
                ]
                }
            ]

}
"""