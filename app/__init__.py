from flask import Flask, request, render_template, redirect 
from flask_cors import CORS

from app.db.model import db

def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object('config')
    app.config.from_pyfile('config_dev.py')
    CORS(app, support_credentials=True)

    with app.app_context():
        from .routes import user, ctrl_panel 
        add_routes(app, user, ctrl_panel)
        db.init_app(app)
        return app

def add_routes(app, user, ctrl_panel):
        #User routes
        app.add_url_rule(user['login'], view_func=user['view_func_login'])
        app.add_url_rule(user['register'], view_func=user['view_func_register'])
        app.add_url_rule(ctrl_panel['panel'], view_func=ctrl_panel['view_func_panel']) 
