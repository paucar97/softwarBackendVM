class ResponseMessage:
    def __init__(self, code=0, errorcode=0, mssg="null"):
        self.opcode = code
        self.errcode = errorcode
        self.message = mssg

    def __str__(self):
        return '(' + str(self.opcode) + ',' + str(self.errcode) + ',' + self.message + ')'

    def jsonify(self):
        json = dict()
        json['codigo'] = self.opcode
        json['error'] = self.errcode
        json['mensaje'] = self.message
        return json

# ############################ #
# opcode
#   values:
#       0: ok
#       1: error
# errcode
#   values:
#       0: null
#       1: validation error
#       2: database error (exception)
# ############################ #
