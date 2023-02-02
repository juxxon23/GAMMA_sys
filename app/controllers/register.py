from flask.views import MethodView
from flask import jsonify, request

from app.db.model import User
from app.db.dbtool import DBTool
from app.helpers.encrypt_pass import Crypt

cry = Crypt()
dbt = DBTool()

class Register(MethodView):

    def post(self):
        try:
            user_reg = request.get_json()
            # Validadores
            user_exists = dbt.get_by_email(User, user_reg['businessEmail'])
            if user_exists is not None:
            # Verificar si en la data existe alguna llave 'exception'
                return jsonify({'status': 'user alredy exists'})
            new_user = User(
                    business_name = user_reg['businessName'], 
                    business_email = user_reg['businessEmail'], 
                    business_password = cry.hash_string(user_reg['businessPassword']),
                    comercial_activity = user_reg['comercialActivity'], 
                    plan_type = int(user_reg['planType']))
            state = dbt.add(new_user)
            # Falta manejar los errores de state
            return jsonify({'status': 'ok', 'msg': 'Successful registration'}), 200
        except Exception as ex:
            return jsonify({'status':'exception', 'ex': str(ex)}), 403
