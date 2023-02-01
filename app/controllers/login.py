from flask.views import MethodView
from flask import request, jsonify
from flask import current_app as app

import jwt
import datetime

from app.db.model import User
from app.db.dbtool import DBTool
from app.helpers.encrypt_pass import Crypt


dbt = DBTool()
cry = Crypt()

class Login(MethodView):

    def post(self):
        try:
            user_log = request.get_json()
            user_exists = dbt.get_by_email(User, user_log['businessEmail'])
            if 'exception' in user_exists:
                return jsonify(user_exists)
            return jsonify({'status':'ok', 'user-data': user_exists})
            # Verificar que el correo del usuario existe
            # si no existe retornar error, el usuario no esta registrado.
            # si existe verificar si la contrasena es correcta
            # si es correcta permitir el acceso al sistema y entregar token de
            # acceso
            # si no es correcta retorna error, la contrasena no es correcta
        except Exception as ex:
            return jsonify({'status':'exception', 'ex':str(ex)}), 400

