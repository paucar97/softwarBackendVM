from app import api
if __name__ == '__main__':
    api.app.run(host="localhost", port=5000, debug=True)
    #api.manager.run()
    # para migrar escribir python runserver.py db migrate
    """
    python runserver.py db stamp heads
    pyhton runserver.py db migrate
    python runserver.py db upgrade
    para saltar migracion
    heads
    current
    stamp heads
    """
