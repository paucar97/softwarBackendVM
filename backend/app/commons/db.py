from app.api import app
from flask_sqlalchemy import SQLAlchemy
import sshtunnel
import sqlalchemy
from io import StringIO


def getSessionServer():
    #"""
    user='root'
    ssh_user = 'inf245'
    passwssh = "6CmINL2eRPo%baH"
    passw= 'GiME4OI9'
    dbName = 'florestack'
    localhost = '127.0.0.1'
    port = 3307
    host = "200.16.7.185"
    tunnel = sshtunnel.SSHTunnelForwarder(
            (host,22),
            ssh_password = passwssh,
            ssh_username=ssh_user,
            remote_bind_address=(localhost, 3306)
    )
    tunnel.start()
    #app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://{}:{}@{}:{}/{}'.format(user,passw,localhost,tunnel.local_bind_port,dbName)
    #"""
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:holi123@localhost:3306/florestack'
    app.config['SQLALCHEMY_POOL_SIZE'] = 5
    app.config['SQLALCHEMY_POOL_TIMEOUT'] = 30
    app.config['SQLALCHEMY_POOL_RECYCLE']=31
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db = SQLAlchemy(app)
    
    return db
"""
def getSessionEngine():
    user='admin'
    ssh_user = 'ubuntu'
    passw= 'Telefonica#2019'
    dbName = 'genesis'
    localhost = '127.0.0.1'
    port = 3307
    host = "ec2-18-222-229-189.us-east-2.compute.amazonaws.com"


    database_connection  = sqlalchemy.create_engine('mysql+mysqlconnector://{}:{}@{}:{}/{}'.format(
    user, 
    passw,
    host,
    port,
    dbName))
    return database_connection.connect()
"""