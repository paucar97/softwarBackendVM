from flask_restful import Resource
from flask import Flask, request
#from sqlalchemy import create_engine
from app.controller.petCTR import *

class PetListarSRC(Resource):
    def get(self):
        
        return listarPets()



    

