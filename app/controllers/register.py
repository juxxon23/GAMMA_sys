from flask.views import MethodView
from flask import jsonify, request
from app.db.model import User


class Register(MethodView):

    def post(self):
        try:
            user_reg = request.get_json()
            # Error handler
            new_user = User(
                    business_name = user_reg['business_name'], 
                    business_email = user_reg['business_email'], 
                    business_password = user_reg['business_password'], 
                    comercial_activity = user_reg['comercial_activity'], 
                    plan_type = user_reg['plan_type'])
            return jsonify({'status': 'ok', 'msg': 'Successful registration'}), 200
        except Exception as ex:
            return jsonify({'status':'exception', 'ex': str(ex)}), 403
