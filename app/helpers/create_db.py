from flask import Flask
from db.model import db, User

def create_db():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://grim:Gammagr.03@localhost/gmdb'
    with app.app_context():
        db.init_app(app)
        db.create_all()
    return app
