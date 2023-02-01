from flask.views import MethodView
from flask import jsonify, request


class Panel(MethodView):

    def get(self):
        return jsonify({'status':'GET ok'}), 200

    def post(self):
        return jsonify({'status':'POST ok'}), 200

    def put(self):
        return jsonify({'status':'PUT ok'}), 200

    def delete(self):
        return jsonify({'status':'DELETE ok'}), 200
