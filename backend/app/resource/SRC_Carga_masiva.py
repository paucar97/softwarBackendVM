from flask_restful import Resource
from flask import Flask, request
from app.controller.CTR_Carga_Masiva import *
class Carga_masiva_horarios(Resource):
    def post(self):
        key = 'file 1'
        file  = request.files.get(key)
        idCurso = int(request.form['idCurso'])
        idEspecialidad = int(request.form['idEspecialidad'])
        return cargaMasivaHorarios(file,idCurso,idEspecialidad)
    
class Carga_masiva_cursos(Resource):
    def post(self):
        key = 'file 1'
        file = request.files.get(key)
        idEspecialidad= request.form['idEspecialidad'] 
        
        return cargaMasivaCursos(file,idEspecialidad)

class Carga_masiva_profesor_jp(Resource):
    def post(self):
        key = 'file 1'
        file = request.files.get(key)
        idEspecialidad = request.form['idEspecialidad']
        idCurso = request.form['idCurso']
        
        
        return cargaMasivaProfesorJP(file,idEspecialidad,idCurso)
