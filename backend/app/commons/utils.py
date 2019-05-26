def convertDatetime(tiempo):
    tiempo = tiempo.__str__()
    tiempo = tiempo.replace("T"," ")
    tiempo = tiempo[:-6]
    return tiempo