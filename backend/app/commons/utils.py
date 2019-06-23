import smtplib

def convertDatetime(tiempo):
    tiempo = tiempo.__str__()
    tiempo = tiempo.replace("T"," ")
    tiempo = tiempo[:-6]
    return tiempo

correoSistemaSec = "florestacksistemasec2@gmail.com"
contrasenaSistemaSec = "florestack123"

def envioCorreo(destinatario,asunto,mensage):
    me = 'Subject: {}\n\n{}'.format(asunto,mensage)
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login(correoSistemaSec,contrasenaSistemaSec)
    server.sendmail(correoSistemaSec,destinatario,me)
    server.quit()
    return

