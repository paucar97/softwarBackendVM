from flask_restful import Api
from flask import Flask
from flask_cors import CORS, cross_origin
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand


app = Flask(__name__)
api = Api(app)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})


################################################ MODELS ################################################
from app.commons.db import getSessionServer
from app.models import db
from app.models.semestre import Semestre
from app.models.especialidad import Especialidad
from app.models.usuario import Usuario
from app.models.semestre_especialidad import Semestre_especialidad
from app.models.permiso import Permiso
from app.models.curso import Curso
from app.models.horario import Horario
from app.models.permiso_usuario_horario import Permiso_usuario_horario
from app.models.grupo import Grupo
from app.models.grupo_alumno_horario import Grupo_alumno_horario
from app.models.rubrica import Rubrica
from app.models.aspecto import Aspecto
from app.models.rubrica_aspecto import Rubrica_aspecto
from app.models.indicador import Indicador
from app.models.rubrica_aspecto_indicador import Rubrica_aspecto_indicador
from app.models.actividad import Actividad
from app.models.alarma import Alarma
from app.models.actividad_alarma import Actividad_alarma
from app.models.encuesta import Encuesta
from app.models.pregunta import Pregunta
from app.models.encuesta_pregunta import Encuesta_pregunta
from app.models.horario_encuesta import Horario_encuesta
from app.models.alumno_encuesta_respuesta import Alumno_encuesta_respuesta
from app.models.feedback_actividad import Feedback_actividad
from app.models.alumno_actividad import Alumno_actividad
from app.models.entregable import Entregable
from app.models.alumno_nota_aspecto import Alumno_nota_aspecto
from app.models.alumno_nota_indicador import Alumno_nota_indicador
from app.models.notificacion import Notificacion
##########################################################################################################
migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)
############################################## RESOURCE ##################################################
from app.resource.SRC_Usuario import *
from app.resource.SRC_Auto_evaluacion import *
from app.resource.SRC_Entregable import *
from app.resource.SRC_Calificacion import *
from app.resource.SRC_Alumno_actividad import *
from app.resource.SRC_Permiso_usuario_horario import *
from app.resource.SRC_Curso import *
from app.resource.SRC_Actividad import *
from app.resource.basic import Hello
from app.resource.SRC_Grupo import *
from app.resource.SRC_Co_evaluacion import *
##########################################################################################################
############################################ SERVICIOS ###################################################
api.add_resource(Obtener_cursos_activos_alumno, '/api/permiso_usuario_horario/cursos_activos_alumno')
api.add_resource(Listar_Cursos,'/api/curso/listar_cursos')
api.add_resource(Hello,'/api/hello')
api.add_resource(Login,'/api/login')
api.add_resource(Crear_auto_evaluacion,'/api/auto-evaluacion/creacion')
api.add_resource(Obtener_rubrica_idactividad, '/api/actividad/obtener_rubrica_idactividad')
api.add_resource(Obtener_rubricas_pasadas, '/api/actividad/obtener_rubricas_pasadas')
api.add_resource(Crear_rubrica, '/api/actividad/crear_rubrica')
api.add_resource(Crear_Actividad,'/api/actividad/crear_actividad')
api.add_resource(Editar_Actividad,'/api/actividad/editar_actividad')
api.add_resource(Mostar_entregable,'/api/entregables/lista')
api.add_resource(Subir_entregable,'/api/entregable/entrega')
api.add_resource(ListarObjetos,'/api/auto-evaluacion/listarPreguntas')
api.add_resource(Listar_cursos_dictando, '/api/profesor/cursos')
api.add_resource(Obtener_alumnos_entregable_entregado,'/api/actividad/alumnos/entregables')
#api.add_resource(Registrar_calificaciones,'/api/actividad/registrar-calificaciones')
#api.add_resource(Obtener_entregables_actividad_por_alumno, '/api/actividad/entregables')
api.add_resource(Calificar_alumno_actividad, '/api/actividad/alumnos/calificar')
api.add_resource(Editar_nota_alumno_actividad, '/api/actividad/alumnos/editar_nota')
api.add_resource(Publicar_calificacion_para_revision, '/api/actividad/jp/publicar_calificacion')
api.add_resource(Editar_rubrica, '/api/actividad/editar_rubrica')
api.add_resource(Obtener_nota_alumno, '/api/actividad/alumnos/obtener_nota_alumno')

api.add_resource(Crear_co_evaluacion,'/api/co-evaluacion/crear_co_evaluacion')
api.add_resource(ListarPreguntas,'/api/co-evaluacion/listarPreguntas')
api.add_resource(Editar_co_evaluacion,'/api/co-evaluacion/editar')
api.add_resource(Eliminar_co_evaluacion,'/api/co-evaluacion/eliminar')

# iter2 mod:comentarios
api.add_resource(Ingresar_comentario_alumno, '/api/actividad/ingresar_comentario_alumno')
api.add_resource(Responder_comentario_alumno, '/api/actividad/responder_comentario_alumno')
# api.add_resource(, '/api/actividad/listar_comentarios')
api.add_resource(Obtener_entregables_actividad_por_alumno, '/api/actividad/entregables')
api.add_resource(Obtener_alumnos_actividad,'/api/actividad/alumnos')
api.add_resource(Editar_auto_evaluacion,'/api/auto-evaluacion/editar')
api.add_resource(Eliminar_auto_evaluacion,'/api/auto-evaluacion/eliminar')
api.add_resource(Crear_grupo,'/api/grupo/crear') # FALTA PROBAR @INDIOKER
api.add_resource(Crear_grupo_general,'/api/grupo/crear-general') # FALTA PROBAR @INDIOKER
api.add_resource(Listar_grupo_general,'/api/grupo/listar-general') # se probo con pstman PROCEDE
api.add_resource(Listar_Actividad,'/api/actividad/lista')
api.add_resource(Listar_integrantes,'/api/grupo/integrantes')
api.add_resource(Existe_autoevaluacion,'/api/autoevaluacion/existencia')
api.add_resource(Existe_Co_evaluacion,'/api/co-evaluacion/existencia')
api.add_resource(Listar_alumnos_destacados, '/api/actividad/alumnos_destaca')
# api.add_resource(, '/api/actividad/')
