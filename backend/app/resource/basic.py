from flask_restful import Resource

class Hello(Resource):
    def post(self):
        return {"message":"Hola mundo BBCITA"}