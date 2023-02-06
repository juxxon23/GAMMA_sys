from flask.views import MethodView
from flask import request, jsonify
from flask import current_app as app

import jwt # modulo PyJWT 
import datetime

from app.db.model import User
from app.db.dbtool import DBTool
from app.helpers.encrypt_pass import Crypt
from app.helpers.exc_handler import ExceptionHandler
from app.validators.user_val import LoginUser

dbt = DBTool()
cry = Crypt()
exh = ExceptionHandler()
log_schema = LoginUser()

class Login(MethodView):

    def post(self):
        try:
            user_log = request.get_json()
            errors = log_schema.validate(user_log)
            if errors:
                return jsonify({'status':'validators', 'error':errors}), 400
            user_exists = dbt.get_by_email(User, user_log['businessEmail'])
            msg = exh.wrap(user_exists)
            if msg.get('status') != 'ok':
                return jsonify(msg)
            if cry.check_hash(user_log['businessPassword'],
                               user_exists.business_password):
                encoded_jwt = jwt.encode({'exp':
                                          datetime.datetime.utcnow()+datetime.timedelta(seconds=300),
                                          'uem': user_exists.business_email},
                                         app.config['SECRET_KEY'],
                                         algorithm='HS256')
                return jsonify({'status':'welcome', 'businessEmail':
                                user_exists.business_email,
                                'tkse':encoded_jwt})
            return jsonify({'status':'password incorrect'})
            # Verificar que el correo del usuario existe
            # si no existe retornar error, el usuario no esta registrado.
            # si existe verificar si la contrasena es correcta
            # si es correcta permitir el acceso al sistema y entregar token de
            # acceso
            # si no es correcta retorna error, la contrasena no es correcta
        except Exception as ex:
            return jsonify({'status':'exception', 'ex':str(ex)}), 400

