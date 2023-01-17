from flask.views import MethodView
from flask import request, jsonify


class Login(MethodView):

    def post(self):
        try:
            #user_log = request.get_json()
            business_email = request.form.get('business_email')
            business_password = request.form.get('business_password')
            print(business_email, business_password)
            return jsonify({'status':'ok'}), 200
            # Verificar que el correo del usuario existe
            # si no existe retornar error, el usuario no esta registrado.
            # si existe verificar si la contrasena es correcta
            # si es correcta permitir el acceso al sistema y entregar token de
            # acceso
            # si no es correcta retorna error, la contrasena no es correcta
        except Exception as ex:
            return jsonify({'status':'exception', 'ex':str(ex)}), 400

