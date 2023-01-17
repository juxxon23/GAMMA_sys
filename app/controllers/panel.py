from flask.views import MethodView
from flask import jsonify, request
from app.helpers.json_tool import JSONTool


jst = JSONTool()

class Panel(MethodView):

    def get(self):
        register_list = jst.load()
        return jsonify({'status':'GET ok', 'users list': register_list}), 200

    def post(self):
        return jsonify({'status':'POST ok'}), 200

    def put(self):
        return jsonify({'status':'PUT ok'}), 200

    def delete(self):
        return jsonify({'status':'DELETE ok'}), 200
