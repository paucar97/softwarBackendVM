from flask_restful import Resource
from flask import Flask, request
from app.controller.pet_x_userCTR import listar

class listarPet_x_UserSRC(Resource):
    def get(seflf):
        return listar()