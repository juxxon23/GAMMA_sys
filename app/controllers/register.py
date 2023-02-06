from flask.views import MethodView
from flask import jsonify, request

from app.db.model import User
from app.db.dbtool import DBTool
from app.helpers.encrypt_pass import Crypt
from app.helpers.exc_handler import ExceptionHandler
from app.validators.user_val import RegisterUser 

cry = Crypt()
dbt = DBTool()
exh = ExceptionHandler()
reg_schema = RegisterUser()

class Register(MethodView):

    def post(self):
        try:
            user_reg = request.get_json()
            errors = reg_schema.validate(user_reg)
            if errors:
                return jsonify({'status':'validators', 'error':errors}), 400
            user_exists = dbt.get_by_email(User, user_reg['businessEmail'])
            msg = exh.wrap(user_exists) # Falta ajustar el mensaje cuando el usuario existe ya que es un objeto de la clase User
            if msg.get('status') == 'user':
                new_user = User(
                        business_name = user_reg['businessName'], 
                        business_email = user_reg['businessEmail'], 
                        business_password = cry.hash_string(user_reg['businessPassword']),
                        comercial_activity = user_reg['comercialActivity'], 
                        plan_type = int(user_reg['planType']))
                state = dbt.add(new_user)
                msg = exh.wrap(state)
                if msg.get('status') == 'ok':
                    return jsonify({'status': 'ok', 'msg': 'Successful registration'}), 200
                else:
                    return jsonify(msg), 400
            else:
                return jsonify(msg), 400
        except Exception as ex:
            return jsonify({'status':'exception', 'ex': str(ex)}), 403
